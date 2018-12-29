from collections import deque


def show_previous_lines_when_matched(lines, pattern, previous_lines=2):
	previous_lines = deque(maxlen=previous_lines)
	for line in lines:
		if pattern in line:
			yield line, previous_lines
		previous_lines.append(line)


if __name__ == '__main__':
	with open('error_log.txt', 'r') as fin:
		for line, previous_lines in show_previous_lines_when_matched(fin, 'installd'):
			for pre_line in previous_lines:
				print(pre_line, end='')
			print(pre_line, end='')
			print('-' * 20)
