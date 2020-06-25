from cgi import parse_qs
from calc_template import html

def application(environ, start_response):
        d = parse_qs(environ['QUERY_STRING'])
        a = d.get('a', [''])[0]
        b = d.get('b', [''])[0]
        sum, mul = 0, 0
	try:
                a, b = int(a), int(b)
                sum = a + b
                mul = a * b
	except ValuError:
		sum = "None"
		mul = "None"
	response_body = html % {'Sum':sum, 'Mul':mul}
        start_response('200 OK', [
                ('Content-Type', 'text/html'),
                ('Content-Length', str(len(response_body)))
        ])
        return [response_body]

