{
  "title": "Computational Geometry",
  "date": "2013-12-05",
  "categories": [
  "study"
  ]
}

##Segment Intersection
Test whether segments (a,b) and (c,d) intersect

Two segments (p1,q1) and (p2,q2) intersect if and only if one of the 
following two conditions holds:
1. general case: (p1,q1,p2) and (p1,q1,q2) have different orientations and 
(p2,q2,p1) and (p2,q2,q1) have different orientations.
2. special case: (p1,q1,p2), (p1,q1,q2), (p2,q2,p1), (p2,q2,q1) are all 
collinear and the x-projections of (p1,q1) and (p2,q2) intersect and the y-projections of (p1,q1) and (p2,q2) intersect.

##Simple Closed Path
Anchor point
Traversing the points by increasing angle yields a simple closed path

##Convex Hull

##Sweep-Line Method!
-Sweep-line active list L: this structure is updated as the line goes 
through a finite number of positions, called events.
-Event list E: known beforehand (managed as a linked list) or discovered 
step-by-step as sweep goes on (managed by a more flexible structure, 
e.g., priority queue).
-Bsp: Rectangle-Intersection

#Polygon

**Simple Polygon**

- A polygon encloses a region (called its interior) which always has a measurable area.
- The line segments that make-up a polygon (called sides or edges) meet only at
  their endpoints, called vertices (singular: vertex) or less formally "corners".
- Exactly two edges meet at each vertex.
- The number of edges always equals the number of vertices. 

**Monotone Polygon**

- A polygon P in the plane is called monotone with respect to a
  straight line L, if every line orthogonal to L intersects P at most twice

**Polygon complexity**

The ordering by complexity is
- ``generic > simple > monotone > convex``
- [Script reference]({{urls.media}}/gertz/rdb/03-comp-geometry.pdf#page=32)

[Triangulation]({{urls.media}}/gertz/rdb/03-comp-geometry.pdf#page=35)

- Non-deterministic
- n-2 triangles
- Monotone polygons can be triangulated linearly, thus partitioning a 
  simple polygon into monotone polygons is key to efficient triangulation

Monotone chain
: Andrew's monotone chain convex hull algorithm 
  
- Sorting the points lexicographically (first by x-coordinate,
  and in case of a tie, by y-coordinate), and then constructing upper and lower
  hulls of the points in O(n) time.
- [wiki](en.wikibooks.org/wiki/Algorithm_Implementation/Geometry/Convex_hull/Monotone_chain)

Triangulation works as follows: [Example]({{urls.media}}/gertz/rdb/03-comp-geometry.pdf#page=36)

0. Active stack S, reserve stack R, both stacks hold vertices,
   vertices sorted according to the monotone chain criteria
1. Iterate over sorted vertices, pop into S
2. If #S == 3, check if these points construct a triangle, otherwise move one
   the points to R
3. If a triangle was completed, S = R, clear R

**Complexity**: $$N \log N$$ due to sorting
