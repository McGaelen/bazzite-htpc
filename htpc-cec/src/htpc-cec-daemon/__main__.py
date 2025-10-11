import signal

import cec
import daemon
import posix_ipc

from shared import logger, const, Command


def main():
    # with daemon.DaemonContext(detach_process=False):
    logger.info("initializing CEC")

    try:
        cec.init()
    except:
        logger.exception(
            "Failed to initialize CEC - does this devices support HDMI-CEC?"
        )
        exit(1)

    tv = cec.Device(cec.CECDEVICE_TV)

    logger.info(f"creating message queue {const.QUEUE_NAME}")
    q = posix_ipc.MessageQueue(name=const.QUEUE_NAME, flags=posix_ipc.O_CREAT)

    def cleanup():
        q.close()
        q.unlink()

    signal.signal(signal.SIGTERM, cleanup)
    signal.signal(signal.SIGINT, cleanup)

    def handle_command(command: str):
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
                logger.warning("Invalid command.")

    logger.info("listening for commands")
    while True:
        try:
            recv_bytes, _ = q.receive()
            recv_str = recv_bytes.decode()
            logger.debug(f"received: {recv_str}")
            handle_command(recv_str)
        except posix_ipc.SignalError:
            # We get here if the program was terminated/ctrl+c'd while waiting for receive(), so just exit.
            exit()


if __name__ == "__main__":
    main()
