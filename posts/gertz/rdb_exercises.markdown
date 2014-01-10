{
  "title": "Exercises for rdb",
  "date": "2014-01-07",
  "categories": [
"database",
"exercises"
  ],
  "tags": [
  "algorithms"
  ],
 "widgets": {
        "google_prettify": {
            "use": "sql"
        }
    }
}


##[Zettel1]({{urls.media}}/gertz/rdb/assignment1.pdf)
1:

~~~sql
Select count(*), name from Polygons natural join Countries group by country_id, name;

select count(distinct p2.country_id) from Countries natural join Polygons as p1, Polygons as p2 where p1.point_id = p2.point_d group by
p1.country_id;

Select count(distinct p2.country_id) as neighbour_count from Countries, Polygons as p1, Polygons as p2 where ST_INTERSECTS(p1, p2) 
and Countries_id = p1.country_id and p1.country_id <> p2.country_id group by country_id order by neighbour_count;
~~~


##2:

###Metrik

  - \$$d(x,x) = 0$$
  - $$d(x,z) \leq d(x,y) + d(y,z)$$ (Dreiecksungleichung)
  - $$d(x,y) = d(y,x)$$ (Symmetrie)
  - if $$ x != y, d(x,y) > 0$$ voll-dim

i) assymetrisch
ii) metrik
iii) 0 für orthogonale vektoren

b)
Quasi-metrik wenn asymetrisch, also d(x,y) != d(y,x)
pseudo-metrik wenn nullteiler, also wenn es x,y gibt mit d(x,y) = 0, aber x != y

##3:
Monotone Polyline:
Betrachte die Linie als ihre Teilstücke.
Der Winkel zwischen einem Stück und seinen folgenden Stücken muss größer als 0 sein
Dabei müssen die Winkel je gleich gemessen werden.





##[Zettel2]({{urls.media}}/gertz/rdb/assignment2_v2.pdf)

References:

