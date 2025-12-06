import os
os.chdir(os.path.dirname(__file__))

def reader():
  return open(f"input.txt", 'r').read().splitlines()

data=reader()

def part_1(data):
  neighbours=set()
  rem_count=0
  for i, I in enumerate(data):
    for j, J in enumerate(I):
      if J=='@':
        neighbours.add((i,j))
  for i,j in neighbours:
    n_count=0
    for dr in [-1, 0, 1]:
      for dc in [-1, 0, 1]:
        if dr == 0 and dc == 0: 
          continue               
        if (i + dr, j + dc) in neighbours:
          n_count += 1
    if n_count <= 3:
      rem_count += 1    
       
  return rem_count

def make_set(data):
  neighbours=set()
  for i, I in enumerate(data):
    for j, J in enumerate(I):
      if J=='@':
        neighbours.add((i,j))
  return neighbours
      
data_set=make_set(data)

def part_2(data_set, rem_count=0):
  neighbour_cells = {
    (-1, -1), (-1, 0), (-1, 1),
    ( 0, -1),          ( 0, 1),
    ( 1, -1), ( 1, 0), ( 1, 1)
}
  unneighbours=set()
  new_rem_count=0
  for i,j in data_set:
    n_count=0
    for dr, dc in neighbour_cells:              
      if (i + dr, j + dc) in data_set:
         n_count += 1
    if n_count <= 3:
      new_rem_count += 1 
      unneighbours.add((i,j))
  data_set-=unneighbours
  rem_count+=new_rem_count
  if new_rem_count==0:
    return rem_count
  return part_2(data_set, rem_count)

print(part_2(data_set))
