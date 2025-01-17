CORS_ORIGIN_ALLOW_ALL = True
LOGIN_REQUIRED = True
REMOTE_AUTH_AUTO_CREATE_GROUPS = True
REMOTE_AUTH_AUTO_CREATE_USER = True
REMOTE_AUTH_ENABLED = True
REMOTE_AUTH_GROUP_HEADER = "HTTP_X_FORWARDED_GROUPS"
REMOTE_AUTH_GROUP_SEPARATOR = ","
REMOTE_AUTH_GROUP_SYNC_ENABLED = True
REMOTE_AUTH_HEADER = "HTTP_X_FORWARDED_PREFERRED_USERNAME"
REMOTE_AUTH_STAFF_GROUPS = ["netbox-admins"]
REMOTE_AUTH_SUPERUSER_GROUPS = ["netbox-admins"]
SKIP_SUPERUSER = True
