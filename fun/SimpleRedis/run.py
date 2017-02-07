#! /usr/bin/env python
import db

# Initialize database with its size.
tdb = db.SimpleRedis(65535)

mode = int(raw_input('Please select mode: 1) command line mode;  2) read from file > '))

file = "input.txt"
file_out = "output.txt"

assert mode in [1, 2]

def process(cmd):
    return tdb.cmd(cmd)

#********************************************************************************
if mode == 1:
    while True:
        input = raw_input('SimpleRedis > ')
        ret = process(input)
        if ret == None:
            continue
        if ret == 'END':
            break
        print ret

elif mode == 2:
    fp = open(file, "rt")
    fp_o = open(file_out, "w")
    for cmd in fp.readlines():
        ret = process(cmd)

        if ret == None:
            fp_o.write(cmd[:-1] + '\t\t\t\t\t\t' + '\n')
            continue
        else:
            fp_o.write(cmd[:-1] + '\t\t\t\t\t\t' + str(ret) + '\n')

        if ret == 'END':
            break
