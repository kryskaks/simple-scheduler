import logging
from datetime import date, timedelta

from utils import Struct

DEBUG = True

THREADS_PER_PAGE = 8

CSRF_ENABLED = True

SECRET_KEY = 'SeCmt#dnK!'

PERMANENT_SESSION_LIFETIME = timedelta(minutes=20)

DATABASE_URL = 'postgres://postgres:test@localhost/nosypm'

LOG_TO = "/home/kryskaks/nosy-pm/logs"

TMP_DIR = "/home/kryskaks/nosy-pm/tmp"

JOB_STORE_URL = "postgres://postgres:test@localhost/scheduler"

LOGGER = Struct(level = logging.DEBUG, 
				name = "SimpleScheduler", 
				file = "log_{date:%Y-%m-%d}.log".format(date = date.today()),
				formatter = logging.Formatter("%(asctime)s[%(levelname)s] - %(name)s:%(message)s"))

