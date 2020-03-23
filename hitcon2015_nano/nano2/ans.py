#!/usr/bin/python
# -*- coding: utf-8 -*-

import re
import serial
import time

port = None

lines = []
maps = []
ox = 0
oy = 0

def game0(line):
	if line == 'Nano$ enter your answer:':
		# enter you answer here
		answer = ''
		port.write('%s\n' % answer)
		port.flush()

def game1(line):
	if line == 'Nano$ show map':
		global lines, maps
		# here is map
		lines = lines[-3:]
		for line in lines:
			print line

		lx, ly = get_local_coordinate(lines)
		debug("lx: %d, ly: %d" % (lx, ly))
		direction = determine_direction(maps)
		update_o_coordinate(direction)
		port.write(direction + "\n")
		#port.write('d\n')
		port.flush()
	else:
		lines.append(line)

def debug(msg):
	print "Debug$ " + msg + "\n"

def update_o_coordinate(direction):
	global ox, oy

	if direction == 'w':
		oy = oy - 1
	elif direction == 's':
		oy = oy + 1
	elif direction == 'a':
		ox = ox - 1
	elif direction == 'd':
		ox = ox + 1

def determine_direction(maps):
	direction = raw_input()
	return direction

def get_local_coordinate(lines):
	for y in range(len(lines)):
		line = lines[y]
		for x in range(len(line)):
			c = line[x]
			if 'O' == c:
				return x, y
	
	raise Error()



def game2(line):
	if line == 'Nano$ enter your answer:':
		global lines
		lines = lines[-1:]
		total = 0
		# write you rules to calculate answer here

		port.write('%d\n' % total)
		port.flush()
	else:
		lines.append(line)

def main():
	# enter your choice here
	choice = '1'
	while True:
		line = port.readline()[:-1]
		if line.startswith('Nano$'):
			print line
		if line == 'Nano$ enter your choice:':
			port.write('%s\n' % choice)
			port.flush()
		if line == 'Nano$ finish':
			port.close()
			break
		if choice == '0':
			game0(line)
		if choice == '1':
			game1(line)
		if choice == '2':
			game2(line)
		if choice == '3':
			game3(line)

if __name__ == '__main__':
	port = serial.Serial(port='/dev/tty.wchusbserial1420', baudrate=115200, bytesize=serial.EIGHTBITS, parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE)
	main()
