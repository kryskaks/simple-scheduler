import types

from flask import request, render_template, redirect, url_for

from service import app, sched
from forms import JobForm
import jobs as user_jobs

@app.route('/hello')
def hello():
	return "Hello from simple-scheduler service!"

@app.route('/jobs/<job_id>')
@app.route('/jobs')
def jobs(job_id = None):	
	if job_id:
		return str(sched.get_job(job_id = job_id))
	
	return "<br>".join(["id: %s => %s" % (j.id, j) for j in sched.get_jobs()])
	return "jobs!"

@app.route('/jobs/new', methods = ["GET", "POST"])
def new_job():
	if request.method == "GET":
		job_form = JobForm()
		job_form.func_name.choices = [(o,o) for o in dir(user_jobs) if isinstance(getattr(user_jobs, o), types.FunctionType)]
		return render_template("new_job.html", job_form = job_form)

	job_name = request.form.get("name", "")
	cron = request.form.get("cron_expression", "")
	func_name = request.form.get("func_name", "")

	func = getattr(user_jobs, func_name)

	print "func():", func()

	second = int(cron)

	sched.add_job(func, id=job_name, trigger="cron", second=second)

	return redirect(url_for("jobs"))

@app.route('/jobs/<job_id>/remove', methods = ["GET"])
def remove_job(job_id):
	sched.remove_job(job_id = job_id)
	return redirect(url_for("jobs"))
