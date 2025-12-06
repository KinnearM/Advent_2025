# Daily Log

## Day 6

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
- Then I decided the best way to iterate this for part 2 is to do it recursively. This led to having to repeatedly read out the data list into a set and then reconstruct the list each time so I wrote a little function to make a set of the coordinates to use as input for my recursive function.
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
