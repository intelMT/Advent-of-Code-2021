
example = """forward 5
down 5
forward 8
up 3
down 8
forward 2"""

def calc_pos(data : str):
	commands = [x for x in data.split('\n')]
	hor = 0
	dep = 0
	for command in commands:
		direction, amount = command.split()

		if direction == 'forward':
			hor += int(amount)
		if direction == 'down':
			dep += int(amount)
		if direction == 'up':
			dep -= int(amount)
	return dep*hor

assert calc_pos(example) == 150

#Part-2
def calc_pos_w_aim(data : str):
	commands = [x for x in data.split('\n')]
	hor = 0
	aim = 0
	dep = 0
	for command in commands:
		direction, amount = command.split()

		if direction == 'forward':
			hor += int(amount)
			dep += int(amount)*aim
		if direction == 'down':
			aim += int(amount)
		if direction == 'up':
			aim -= int(amount)
	return dep*hor

assert calc_pos_w_aim(example) == 900


if __name__ == '__main__':
	with open('d2.txt') as f:
		content = f.read()

	print(calc_pos(content))
	print(calc_pos_w_aim(content))