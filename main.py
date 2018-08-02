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
        event_name = self.request.get('EventName')
        days_of_week = self.request.get_all('daysOfWeek')
        flextime = self.request.get('Eventamount')
        conc_start_time = str(self.request.get('EventStartTime'))
        conc_end_time = str(self.request.get('EventEndTime'))
        event_date = str(self.request.get('EventDate'))
        flex_event_freq = self.request.get('EventFreq')
        print ("********** REQUEST " + conc_start_time)

        if flextime != '1' or flextime != '2':
            flextime = "0"
            flex_event_freq = "0"

        #if flextime == "1" or flextime =="2":
            #conc_start_num = "02:00"
            #conc_end_num = "03:00"


        if flextime == "0":
            conc_start_time = conc_start_time[0:2]
            conc_end_time = conc_end_time[0:2]
            conc_start_num = int(conc_start_time)
            conc_end_num = int(conc_end_time)

            if conc_start_num > 12:
                conc_start_num = str(((conc_start_num - 12) *100) -100)

            if conc_end_num > 12:
                conc_end_num = str(((conc_end_num - 12) *100) -100)

            if conc_start_num == 12:
                conc_start_num = str(conc_start_num)

            start_time_url = conc_start_num[0:2] + conc_start_num[3:5]
            end_time_url = conc_end_num[0:2] + conc_end_num[3:5]
            date_url = event_date[0:4] + event_date[5:7] + event_date[8:10]

        params = urllib.urlencode({'text': event_name})

        #start_date_time = datetime.datetime.strptime(str(event_date) + "T" + str(conc_start_time), '%Y-%m-%dT%H:%M')
        #end_date_time = datetime.datetime.strptime(str(event_date) + "T" + str(conc_end_time), '%Y-%m-%dT%H:%M')
        if flextime == "0":
            new_url = "https://www.google.com/calendar/render?action=TEMPLATE&" + params + "&dates=" + date_url + "T2" + start_time_url + "000Z/" + date_url + "T2" + end_time_url + "000Z"
        if flextime == '1':
            new_url = "https://www.google.com/calendar/render?action=TEMPLATE&" + params + "&dates=20180807T240000Z/20180807T250000Z"
        if flextime == '2':
             new_url = "https://www.google.com/calendar/render?action=TEMPLATE&" + params + "&dates=20180809T250000Z/20180809T270000Z"
        template_vars = {
            'url': new_url
        }
        results_template = JINJA_ENVIRONMENT.get_template('templates/results.html')
        self.response.write(results_template.render(template_vars))


class Event(ndb.Model):
    organizer = ndb.StringProperty(required=True)
    title = ndb.StringProperty(required=True)

#Event(organizer=user.user_id(), title="CSSI Presentations")

app = webapp2.WSGIApplication([
    ('/', EnterInfoHandler),
    ('/ShowCalendar', ShowCalendarHandler)
], debug = True)


