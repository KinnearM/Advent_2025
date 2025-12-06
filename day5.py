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

    def part_2(fresh_codes):
      
    fresh_codes.sort()
    
    first_start, first_end = fresh_codes[0]
    
    total_count = first_end - first_start + 1
    current_max = first_end

    for next_start, next_end in fresh_codes[1:]:

        effective_start = max(next_start, current_max + 1)
        
        if next_end >= effective_start:
            added_amount = next_end - effective_start + 1
            total_count += added_amount
            
            current_max = next_end
            
    return total_count

print(part_1(fresh_codes, produce))
print(part_2(fresh_codes))

