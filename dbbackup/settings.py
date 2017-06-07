# DO NOT IMPORT THIS BEFORE django.configure() has been run!

import logging.config
import tempfile
import socket
from django.conf import settings
import dbbackup.log

DATABASES = getattr(settings, 'DBBACKUP_DATABASES', list(settings.DATABASES.keys()))

# Fake host
HOSTNAME = getattr(settings, 'DBBACKUP_HOSTNAME', socket.gethostname())

# Directory to use for temporary files
TMP_DIR = getattr(settings, 'DBBACKUP_TMP_DIR', tempfile.gettempdir())
TMP_FILE_MAX_SIZE = getattr(settings, 'DBBACKUP_TMP_FILE_MAX_SIZE', 10*1024*1024)
TMP_FILE_READ_SIZE = getattr(settings, 'DBBACKUP_TMP_FILE_READ_SIZE', 1024*1000)

# Days to keep
CLEANUP_KEEP = getattr(settings, 'DBBACKUP_CLEANUP_KEEP', 10)
CLEANUP_KEEP_MEDIA = getattr(settings, 'DBBACKUP_CLEANUP_KEEP_MEDIA', CLEANUP_KEEP)
CLEANUP_KEEP_FILTER = getattr(settings, 'DBBACKUP_CLEANUP_KEEP_FILTER', lambda x: False)

MEDIA_PATH = getattr(settings, 'DBBACKUP_MEDIA_PATH', settings.MEDIA_ROOT)

DATE_FORMAT = getattr(settings, 'DBBACKUP_DATE_FORMAT', '%Y-%m-%d-%H%M%S')
FILENAME_TEMPLATE = getattr(settings, 'DBBACKUP_FILENAME_TEMPLATE', '{databasename}-{servername}-{datetime}.{extension}')
MEDIA_FILENAME_TEMPLATE = getattr(settings, 'DBBACKUP_MEDIA_FILENAME_TEMPLATE', '{servername}-{datetime}.{extension}')

GPG_ALWAYS_TRUST = getattr(settings, 'DBBACKUP_GPG_ALWAYS_TRUST', False)
GPG_RECIPIENT = GPG_ALWAYS_TRUST = getattr(settings, 'DBBACKUP_GPG_RECIPIENT', None)

STORAGE = getattr(settings, 'DBBACKUP_STORAGE', 'dbbackup.storage.filesystem_storage')
STORAGE_OPTIONS = getattr(settings, 'DBBACKUP_STORAGE_OPTIONS', {})

CONNECTORS = getattr(settings, 'DBBACKUP_CONNECTORS', {})

CUSTOM_CONNECTOR_MAPPING = getattr(settings, 'DBBACKUP_CONNECTOR_MAPPING', {})

# Logging
LOGGING = getattr(settings, 'DBBACKUP_LOGGING', dbbackup.log.DEFAULT_LOGGING)
LOG_CONFIGURATOR = logging.config.DictConfigurator(LOGGING)
LOG_CONFIGURATOR.configure()

# Mail
SEND_EMAIL = getattr(settings, 'DBBACKUP_SEND_EMAIL', True)
SERVER_EMAIL = getattr(settings, 'DBBACKUP_SERVER_EMAIL', settings.SERVER_EMAIL)
FAILURE_RECIPIENTS = getattr(settings, 'DBBACKUP_FAILURE_RECIPIENTS', None)
if FAILURE_RECIPIENTS is None:
    ADMINS = getattr(settings, 'DBBACKUP_ADMIN', settings.ADMINS)
else:
    ADMINS = FAILURE_RECIPIENTS
EMAIL_SUBJECT_PREFIX = getattr(settings, 'DBBACKUP_EMAIL_SUBJECT_PREFIX', '[dbbackup] ')
