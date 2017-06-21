from tornado.ioloop import IOLoop
from tornado.web import Application, url

import myutil
from controller import MainHandler

def make_app():
    return Application([
        url(r"/", MainHandler)
    ])

if __name__ == "__main__":
    fs = myutil.FastStop()
    fs.enable()
    app = make_app()
    app.listen(8080)
    IOLoop.current().start()
