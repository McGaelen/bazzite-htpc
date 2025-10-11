import sys
import logging.handlers

logger = logging.getLogger("CecDaemonLogger")
logger.setLevel(logging.DEBUG)
logger.addHandler(logging.handlers.SysLogHandler(address="/dev/log"))
logger.addHandler(logging.StreamHandler(sys.stdout))

debug = logger.debug
info = logger.info
warning = logger.warning
error = logger.error
exception = logger.exception
