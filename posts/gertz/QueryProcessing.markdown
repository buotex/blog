{
  "title": "Query Processing",
  "date": "2013-12-05",
  "categories": [
   "study",
   "databases"
  ]
}

##Optimal I/O

###Sort/Merge
  - Sort relations on join attribute
  - merge-join
  - $O(N \log N)$
  - Is essentially a merge-sort (which has an implicit binary tree)

###External Sort/Merge
  - Now the tree is based on pages, not records - i.e. we now sort pages
  - Put m pages into memory, sort, write to disk

##Spatial join

##Complex queries

##Similarity search

##Nearest-Neighbor queries

##Reverse Neares-Neighbor queries


