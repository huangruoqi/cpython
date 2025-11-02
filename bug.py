from collections import UserString

us = UserString("hello world")
sub = UserString("world")

assert us.rfind(sub) == us.rfind(sub.data)
assert us.rindex(sub) == us.rindex(sub.data)
