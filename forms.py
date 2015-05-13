# -*- coding: utf-8 -*-
from datetime import datetime

from flask.ext.wtf import Form
from wtforms import TextField, SelectField, BooleanField, PasswordField, DateField
from wtforms.validators import Required, Length

class JobForm(Form):	
	cron_expression = TextField(u'CRON')
	name = TextField(u'Имя')
	func_name = SelectField(u'Функция')