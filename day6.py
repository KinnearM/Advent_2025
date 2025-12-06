import os
import sys

os.chdir(os.path.dirname(os.path.abspath(__file__)))

def part_1():
    with open("input.txt", 'r') as f:
        lines = f.read().splitlines()
    ops = lines.pop().split() 
    start_line = lines.pop()
    totals = [int(x) for x in start_line.split()]
    for line in lines:
        current_row = [int(x) for x in line.split()]
        for i, I in enumerate(current_row):
            op = operators[i]
            if op == '+':
                totals[i] += I
            elif op == '*':
                totals[i] *= I
    return sum(totals)
  
    print(part_1())

