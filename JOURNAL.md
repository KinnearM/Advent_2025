# Daily Log
## Day 4
- My log starts today! 
- I opened the problem last night and slept on it as I have not seen a problem like this so far. 
I can see how one would brute force it -- for each gridpoint if the entry is `'@'` then count the neighbouring bales.
- I think I can make a set containing bale coordinates and then for each bale count the neighbours and keep count of the bales with less than 3 neighbours.
- I think the edge cases here are very literally around the edges, and the logic of counting bales is unaffected by neighbouring cells being empty so this is fine.

---

## Days 1-3
- My main takeaway so far is that I need to stop being lazy with the edge cases -- try to think of logic that accounts for them instead of just manually adding cases...
- The other things that has slowed me down is not realising that my input is unique. I lost my day 1 solutions and spent *too long to mention* trying to work out why I couldn't recreate it. 
Turns out I was using the wrong input and chasing a non-existant bug. Lesson learned.

---
