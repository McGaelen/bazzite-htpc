import sys
import logging
import logging.handlers

logger = logging.getLogger('CecDaemonLogger')
logger.setLevel(logging.DEBUG)
logger.addHandler(logging.handlers.SysLogHandler(address = '/dev/log'))
logger.addHandler(logging.StreamHandler(sys.stdout))
