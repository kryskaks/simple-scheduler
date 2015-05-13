import os
from datetime import datetime, date
import logging

from scheduler import SimpleScheduler

if __name__ == '__main__':	
	sched = SimpleScheduler.get_scheduler(True)
	print sched.running
	sched.start_scheduler()	