- [posts/Polygon](/posts/gertz/ComputationalGeometry#polygon)
- [Polygon partitioning](http://www.personal.kent.edu/~rmuhamma/Compgeometry/MyCG/PolyPart/polyPartition.htm)

###1:
Too Postgis specific, skipping for now

###2:

- Prove that every simple Polygon has a triangulation.
- Prove that any triangulation of a simple polygon with n vertices contains n-2 triangles.


The second part is trivial due to the algorithm, as 3 points always construct a
triangle and are then removed.
It remains to show that you can always find 3 points to construct a triangle.

**Recursion**:

- $$n = 3$$: trivial
- $$n \rightarrow n-1$$: 
  By cutting off the left-most triangle, you create a new simple polygon with
$$n-1$$ points

###3:


- _Convex_ Polygon Distances: Compute the minimum and maximum distance between two convex, non-overlapping polygons
- Goal: $$O(log(N))$$

####Important:

For a one-time query, actually building a data structure like an
[R-Tree](http://en.wikipedia.org/wiki/R-tree) has too much overhead to still fit
into our requirements, a dynamic approach here is better.
Also: minimum and maximum are almost the same, so I'll just describe one of the
two (**minimum**)

~~~Python
#P,Q are lists of points

p = P[0]
while len(Q) > 1:
  step = len(Q)/4
  distances = [dist(p,q) for q in [Q[i] for i in range(0,len(Q), step]]
  indices = argmin(distances)
  #Select quarter with the two closest points
  Q = Q[indices[0] *step:indices[1] * step]
  #repeat

#Switch Q and P

~~~

###4:
See
[posts/Douglas Peucker](/posts/gertz/douglas_peucker)




##[Zettel3]({{urls.media}}/gertz/rdb/assignment3_v4.pdf)

**’Plane-sweep’ and ’Divide and Conquer’ Algorithms**

##[Zettel4]({{urls.media}}/gertz/rdb/assignment4.pdf)

###1:
Actually, I still have the old solutions for that!


####a:

~~~sql

Explain ANALYZE
SELECT id
FROM places
WHERE
((lng-8.693)^2 + (lat-49.41)^2) <= 0.25
Order By ((lng-8.693)^2 + (lat-49.41)^2) ASC
Limit 5;
~~~

Just standard database query.


####b:

~~~sql
--Explain ANALYZE
Select id
From places
Where 
lng Between 8.193 And 9.193 AND
lat Between 48.91 And 49.91 AND
((lng-8.693)^2 + (lat-49.41)^2) <= 0.25
Order By ((lng-8.693)^2 + (lat-49.41)^2) ASC
Limit 5;
~~~

Limit results beforehand with indices on lng and lat, by user knowledge of the
metric used.

####c:

~~~sql
--Explain ANALYZE
Select id
From places
Where ST_Distance(ST_GeomFromText('POINT(8.693 49.41)',4326),point)<=0.5
Order By ST_Distance(ST_GeomFromText('POINT(8.693 49.41)',4326),point) ASC
Limit 5;
~~~

Use of ``ST_Distance``, which uses the euclidean metric, doing a query region / point overlap.

####d:

~~~sql
--Explain ANALYZE
Select id
From places
Where point && ST_Expand(ST_GeomFromText('Point(8.693 49.41)', 4326), 0.5) AND
	ST_Distance(ST_GeomFromText('POINT(8.693 49.41)', 4326), point) <= 0.5
Order By ST_Distance(ST_GeomFromText('POINT(8.693 49.41)', 4326), point) ASC
Limit 5;

~~~

Use of ``ST_Expand``, which creates a neighborhood around the query point, so
now we query region / region overlap.


###2:

~~~python
#Let P = points
#Let C = convexHull(P)

minrect = rect(inf,inf)
for c1,c2 in zip(C[::2],C[1::2]):
  l = line(c1,c2)
  #Rotate all points so that the line is axis-aligned
  P_rotated = transform_coordinates_to_axes(l, P)
  rect = bounding_box(p_rotated)
  if rect <= minrect:
    minrect = rect

~~~

What is the runtime for that?
The outer loop runs in $$O(n)$$, so the runtime of the bounding box algorithm
that's important.
Given that we restrict the bounding boxes to be axis aligned (due to the
rotation), it can just be computed via min/max values.
That said, this actually still takes linear time, as we have to recompute after
every rotation, so it is still $$O(n^2)$$ combined.


[Rotating calipers](http://en.wikipedia.org/wiki/Rotating_calipers)



###3:

####KD-Tree

- [posts/kdtree](/posts/gertz/kdtree)




##[Zettel5]({{urls.media}}/gertz/rdb/assignment5_v2.pdf)

###1:

~~~sql
SET client_encoding = 'UTF8';
SET standard_conforming_strings = off;
SET check_function_bodies = false;
SET client_min_messages = warning;
SET escape_string_warning = off;
SET search_path = public, pg_catalog;
SET default_tablespace = '';
SET default_with_oids = false;


CREATE TABLE places(
         id integer PRIMARY KEY, 
         name varchar, 
		 type varchar,
         lat float, 
         lng float);
SELECT addgeometrycolumn('places', 'point', 4326, 'POINT', 2);
COPY places(id, name, type, lat, lng) FROM STDIN; 
~~~

~~~sql
SELECT *
FROM places
where point && ST_Expand(ST_GeomFromText('Point(8.9 48.8)', 4326), 0.1) AND
ST_Distance(ST_GeomFromText('POINT(8.9 48.8)', 4326), point) <= 0.1
AND type = 'restaurant'
ORDER BY ST_DISTANCE(ST_GeomFromText('Point(8.9 48.8)', 4326), point) ASC
LIMIT 10;
~~~



###2:

Task: algorithm for the overlap of 2 region quad trees

~~~python
def intersect(tree1, tree2, tree3):
  if tree1 is leaf or tree2 is leaf: 
    if tree1.filled() and tree2.filled():
      tree3.setFilled()
      return
  if tree1.children == tree2.children:
    tree3.children = tree1.children
  else:
    tree3.createChildren()
    for t1,t2,t3 in zip(tree1,tree2,tree3):
      intersect(t1,t2,t3)



~~~
Complexity: $$O(n * (d + 1))$$ where d = max(d1,d2)

####QuadTree

- [posts/quadtree](/posts/gertz/QuadTree)

####RTree

- [posts/rtree](/posts/gertz/rtree)


##[Zettel6]({{urls.media}}/gertz/rdb/assignment6.pdf)
