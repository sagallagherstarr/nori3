import HelloWorld
from HelloWorld import HelloWorldHandler

__all__ = (
  "routes",
  "HelloWorldHandler",
)

routes = [ ] + HelloWorld.routes
