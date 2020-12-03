from apscheduler.schedulers.blocking import BlockingScheduler
import refresh_code as rc


def job():
    print('开始刷新沙箱密钥', flush=True)
    rc.main()


def config():
    # BlockingScheduler
    scheduler = BlockingScheduler()
    #scheduler.add_job(job, 'interval', minutes=1)  # 添加任务 for debug
    scheduler.add_job(job, "cron", day_of_week="0-6", hour=9, minute=1)
    scheduler.start()


if __name__ == "__main__":
    config()