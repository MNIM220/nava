import json

custom_types_selection = {}


def set_selection(selection):
    """
    Sets the given custom types selection for dynamic_json methods to dump/load with.

    :param selection: Custom types selection
    :type selection: dict
    """
    global custom_types_selection
    custom_types_selection = selection


class CustomEncoder(json.JSONEncoder):
    """
    CustomEncoder class inherited from JSONEncoder.
    Overwrites the "default" method which allows you to dump all types in custom_types as well.
    """

    def default(self, obj):
        # Use custom dumpers on custom types.
        if type(obj) in custom_types_selection:
            return custom_types_selection[type(obj)]['dumper'](obj)

        # Use the builtin dump method on other types.
        return json.JSONEncoder.default(self, obj)


class CustomDecoder(json.JSONDecoder):
    """
    CustomDecoder class inherited from JSONDecoder.
    Defines a dict_to_object method which allows you to load all types in custom_types as well.
    """

    @staticmethod
    def dict_to_object(dictionary):
        # Load each value that has one of the custom types.
        for key in dictionary:
            value = dictionary[key]

            # Skip loading this (key: value) pair if value is None.
            if value is None or type(value) is dict:
                continue

            # Try all custom loaders. If one works move to the next key.
            for custom_type in custom_types_selection:
                try:
                    dictionary[key] = custom_types_selection[custom_type]['loader'](value)
                    break
                except:
                    pass
        return dictionary


def dump(dictionary):
    """
    Uses the CustomEncoder class to dump a dictionary.

    :param dictionary: Input dictionary
    :type dictionary: dict

    :returns: Dumped dictionary
    :type: str
    """
    return json.dumps(dictionary, cls=CustomEncoder, sort_keys=True)


def load(data):
    """
    Uses the CustomDecoder class to load a dictionary from the input string.

    :param data: Input data string
    :type data: str

    :returns: Loaded dictionary
    :type: dict
    """
    if data:
        return json.loads(data, object_hook=CustomDecoder.dict_to_object)
    return {}


def get_serializable(dictionary):
    """
    Gets a dictionary and makes all its values serializable.

    :param dictionary: Input dictionary
    :type dictionary: dict

    :returns: Serializable dictionary
    :rtype: dict
    """
    return json.loads(json.dumps(dictionary, cls=CustomEncoder, sort_keys=True))
