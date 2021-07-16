import pytz

from datetime import datetime
from jdatetime import datetime as jdatetime


def dump(obj):
    """
    Converts a UTC ‌datetime object into local jdatetime then dumps it.

    :param obj: Input UTC datetime object
    :type obj: datetime

    :returns: Local jdatetime string
    :rtype: str
    """
    obj = obj.replace(tzinfo=pytz.utc)
    obj = obj.astimezone(pytz.timezone('Asia/Tehran'))
    obj = jdatetime.fromgregorian(datetime=obj)
    return obj.strftime('%Y/%m/%d %H:%M:%S')
