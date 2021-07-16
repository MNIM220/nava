class LocalProxy(object):
    __value__ = None

    def __getattr__(self, item):
        if hasattr(self.val, item):
            return getattr(self.val, item)

    def set(self, item):
        """
        Set the given item as the current value.

        :param item: Instance to assign value to
        :type item: any
        """
        self.__value__ = item

    @property
    def val(self):
        """
        Returns the currently set value.

        :returns: The assigned value of current item.
        :rtype: any
        """
        if not self.__value__:
            raise LookupError("Local Proxy is not initialized."
                              "Trying to use proxy instance before its assignment?")
        return self.__value__


def validate_pagination_args(page, per_page):
    """
    Validates the given pagination args (page, per_page).
    Can be used by controllers to validate requests.

    :param page: Page number
    :type page: any

    :param per_page: Page size
    :type per_page: any

    :returns: page, per_page (in the correct format)
    :rtype: int, int

    :returns: None, None (if pagination args are not valid)
    """
    # ‌Pagination args must not be None.
    if page is None or per_page is None:
        return None, None

    # ‌Pagination args must be of type int.
    try:
        page = int(page)
        per_page = int(per_page)
    except ValueError:
        return None, None

    # Pagination args must not be less than 1.
    if page < 1 or per_page < 1:
        return None, None

    return page, per_page
