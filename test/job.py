import threading
import time
import schedule
import arrow


def job():
    print("job running on thread %s" % threading.current_thread())
    time.sleep(5)
    print("job end time: %s" % arrow.get().to('Asia/Shanghai').format('YYYY-MM-DD HH:mm:ss'))


def job1():
    print("job1 running on thread %s" % threading.current_thread())
    time.sleep(2)
    print("job1 end time: %s" % arrow.get().to('Asia/Shanghai').format('YYYY-MM-DD HH:mm:ss'))


# 多线程版本
def run_threaded(job_func):
    job_thread = threading.Thread(target=job_func)
    job_thread.start()
    print("job thread start......")


# 定义你要周期运行的函数
def cron():
    print("I'm working...")
    # schedule.every(10).seconds.do(job)               # 每隔 10 秒钟运行一次 job 函数
    # schedule.every(10).minutes.do(job)               # 每隔 10 分钟运行一次 job 函数
    # schedule.every().hour.do(job)                    # 每隔 1 小时运行一次 job 函数
    # schedule.every().day.at("10:30").do(job)         # 每天在 10:30 时间点运行 job 函数
    # schedule.every().monday.do(job)                  # 每周一 运行一次 job 函数
    # schedule.every().wednesday.at("13:15").do(job)   # 每周三 13：15 时间点运行 job 函数
    # schedule.every().minute.at(":17").do(job)        # 每分钟的 17 秒时间点运行 job 函数

    schedule.every(2).hours.do(run_threaded, job)
    # schedule.every(5).seconds.do(run_threaded, job1)

    while True:
        schedule.run_pending()   # 运行所有可以运行的任务
        time.sleep(1)


if __name__ == "__main__":
    print("11111111")
    cron()
    print("222222222222")


