# ecoding=utf-8
# Author: 翁彦彬 | Sven_Weng
# Email : sven_weng@wengyb.com
# Web   : http://wybblog.applinzi.com
from django.shortcuts import render
from django.http import JsonResponse
import json
import method
import errconfig
from LogRecord import logMethod
from UserGroup.method import Login
from models import Interface
api_manage = method.ApiManage()
logRecord = logMethod.LogOperate()
login = Login()


def index(request):

	return render(request, 'InterFaceManage/index.html')


def newinterface(request):
	if request.method == 'POST':
		rst_data = {}
		inputParas = []
		inputCount = 0
		returnParas = []
		returnCount = 0
		for key in request.POST:
			if key.startswith('inputparas'):
				inputCount += 1
			if key.startswith('returnparas'):
				returnCount += 1
		inputCount /= 6
		returnCount /= 5
		for x in range(inputCount):
			data = {
				'paraName': request.POST.get('inputparas[' + str(x) + '][paraName]'),
				'paraType': request.POST.get('inputparas[' + str(x) + '][paraType]'),
				'paraLength': request.POST.get('inputparas[' + str(x) + '][paraLength]'),
				'paraDoc': request.POST.get('inputparas[' + str(x) + '][paraDoc]'),
				'paraDefault': request.POST.get('inputparas[' + str(x) + '][paraDefault]'),
				'paraIsNeed': request.POST.get('inputparas[' + str(x) + '][paraIsNeed]')
			}
			inputParas.append(data)
		for x in range(returnCount):
			data = {
				'paraName': request.POST.get('returnparas['+ str(x) + '][paraName]'),
				'paraType': request.POST.get('returnparas['+ str(x) + '][paraType]'),
				'paraLength': request.POST.get('returnparas['+ str(x) + '][paraLength]'),
				'paraDoc': request.POST.get('returnparas['+ str(x) + '][paraDoc]'),
				'paraIsNeed': request.POST.get('returnparas['+ str(x) + '][paraIsNeed]')
			}
			returnParas.append(data)
		interface_data = {
			'api_status': request.POST.get('apistatus'),
			'belong_model': request.POST.get('belongmodel'),
			'belong_system': request.POST.get('belongsystem'),
			'request_method': request.POST.get('requestmethod'),
			'mock_url': request.POST.get('mockurl'),
			'request_head_doc': request.POST.get('requestheaddoc'),
			'api_name': request.POST.get('apiname'),
			'user_range': request.POST.get('userrange'),
			'api_url': request.POST.get('apiurl'),
			'right_return_doc': request.POST.get('rightreturndoc'),
			'err_return_doc': request.POST.get('errreturndoc'),
			'err_code': request.POST.get('errcode'),
			'api_version': request.POST.get('apiversion'),
			'developer': request.POST.get('developer'),
			'request_demo': request.POST.get('requestdemo'),
			'input_paras': json.dumps(inputParas),
			'return_paras': json.dumps(returnParas)
		}
		try:
			api_manage.create_api(interface_data)
			rst_data['error_no'] = 'IF0000'
			rst_data['error_info'] = errconfig.errConfig['IF0000']
			userinfo = login.get_user_info(interface_data['developer'], 'username')
			logData = {
				'username': userinfo['username'],
				'nickname': userinfo['nickname'],
				'operate_action': errconfig.actionConfig['AC0001']
			}
			logRecord.write_log(logData)
		except TypeError:
			rst_data['error_no'] = 'IF0001'
			rst_data['error_info'] = errconfig.errConfig['IF0001']
		except Exception:
			rst_data['error_no'] = 'IF0002'
			rst_data['error_info'] = errconfig.errConfig['IF0002']
		return JsonResponse(rst_data, safe=False)
	return render(request, 'InterFaceManage/newinterface.html')


def interface(request, api_id):
	api_info = Interface.objects.get(id=int(api_id))
	return render(request, 'InterFaceManage/interface.html', {'api_info': api_info})


