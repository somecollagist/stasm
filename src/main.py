import sys
import assembler
import disassembler
from utils import Option

def helper(args: list[str], flags: list[str]):
	print("STASM - x86 Assembler and Disassembler")
	print("https://github.com/somecollagist/stasm")
	print("Licensed under GPL-3")
	print()

	output = []
	max_length = 0
	for x in [*options, *modifiers]:
		flag_length = len(", ".join(x.flags))
		max_length =  flag_length if flag_length > max_length else max_length
		output.append([
			", ".join(x.flags),
			x.description
		])
	for x in output:
		print(f"{str.ljust(x[0], max_length)} : {x[1]}")

options = [
	Option(["-h", "--help"], "Help for this tool", helper),
	assembler.option,
	disassembler.option
]

## These shouldn't be run
modifiers = [
	Option(["-v", "--verbose"], "(Dis)assembles a file in verbose mode", helper)
]

def main(args):
	flags = [x for x in args if x.startswith("-")]
	if(len(args) > 0):
		for x in options:
			if args[0] in x.flags:
				x.binder(args, flags)
		print(f"Unknown option {args[0]}")
	else:
		helper(args, flags)

if __name__ == "__main__":
	main(sys.argv[1:])