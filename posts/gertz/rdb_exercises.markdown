{
  "title": "Exercises for rdb",
  "date": "2013-12-09",
  "categories": [
"exercises"
  ],
  "tags": [
  "algorithms"
  ]
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
[Douglas Peucker](./douglas_peucker)




##[Zettel3]({{urls.media}}/gertz/rdb/assignment3_v4.pdf)

##[Zettel4]({{urls.media}}/gertz/rdb/assignment4.pdf)


