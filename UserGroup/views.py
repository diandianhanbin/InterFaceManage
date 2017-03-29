# ecoding=utf-8
# Author: 翁彦彬 | Sven_Weng
# Email : sven_weng@wengyb.com
# Web   : http://wybblog.applinzi.com
from django.http import JsonResponse, HttpResponseRedirect
from django.shortcuts import render

from models import UserGroup
import datetime
import method
import errconfig

Login_Check = method.Login()


def index(request):
	if request.method == 'POST':
		username = request.POST.get('user')
		password = request.POST.get('password')
		if Login_Check.login_check(username, password):
			if Login_Check.write_hash(username):
				userinfo = Login_Check.get_user_info(username, 'username')
				return render(request, 'UserGroup/usercenter.html',
							  {"nickname": userinfo['nickname'], 'loginToken': str(userinfo['loginToken'])})
			else:
				return render(request, 'UserGroup/index.html',
							  {"errCode": "UG0002", "errMsg": errconfig.errConfig['UG0002']})
		else:
			return render(request, 'UserGroup/index.html',
						  {"errCode": "UG0001", "errMsg": errconfig.errConfig['UG0001']})
	return render(request, 'UserGroup/index.html', {"errCode": "UG0000", "errMsg": errconfig.errConfig['UG0000']})


def user(request):
	error = 'success'
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')
		nickname = request.POST.get('nickname')
		level = request.POST.get('level')
		id_insert = UserGroup(username=username,
							  password=password,
							  nickname=nickname,
							  level=level,
							  create_time=datetime.time())
		try:
			id_insert.save()
		except Exception as e:
			error = e
		return HttpResponseRedirect('UserGroup/user/', {'error': error})
	return render(request, 'UserGroup/user.html')


def usercenter(request):
	return render(request, 'UserGroup/usercenter.html')


def operation_log(request):
	return render(request, 'UserGroup/usercenterlog.html')


def update_info(request):
	return render(request, 'UserGroup/usercenterupdateinfo.html')

# =================================Ajax==================================


def check_token(request):
	token = request.GET.get('usertoken')
	if Login_Check.check_token(token):
		userinfo = Login_Check.get_user_info(token, 'token')
		userinfo['error_no'] = 'UG0000'
		userinfo['error_msg'] = errconfig.errConfig['UG0000']
	else:
		userinfo = {
			'error_no': 'UG0003',
			'error_msg': errconfig.errConfig['UG0003']
		}
	return JsonResponse(userinfo, safe=False)


def check_auth(request):
	token = request.GET.get('usertoken')
	if Login_Check.check_auth(token, 99):
		userinfo = Login_Check.get_user_info(token, 'token')
		userinfo['error_no'] = 'UG0000'
		userinfo['error_msg'] = errconfig.errConfig['UG0000']
	else:
		userinfo = {
			'error_no': 'UG0004',
			'error_msg': errconfig.errConfig['UG0004']
		}
	return JsonResponse(userinfo, safe=False)


def sign_out(request):
	token = request.GET.get('usertoken')
	data = {}
	if Login_Check.check_token(token):
		if Login_Check.sign_out(token):
			data['error_no'] = 'UG0000'
			data['error_msg'] = errconfig.errConfig['UG0000']
		else:
			data['error_no'] = 'UG0005'
			data['error_msg'] = errconfig.errConfig['UG0005']
	else:
		data['error_no'] = 'UG0003'
		data['error_msg'] = errconfig.errConfig['UG0003']
	return JsonResponse(data, safe=False)