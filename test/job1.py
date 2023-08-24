import arrow
import schedule
import time


def job1():
    print("job1 start time: %s" % arrow.get().to('Asia/Shanghai').format('YYYY-MM-DD HH:mm:ss'))
    time.sleep(2)
    print("job1 end time: %s" % arrow.get().to('Asia/Shanghai').format('YYYY-MM-DD HH:mm:ss'))


def job2():
    print("job2 start time: %s" % arrow.get().to('Asia/Shanghai').format('YYYY-MM-DD HH:mm:ss'))
    time.sleep(5)
    print("job2 end time: %s" % arrow.get().to('Asia/Shanghai').format('YYYY-MM-DD HH:mm:ss'))


def job3():
    print("job3 start time: %s" % arrow.get().to('Asia/Shanghai').format('YYYY-MM-DD HH:mm:ss'))
    time.sleep(10)
    print("job3 end time: %s" % arrow.get().to('Asia/Shanghai').format('YYYY-MM-DD HH:mm:ss'))


if __name__ == '__main__':
    schedule.every(10).seconds.do(job1)
    schedule.every(30).seconds.do(job2)
    schedule.every(5).to(10).seconds.do(job3)  # 5~10s随机执行
    # 单线程版本
    while True:
        schedule.run_pending()
