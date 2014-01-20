{
  "title": "Nearest Neighbour",
  "date": "2014-01-20",
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

- Thus, if the MAXDIST is smaller than the current best nearest neighbour, a new NN-candidate is found, **results.farthest** can be replaced
- This can be formulated as MAXDIST(q, region) = $$\sqrt{\sum_{0<i\leq d} \max{[(q_i - region.UB_i)^2, (q_i - region.LB_i)^2]}}$$

We can further improve on the **MAXDIST** estimate, if the enclosing object is a **minimal bounding
box**[^mbb].

The **MINMAXDIST**[^minmaxdist] takes advantage of the fact that a **minimal bounding box is
deterministic**, it is defined by its most outer points (see convex hull[^convhull]).

- On every edge of the MBR, there must be at least one point
- Prior to the recursive descent: sort child pages based on MINDIST (has 
been shown to be best priority criterion in experiments)

<details><summary>MinMaxDist Visualized</summary><img src="{{urls.media}}/gertz/rdb/minmaxdist.png"></details>

<details><summary>RKV comparison</summary><img src="{{urls.media}}/gertz/rdb/rkv.png"></details>

####Summary

- Prioritization using MINDIST reduces page accesses from 7 to 3
- MINMAXDIST improves pruning distance, but **doesn’t avoid page accesses**
- Despite prioritization: depth-first search can be severely misguided,
e.g., when a page on the first level is very close to query point but child
pages are relatively far away

<details><summary>RKV issues</summary><img src="{{urls.media}}/gertz/rdb/rkv_2.png"></details>

####Notes

- Why are we using DFS instead of BFS?
- BFS can not utilize pruning as well, because *true* distances are only known in the end
- Therefore, too many node-loads have to be done.


##Another Approach: Priority-search

In contrast to the Depth-first search, now we employ some advanced ideas:

The concept is now a priority-list instead of simple recursion.
In short, the pages are kept in ``set(pages, lambda x: mindist(q, x))``

###Summary:

- Storage may be more expensive at $$O(n)$$ instead of $$O(log n)$$ for dfs
- RKV-based priority search is optimal with respect to page accesses
- Lemma 1: A correct NN algorithm has to load at least those s pages
that satisfy $$MINDIST(q,s) ≤ NN-distance(q)$$
- Lemma 2: The approach accesses pages of the index in ascending
order according to MINDIST.
- Lemma 3: The approach does not access a page s for which
$$MINDIST(q,s) > NN-distance(q)$$.



##Voronoi-Diagram

- For each point p, compute the space for which p is the nearest neighbor
(Voronoi cells)
- Store Voronoi cells in DB
- NN-query corresponds to point
query q over Voronoi cells
⇒ point p whose Voronoi cell
contains q is NN of q

####Notes:

- Voronoi cells may be very complex for higher (higher than 2) dimensions, so approximations are
recommended, such as using the mbr and later refining the results.

<details><summary>Voronoi</summary><img src="{{urls.media}}/gertz/rdb/voronoi.png"></details>



##Filtering and refinement
Instead of directly using the ``dist(p,q)`` function, we can first use an approximate solution. Which would be the most
useful? Well, a lower estimate, $$LB$$ is fitting here: if we *underestimate the distance*, we can later refine it.

Costs:

- I/O cost: Filtering (page access)
- Computation cost: Refinement (Distance calculation in higher dimensions)

###Notes for NN-queries in general
Compared to **range queries** [^range]:

- Next neighbour can be located very far from the query point (Unlimited query)
- Specification of query point not known in advance (also, k not known)
- Not known if a specific page is needed in advance (external storage problems)
- Usage of a page depends on content of other pages (divide and conquer may not be possible)

<details><summary>Range vs Nearest Neighbour queries</summary><img src="{{urls.media}}/gertz/rdb/rangevsnn.png"></details>

###General algorithm:

1. NN-query with filter, to create another limit $$d$$ similar to **MAXDIST** (e.g. using mbr)
2. Use Range query RQ(q,d) to get candidates
3. Refine (evaluate) results

Variants:

- Refine candidate immediately if in range (can't be pruned)
- Rank candidates first before evaluating


#K-NN

- Pruning with MINMAXDIST in RKV-algorithm not that useful
- In general, algorithms for NN can just be used for kNN by changing the pruning / furthest
interpretation

<details><summary>LB + UB kNN</summary><img src="{{urls.media}}/gertz/rdb/knn_1.png">
<img src="{{urls.media}}/gertz/rdb/knn_2.png">
</details>

##Optimal (UB + LB)-based kNN search

If only the ids of the nearest neighbours is relevant and not so much their exact location (or
ranking), we can save on several refinements:

- Goal: Only refine those objects whose lower and upper distance
estimate covers the k-NN distance nnk-dist(q)
- Provable: there exists always one candidate whose lower and upper
distance covers LBk as well as UBk as thus k-NN distance nnk-dist(q)

The algorithm again is a greedy approach, which solves the problem optimally due to its convexity.

- Optimality of page accesses as (like before), only elements whose MINDIST is close enough are added to the candidates
- Optimality of number or refinements: We only refine elements whose possible extent may surpass the
 current kNN-limit.



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
