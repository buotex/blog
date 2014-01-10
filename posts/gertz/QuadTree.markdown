{
  "title": "Quad Tree",
  "date": "2014-01-07",
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


#MX QuadTree

#PM QuadTree


[Script]({{urls.media}}/gertz/rdb/04-indexing-2.pdf)
[Quadtree-slides](http://www.win.tue.nl/~kbuchin/teaching/2IL55/slides/03quadtrees.pdf)
