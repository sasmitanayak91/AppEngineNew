#!/usr/bin/env python

import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('Lets Test the autodeployment')

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)