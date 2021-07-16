from bson import ObjectId


def dump(obj):
    """
    Dumps an object id into an id string

    :param obj: Input object id
    :type obj: ObjectId

    :returns: Object id string
    :rtype: str
    """
    return str(obj)


def load(data):
    """
    Loads an object id string into an object id.

    :param data: Object id string
    :type data: str

    :returns: Object id
    :rtype: ObjectId
    """
    return ObjectId(data)
