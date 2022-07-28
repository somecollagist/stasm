import utils

def disassemble(args: list[str], flags: list[str]):
	content = utils.readbinary(utils.getflagargument(args, option.flags))
	print(content)
	pass

option = utils.Option(["-d", "--disassemble"], "Disassembles a file", disassemble)