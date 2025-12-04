import numpy as np
import os
os.chdir(os.path.dirname(__file__))


def reader():
  return open(f"input.txt", 'r').read().splitlines()

data=reader()

#part 1
def split_2(string):
  low, up=string.split('-')
  n=len(up)
  if len(low)<n:
    diff=n-len(low)
    low=diff*'0'+low
  lower_int=int(low)
  upper_int=int(up)
  counted=set()
  lower_mth=int(low[:n// 2])
  guess=int(str(lower_mth)*2)
  while (guess<=upper_int):
    if (guess>=lower_int):
      counted.add(guess)
    lower_mth+=1
    guess=int(str(lower_mth)*2)
  return sum(counted)

def part_1(arr):
  count=0
  for string in arr:
    count+=split_2(string)
  return (count)

part_1(data)
  
def split_count(string):
  low, up=string.split('-')
  n=len(up)
  if len(low)<n:
    diff=n-len(low)
    low=diff*'0'+low
  lower_int=int(low)
  upper_int=int(up)
  counted=set()
  for m in range(2,n+1): 
    lower_mth=int(low[:n// m])
    guess=int(str(lower_mth)*m)
    while (guess<=upper_int):
      if (guess>=lower_int):
        counted.add(guess)
      lower_mth+=1
      guess=int(str(lower_mth)*m)
  return sum(counted)

def part_2(arr):
  count=0
  for string in arr:
    count+=split_count(string)
  return (count)

part_2(data)
