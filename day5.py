import os
os.chdir(os.path.dirname(__file__))

def reader():
    return open("test2.txt", 'r').read()

raw_data = reader()
block_1, block_2 = raw_data.strip().split('\n\n')

fresh_codes = []
for line in block_1.splitlines():
    start_str, end_str = line.split('-')
    fresh_codes.append((int(start_str), int(end_str)))

produce = [int(line) for line in block_2.splitlines()]

def part_1(fresh_codes, produce):
  counted=0
  fresh_codes.sort()
  for code in produce:
    for range in fresh_codes:
      if code<range[0]:
        break
      if code >= range[0] and code <= range[1]:
        counted+=1
        break
  return counted


    

  print(part_1(fresh_codes, produce))
