import webapp2
import jinja2
import os
from google.appengine.api import users
import urllib
from google.appengine.ext import ndb
import time
import datetime

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

current_day_of_week = datetime.date.today().strftime("%A")
  if current_day_of_week == 'Sunday':
      date = datetime.datetime.now().strftime("%y%m%d")
      mon_date = int(date) +1
      tue_date = int(date) +2
      wed_date = int(date) +3
      thur_date = int(date) +4
      fri_date = int(date) +5
      sat_date = int(date) +6
      sun_date = date
  if current_day_of_week == 'Monday:
      date = datetime.datetime.now().strftime("%y%m%d")
      mon_date = date
      tue_date = int(date) +1
      wed_date = int(date) +2
      thur_date = int(date) +3
      fri_date = int(date) +4
      sat_date = int(date) +5
      sun_date = int(date) +6
  if current_day_of_week == 'Tuesday':
      date = datetime.datetime.now().strftime("%y%m%d")
      mon_date = int(date) +6
      tue_date = date
      wed_date = int(date) +1
      thur_date = int(date) +2
      fri_date = int(date) +3
      sat_date = int(date) +4
      sun_date = int(date) +5
  if current_day_of_week == 'Wednesday':
      date = datetime.datetime.now().strftime("%y%m%d")
      mon_date = int(date) +5
      tue_date = int(date) +6
      wed_date = date
      thur_date = int(date) +1
      fri_date = int(date) +2
      sat_date = int(date) +3
      sun_date = int(date) +4
  if current_day_of_week == 'Thursday':
      date = datetime.datetime.now().strftime("%y%m%d")
      mon_date = int(date) +4
      tue_date = int(date) +5
      wed_date = int(date) +6
      thur_date = date
      fri_date = int(date) +1
      sat_date = int(date) +2
      sun_date = int(date) +3
  if current_day_of_week == 'Friday':
      date = datetime.datetime.now().strftime("%y%m%d")
      mon_date = int(date) +3
      tue_date = int(date) +4
      wed_date = int(date) +5
      thur_date = int(date) +6
      fri_date = date
      sat_date = int(date) +1
      sun_date = int(date) +2
  if current_day_of_week == 'Saturday':
      date = datetime.datetime.now().strftime("%y%m%d")
      mon_date = int(date) +2
      tue_date = int(date) +3
      wed_date = int(date) +4
      thur_date = int(date) +5
      fri_date = int(date) +6
      sat_date = date
      sun_date = int(date) +1
app = webapp2.WSGIApplication([
    ('/', EnterInfoHandler),
], debug = True)
