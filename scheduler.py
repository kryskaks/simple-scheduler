from datetime import datetime
import os

from apscheduler.schedulers.blocking import BlockingScheduler

def tick():
	print('Tick! The time is: %s' % datetime.now())
	scheduler = BlockingScheduler()
	scheduler.add_jobstore('sqlalchemy', url=url)
	jobs = scheduler.get_jobs()
	print jobs

if __name__ == '__main__':
	scheduler = BlockingScheduler()
	url = "postgres://postgres:test@localhost/scheduler"
	scheduler.add_jobstore('sqlalchemy', url=url)
	#scheduler.add_job(tick, 'interval', seconds=5)
	print('Press Ctrl+{0} to exit'.format('Break' if os.name == 'nt' else 'C'))
	try:
		scheduler.start()
	except (KeyboardInterrupt, SystemExit):
		pass