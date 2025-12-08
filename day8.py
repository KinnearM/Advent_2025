import os
os.chdir(os.path.dirname(__file__))


def reader():
  return open(f"input.txt", 'r').read().splitlines()

data=reader()


class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.count=n
        
    def find(self, i):
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]
    
    def union(self, i, j):
        root_i = self.find(i)
        root_j = self.find(j)
        if root_i != root_j:
            self.parent[root_i] = root_j
            self.count-=1
            return True
        return False

def get_dist(p1, p2):
    c1 = [float(x) for x in p1.split(',')]
    c2 = [float(x) for x in p2.split(',')]
    sq_sum = sum((a - b)**2 for a, b in zip(c1, c2)) 
    return sq_sum

def part_1(data):
    n = len(data)
    uf = UnionFind(n)
    edges = []

    for i in range(n):
        for j in range(i + 1, n):
            dist = get_dist(data[i], data[j])
            edges.append((dist, i, j))

    edges.sort(key=lambda x: x[0])

    cutoff = n 
    for dist, i, j in edges[:cutoff]:
        uf.union(i, j)

    group_counts = {}
    for i in range(n):
        root = uf.find(i)
        group_counts[root] = group_counts.get(root, 0) + 1
    
    sizes = sorted(group_counts.values(), reverse=True)
    
    soln = 1
    for s in sizes[:3]:
        soln *= s
        
    return soln

def part_2(data):
    n = len(data)
    uf = UnionFind(n)
    edges = []

    for i in range(n):
        for j in range(i + 1, n):
            dist = get_dist(data[i], data[j])
            edges.append((dist, i, j))

    edges.sort(key=lambda x: x[0])

    last_pair=0
    i=0

    while uf.count>1 and i<len(edges):
        dist, u, v = edges[i]
        if uf.union(u, v):
          last_pair=edges[i]
        i+=1
    
    j_1=int(data[last_pair[1]].split(',')[0])
    j_2=int(data[last_pair[2]].split(',')[0])
    
    soln = j_1*j_2
        
    return soln

print(part_1(data))
print(part_2(data))