def update_api(request, api_id):
	if request.method == 'POST':
		rst_data = {'ttt': 'ttt'}
		inputParas = []
		inputCount = 0
		returnParas = []
		returnCount = 0
		for key in request.POST:
			if key.startswith('inputparas'):
				inputCount += 1
			if key.startswith('returnparas'):
				returnCount += 1
		inputCount /= 6
		returnCount /= 5
		for x in range(inputCount):
			data = {
				'paraName': request.POST.get('inputparas[' + str(x) + '][paraName]'),
				'paraType': request.POST.get('inputparas[' + str(x) + '][paraType]'),
				'paraLength': request.POST.get('inputparas[' + str(x) + '][paraLength]'),
				'paraDoc': request.POST.get('inputparas[' + str(x) + '][paraDoc]'),
				'paraDefault': request.POST.get('inputparas[' + str(x) + '][paraDefault]'),
				'paraIsNeed': request.POST.get('inputparas[' + str(x) + '][paraIsNeed]')
			}
			inputParas.append(data)
		for x in range(returnCount):
			data = {
				'paraName': request.POST.get('returnparas[' + str(x) + '][paraName]'),
				'paraType': request.POST.get('returnparas[' + str(x) + '][paraType]'),
				'paraLength': request.POST.get('returnparas[' + str(x) + '][paraLength]'),
				'paraDoc': request.POST.get('returnparas[' + str(x) + '][paraDoc]'),
				'paraIsNeed': request.POST.get('returnparas[' + str(x) + '][paraIsNeed]')
			}
			returnParas.append(data)
		interface_data = {
			'api_status': request.POST.get('apistatus'),
			'belong_model': request.POST.get('belongmodel'),
			'belong_system': request.POST.get('belongsystem'),
			'request_method': request.POST.get('requestmethod'),
			'mock_url': request.POST.get('mockurl'),
			'request_head_doc': request.POST.get('requestheaddoc'),
			'api_name': request.POST.get('apiname'),
			'user_range': request.POST.get('userrange'),
			'api_url': request.POST.get('apiurl'),
			'right_return_doc': request.POST.get('rightreturndoc'),
			'err_return_doc': request.POST.get('errreturndoc'),
			'err_code': request.POST.get('errcode'),
			'api_version': request.POST.get('apiversion'),
			'developer': request.POST.get('developer'),
			'request_demo': request.POST.get('requestdemo'),
			'input_paras': json.dumps(inputParas),
			'return_paras': json.dumps(returnParas)
		}
		print interface_data
		try:
			api_manage.update_api(api_id, interface_data)  # 更新数据库
			rst_data['error_no'] = 'IF0000'
			rst_data['error_info'] = errconfig.errConfig['IF0000']
			userinfo = login.get_user_info(interface_data['developer'], 'username')
			logData = {
				'username': userinfo['username'],
				'nickname': userinfo['nickname'],
				'operate_action': errconfig.actionConfig['AC0002']
			}
			logRecord.write_log(logData)
		except Exception as e:
			print e
			rst_data['error_no'] = 'IF0002'
			rst_data['error_info'] = errconfig.errConfig['IF0002']
		return JsonResponse(rst_data, safe=False)

	api_info = Interface.objects.get(id=int(api_id))
	rst_info = {
		'api_version': api_info.ApiVersion,
		'api_name': api_info.ApiName,
		'api_status': api_info.ApiStatus,
		'belong_model': api_info.BelongModel,
		'belong_system': api_info.BelongSystem,
		'developer': api_info.Developer,
		'user_range': api_info.UserRange.replace('\n', '\\n'),
		'api_url': api_info.ApiUrl,
		'request_method': api_info.RequestMethod,
		'mock_url': api_info.MockUrl.replace('\n', '\\n'),
		'request_head_doc': api_info.RequestHeadDoc,
		'input_paras': api_info.InputParas,
		'request_demo': api_info.RequestDemo.replace('\n', '\\n'),
		'return_paras': api_info.ReturnParas,
		'right_return_doc': api_info.RightReturnDoc.replace('\n', '\\n'),
		'err_return_doc': api_info.ErrReturnDoc.replace('\n', '\\n'),
		'err_code': api_info.ErrCode.replace('\n', '\\n'),
		'id': api_id
	}

	return render(request, 'InterFaceManage/updateapi.html', {'api_info': rst_info})


def qry_api(request):
	return render(request, 'InterFaceManage/qryapi.html')

# ===============AJAX======================


def get_api_record(request):
	rst = []
	api_info = Interface.objects.all().order_by('-pk')[:20]
	for x in api_info:
		data = {
			'api_name': x.ApiName,
			'api_id': x.id,
		}
		rst.append(data)
	return JsonResponse(rst, safe=False)


def get_api(request):
	qry_method = request.GET.get('qry_method')
	qry_data = request.GET.get('qry_data')
	print qry_data
	try:
		data = api_manage.qry_api(qry_method, qry_data)
		return JsonResponse(data, safe=False)
	except Exception as e:
		print e