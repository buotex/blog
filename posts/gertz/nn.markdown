{
  "title": "Nearest Neighbour",
  "date": "2014-01-16",
  "categories": [
    
  ],
  "tags": [
    
  ]
}

#Basics

``NN(p,k)`` applied on a database DB.
Given a query point $$p$$, find k objects $$O \in DB$$, such that $$dist(p,o) \leq dist(p,o') \forall o \in O, o' \in
DB \setminus O$$

Two interpretations:
- Find **at least** k nearest neighbours, this is deterministic.
- Find exactly k-nn, this is not necessarily deterministic, as some objects could have the same distance.

#Algorithms

##Depth-first

###Basic variant

~~~python
def dfs_nn(p, node, k):
  if node is leaf:
    for child in node:
      if dist(p, child) <= results.farthest:
        results.add(child)
        if len(results) < k:
          results.pop_farthest()
    else:
      for child in node:
        if dist(p, child) <= results.farthest:
          results += dfs_nn(p, child, k)
~~~

Issues with this basic variant are obvious: as results.farthest may be uninitialized / very high, there is no sensible
pruning done. The first candidates may be very far in distance. 
At the same time, ``dist(p,q)`` may be a very expensive operation, so we should use some features of our spatial
database to improve on that!

###Filtering
Instead of directly using the ``dist(p,q)`` function, we can first use an approximate solution. Which would be the most
useful? Well, a lower estimate, $$LB$$ is fitting here: if we *underestimate the distance*, we can later refine it.

Possible ways for an underestimate:

- For an object $$q$$, simplify q and calculate ``dist(p,mbb(q))``.


Maxdist
Mindist
Minmaxdist


##RKV


