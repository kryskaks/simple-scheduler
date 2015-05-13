from datetime import timedelta, date
import logging
import os

from flask import Flask, session

from scheduler import SimpleScheduler
import config

app = Flask(__name__)
app.config.from_object('config')

logger = logging.getLogger(config.LOGGER.name)
logger.setLevel(config.LOGGER.level) 
fh = logging.FileHandler(config.LOGGER.file)
fh.setLevel(config.LOGGER.level)
fh.setFormatter(config.LOGGER.formatter)
logger.addHandler(fh)
logging.getLogger("apscheduler.executors.default").addHandler(fh)

sched = SimpleScheduler.get_scheduler(logger = logger)

import views