import logging

###
###global_setting
###
class Setting(object):
    DEBUG=True
    ONLINE=False
    REMOTE_URL=None
    CUSTOM_SETTING=None
    LOG_LEVEL=logging.DEBUG
    LOG_ROOT='xxxx'
    LOG_FILE_ROOT_PATH='logs'
    ENABLE_RADIS_OUTPUT=False
    SERVERSTATICROOT=None
    SERVER_PORT=5000
    MAX_CAMERA_RECONNECT_TIMES=10