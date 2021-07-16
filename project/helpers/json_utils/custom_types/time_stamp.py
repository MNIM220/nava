from datetime import datetime


def dump(obj):
    """
    Dumps a datetime into the timestamp format.

    :param obj: Input datetime object
    :type obj: datetime

    :returns: Timestamp equivalent of the given datetime
    :rtype: int
    """
    return int(obj.timestamp())
