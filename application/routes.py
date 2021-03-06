import os
import secrets
from PIL import Image
from flask import render_template, url_for, flash, redirect, request, abort, jsonify, send_from_directory, Response
from application.initialize.bcrypt_init import bcrypt
from application.initialize.db_init import db
from application.initialize.scheduler_jobstore_init import scheduler as apscheduler
from application.app_setup import application
from application.forms import RegistrationForm, LoginForm, UpdateAccountForm, PostForm, ChangePasswordForm
from application.models import User, Post, RawSlackEvent
from flask_login import login_user, current_user, logout_user, login_required
from application import slack_auth
from application import google_auth
from application import github_auth
from flask_wtf import csrf
import jwt
from flask import session
from datetime import datetime, timedelta
from application.applied_science.data_annotation import labelled_focus_time_df
from application.scheduled_data_tasks import nudge

# this should eventually be replaced by a CDN
@application.route('/', methods=['GET'])
def app():
	return send_from_directory('doxa-frontend/dist/', 'index.html')

@application.route('/static_files/js/<path:filename>', methods=['GET'])
def send_static_js(filename):
	return send_from_directory('doxa-frontend/dist/static_files/js', filename)

@application.route('/static_files/css/<path:filename>', methods=['GET'])
def send_static_css(filename):
	return send_from_directory('doxa-frontend/dist/static_files/css', filename)

@application.route('/static_files/img/<path:filename>', methods=['GET'])
def send_static_img(filename):
	return send_from_directory('doxa-frontend/dist/static_files/img', filename)

@application.route('/static_files/<path:filename>', methods=['GET'])
def send_static_favicon(filename):
	return send_from_directory('doxa-frontend/dist/static_files', 'favicon.png')

@application.route('/favicon.ico', methods=['GET'])
def send_favicon():
	return send_from_directory('doxa-frontend/dist/static_files', 'favicon.png')

@application.route('/slack-event', methods=['POST'])
def slack_event():
	print(request)
	try:
		if request.json.get('type') != 'url_verification':
			print(request.json) # this is where we log / store things
			raw_slack_event = RawSlackEvent(json_data = request.json)
			raw_slack_event.save()
			return '200'
		else:
			print(request.json)
			return request.json.get('challenge')
	except:
		print('excepted:')
		print(request.json)
		return '200'
	return '200'

@application.route('/api/check-login', methods=['GET'])
def logged_in():
	if current_user.is_authenticated:
		return jsonify(current_user.to_dict())
	return jsonify(None)

@application.route('/api/login', methods=['POST'])
def api_login_2():
	form = LoginForm()
	user = User.query.filter_by(email=form.email.data).first()
	if user and bcrypt.check_password_hash(user.password, form.password.data):
		login_user(user, True)
		print(session)
		response = user.to_dict()
		response['authenticated'] = True
		return jsonify(response)
	response = form.errors
	response['errors'] = { 'Credentials': ['Login unsuccessful. Please check email and password.'] }
	return jsonify(response), 401

@application.route('/api/logout', methods=['GET'])
def api_logout():
	if current_user.is_authenticated:
		logout_user()
		return jsonify(True)
	return jsonify({ 'errors': { 'Logout': ['No user is logged in.']}}), 401


@application.route('/api/users', methods=['GET'])
def api_users():
	users = User.query.all()
	response = jsonify([user.to_dict() for user in users])
	return response

@application.route('/api/users/<int:user_id>', methods=['GET'])
def api_user(user_id):
	user = User.query.get_or_404(user_id)
	return jsonify(user.to_dict())

@application.route('/api/get_csrf', methods=['GET'])
def api_get_csrf():
	csrf_token = csrf.generate_csrf()
	return jsonify({ 'csrf_token':  csrf_token})

@application.route('/api/user_details', methods=['GET'])
@login_required
def user_details():
	return jsonify(current_user.user_details())

@application.route('/api/change-password', methods=['POST'])
@login_required
def api_change_password():
	form = ChangePasswordForm()
	if form.validate_on_submit():
		hashed_password = bcrypt.generate_password_hash(form.new_password.data).decode('utf-8')
		current_user.password = hashed_password
		db.session.add(current_user)
		db.session.commit()
		return jsonify({ 'Response': 'Password successfully changed' })
	response = {}
	response['errors'] = form.errors
	return jsonify(response), 401

@application.route('/api/register', methods=['POST'])
def api_register():
	form = RegistrationForm()
	user = User(username=form.username.data, email=form.email.data)
	if form.validate_on_submit():
		hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')	
		user.password = hashed_password
		db.session.add(user)
		db.session.commit()
		return jsonify(user.to_dict())
	response = user.to_dict()
	response['errors'] = form.errors
	return jsonify(response), 401

@application.route('/api/activity-data', methods=['GET'])
@login_required
def activity_data():
	week_offset = request.args.get('week-offset')
	if week_offset == 'undefined':
		week_offset = 0
	week_offset = int(week_offset)
	activity_df = labelled_focus_time_df(current_user, week_offset=week_offset)
	return Response(activity_df.to_json(orient='records', date_format='iso'), mimetype='application/json')

@application.route('/api/activate-nudge', methods=['GET'])
@login_required
def activate_nudge():
	nudge_type = request.args.get('nudge_type')
	return jsonify(nudge.schedule_nudge(nudge_type, user_id=current_user.id)), 200

# @application.route('/api/next-focus', methods=['GET'])
# @login_required
# def next_focus_time():
# 	