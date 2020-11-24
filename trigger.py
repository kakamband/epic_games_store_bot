from glist import Glist
from main import Bot
from apscheduler.schedulers.blocking import BlockingScheduler

new_dta = Glist().check(mode='trigger')
sched = BlockingScheduler()

def trigger():
    for j in new_dta['games']:
        with open('gamesordered.txt', 'r') as a:
            if not j['title'] in [ i.replace('\n', '') for i in a.readlines() ]:
                Bot().main()



if __name__ == '__main__':
    sched.add_job(trigger, 'cron', day_of_week='mon-sun', hour=14)
    sched.start()
