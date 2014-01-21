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

##Voronoi-planes
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

####Notes

Pruning is done based on _points_, as they define the planes.
In the next section, we show an algorithm that uses information from the directory rect again for
pruning - based on minmax-distances.


##Min/Max-Dist-approach

This method again also works for metric data, as we work with min/max distances.
In addition, nothing is precomputed, so we work with lower and upper bounds instead which are
computed "live".


![Pruning]({{urls.media}}/gertz/rdb/minmaxpruning2.png)

<details><summary>Disadvantages of the approach</summary>
<img
src="{{urls.media}}/gertz/rdb/minmaxpruning.png"></details>

##Extension of Pruning to Higher Index Levels

ln an extension to the previous voronoi-hyperplane approach, we can extend this to higher index
levels by creating a hyperplane for every point in a page.
Note that we can choose to use a heuristic, such that we don't have to refine every single point,
just use a conservative approximation.

![Conservative approximation]({{urls.media}}/gertz/rdb/conservativeapproximation.png)

To calculate the approximation, we use the following approach:

- Split data space into 2d partitions based on center of page region E
(e.g., 4 partitions NW, NE, SE, and SW in 2d space)
For each partition P: choose reference point Re such that:
$$\forall p \in P, \exists e \in E$$ with $$dist(p,e) \leq dist(p,Re)$$
Note: reference point is unique due to chosen partitioning

**Intuitively**, pick the points that are farthest away from the query point on the rectangle.


![Higher index pruning]({{urls.media}}/gertz/rdb/higherindexpruning1.png)


##Extension of Geometric RkNN-Search[^georknn] for $$k \geq 1$$

Extension idea: also remember the number of points that an approximate hyperplane represents, if it
is high enough (say, k), then RkNN-candidates can be pruned.

####Notes

- flexible with regards to k
- better pruning than min/max-dist
- updates are relatively cheap, unless the page itself is changed
- storage for all 2d hyperplanes
- pruning test costly

![Higher index pruning]({{urls.media}}/gertz/rdb/higherindexpruning2.png)

##Optimal pruning

Idea: Check for each individual point in page if the dist(q,p) is too high compared to MAXDIST(e,p)
for a given entity e, if so then prune entire page.

####Notes

- Pruning is equal to geometric approximate hyperplane approach in some cases
- no extra index
- flexible with regards to k
- cheap in the actual testing, as MAXDIST is cheap
- only for vector data



###Footnotes:

- [Summary]({{urls.media}}/gertz/rdb/05-queryp-5.pdf#page=9)
