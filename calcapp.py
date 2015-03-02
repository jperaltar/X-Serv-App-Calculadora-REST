#!/usr/bin/python
# -*- coding: utf-8 -*-

import webapp
import sys
import calculadora


class Operation(webapp.app):
    op = None
    state = None

    def parse(self, request, rest):
        splitted_req = request.split(' ')
        verb = splitted_req[0]
        resource = splitted_req[1][1:]
        body = request.split('\r\n\r\n')[1]
        return (verb, resource, body)

    def process(self, parsedrequest):
        verb = parsedrequest[0]
        resource = parsedrequest[1]
        body = parsedrequest[2]

        if verb == "PUT":
            self.op = body
            if len(self.op) != 3:
                reply = "Bad usage: factor1 operator factor2"
                html_code = "400 Bad Request"
            else:
                first = int(self.op[0])
                operation = self.op[1]
                second = int(self.op[2])
                reply = "<h1>Got It!</h1>"
                html_code = "200 OK"
                if(operation == "+"):
                    self.state = calculadora.add(first, second)
                elif(operation == "-"):
                    self.state = calculadora.sub(first, second)
                elif(operation == "*"):
                    self.state = calculadora.mult(first, second)
                elif(operation == "/"):
                    self.state = calculadora.div(first, second)
                else:
                    reply = "<h1>Operation not available</h1>"
                    html_code = "404 Not Found"

        elif verb == "GET":
            if resource == self.op:
                html_code = "200 OK"
                reply = "The result is: " + str(self.state)
            else:
                html_code = "400 Bad Request"
                reply = "Bad request"
        else:
            html_code = "400 Bad Request"
            reply = "Not available request"

        return (html_code, "<html><body>" + reply +
                "</body></html>\r\n")

if __name__ == "__main__":
    try:
        operation = Operation()
        testWebApp = webapp.webApp("localhost", 1234, {'/': operation})
    except KeyboardInterrupt:
        print "Finishing service"
        sys.exit()
