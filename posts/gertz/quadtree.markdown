{
  "title": "Quad Tree",
  "date": "2014-01-14",
  "categories": [
	"database"
    
  ],
  "tags": [
	"data structure"
  ]
}

#Point QuadTree
- Multidimensional binary search tree
– It is not necessary that every node v stores its corresponding square.
- As defined in the lecture, points sitting on boundaries belong to the bottom/left
  child
- Split the current square into four quadrants
- Recursion stops when the point set contains less than two points
- How to find the square to start the computation with for a set P ?
(see also slide 4-56)
- A split into four quadrants does not mean that the point set is split as
well. Therefore, the quadtree can be quite unbalanced.

![]({{urls.media}}/gertz/rdb/point_quad.png)
![]({{urls.media}}/gertz/rdb/point_quad_ex1.png)


##Complexity:
It is not possible to express the size and depth of a quadtree as a function
of the number of points it stores. However, the depth of a quadtree is
related to the distance between points and the size of the initial square.

**Lemma**: The depth of a quadtree for a set P of points in the plane is at
most $$log(s/c) + 3/2$$, where c is the smallest distance between any two
points in P and s is the side length of the initial square.

**Proof**: 
- Any internal node has at least 2 points of P
- Node at depth i has side-length $$s = S / 2^i$$, diagonal length $$d = s \sqrt(2)$$
- $$c = S / 2^i \sqrt(2) \rightarrow $$
- $$i = log(S / c) + 1/2$$
- One additional split required to split up the last two.

#Region QuadTree

- Simpler variant, imagine pixel grid


**Theorem**: A quadtree of depth d storing a set n of points has
$$O((d+1)n)$$ nodes and can be constructed in $$O((d+1)n)$$ time.


#Balancing QuadTree
![]({{urls.media}}/gertz/rdb/quad_balancing.png)

#Applications:

##[Nearest neighbour]({{urls.media}}/gertz/rdb/04-indexing-2.pdf#page=11)
- Recursive approach, for north-neighbour find the entry that is most south from
  your northern sibling
- Does only work for directional NN


#Quadtree Complexity:
For a given polygon with perimeter $$p$$,
$$O(n+p)$$

#MX QuadTree

Aim:

- Ensure that the shape (and height) of the tree is independent of the
number of nodes in the tree, as well as the order of insertions.
- Adequate presentation for points as long as the domain of the points is
finite and discrete (i.e., there’s a minimum separation between points).


<details>
<img src="{{urls.media}}/gertz/rdb/mx_quad1.png">
<img src="{{urls.media}}/gertz/rdb/mx_quad2.png"></details>


#PM QuadTree

- Represent polygonal maps
- Either vertex or edge-based

$$PM_1$$
- Instead of requiring that points in a square are homogeneous, we
require that
1. every leaf of the quadtree corresponds to a square that has at most one
point (vertex of the polygon) located in it.
2. a leaf node that stores information about a vertex may only contain
additional information about edges that are incident to that vertex.
3. a leaf that does not contain information about a vertex may only contain
information about at most one part of an edge.
If the above conditions cannot be satisfied, the square has to be partitioned
further.

$$PM_2$$
- If a leaf node’s region contains no vertices, then it can contain
only edges that meet at a common vertex exterior to the region.

<details><img src="{{urls.media}}/gertz/rdb/pm_quad1.png"></details>

#Space-Filling curves

A space-filling curve defines a total order on the cells of a 2-dimensional
grid. They assign numbers to cells such that cells that are close in space
are also close in the total (physical) order imposed by the space filling
curve.
In general, a space-filling curve tries to map a 2-dimensional space into a
1-dimensional space (extension to 3-dimensional exist as well).
<details>
<summary>Morton code</summary>
<img src="{{urls.media}}/gertz/rdb/space_filling.png"></details>


[Script]({{urls.media}}/gertz/rdb/04-indexing-2.pdf)
[Quadtree-slides](http://www.win.tue.nl/~kbuchin/teaching/2IL55/slides/03quadtrees.pdf)
