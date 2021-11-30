def load_file(filepath: str) -> str:
	with open(filepath, 'r') as file:
		contents = file.read()
	return contents

def print_ill_char(char: str) -> None:
	if len(char) != 1: return
	code = ord(char)
	
	for c in range(7, -1, -1): 
		print('I' if (code >> c) & 1 else 'l', end='')

def print_ill(string: str) -> None:
	print(string)
	# for char in string: print_ill_char(char)

def error(info):
	print()
	print_ill(f'ERROR: {info}')
	print('\n')
	exit(1)