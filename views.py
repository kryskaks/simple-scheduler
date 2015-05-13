from flask import request, render_template

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
		job_form.func_name.choices = [(f,f.__name__) for f in user_jobs.all_jobs]
		return render_template("new_job.html", job_form = job_form)

	job_name = request.form.get("name", "")
	cron = request.form.get("cron_expression", "")
	func_name = request.form.get("func_name", "")

	print func_name

	return "New job creating!"
