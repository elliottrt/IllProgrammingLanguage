import ill_io as io
import ill_interpret as interpreter
import sys

def main():

	if len(sys.argv) < 2:
		io.error('Requires at least 1 argument.')
	file_path = sys.argv[1]
	mode = 'std' if len(sys.argv) >= 3 and sys.argv[2] == '-s' else 'ill'

	file_contents = io.load_file(file_path)

	if mode == 'std': interpreter.interpret_std(file_contents)
	elif mode == 'ill': interpreter.interpret_ill(file_contents)


if __name__ == '__main__':
	main()