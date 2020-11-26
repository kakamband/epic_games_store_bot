from lib.glist import Glist
from lib.main import Bot
from apscheduler.schedulers.blocking import BlockingScheduler

new_dta = Glist().check(mode='trigger')
sched = BlockingScheduler()

def trigg():
    for j in new_dta['games']:
        with open('src/gamesordered.txt', 'r') as a:
            if not j['title'] in [ i.replace('\n', '') for i in a.readlines() ]:
                Bot().main()


if __name__ == '__main__':
    sched.add_job(trigg, 'cron', day_of_week='mon-sun', hour=12) # Runs everyday @ 12:00
    sched.start()
