import os
os.chdir(os.path.dirname(__file__))


def reader():
  return open(f"input.txt", 'r').read().splitlines()

data=reader()


def part_1(data):
    count = 0
    for line in data:
        one = max(line[:-1]) 
        id_one = line.find(one)
        two = max(line[id_one+1:])
        count += int(one + two) 
    return count

part_1(data)

def part_1_alt(data):
    count = 0
    for line in data:
        n=len(line)
        one_id = 0
        i = 0
        one=line[0] 
        while i < n-1:
            if line[i] > one:
                one = line[i]
                one_id = i
                if one == '9': 
                    break
            i += 1
        j = one_id + 1
        two=line[j]
        while j < n:
            if line[j] > two:
                two = line[j]
                if two == '9':
                    break
            j += 1
        count += int(one + two)   
    return count

def part_2(data):
    count = 0
    for line in data:
      digits = list(line[:12])
      line+= ' '
      last_id=-1
      for i in range(0,12):
        digits[i]=max(line[last_id+1:i-12])
        last_id = line[last_id+1:i-12].find(digits[i])+last_id+1
      count += int("".join(digits))
    return count

part_2(data)
