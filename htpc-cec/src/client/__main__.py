import sys
import posix_ipc

from shared import logger, const


def main():
    try:
        q = posix_ipc.MessageQueue(name=const.QUEUE_NAME)
        q.send(sys.argv[1])
        q.close()
    except posix_ipc.ExistentialError:
        logger.error("Failed to send command - the daemon is not running.")


if __name__ == "__main__":
    main()
