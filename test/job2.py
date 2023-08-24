import threading
import schedule
import time
import arrow


def job1():
    print("job1 running on thread %s" % threading.current_thread())
    print("job1 start time: %s" % arrow.get().to('Asia/Shanghai').format('YYYY-MM-DD HH:mm:ss'))


def job2():
    print("job2 running on thread %s" % threading.current_thread())
    print("job2 start time: %s" % arrow.get().to('Asia/Shanghai').format('YYYY-MM-DD HH:mm:ss'))


def ensure_schedule():
    schedule.every(5).seconds.do(job1)


def ensure_schedule_2():
    schedule.every(10).seconds.do(job2)


def run_daemon_thread(target, *args, **kwargs):
    job_thread = threading.Thread(target=target, args=args, kwargs=kwargs)
    job_thread.setDaemon(True)
    job_thread.start()


def __start_schedule_daemon():
    def schedule_run():
        while True:
            schedule.run_pending()
            time.sleep(1)

    t = threading.Thread(target=schedule_run)
    t.setDaemon(True)
    t.start()


def init_schedule_job():
    run_daemon_thread(ensure_schedule)
    run_daemon_thread(ensure_schedule_2)


if __name__ == '__main__':
    print("111111111111")

    init_schedule_job()
    __start_schedule_daemon()
    print("2222222222222")
    time.sleep(100)

