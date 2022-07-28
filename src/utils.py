from exceptions import *

class Option:
	def __init__(self, flags: list[str], description: str, binding: callable):
		self.flags = flags
		self.description = description
		self.binding = binding

def readbinary(path: str) -> bytes:
	with open(path, "rb") as f:
		return f.read() if f else b""

def readascii(path: str) -> str:
	with open(path, "r") as f:
		return f.read()	if f else ""

def getflagargument(args: list[str], flags: list[str]) -> str:
	intersection = [x for x in args if x in flags]
	if len(intersection) == 0:
		raise ArgumentNotFoundException
	return args[args.index(intersection[0]) + 1]