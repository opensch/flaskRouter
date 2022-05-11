from flask import Response

def hello(request):
	return Response("YAY")

def page2(request):
	return Response(request.headers['User-Agent'])
