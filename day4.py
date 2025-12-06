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
