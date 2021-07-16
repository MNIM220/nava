import os

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
print(ROOT_DIR)

# ‌TODO: Check and validate all env variables and their fallback values.
class DefaultConfig(object):
    """
    Contains configs used and overwritten by other configs.
    Used by Dev, Production and Test config classes.
    """

    # Basic Service ‌Config:
    API_VERSIONS = ['v1']
    SERVICE_NAME = os.getenv('SERVICE_NAME', 'nava')


class DevConfig(DefaultConfig):
    DEBUG = True
    MOCK_APP = True


class ProductionConfig(DefaultConfig):
    DEBUG = False
