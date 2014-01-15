{
  "title": "M-Tree",
  "date": "2014-01-13",
  "categories": [
   "databases" 
  ],
  "tags": [
    
  ]
}

#Basics
- Similar to R-Tree and B-Tree
- Based on a metric and therefore relies on triangle inequality
- Range and kNN queries
- May have large overlaps

<details><img src="{{urls.media}}/gertz/rdb/mtree.svg"></details>

##Node:
Every node has the following entries:

- obj: The routing object (point) of the node
- cov rad: The radius covering all child nodes
- parent dist: The distance from the routing object to the center of the parent node
- ptr: A pointer to the root node of the subtree (pointer to child node)

![]({{urls.media}}/gertz/rdb/mtree.png)