#current_day_of_week = datetime.date.today().strftime("%A")
#if current_day_of_week == 'Sunday':
#      date = datetime.datetime.now().strftime("%y%m%d")
#      mon_date = int(date) +1
#      tue_date = int(date) +2
#      wed_date = int(date) +3
#      thur_date = int(date) +4
#      fri_date = int(date) +5
#      sat_date = int(date) +6
#      sun_date = date
#if current_day_of_week == 'Monday':
#      date = datetime.datetime.now().strftime("%y%m%d")
#      mon_date = date
#      tue_date = int(date) +1
#      wed_date = int(date) +2
#      thur_date = int(date) +3
#      fri_date = int(date) +4
#      sat_date = int(date) +5
#      sun_date = int(date) +6
#if current_day_of_week == 'Tuesday':
#      date = datetime.datetime.now().strftime("%y%m%d")
#      mon_date = int(date) +6
#      tue_date = date
#      wed_date = int(date) +1
#      thur_date = int(date) +2
#      fri_date = int(date) +3
#      sat_date = int(date) +4
#      sun_date = int(date) +5
#if current_day_of_week == 'Wednesday':
#      date = datetime.datetime.now().strftime("%y%m%d")
#      mon_date = int(date) +5
#      tue_date = int(date) +6
#      wed_date = date
#      thur_date = int(date) +1
#      fri_date = int(date) +2
#      sat_date = int(date) +3
#      sun_date = int(date) +4
#if current_day_of_week == 'Thursday':
#      date = datetime.datetime.now().strftime("%y%m%d")
#      mon_date = int(date) +4
#      tue_date = int(date) +5
#      wed_date = int(date) +6
#      thur_date = date
#      fri_date = int(date) +1
#      sat_date = int(date) +2
#      sun_date = int(date) +3
#if current_day_of_week == 'Friday':
#      date = datetime.datetime.now().strftime("%y%m%d")
#      mon_date = int(date) +3
#      tue_date = int(date) +4
#      wed_date = int(date) +5
#      thur_date = int(date) +6
#      fri_date = date
#      sat_date = int(date) +1
#      sun_date = int(date) +2
#if current_day_of_week == 'Saturday':
#      date = datetime.datetime.now().strftime("%y%m%d")
#      mon_date = int(date) +2
#      tue_date = int(date) +3
#      wed_date = int(date) +4
#      thur_date = int(date) +5
#      fri_date = int(date) +6
#      sat_date = date
#      sun_date = int(date) +1

#dict_mon = {
#"0": "",
#"1": "",
#"2": "",
#"3": "",
#"4": "",
#"5": "",
#"6": "",
#"7": "",
#"8": "",
#"9": "",
#"10": "",
#"11": "",
#"12": "",
#"13": "",
#"14": "",
#"15": "",
#"16": "",
#"17": "",
#"18": "",
#"19": "",
#"20": "",
#"21": "",
#"22": "",
#"23": "",
#"24": "",
#}

#dict_tues = {
#"0": "",
#"2": "",
#"3": "",
#"4": "",
#"5": "",
#"6": "",
#"7": "",
#8": "",
#"9": "",
#"10": "",
#"11": "",
#"12": "",
#"13": "",
#"14": "",
#"15": "",
#"16": "",
#"17": "",
#"18": "",
#"19": "",
#"20": "",
#"21": "",
#"22": "",
#"23": "",
#"24": "",
#}

#dict_wed = {
#"0": "",
#"1": "",
#"2": "",
#"3": "",
#"4": "",
#"5": "",
#"6": "",
#"7": "",
#"8": "",
#"9": "",
#"10": "",
#"11": "",
#"12": "",
#"13": "",
#"14": "",
#"15": "",
#"16": "",
#"17": "",
#"18": "",
#"19": "",
#"20": "",
#"21": "",
#"22": "",
#"23": "",
#"24": "",
#}

#"0": "",
#"1": "",
#"2": "",
#"3": "",
#"4": "",
#"5": "",
#"6": "",
#"7": "",
#"8": "",
#"9": "",
#"10": "",
#"11": "",
#"12": "",
#"13": "",
#"14": "",
#"15": "",
#"16": "",
#"17": "",
#"18": "",
#"19": "",
#"20": "",
#"21": "",
#"22": "",
#"23": "",
#"24": "",
#}

#dict_fri = {
#"0": "",
#"1": "",
#"2": "",
#"3": "",
#"4": "",
#"5": "",
#"6": "",
#"7": "",
#"8": "",
#"9": "",
#"10": "",
#"11": "",
#"12": "",
#"13": "",
#"14": "",
#"15": "",
#"16": "",
#"17": "",
#"18": "",
#"19": "",
#"20": "",
#"21": "",
#"22": "",
#"23": "",
#"24": "",
#}

#dict_sat = {
#"0": "",
#"1": "",
#"2": "",
#"3": "",
#"4": "",
#"5": "",
#"6": "",
#"7": "",
#"8": "",
#"9": "",
#"10": "",
#"11": "",
#"12": "",
#"13": "",
