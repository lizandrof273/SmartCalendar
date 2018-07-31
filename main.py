import webapp2
import jinja2
import os
from google.appengine.api import users
import urllib
from google.appengine.ext import ndb

JINJA_ENVIRONMENT = jinja2.Environment(
    loader = jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions = ['jinja2.ext.autoescape'],
    autoescape=True)

class EnterInfoHandler(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()

        if user:
            auth_url = users.create_logout_url('/')
            greeting = 'logout'
        else:
            auth_url = users.create_login_url('/')
            greeting = 'login'
        welcome_template = JINJA_ENVIRONMENT.get_template('templates/index.html')
        self.response.write(welcome_template.render({'auth_url': auth_url, 'greeting':greeting}))
#class ShowCalendarHandler(webapp2.RequestHandler):
#    def post(self):
#        template_vars = {
#            'concrete': self.request.get('ConcreteEvents'),
#            'flexible': self.request.get('FlexibleEvents')
#        }
#        results_template = JINJA_ENVIRONMENT.get_template('template/results.html')
#        self.response.write(results_template.render(template_vars))


class Event(ndb.Model):
    organizer = ndb.StringProperty(required=True)
    title = ndb.StringProperty(required=True)

#Event(organizer=user.user_id(), title="CSSI Presentations")

app = webapp2.WSGIApplication([
    ('/', EnterInfoHandler),
], debug = True)
