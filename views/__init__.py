import HelloWorld
from HelloWorld import HelloWorldHandler

import PopulateTestData
from PopulateTestData import PopulateTestDataHandler

__all__ = (
  "routes",
  "HelloWorldHandler",
  "PopulateTestDataHandler",
)

routes = [ ] + HelloWorld.routes + PopulateTestData.routes
