import os
os.chdir(os.path.dirname(__file__))


def reader():
  return open(f"input.txt", 'r').read().splitlines()

data=reader()

def part_1(arr):
  zero_count=0
  current_position=50
  i=0
  while i<len(arr):
    if arr[i].startswith('R'):
      factor=1
    else:
      factor=-1
    new_position=int(current_position+factor*float(arr[i][1:]))
    current_position=int(new_position%100)
    if current_position==0:
      zero_count+=1
    i+=1
  return zero_count

part1(data)

def part_2(arr):
  zero_count=0
  current_position=50
  i=0
  while i<len(arr):
    if arr[i].startswith('R'):
      new_position=current_position+float(arr[i][1:])
      if new_position>=100:
        zero_count+=new_position//100
      current_position=new_position%100
    elif arr[i].startswith('L'):
      new_position=current_position-float(arr[i][1:])
      if current_position==0:
        zero_count-=1
      if new_position<=0:
        zero_count+=abs(new_position-1//100)
      current_position=new_position%100
    i+=1
  return zero_count

part2()
