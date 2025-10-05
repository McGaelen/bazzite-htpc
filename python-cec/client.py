import sys
import posix_ipc

q = posix_ipc.MessageQueue(name = '/org.mcgaelen.CecDaemon', flags = posix_ipc.O_CREAT)
q.send(sys.argv[1])
q.close()
