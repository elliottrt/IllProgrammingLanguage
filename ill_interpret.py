import ill_io as io
import random, sys

def call_tree(calls: list, data_width: int):
	data_p, data_len = 0, 30000
	data = [0] * data_len
	call_count, call_p = len(calls), 0

	while call_p < call_count:
		match calls[call_p]:
			case ('IIII' | '~'): # get input as int
				data[data_p] = int(input())

			case ('IIIl' | '!'): # print integer
				# this is here because I am nice
				print(data[data_p])

			case ('IIlI' | '_'): # sets all cell values to the current cell
				cur_cell_v = data[data_p]
				data = [cur_cell_v] * data_len

			case ('IIll' | '|'): # data load
				if data_width == 1:
					call_p += 1
					while calls[call_p] != '|':
						data[data_p] = ord(calls[call_p])
						data_p += 1
						call_p += 1
				if data_width == 4:
					while True:
						call_p += 1
						bits = calls[call_p]
						call_p += 1
						bits += calls[call_p]
						bits = bits.replace('I', '1').replace('l', '0')

						if bits == '00000000': break

						# print(bits)

						# convert 2 calls into a single character
						# and put it in the cell

						data[data_p] = int(bits, 2)
						data_p += 1
				data[data_p] = 0			

			case ('IlII' | ';'): # string input
				inp = input(';') + '\0'
				for char in inp:
					data[data_p] = ord(char)
					data_p += 1

			case ('IlIl' | '#'): # random number from 0 to data[data_p]
				# for random numbers
				data[data_p] = random.randint(0, data[data_p])

			case ('IllI' | '$'): # get index
				# set the value of the current cell to its index
				data[data_p] = data_p

			case ('Illl' | '^'): # jump
				# jump to the cell with the index of
				# the current cell
				data_p = data[data_p]

			case ('lIII' | ']'): # close bracket
				if data[data_p] != 0:
					depth = 1
					tmp_call_p = call_p
					while depth != 0:
						tmp_call_p -= 1
						if calls[tmp_call_p] == 'lIII' or calls[tmp_call_p] == ']': 
							depth += 1
						if calls[tmp_call_p] == 'lIIl' or calls[tmp_call_p] == '[':
							depth -= 1
					call_p = tmp_call_p

			case ('lIIl' | '['): # open bracket
				if data[data_p] == 0:
					depth = 1
					tmp_call_p = call_p
					while depth != 0:
						tmp_call_p += 1
						if calls[tmp_call_p] == 'lIIl' or calls[tmp_call_p] == '[': 
							depth += 1
						if calls[tmp_call_p] == 'lIII' or calls[tmp_call_p] == ']':
							depth -= 1
					call_p = tmp_call_p

			case ('lIlI' | ','): # comma 
				input_char = input(',')
				if len(input_char) != 1:
					io.error('Input longer than 1.')
				data[data_p] = ord(input_char)

			case ('lIll' | '.'): # period
				# woo!
				print(chr(data[data_p]), end='')

			case ('llII' | '-'): # minus 
				# no limits babyyyyyy
				data[data_p] -= 1

			case ('llIl' | '+'): # plus
				# i'm not limiting this bc python probably will
				data[data_p] += 1

			case ('lllI' | '<'): # left arrow 
				if data_p > 0: data_p -= 1
				else: data_p = data_len - 1

			case ('llll' | '>'): # right arrow 
				if data_p + 1 < data_len: data_p += 1
				else: data_p = 0

			case (' '): # things that are fine but shouldn't be removed
				pass

			case (_):
				# shouldn't get here, but just in case
				io.error(f'Invalid instruction {calls[call_p]}.')
		call_p += 1

def interpret_ill(code: str):
	code = code.replace('\n', '')
	code_length = len(code)
	# make sure that the code only has 4 bits per instruction
	if code_length % 4 != 0:
		io.error('Code length is not divisible by 4.')
	code_index, calls = 0, []
	while code_index < code_length:
		inst = code[code_index:code_index+4]
		code_index += 4
		calls.append(inst)
	call_tree(calls, 4)

def interpret_std(code: str):
	code = code.replace('\n', '')
	code_length = len(code)
	code_index, calls = 0, []
	while code_index < code_length:
		inst = code[code_index]
		code_index += 1
		calls.append(inst)
	call_tree(calls, 1)