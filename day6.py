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

def split_into_char_columns(lines):
    max_len = max(len(line) for line in lines)
    padded_lines = [line.ljust(max_len) for line in lines]

    columns = []
    for x in range(max_len):
        col = [line[x] for line in padded_lines]
        columns.append(col)
        
    return columns

def part_2():

  with open('input.txt, 'r') as f:
        raw_data = f.read()
    
  lines = raw_data.splitlines()
  cols = split_into_char_columns(lines)

  sum_total=0
  col_total=0
  op='+'

  for col in cols:
    last_place=col.pop()
    string=''.join(col)
    if string.strip() == '':
      continue
    else:
      value=int(string)
      if last_place != ' ':
        sum_total+=col_total
        op=last_place
        col_total=value
      elif op=='+':
        col_total+=value
      elif op=='*': 
        col_total*=value
  sum_total += col_total
  return sum_total

print(part_1())
print(part_2())
