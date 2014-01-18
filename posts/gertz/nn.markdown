{
  "title": "Nearest Neighbour",
  "date": "2014-01-18",
  "categories": [
"database"    
  ],
  "tags": [
    "algorithm"
  ]
}

#Basics

``NN(q,k)`` [^Script1] [^Script2] applied on a database DB.
Given a query point $$q$$, find k objects $$O \in DB$$, such that $$dist(p,o) \leq dist(p,o') \forall o \in O, o' \in
DB \setminus O$$

Two interpretations for ambiguities for **k**-nearest neighbours
- Find **at least** k nearest neighbours, this is deterministic.
- Find exactly k-nn, this is not necessarily deterministic, as some objects could have the same distance.

The standard nearest-neighbours algorithm just conform to $$k = 1$$.
<details><summary>Ambiguity</summary><img src="{{urls.media}}/gertz/rdb/nn_1.png"></details>

#Algorithms

##Depth-first

The most generic algorithm, which is skipped here, has to be used when no indexing structure is
available - every sample has the same priority.
Given those circumstances, only a sequential search can be performed, to find the nearest
neighbours.

### **With Index**

When a tree data structure is available, we can already improve quite significantly on the basic
approach: 

~~~python

results.farthest = math.inf

def dfs_nn(q, node, k):
  if node is leaf: #Nodes only exist with an index
    for child in node: #If there are no nodes, _every_ point has to be checked.
      if mindist(q, child) <= results.farthest:
        results.add(child)
        if len(results) < k:
          results.pop_farthest()
    else:
      for child in node:
        if mindist(q, child) <= results.farthest:
          results += dfs_nn(q, child, k)
~~~

We make use of the following properties:

1. For a given index structure(say, M-Tree[^mtree]), the extent of the children is limited by the
   extent of their parents.
2. Thus, if a directory rectangle of a parent is too far away from the query point to be relevant,
   all its children can be pruned from the query as well.
3. The concept used here is called MINDIST(q, child)[^mindist], which is the minimum distance between a query
   point and a specific structure (dr[^dr], mbb[^mbb]).

Issues with this basic variant are obvious: as results.farthest may be uninitialized / very high, 
there is no sensible pruning done in that direction.

For more advanced pruning, the maximum distance MAXDIST(q, child)[^maxdist] has to be evaluated,
which gives rise to the following algorithm:

###RKV

The **MAXDIST**[^maxdist] for a query and a region is defined in a simple way: Intuitively, the
region has to contain at least one point. This point cannot be further away from the query point
than the **furthest possible point** in the region. 

- Thus, if the MAXDIST is smaller than the current best nearest neighbour, a new NN-candidate is found.
- This can be formulated as MAXDIST(q, region) = $$\sqrt{\sum_{0<i\leq d} \max{[(q_i - region.UB_i)^2, (q_i - region.LB_i)^2]}}$$

We can further improve on the **MAXDIST** estimate, if the enclosing object is a **minimal bounding
box**[^mbb].

The **MINMAXDIST**[^minmaxdist] takes advantage of the fact that a **minimal bounding box is
deterministic**, it is defined by its most outer points (see convex hull[^convhull]).

- **MBRs** as page regions: improved estimate of maixmum NN-distance
- On every edge of the MBR, there must be a point
- Intuition: closest edge, farthest point
Still, depending on the data structure used, ``dist(q,child)`` may be a very expensive operation in practice.
For example, the distance to an arbitrary polygon is non-trivial.
We introduce the concept of **Filtering** and **Refinement** to improve the process.

<details><summary>MinMaxDist Visualized</summary><img src="{{urls.media}}/gertz/rdb/minmaxdist.png"></details>

####Notes:
Compared to **range queries** [^range]:

- Next neighbour can be located very far from the query point (Unlimited query)
- Specification of query point not known in advance (also, k not known)
- Not known if a specific page is needed in advance (external storage problems)
- Usage of a page depends on content of other pages (divide and conquer may not be possible)

###Filtering
Instead of directly using the ``dist(p,q)`` function, we can first use an approximate solution. Which would be the most
useful? Well, a lower estimate, $$LB$$ is fitting here: if we *underestimate the distance*, we can later refine it.



Possible ways for an underestimate:

- For an object $$q$$, simplify q and calculate ``dist(p,mbb(q))``.


Maxdist
Mindist
Minmaxdist




#Footnotes

[^Script1]: [Gertz, Nearest Neighbour Queries 1]({{urls.media}}/gertz/rdb/05-queryp-3.pdf)
[^Script2]: [Gertz, Nearest Neighbour Queries 2]({{urls.media}}/gertz/rdb/05-queryp-4.pdf)
[^range]: [Range Queries](posts/gertz/rangequeries)
[^maxdist]: [Gertz, MaxDist]({{urls.media}}/gertz/rdb/05-queryp-3.pdf#page=5)
[^mindist]: [Gertz, MinDist]({{urls.media}}/gertz/rdb/05-queryp-3.pdf#page=4)
[^minmaxdist]: [Gertz, MinMaxDist]({{urls.media}}/gertz/rdb/05-queryp-3.pdf#page=6)
[^dr]: [Directory Rectangle](Footnotelink)
[^mbb]: [Minimal bounding box](Footnotelink)
[^mtree]: [MTree](/posts/gertz/rdb/mtree)
