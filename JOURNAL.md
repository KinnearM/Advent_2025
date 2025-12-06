# Daily Log
## Day 4
- My log starts today! 
- I opened the problem last night and slept on it as I have not seen a problem like this so far. 
I can see how one would brute force it -- for each gridpoint if the entry is `'@'` then count the neighbouring bales.
- I think I can make a set containing bale coordinates and then for each bale count the neighbours and keep count of the bales with less than 3 neighbours.
- I think the edge cases here are very literally around the edges, and the logic of counting bales is unaffected by neighbouring cells being empty so this is fine.
- I started by solving part 1 by adding the coordinates of the bales to a set and then counting the neighbours of each bale in this set. Simple.
- Then I decided the best way to iterate this for part 2 is to do it recursively. This led to having to repeatedly read out the data list into a set and then reconstruct the list each time so I wrote a little function to make a set of the coordinates to use as input for my recursive function.
- I know Python isn't keen on recursive functions but the logic made sense to me. This is O(N^2) though since worst case scenario we need to scan the whole set of bales as many times as there are killable bales left...
- Here is a solution from Gemini that uses a dictionary to track the number of neighbours of each bale and then when a bale is removed updates the count of each bale that the removed bale was neighbour to. Before I saw part 2 I had an idea like this and I wish I had remembered it when I started part 2!
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

---

## Days 1-3
- My main takeaway so far is that I need to stop being lazy with the edge cases -- try to think of logic that accounts for them instead of just manually adding cases...
- The other things that has slowed me down is not realising that my input is unique. I lost my day 1 solutions and spent *too long to mention* trying to work out why I couldn't recreate it. 
Turns out I was using the wrong input and chasing a non-existant bug. Lesson learned.

---
