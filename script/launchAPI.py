import apimachine
import threading

th = threading.Thread(target=apimachine.hi())

th.start()
