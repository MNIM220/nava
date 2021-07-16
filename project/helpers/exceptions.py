class NotFoundError(Exception):
    """
    Not found exception. HTTP status code 404.
    """

    def __init__(self, *args, **kwargs):
        super().__init__(args, kwargs)
        self.field = None
        self.error = args[0] if args else None


class ForbiddenError(Exception):
    """
    Forbidden exception. HTTP status code 403.
    """

    def __init__(self, *args, **kwargs):
        super().__init__(args, kwargs)
        self.field = None
        self.error = args[0] if args else None


class ValidationError(Exception):
    """
    Validation exception. HTTP status code 400.
    """

    def __init__(self, field=None, error=None):
        self.error = error or field
        self.field = field if error else None


class InternalServiceError(Exception):
    """
    InternalError exception. HTTP status code 500.
    """

    def __init__(self, status_code, service_error, error=None):
        self.status_code = status_code
        self.service_error = service_error
        self.error = error
