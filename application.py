from flask import Flask

# print a nice greeting.
def say_hello(title = "Hello"):
    return '<iframe src="https://en.wikipedia.org/wiki/%s" width="1200" height="500" frameborder="0"></iframe>\n' % title

# some bits of text for the page.
header_text = '''
    <html>\n<head> <title>EB Flask Test</title> </head>\n<body>'''
instructions = '''
    <p><em>Hint</em>: This is a RESTful web service! With changes made. Append a title
    to the URL (for example: <code>/Thelonious</code>) to open(display) its wikipedia page</p>\n'''
#dashboard_frame = '''<iframe src="https://en.wikipedia.org/wiki/Halloween"
home_link = '<p><a href="/">Back</a></p>\n'
footer_text = '</body>\n</html>'

# EB looks for an 'application' callable by default.
application = Flask(__name__)

# add a rule for the index page.
application.add_url_rule('/', 'index', (lambda: header_text +
    say_hello() + instructions + footer_text))

application.add_url_rule('/<title>', 'Wikipedia Search', (lambda title: header_text +
    say_hello(title) + instructions + footer_text))
# display a dashboard
#application.add_url_rule('/d', 'dashboard', (lambda:
#    header_text + dashboard_frame + home_link + footer_text))

# run the app.
if __name__ == "__main__":
    # Setting debug to True enables debug output. This line should be
    # removed before deploying a production app.
    application.debug = True
    application.run()
