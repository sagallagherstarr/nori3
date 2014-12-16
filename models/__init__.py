import sys

print("sys.path is %s", sys.path)

from MyModels import (
  TodoList,
  User,
)

__all__ = [
  "TodoList",
  "User",
]
