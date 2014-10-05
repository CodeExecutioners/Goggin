import os
import urllib
import webapp2
import jinja2

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)
	
class NoPage(webapp2.RequestHandler):
   def get(self):
        #self.response.write('Hello world!')
		template_values ={}
		template = JINJA_ENVIRONMENT.get_template('templates/no-sidebar.html')
		self.response.write(template.render(template_values))

app = webapp2.WSGIApplication([('/no-sidebar', NoPage)],
                              debug=True)