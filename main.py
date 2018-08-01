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
class ShowCalendarHandler(webapp2.RequestHandler):
    def post(self):
        days_of_week = self.request.get_all('daysOfWeek')
        flextime = self.request.get('Eventamount')
        conc_start_time = self.request.get('EventStartTime')
        conc_end_time = self.request.get('EventEndTime')
        event_date = self.request.get('EventDate')
        flex_event_freq = self.request.get('EventFreq')
        print ("************ REQUEST " + conc_start_time)
        template_vars = {
            'monday': self.request.get('Monday'),
            'tuesday': self.request.get('Tuesday'),
            'wednesday': self.request.get('Wednesday'),
            'thursday': self.request.get('Thursday'),
            'friday': self.request.get('Friday'),
            'saturday': self.request.get('Saturday'),
            'sunday': self.request.get('Sunday'),
            'url': "www"
        }
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
        if current_day_of_week == 'Monday':
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

        dict_mon = {
        "0": "",
        "1": "",
        "2": "",
        "3": "",
        "4": "",
        "5": "",
        "6": "",
        "7": "",
        "8": "",
        "9": "",
        "10": "",
        "11": "",
        "12": "",
        "13": "",
        "14": "",
        "15": "",
        "16": "",
        "17": "",
        "18": "",
        "19": "",
        "20": "",
        "21": "",
        "22": "",
        "23": "",
        "24": "",
        }

        dict_tues = {
        "0": "",
        "1": "",
        "2": "",
        "3": "",
        "4": "",
        "5": "",
        "6": "",
        "7": "",
        "8": "",
        "9": "",
        "10": "",
        "11": "",
        "12": "",
        "13": "",
        "14": "",
        "15": "",
        "16": "",
        "17": "",
        "18": "",
        "19": "",
        "20": "",
        "21": "",
        "22": "",
        "23": "",
        "24": "",
        }

        dict_wed = {
        "0": "",
        "1": "",
        "2": "",
        "3": "",
        "4": "",
        "5": "",
        "6": "",
        "7": "",
        "8": "",
        "9": "",
        "10": "",
        "11": "",
        "12": "",
        "13": "",
        "14": "",
        "15": "",
        "16": "",
        "17": "",
        "18": "",
        "19": "",
        "20": "",
        "21": "",
        "22": "",
        "23": "",
        "24": "",
        }

        dict_thur = {
        "0": "",
        "1": "",
        "2": "",
        "3": "",
        "4": "",
        "5": "",
        "6": "",
        "7": "",
        "8": "",
        "9": "",
        "10": "",
        "11": "",
        "12": "",
        "13": "",
        "14": "",
        "15": "",
        "16": "",
        "17": "",
        "18": "",
        "19": "",
        "20": "",
        "21": "",
        "22": "",
        "23": "",
        "24": "",
        }

        dict_fri = {
        "0": "",
        "1": "",
        "2": "",
        "3": "",
        "4": "",
        "5": "",
        "6": "",
        "7": "",
        "8": "",
        "9": "",
        "10": "",
        "11": "",
        "12": "",
        "13": "",
        "14": "",
        "15": "",
        "16": "",
        "17": "",
        "18": "",
        "19": "",
        "20": "",
        "21": "",
        "22": "",
        "23": "",
        "24": "",
        }

        dict_sat = {
        "0": "",
        "1": "",
        "2": "",
        "3": "",
        "4": "",
        "5": "",
        "6": "",
        "7": "",
        "8": "",
        "9": "",
        "10": "",
        "11": "",
        "12": "",
        "13": "",
        "14": "",
        "15": "",
        "16": "",
        "17": "",
        "18": "",
        "19": "",
        "20": "",
        "21": "",
        "22": "",
        "23": "",
        "24": "",
        }

        dict_sun = {
        "0": "",
        "1": "",
        "2": "",
        "3": "",
        "4": "",
        "5": "",
        "6": "",
        "7": "",
        "8": "",
        "9": "",
        "10": "",
        "11": "",
        "12": "",
        "13": "",
        "14": "",
        "15": "",
        "16": "",
        "17": "",
        "18": "",
        "19": "",
        "20": "",
        "21": "",
        "22": "",
        "23": "",
        "24": "",
        }

        for i in range(25):
            if dict_mon == "" and flextime == 1:
                dict_mon[str(i)] = "event"
            elif dict_mon == "" and flextime == 2:
                if i+1 == None:
                    dict_mon[str(i)] = "event"
            elif dict_mon != "" and flextime == 3:
                if i+1 == None:
                    dict_mon[str(i)] = "event"

        for i in range(25):
            if dict_tues == "" and flextime == 1:
                dict_tues[str(i)] = "event"
            elif dict_tues == "" and flextime == 2:
                if i+1 == None:
                    dict_tues[str(i)] = "event"
            elif dict_tues != "" and flextime == 3:
                if i+1 == None:
                    dict_tues[str(i)] = "event"

        for i in range(25):
            if dict_wed == "" and flextime == 1:
                dict_wed[str(i)] = "event"
            elif dict_wed == "" and flextime == 2:
                if i+1 == None:
                    dict_wed[str(i)] = "event"
            elif dict_wed != "" and flextime == 3:
                if i+1 == None:
                    dict_wed[str(i)] = "event"

        for i in range(25):
            if dict_thur == "" and flextime == 1:
                dict_mon[str(i)] = "event"
            elif dict_thur == "" and flextime == 2:
                if i+1 == None:
                    dict_thur[str(i)] = "event"
            elif dict_mon != "" and flextime == 3:
                if i+1 == None:
                    dict_thur[str(i)] = "event"

        for i in range(25):
            if dict_fri == "" and flextime == 1:
                dict_fri[str(i)] = "event"
            elif dict_fri== "" and flextime == 2:
                if i+1 == None:
                    dict_fri[str(i)] = "event"
            elif dict_fri != "" and flextime == 3:
                if i+1 == None:
                    dict_fri[str(i)] = "event"

        for i in range(25):
            if dict_sat == "" and flextime == 1:
                dict_sat[str(i)] = "event"
            elif dict_sat == "" and flextime == 2:
                if i+1 == None:
                    dict_sat[str(i)] = "event"
            elif dict_sat != "" and flextime == 3:
                if i+1 == None:
                    dict_sat[str(i)] = "event"

        for i in range(25):
            if dict_sun == "" and flextime == 1:
                dict_sun[str(i)] = "event"
            elif dict_sun == "" and flextime == 2:
                if i+1 == None:
                    dict_sun[str(i)] = "event"
            elif dict_sun != "" and flextime == 3:
                if i+1 == None:
                    dict_sun[str(i)] = "event"
        results_template = JINJA_ENVIRONMENT.get_template('template/results.html')
        self.response.write(results_template.render(template_vars))


class Event(ndb.Model):
    organizer = ndb.StringProperty(required=True)
    title = ndb.StringProperty(required=True)

#Event(organizer=user.user_id(), title="CSSI Presentations")

app = webapp2.WSGIApplication([
    ('/', EnterInfoHandler),
    ('/ShowCalendar', ShowCalendarHandler)
], debug = True)
