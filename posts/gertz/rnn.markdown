{
  "title": "Reverse Nearest Neighbour",
  "date": "2014-01-21",
  "categories": [
    "databases"
  ],
  "tags": [
   "algorithms" 
  ]
}

#Basics

Given a point q, return all points p such that q is the nearest neighbour of p.
Formalized: $$RNN(q, DB) = \{p | dist(p,q) \leq q' \forall q' \in DB\}$$

####Notes:

- Not symmetric
- One solution to the problem is based on calculating all nearest neighbours for all points

Again, the goal is to prune as much as possible from the search space, to lessen the number of
required page loads. The strategies can be split up into two different strategies, self and mutual
pruning ones.

#Self pruning

##Basic strategy

- Materialize all NN-distances for all points and store them (e.g. R-Tree)
- the query point is NN to a point if it is inside the NN-sphere.
- This is equivalent to a point query in the data structure.

![]({{urls.media}}/gertz/rdb/self_pruning.png)

##Advanced data structures

###RNN-Tree

Does as expected for its name, store NN-spheres of points in an R-Tree

<details><summary>RNN-Tree visualization</summary><img src="{{urls.media}}/gertz/rdb/rnn_tree.png"></details>

####Notes

There are some issues with the RNN-Tree approach, mostly in flexibility:

- k has to be hardcoded (as the kNN-distance is stored)
- only suitable for vector data as we rely on the "inside"
- Modifications expensive: have to update page regions etc.

###RdNN-Tree

This time, we also store the maximum NN-distance for directory nodes (based on their children) so we
can prune whole subtrees more easily.

<details><summary>RdNN-Tree visualization</summary><img src="{{urls.media}}/gertz/rdb/rdnn.png"></details>
<details><summary>Prune the whole node for q2</summary><img src="{{urls.media}}/gertz/rdb/rdnn2.png"></details>

####Notes

- Still, very hardcoded - but at least we don't require an additional R-Tree anymore as there are
less overlaps.

###MRkNNCoP-Tree

Instead of computing all kNN-distances separately, we use a heuristic to calculate a lower and an
upper bound for every k-distance.
For "regular" data, the radius of a hyper-sphere and the number of objects contained is proportional
in log-log space.

- Use approximated kNN-distances
- log(k-NN-Dist(o)) ∝ (log(k) / df) in log-log space

![visualization]({{urls.media}}/gertz/rdb/mrknncop.png)

####Notes

- Updates still costly
- Can deal with vector/metric data by using M-Tree/X-Tree, not bound to a data structure


#Mutual pruning strategies

Idea
- If a point x lies on p‘s side of the Voronoi-plane, then q cannot be NN of x;
thus $$x \not \in RNN(q)$$
- Voronoi-plane E(p,q): for all points e ∈E
dist(q,e)=dist(p,e) holds

![visualization]({{urls.media}}/gertz/rdb/voronoi2.png)

A point that is closer to q than any other becomes a candidate (a point that is in the same region
as q). 
The new candidate creates a new plane along with q, which may prune other candidates.
Every candidate that is outside the same patch as q may be removed, as it is closer to a different
point.
Refinement has to be done to convert directory rectangle / mbr / heuristic into a real point, which
then spans the plane.


<details><summary>Example</summary>
<img src="{{urls.media}}/gertz/rdb/voronoi3.png">
In the first iteration, c1-c4 are the candidates, they, along with q, create the displayed
voronoi-net.
p1 is inside the same square that q is in, so q is a NN-candidate for **p1** - another plane has to be
introduced.
Note that the directory rectangle **MUR2** has to be refined as well, because it overlaps with the
center square.
<img src="{{urls.media}}/gertz/rdb/voronoi4.png"></details>
