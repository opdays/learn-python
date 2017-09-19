from multiprocessing import Pool, current_process
import time

def test(*args, **kwargs):
    p = current_process()
    while True:
        print(p.name, p.pid)
        time.sleep(2)
if __name__ == "__main__":
    p = current_process()
    print(p.name,p.pid)
    pool = Pool(3)
    pool.map(test,range(5))
    pool.close()
    pool.join()
