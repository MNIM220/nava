from project.helpers.utils import LocalProxy

# Instantiate object proxies for each project extension.
current_config = LocalProxy()
flask_app = LocalProxy()
mongo_client = LocalProxy()
changelogs = LocalProxy()
mysql_db = LocalProxy()
