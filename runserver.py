from service import app, sched

if __name__ == '__main__':
	print 'Starting simple-scheduler service...'	
	sched.start()	
	app.run(debug = True, host='0.0.0.0', port = 5003)	
	sched.shutdown()
	