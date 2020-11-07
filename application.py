from flask import Flask

# print a nice greeting.
def show_wiki(title = "Hello"):
    return '<iframe src="https://en.wikipedia.org/wiki/%s" width="2000" height="1500" frameborder="0"></iframe>\n' % title

#def show_wolfram(title = "Hello"):
#    return '<iframe src="https://www.wolframalpha.com/input/?i=%s" width="2000" height="1500" frameborder="0"></iframe>\n' % title


# some bits of text for the page.
header_text = '''
    <html>\n<head> <title>EB Flask Test</title> </head>\n<body>'''
instructions = '''
    <p><em>Hint</em>: This is a RESTful web service! With changes made. Append a title
    to the URL (for example: <code>/Thelonious</code>) to open(display). If Wiki then type "wiki-search_term", if Wolfram "wolfram-search_term. Only single words are allowed.'''
#dashboard_frame = '''<iframe src="https://en.wikipedia.org/wiki/Halloween"
home_link = '<p><a href="/">Back</a></p>\n'
footer_text = '</body>\n</html>'

# EB looks for an 'application' callable by default.
application = Flask(__name__)

# add a rule for the index page.
application.add_url_rule('/', 'index', (lambda: header_text + instructions + footer_text))

application.add_url_rule('/wiki-<title>', 'Wikipedia Search', (lambda title: header_text +
    show_wiki(title) + instructions + footer_text))

#application.add_url_rule('/wolfram-<title>', 'Wolfram Search', (lambda title: header_text +
#    show_wolfram(title) + instructions + footer_text))


# run the app.
if __name__ == "__main__":
    # Setting debug to True enables debug output. This line should be
    # removed before deploying a production app.
    application.debug = True
    application.run()
