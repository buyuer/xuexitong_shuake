from main import *
import time

if __name__ == '__main__':
    count = 0
    while True:
        simulate_tap(1000, 100)
        time.sleep(0.5)
        simulate_tap(700,1750)
        simulate_tap(700,1750)
        simulate_tap(850, 1200)
        simulate_tap(1000, 100)
        count += 1
        time.sleep(4.0)
        print('提交第%d次' % count)
        if count > 55:
            break
