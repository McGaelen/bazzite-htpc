import signal
import cec
import daemon

import posix_ipc

import Command
from logger import logger
from const import QUEUE_NAME

# with daemon.DaemonContext(detach_process=False):
logger.info('initializing CEC')
cec.init()
tv = cec.Device(cec.CECDEVICE_TV)

logger.info(f'creating message queue {QUEUE_NAME}')
q = posix_ipc.MessageQueue(name = QUEUE_NAME, flags = posix_ipc.O_CREAT)

def cleanup():
    q.close()
    q.unlink()

signal.signal(signal.SIGTERM, cleanup)
signal.signal(signal.SIGINT, cleanup)

def handleCommand(command: str):
    match command:
        case Command.power_on:
            tv.power_on()
        case Command.standby:
            tv.standby()
        case Command.volup:
            cec.volume_up()
        case Command.voldown:
            cec.volume_down()
        case other:
            logger.warning('Invalid command.')

logger.info('start main loop')
while True:
    try:
        recv_bytes, _ = q.receive()
        recv_str = recv_bytes.decode()
        logger.debug(f'received: {recv_str}')
        handleCommand(recv_str)
    except posix_ipc.SignalError:
        # We get here if the program was terminated/ctrl+c'd while waiting for receive().
        exit()
