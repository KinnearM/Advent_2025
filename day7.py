import os
os.chdir(os.path.dirname(__file__))

def reader():
    return open("input.txt", 'r').read()

data=reader()

def part_1(data):
    lines = data.strip().split('\n')
    relevant_lines=lines[::2]
    split_count=0
    initial_data={i for i, char in enumerate(relevant_lines[0]) if char == 'S'}
    for state in relevant_lines[1:]:
      for i in initial_data.copy():      
        if state[i]=='^':
          split_count+=1
          initial_data.add(i+1)
          initial_data.add(i-1)
          initial_data.discard(i)
    return (len(initial_data),split_count)

def part_2(data):
    lines = data.strip().split('\n')
    relevant_lines=lines[::2]
    timeline_count=1
    current_data = {i: (1 if char == 'S' else 0) for i, char in enumerate(relevant_lines[0])}
    for state in relevant_lines[1:]:
      next_data = current_data
      for i, count in current_data.items():  
        if count > 0:
          pass      
        if state[i]=='^':
          timeline_count+=count
          next_data[i+1]+=count
          next_data[i-1]+=count
          next_data[i]=0
      current_data = next_data
    return timeline_count

print(part_1(data))
print(part_2(data))



