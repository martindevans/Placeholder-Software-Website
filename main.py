from google.appengine.ext import webapp
from google.appengine.ext.webapp import util
from google.appengine.ext.webapp import template
import os

class BaseHandler(webapp.RequestHandler):
    def render(self, filepath, template_values):
        path = os.path.join(os.path.dirname(__file__), filepath)
	html = template.render(path, template_values)

	return html.decode("utf-8")
    
    def get(self, template_values):
        self.response.out.write(self.render('django/index.html', template_values))

class MainHandler(BaseHandler):
    def get(self):
        template_values = {
            "content": BaseHandler.render(self, 'django/main-content.html', {}),
        }

        BaseHandler.get(self, template_values)

class AboutHandler(BaseHandler):
    def get(self):
        template_values = {
            "content": BaseHandler.render(self, 'django/about-content.html', {})
        }

        BaseHandler.get(self, template_values)

class TeamHandler(BaseHandler):
    def get(self):
        template_values = {
            "content": BaseHandler.render(self, 'django/team-content.html', {}),
            "header_links": '<link rel="stylesheet" type="text/css" href="css/team.css" />'
        }

        BaseHandler.get(self, template_values)

def main():
    application = webapp.WSGIApplication([('/about', AboutHandler),
                                          ('/team', TeamHandler),
                                          ('.*', MainHandler)],
                                         debug=True)
    util.run_wsgi_app(application)


if __name__ == '__main__':
    main()
