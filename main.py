from flask import Flask, Response, request
from routes import routingMap

app = Flask(__name__)

def addHeaders(response):
	response.headers['Access-Control-Allow-Origin'] = "*"
	response.headers['Access-Control-Allow-Headers'] = '*'
	response.headers['Access-Control-Allow-Methods'] = '*'
	
	response.headers['Content-type'] = 'application/json'

	return response

def e404():
	return Response("Not found", status = 404)

def e405():
	return Response("method not allowed", status = 405)

def e400():
	return Response("bad request", status = 400)

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def route(path):
	response = e404()

	if path in routingMap.keys():
		if request.method in routingMap[path]['method']:
			response = routingMap[path]['function'](request)
		else:
			response = e400()

	return addHeaders(response)

app.run(host = "0.0.0.0", debug = True)
