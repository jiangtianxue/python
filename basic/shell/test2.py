import argparse

def main():
	print('liurun')
	print('the name of this person is {0}'.format(flags.name))
	print('the age of this person is {0}'.format(flags.age))
	print('the weight of this person is {0}'.format(flags.weight))



parser = argparse.ArgumentParser()

parser.add_argument(
	'--name',
	type=str,
	default='liurun',
	help='the name of this person.'
	)

parser.add_argument(
	'--age',
	type=int,
	default=24,
	help='the age of this person.'
	)

parser.add_argument(
	'--weight',
	type=float,
	default=70.5,
	help='the weight of this person.'
	)

flags, unparsed = parser.parse_known_args()
main()