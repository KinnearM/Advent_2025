# Daily Log

## Day 8
- Famous last words!
- This is a graph theory problem. I don't even have a guess of how I would code this. The brute force approach is compute the distance between every pair of coordinates and then take the n shortest connections and plop the junctions into circuit sets. That's N! distances to compute.
- Can we do like a list of 2 junctions and test each other juncion against the 2 and we find a connection that is smaller than the current one we replace the farther junction? Does that work? I feel like this gives a different answer depending where you start?
- In 1D: [1,4,88,6,34,86,9,55,43,28,7] start with (1,4)->(1,4)->(4,6)->(6,7). Starting at other end (28,7)->(28,43)->(43,55)->(43,34) didn't think so.
- Ok I found the overall logic myself but each function required help. Here is the overall structure:

```
FUNCTION part_1(data):

N = Length of data
uf = Initialize UnionFind(N)
edges = Empty List

FOR i FROM 0 TO N:
    FOR j FROM i + 1 TO N:
        dist = Calculate Distance between data[i] and data[j]
        APPEND (dist, i, j) TO edges

SORT edges BY distance (Ascending)

cutoff = N

FOR each (dist, u, v) IN edges FROM index 0 TO cutoff:
    CALL uf.union(u, v)

group_counts = Map()

FOR i FROM 0 TO N:
    root = CALL uf.find(i)
    group_counts[root] = group_counts.get(root, 0) + 1

sizes = SORT group_counts values (Descending)

result = sizes[0] * sizes[1] * sizes[2]

RETURN result
```
- My distance function was fine. I didn't actually go as far as computing the last sqrt since when x,y > 0, x^2 > y^2 => x > y and once we've compared the distances we never need them again.
- My edge calculating was fine, I don't think there is any way to avoid just computing every single one. I used a `for i to n` and `for j range(i+1,n)` loop to avoid doing n^2 calculations instead of n! and make sure each pair only appears once in my list. then we sort nlogn and take the first 10 (1000) values. Originally I was trying to track just the 10 lowest weight edges but sorting every loop takes way longer than just storing them all and sorting at the end.
- So far so good but this is where I got lost.
- The idea to use a union class was not mine, I tried to do it just using functions which meant a lot of rewriting a list of sets containing the elements of each circuit. I think I also missed cases where an edge connects two existing circuits.
- Gemini used something like a linked list to track which junctions map to which other junctions and then tallied up how many junctions were part of each circuit. This is contained in a class so the function that creates the map can be called for each edge and the list of maps can be updated without rewriting the list of edges like I was doing.
- Then you just sort and multiply to get the solution.
- Part 2 was easy to adapt from my solution to part 1. I just added a counter to the union class to keep track of how many seperate circuits we have by starting at n and taking -1 every time we merge circuits and lose one independant circuit. Now we run the junction mapping function until we have only one group and at this point read out what the last edge was. Then we can multiply the x coordinates of the two junctions.
- Folks on the subreddit are chatting about how easy today was and this was a struggle for me so we'll see how it goes from here lol
- Right, ok. I looked at the comments and it's all people being like "it's just kruskal's algorithm, just use min heap + unionfind" yeah I'm sure these are all easy if you've seen them before! I feel less terrible that I almost figured it out on my own. I do wish I had given myself time to feel out how to create unions of sets before I asked the robot for help but I thought I was just being an idiot because I couldn't solve it immediately. No more reading reddit!

---

## Day 7
- Today I just brute forced it. I got the answers but I will go back in and see if I can do better. Part 1 was easy, just got rid of all the useless data and then used a set to track the indices which currently have beams to select the splitters that are interacted with and update the new beam positions and just counting the splits as a variable as I go.
- Part 2 just required that we track the number of beams in each position so I upgraded to a dictionary but the logic is exactly the same.
- I think we could do this somehow without tracking every position by just scanning in the whole grid and counting the splitters in each row. We know that if every row had the max number of splitters we would get 2^row timelines so we can adapt this relationship to account for removed splitters. Instead of X<sub>n+1</sub> = 2 * X<sub>n</sub> we have X<sub>n+1</sub> = 2 * X<sub>n</sub> - missing_splitters but now we also need to account for the splitters which aren't interacted with and I don't see how to do that without tracking where the beams are. I think there is a clue in the fact that the splitting causes the parity of the indices of the positions to change so we end up with eg an odd beam which falls between the even placed splitters on the next row. To me this still quickly becomes about *where* the previous beams are so I end back at my original method.
- What if we reversed the whole thing and started with 2^row and found some relationship that divides this number depending how many splitters are missing? Then we could also `pop()` each row and I am a big fan of popping these days.
- The number of beams in each position is just Pascal's triangle with zeros in between. So can I start with my fully split {1,0,7,0,21,0,35,0,35,0,21,0,7,0,1} then the row above is missing my "6" splitter so actually it is {1,0,7,0,21,0,35,0,35,0,15,6,1,0,1} and we are 6 down. Now the row before that we are missing "5", "10" and "5" which means row six received {1,0,1,5,10,0,10,10,0,5,1,0,1} instead of {1,0,6,0,15,0,20,0,15,0,6,0,1} so was 20 down but also that's 40 that are not going to be split next row. So for each splitter of rank n that is missing we take 2*n away from the doubling of paths next round and add it to the round after? I'm right back to just simulating it again amn't I? Did I just nail this on the first go?
- I'm a little disappointed there will only be 12 this year and past the halfway point I'm still not finding these very challenging! 

  
---

