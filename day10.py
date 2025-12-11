with open("test.txt") as f:
    data = f.read().splitlines()

def parse_line(line):
    part1, rest = line.split('] ')
    part2, part3 = rest.split(' {')
    
    raw_squares = part1[1:]
    squares = [1 if c == '#' else 0 for c in raw_squares]

    raw_parens = part2[1:-1]
    
    paren_groups = []
    if raw_parens:
        for group in raw_parens.split(') ('):
            nums = set(int(x) for x in group.split(','))
            paren_groups.append(nums)

    raw_curlies = part3[:-1]
    curlies = [int(x) for x in raw_curlies.split(',')]

    return squares, paren_groups, curlies

def solve_line(states, actions):
    start_state = set(i for i, val in enumerate(states) if val == 1)
    
    num_actions = len(actions)

    for k in range(1, num_actions + 1):
        
        for action_group in get_combinations(actions, k):
            current_state = set(start_state)
            for action_set in action_group:
                current_state = current_state ^ action_set
         
            if len(current_state) == 0:
                return k              
    return -1 

def get_combinations(items, k):
    """
    This wasn't me --- I had to look it up! 
    I actually don't even know what yield does. This is definitely cheating. If anybody actually reads this let me know you caught me cheating! and tell me what yield does.
    """
    if k == 0:
        yield []
        return
    for i in range(len(items)):
        first_item = items[i]
        remaining_items = items[i + 1:]
        
        for suffix in get_combinations(remaining_items, k - 1):
            yield [first_item] + suffix

def part_1(data):
  total_actions = 0
  for i in data:
    states, actions, __ = parse_line_manual(i)
    count = solve_part_1(states, actions)
    total_actions += count
  return total_actions

print(part_1(data))
