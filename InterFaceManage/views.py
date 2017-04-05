# ecoding=utf-8
# Author: 翁彦彬 | Sven_Weng
# Email : sven_weng@wengyb.com
# Web   : http://wybblog.applinzi.com
from django.shortcuts import render
from django.http import JsonResponse
import json
import method
import errconfig
api_manage = method.ApiManage()


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
		except TypeError:
			rst_data['error_no'] = 'IF0001'
			rst_data['error_info'] = errconfig.errConfig['IF0001']
		except Exception:
			rst_data['error_no'] = 'IF0002'
			rst_data['error_info'] = errconfig.errConfig['IF0002']
		return JsonResponse(rst_data, safe=False)
	return render(request, 'InterFaceManage/newinterface.html')
