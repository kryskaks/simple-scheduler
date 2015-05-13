from datetime import datetime
import os
import logging

from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.schedulers.background import BackgroundScheduler

from config import JOB_STORE_URL, LOGGER

class SimpleScheduler(object):
	scheduler = None
	def __init__(self, logger, blocking):		
		self._scheduler = BlockingScheduler(logger = logger) if blocking else BackgroundScheduler(logger = logger)
		print "Created %s" % self._scheduler.__class__.__name__
		self._scheduler.add_jobstore('sqlalchemy', url=JOB_STORE_URL)

	def __getattr__(self, attr):
		try:
			return self.__dict__[attr]					
		except KeyError:
			return getattr(self._scheduler, attr)

	@classmethod
	def get_scheduler(cls, logger = None, blocking = False):
		if cls.scheduler is None:
			cls.scheduler = SimpleScheduler(logger, blocking)

		return cls.scheduler