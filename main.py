import webapp2
import jinja2
import os
from google.appengine.api import users
import urllib
from google.appengine.ext import ndb

user = users.get_current_user()

if user:
    logout_url = users.create_logout_url('/')
    greeting = ('Welcome! (<a href="%s">sign out</a>)'
                % logout_url)
else:
    login_url = users.create_login_url('/')
    greeting = '<a href="%s">Sign in</a>' % (login_url,)

JINJA_ENVIRONMENT = jinja2.Environment(
    loader = jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions = ['jinja2.ext.autoescape'],
    autoescape=True)

class EnterInfoHandler(webapp2.RequestHandler):
    def get(self):
        welcome_template = JINJA_ENVIRONMENT.get_template('templates/index.html')
        self.response.write(welcome_template.render())

#class ShowCalendarHandler(webapp2.RequestHandler):
#    def post(self):
#        template_vars = {
#            'concrete': self.request.get('ConcreteEvents'),
#            'flexible': self.request.get('FlexibleEvents')
#        }
#        results_template = JINJA_ENVIRONMENT.get_template('template/results.html')
#        self.response.write(results_template.render(template_vars))

user.user_id()

class Event(ndb.Model):
    organizer = ndb.StringProperty(required=True)
    title = ndb.StringProperty(required=True)


event_date = EventDate
event_name = EventName



params = urllib.urlencode({'text': event_name, 'dates': event_date,})
new_url = urllib.urlopen("https://www.google.com/calendar/render?action=TEMPLATE&")

Event(organizer=user.user_id(), title="CSSI Presentations")

app = webapp2.WSGIApplication([
    ('/', EnterInfoHandler),
], debug = True)
