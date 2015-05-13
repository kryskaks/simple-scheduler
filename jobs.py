from datetime import datetime

import requests

def print_hello_job():
	print "Hello, world! From test job at %s!" % datetime.now()

def get_curl_job():
	url = "http://localhost:5002/hello"
	print "curl", url, "result:", requests.get(url)

def test_job():
	print "%s: It is test job!" % datetime.now()

all_jobs = [print_hello_job, get_curl_job, test_job]