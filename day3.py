import os
os.chdir(os.path.dirname(__file__))


def reader():
  return open(f"input.txt", 'r').read().splitlines()

data=reader()


def part_1(data):
  """
  I wrote this on my first attempt but then I wondered if max() and find() are still efficient when the strings get really long...
  """
    count = 0
    for line in data:
        one = max(line[:-1]) 
        id_one = line.find(one)
        two = max(line[id_one+1:])
        count += int(one + two) 
    return count

part_1(data)

def part_1_alt(data):
  """
  An attempt to be lazy about parsing long strings. Sure is ugly.
  """
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
  """
  Generalisation of part_1() with moving sections. Is adding an empty element to the end of the line really clever or really stupid?
  """
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

def part_2_stack(data):
  """ 
  Not me! Checked my answer with Gemini and it introduced me to stacks.
  Keeping this here in case it is useful.
  """ 
    total = 0
    for line in data:
        stack = []
        removable_count = len(line) - 12 
        for digit in line:
            while stack and stack[-1] < digit and removable_count > 0:
                stack.pop()         
                removable_count -= 1 
            stack.append(digit)
        final_digits = stack[:12]
        total += int("".join(final_digits))  
    return total
