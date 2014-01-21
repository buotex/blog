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

###MRkNNCoP-Tree

• Self pruning strategies
• Points / pages exclude themselves
• Based on k-NN-dist approximation applied to points / page regions
• Points / pages can be excluded if query point not contained in their k-NN-dist-region

• Mutual pruning strategies
• Points / pages are mutually exclusive
• Based on Voronoi hyper-planes



