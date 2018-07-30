import webapp2
import jinja2
import os

JINJA_ENVIRONMENT = jinja2.Environment(
    loader = jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions = ['jinja2.ext.autoescape'],
    autoescape=True)

class EnterInfoHandler(webapp2.RequestHandler):
    def get(self):
        welcome_template = JINJA_ENVIRONMENT.get_template('templates/index.html')
        self.response.write(welcome_template.render())

class ShowCalendarHandler(webapp2.RequestHandler):
    def post(self):
        template_vars = {
            'concrete': self.request.get('ConcreteEvents'),
            'flexible': self.request.get('FlexibleEvents')
        }
        results_template = JINJA_ENVIRONMENT.get_template('template/results.html')
        self.response.write(results_template.render(template_vars))

app = webapp2.WSGIApplication([
    ('/', EnterInfoHandler),
    ('/calendar', ShowCalendarHandler),
], debug = True)
