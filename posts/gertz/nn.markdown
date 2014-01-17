{
  "title": "Nearest Neighbour",
  "date": "2014-01-17",
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

### **With Index**

~~~python

results.farthest = math.inf

def dfs_nn(q, node, k):
  if node is leaf: #Nodes only exist with an index
    for child in node: #If there are no nodes, _every_ point has to be checked.
      if dist(q, child) <= results.farthest:
        results.add(child)
        if len(results) < k:
          results.pop_farthest()
    else:
      for child in node:
        if dist(q, child) <= results.farthest:
          results += dfs_nn(q, child, k)
~~~

Issues with this basic variant are obvious: as results.farthest may be uninitialized / very high, 
there is no sensible pruning done. 
If an indexing mechanism exists, some work can be saved: 

- If the minimal distance ``dist(q, child)`` between the query point
and a directory structure **child** is above the current threshold, 
its children don't have to be taken into account either.

Without any index structure, everything has to be considered, which is very inefficient.

 
Still, depending on the data structure used, ``dist(q,child)`` may be a very expensive operation in practice.
For example, the distance to an arbitrary polygon is non-trivial.
We introduce the concept of **Filtering** and **Refinement** to improve the process.

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


##RKV

As mentioned, **farthest** is uninitialized in the basic approach. If an **index** is available, it
is possible to prune results from the opposite end.
In contrast to the previous **MINDIST(q, region)**, we can use **MAXDIST(q, region)**. 

Properties of **MAXDIST**

- maximum distance between query and *all* points in page region
- NN-distance cannot get worse than MAXDIST

MAXDIST(q, region) = $$\sqrt{\sum_{0<i\leq d} \max{(q_i - region.UB_i)^2, (q_i - region.LB_i)^2)}}$$

Properties of **MINMAXDIST**

- MBRs as page regions: improved estimate of maixmum NN-distance
- On every edge of the MBR, there must be a point
- Intuition: closest edge, farthest point
#Footnotes

[^Script1]: [Gertz, Nearest Neighbour Queries 1]({{urls.media}}/gertz/rdb/05-queryp-3.pdf)
[^Script2]: [Gertz, Nearest Neighbour Queries 2]({{urls.media}}/gertz/rdb/05-queryp-4.pdf)
[^range]: [Range Queries](posts/gertz/rangequeries)
