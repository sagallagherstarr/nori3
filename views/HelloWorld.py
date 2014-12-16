from tornado.web import RequestHandler

class HelloWorldHandler(RequestHandler):
 # @gen.coroutine
  def get(self):
    self.write("Hello World!")

routes = [ (r"/helloworld", HelloWorldHandler) ]