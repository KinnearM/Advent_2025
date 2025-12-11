with open("input.txt") as f:

    data = [tuple(map(int, line.split(','))) for line in f.read().splitlines()]

def square(corner_1,corner_2):
  x_1,y_1=corner_1
  x_2,y_2=corner_2
  sq=(abs(x_2-x_1)+1)*(abs(y_2-y_1)+1)
  return sq



def part_1(data):
  highest_sq=0
  items = list(data)
  n = len(items)
  for i in range(n):
      for j in range(i + 1, n):
          sq=square(items[i],items[j])
          if sq>highest_sq:
              highest_sq=sq
  return highest_sq

def zero_data(data):
    min_x = min(p[0] for p in data)
    min_y = min(p[1] for p in data)
    
    new_data = [(x - min_x, y - min_y) for x, y in data]

    return new_data

def find_squares(data):
  highest_sq=[]
  items = list(data)
  n = len(items)
  for i in range(n):
      for j in range(i + 1, n):
          sq=square(items[i],items[j])
          highest_sq.append((sq,items[i][0], items[j][0],items[i][1], items[j][1]))
  highest_sq.sort(key=lambda x: x[0])
  return highest_sq

def part_2_old(data):
  clean_data=zero_data(data)
  squares=find_squares(clean_data)
  vertical_limits, horizontal_limits=find_greens(clean_data)
  condition=False

  while condition is False:
      current_square=squares.pop()
      other_corner=(current_square[1],current_square[4])
      other_other_corner = (current_square[2],current_square[3])
      if is_is_green(other_corner,vertical_limits, horizontal_limits) and is_is_green(other_other_corner,vertical_limits,horizontal_limits):
        condition=True

  return current_square[0]

def find_greens(clean_data):

    vert_limits = {}
    hor_limits = {}

    for x, y in clean_data:
      
        if x not in vert_limits:
            vert_limits[x] = [y, y] 
        else:
            if y < vert_limits[x][0]: vert_limits[x][0] = y
            if y > vert_limits[x][1]: vert_limits[x][1] = y

        if y not in hor_limits:
            hor_limits[y] = [x, x]
        else:
            if x < hor_limits[y][0]: hor_limits[y][0] = x
            if x > hor_limits[y][1]: hor_limits[y][1] = x

    return vert_limits, hor_limits

def is_green(coord, vertical_limits, horizontal_limits):
    x, y = coord
    
    v_limit = vertical_limits.get(x)
    
    if v_limit is not None:
        v_min, v_max = v_limit
        if v_min <= y <= v_max:
            return True

    h_limit = horizontal_limits.get(y)
    if h_limit is not None:
        h_min, h_max = h_limit
        if h_min <= x <= h_max:
            return True
    return False

def is_is_green(coord,vertical_limits,horizontal_limits):
  x, y = coord
  
  max_x = max(vertical_limits.keys(), default=0)
  max_y = max(horizontal_limits.keys(), default=0)
  min_x = min(vertical_limits.keys(), default=0)
  min_y = min(horizontal_limits.keys(), default=0)

  vert_line = [(x, p) for p in range(min_y,max_y + 1)]
  hor_line = [(p, y) for p in range(min_x,max_x + 1)]
  
  vertical_greens = []
  horizontal_greens = []
  for i in vert_line:
    if is_green(i,vertical_limits,horizontal_limits):
      vertical_greens.append(i)
  if len(vertical_greens)>0:
    min_vert=min(vertical_greens)
    max_vert=max(vertical_greens)
    if min_vert[1]<=y<=max_vert[1]:
      return True
  for i in hor_line:
    if is_green(i,vertical_limits,horizontal_limits):
      horizontal_greens.append(i)
  if len(horizontal_greens)>0:
    min_hor=min(horizontal_greens)
    max_hor=max(horizontal_greens)
    if min_hor[0]<=x<=max_hor[0]:
      return True
  return False

def part_2(data):
    points = list(data)
    n = len(points)

    edges_v = []
    edges_h = []
    
    for i in range(n):
        p1 = points[i]
        p2 = points[(i + 1) % n] 
        
        if p1[0] == p2[0]:
            y_min, y_max = min(p1[1], p2[1]), max(p1[1], p2[1])
            edges_v.append((p1[0], y_min, y_max))
        else: 
            x_min, x_max = min(p1[0], p2[0]), max(p1[0], p2[0])
            edges_h.append((p1[1], x_min, x_max))

    squares=find_squares(data)#reverse or pop
    for area, rx1, rx2, ry1, ry2 in squares:  
        is_cut = False
        for vx, vy1, vy2 in edges_v:
            if rx1 < vx < rx2:
                if max(ry1, vy1) < min(ry2, vy2):
                    is_cut = True
                    break 
        if is_cut: continue 
        for hy, hx1, hx2 in edges_h:
            if ry1 < hy < ry2:
                if max(rx1, hx1) < min(rx2, hx2):
                    is_cut = True
                    break            
        if is_cut: continue 
        return area
    return 0
