import web

render = web.template.render('templates/')

urls = (
'/(.*)', 'hello'
)

app = web.application(urls, globals())

class hello:
	def GET(self, name):
	    name = 'Bob'
	    return render.index()

if __name__ == "__main__":
	app.run()
