{
  "title": "KD-Tree",
  "date": "2013-12-11",
  "categories": [
	"database"
  ],
  "tags": [
	"data structures"
  ]
}

- Balanced binary tree over a set of multi-dimensional points
- Every node and leaf represents one point
- Idea of balanced binary tree, just generalized to multiple dimensions
- The split dimension is chosen according to the depth, cycling over the
  possible ones. (e.g., split on x-axis in the root, then on y-axis, then z,
  then back to x for a 3-dimensional problem)
- Split on the **median** of the splitting dimension
- Used for nearest neighbor queries
- Requires backtracking for these queries

Recursion scheme:
With presorting in all dimensions, we end up with 
$$2 T(n/2) + n $$ which resolves to an overall complexity of 
$$O(n \log n)$$ due to the master theorem.

####Standard operations:

- Building the tree has a complexity of $$O(n \log n)$$
- Adding points may need rebalancing, but otherwise doable in $$O(\log n)$$
- Searching also takes $$O(\log n)$$ due to the binary tree property
- Deleting points breaks things

###References:

- [Wiki](http://en.wikipedia.org/wiki/K-d_tree)
- [Script]({{urls.media}}/gertz/rdb/04-indexing-1.pdf#page=36)
- [Master Theorem](/posts/basics/master_theorem)
