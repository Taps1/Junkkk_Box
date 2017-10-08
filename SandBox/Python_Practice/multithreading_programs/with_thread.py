from time import ctime, sleep
import thread

def loop0(lock):
    print "starting loop0 at: ", ctime()
    sleep(4)
    print "loop 0 done at: ", ctime()
    lock.release()

def loop1(lock):
    print "starting loop1 at: ", ctime()
    sleep(2)
    print "loop 1 done at: ", ctime()
    lock.release()

if __name__ == "__main__":
    lock0 = thread.allocate_lock()
    lock1 = thread.allocate_lock()
    lock0.acquire()
    lock1.acquire()
    print lock0, lock1
    thread.start_new_thread(loop0, (lock0, ))
    thread.start_new_thread(loop1, (lock1, ))
    while lock0.locked():
        pass
    while lock1.locked():
        pass
