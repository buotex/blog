{
  "title": "R Tree",
  "date": "2014-01-10",
  "categories": [
    "database"
  ],
  "tags": [
    "data structure"
  ]
}

**The key idea of the data structure is to group nearby objects and represent them
with their minimum bounding rectangle in the next higher level of the tree; the
"R" in R-tree is for rectangle.**

- Balanced search tree
- Organizes the data in pages
- Designed for storage on disk (as used in
databases). 
- Each page contains between m ($$\in [0, M/2]$$) and M entries
- Rectangles shall not cover too much empty space and not overlap too much (so that during search, fewer subtrees need to be processed). 



![]({{urls.media}}/gertz/rdb/r_optimization.png)






- Maximum number of entries in nodes depends on entry size size(E) and
disk page capacity size(P): M = ⎣size(P)/size(E) ⎦. M might differ for leaf
and non-leaf nodes (oid versus nodeid).

The tuning of the number of entries m per node between 0 and M/2 is
related to the splitting strategy:

- an R-tree of depth d indexes between md+1 and Md+1 objects
- for N objects, the depth of an R-tree is between ⎣logm(N)⎦ -1 and
⎣logM(N)⎦ -1 (the exact value depends on page utilization).
Example: assume size(P)=4K and size(E)=16 (for mbb) + 4 (for oid) bytes,
and m is set to 40% of page capacity. Thus, M=204 and m=81.
R-tree of depth 1 can index at least 6,561 objects.
R-tree of depth 2 can index at least 531,441 and up to 8,489,664 objects.
For 1,000,000 objects, it takes 4 page accesses to get the object.





#Applications:

##Queries:

- Point query: Given a point P, which objects contain that point
- Window query: Given a query window, which objects intersect that window
- Both queries are done by the canonical recursive scheme

![]({{urls.media}}/gertz/rdb/r_query1.png)

##Insertions:

![]({{urls.media}}/gertz/rdb/r_insertion1.png)

Given an object o with its mbb. Traverse tree top-down and either

~~~
find a node whose dr contains mbb, continue traversal, or there is no such node. 
Then choose a node such the enlargement of its
dr is minimal.
Repeat the above until leaf is reached.
~~~

Then

~~~
if the leave is not full, add entry [mbb, oid]
if a leaf node’s dr needs to be enlarged, the corresponding entry of the
parent node must be updated, too. (can propagate up to the root)
if a leaf is full, a split occurs (this is the tricky part....)
in the worst case, split can propagate up to the root, which causes an
increase of the tree’s depth.
~~~

###Splitting strategies

####Quadratic split technique:

~~~python
For all pairs of entries, find the pair such that the mbb containing both has the most dead space. Put both entries of that pair into *two* different drs.
For i in [0, M-2]:
	For j in entries:
		diff[j] = difference in dead space between dr1 + j and dr2 + j
	maxentry = indexmax(diff)
	dr[find_minimal(maxentry)].append(entry(maxentry))
	entries.pop(maxentry)
~~~

####Linear splitting:
– choose the seeds such that the distance along one axis is the greatest
– assign each remaining entry to the group whose mbb needs the least
area enlargement.

Difference in methods: 
Linear is way more greedy and depends on the order of the entries.


[Script]({{urls.media}}/gertz/rdb/04-indexing-3.pdf#page=16)

##Deletion

- Find leaf with object
- remove object from leaf
- reorganize the tree if necessary (optional)


[Script-Reorganize]({{urls.media}}/gertz/rdb/04-indexing-3.pdf#page=21)

**Reorganize** is executed on the **leaf + entry** to be deleted

Reorganization is required if the deletion results in a leaf node which has less
than $$m$$ entries.

~~~python

def Reorganize(N,e):
  Q = []
  delete e from N
  if (|N| < m):
    Q.append(N)

    F = GetParent(N)
    Q.extend( Reorganize(F, entry of N in F) )
  
  else:
    AdjustPath(N) // N has been modified, adjust path 

Q = Reorganize(L,e)
Reinsert(Q)
~~~



![]({{urls.media}}/gertz/rdb/r_tree.svg)

#Variants

##R* Tree

Optimizing for 
- node overlapping,
- area covered by a node, and
- perimeter of a node’s directory rectangle

###Ideas:

####Splitting priority
Find the best **axis** to split on.

#### Forced reinsertion
R*-tree tries to avoid splitting by 
reinserting the rectangles from v for 
which the dead space in the node is the largest
- compute distance *d* 
between their centroid and the centroid of the node’s mbb
- sort in decreasing order on *d*
- take the first *p* entries from the sorted list (typically, *p* = 30%)

##R+ Tree






[Script]({{urls.media}}/gertz/rdb/04-indexing-3.pdf)

[Another Script]({{urls.media}}/gertz/rdb/rtree_1rotated.pdf)

<audio controls>
  <source src="{{urls.media}}/gertz/rdb/101 Overture.mp3" type="audio/mpeg">
Your browser does not support the audio element.
</audio>

#Research:

####Parameter m:

- With higher m, you get denser trees which are less deep.
- Under/Overflows are more likely, so searches are preferred compared to
manipulations.

#Todo:
{{#todo_block}}
- []Bad example for insertions, as they are order-dependent
{{/todo_block}}


dr
: directory rectangle

mbb
: minimal bounding box