## Day 6
- Part 1 was suspiciously easy. Good practice using `.pop()`. Add/multiplying each line to a list of running totals is the only thing that really made sense to do and it.
- Ugh part 2 is gross. I guess we still have a list of length N and we still pop the operations but then we have to somehow keep track of which digits belong to which numbers.
- Ok I sliced it into character-width columns and for each column popped the last element, if the result is an operation then I added the column total to the sum total and defined the new column total as the join of the rest of the column. Otherwise I just keep constructing and operating columns onto the column total. The robot tells me this is a state machine. Speed is O(N) and memory is O(1).
- I want to try using some more in-built python functions in the next few days. What do map and lambda do for example? and eval?

  
---

## Day 5
- So the test case is misleading on this one! I saw the little ranges of numbers and I was like easy peasy we can plop those in a set and just N*O(1) look up our codes! Alas. So seeing the actual input data, my first instinct is that we only look at the first few digits of each range. e.g., we don't care if 415815768268371 in the range 415615768268371-416146851443768, we can really easily round our bounds up and down respectively and see it is in 415700000000000-416000000000000 which implies it is in the original range. We are rounding and proving a stronger condition. This is as slow as checking every value against the range if every produce code lies on the edge of a range. No wait this is slower than just checking the range. Nevermind.
- I coded up my brute force code and for M ranges and N produce codes this is O(NM).
- Now, if I sort the ranges by their lower bound (or upper bound), I can stop when I reach a lower bound that is higher than my value. This way it is only O(NlogM) comparisons plus the initial sort which is O(MlogM). Also, I no longer need to track which codes I've checked so my count can be an updating value instead of a set.
- I did a lot better on part 2. I noticed that I can do this by running through the sorted lower and upper bounds, tracking only the index and the total count. At each step I compute the difference between the upper bound and the max of lower bound and the upper bound from the previous step. This process is O(M) so it is limited by the O(MlogM) sorting step.
  
---
## Day 4
- My log starts today! 
- I opened the problem last night and slept on it as I have not seen a problem like this so far. 
I can see how one would brute force it -- for each gridpoint if the entry is `'@'` then count the neighbouring bales.
- I think I can make a set containing bale coordinates and then for each bale count the neighbours and keep count of the bales with less than 3 neighbours.
- I think the edge cases here are very literally around the edges, and the logic of counting bales is unaffected by neighbouring cells being empty so this is fine.
- I started by solving part 1 by adding the coordinates of the bales to a set and then counting the neighbours of each bale in this set. Simple.
- Then I decided the best way to iterate this for part 2 is to do it recursively. This led to having to repeatedly read out the data list into a set and then reconstruct the list each time so I wrote a little function to make a set of the coordinates to use as input for my recursive function. This is like game of life except everybody dies right? One of my first ever maths lectures I attended was on the game of life!
- I know Python isn't keen on recursive functions but the logic made sense to me. This is O(N^2) though since worst case scenario we need to scan the whole set of bales as many times as there are killable bales left...
- Here is an O(N) solution from Gemini that uses a dictionary to track the number of neighbours of each bale and then when a bale is removed updates the count of each bale that the removed bale was neighbour to. Before I saw part 2 I had an idea like this and I wish I had remembered it when I started part 2!
```
FUNCTION part_2_queue(grid):

    paper_rolls = Find all coordinates (r, c) with '@'

    adjacent_counts = Map()
    
    forklift_queue = Empty List

    FOR each roll IN paper_rolls:
        n = Count adjacent rolls (neighbors)
        adjacent_counts[roll] = n

        IF n < 4:
            ENQUEUE roll into forklift_queue

    total_removed = 0

    WHILE forklift_queue IS NOT EMPTY:
        current_roll = DEQUEUE from forklift_queue
        
        IF current_roll IS NOT IN paper_rolls:
            CONTINUE

        REMOVE current_roll FROM paper_rolls
        total_removed = total_removed + 1

        FOR each neighbor OF current_roll:
            IF neighbor IS IN paper_rolls:
                adjacent_counts[neighbor] = adjacent_counts[neighbor] - 1
                
                IF adjacent_counts[neighbor] == 3:
                    ENQUEUE neighbor into forklift_queue

    RETURN total_removed
```
- Today seemed easier than the previous days but it was less obvious how to do it well. I think this i the first day where I have not reached O(N).
---

## Days 1-3
- My main takeaway so far is that I need to stop being lazy with the edge cases -- try to think of logic that accounts for them instead of just manually adding cases...
- The other things that has slowed me down is not realising that my input is unique. I lost my day 1 solutions and spent *too long to mention* trying to work out why I couldn't recreate it. 
Turns out I was using the wrong input and chasing a non-existant bug. Lesson learned.

---
