import utils

def assemble(args: list[str], flags: list[str]):
	content = utils.readascii(utils.getflagargument(args, option.flags))
	pass

option = utils.Option(["-a", "--assemble"], "Assembles a file", assemble)