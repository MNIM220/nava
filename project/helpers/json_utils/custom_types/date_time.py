import pytz

from datetime import datetime


def dump(obj):
    """
    Dumps a datetime object using standard ISO format.

    :param obj: Input datetime object
    :type obj: datetime

    :returns: Datetime string in ISO format
    :rtype: str
    """
    return obj.strftime('%Y-%m-%dT%H:%M:%S.%f')


def load(data):
    """
    Loads a datetime string into a UTC datetime object.
    Input datetime string must be in ISO format.

    :param data: Input datetime string.
    :type data: str

    :returns: UTC datetime object
    :rtype: datetime
    """
    result = datetime.strptime(data, '%Y-%m-%dT%H:%M:%S.%f').replace(tzinfo=pytz.utc)
    return result
