from time import ctime, sleep

def loop0():
    print "starting loop0 at: ", ctime()
    sleep(4)
    print "loop 0 done at: ", ctime()

def loop1():
    print "starting loop1 at: ", ctime()
    sleep(2)
    print "loop 1 done at: ", ctime()

if __name__ == "__main__":
    loop0()
    loop1()
