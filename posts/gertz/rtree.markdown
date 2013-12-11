{
  "title": "R Tree",
  "date": "2013-12-11",
  "categories": [
    "database"
  ],
  "tags": [
    "data structure"
  ]
}



- hold d-dimensional objects
- query: points
– Each node has a 
	directory rectangle
	(dr),
	which is the minimal bounding 
	box of its child nodes.
– Access to rectangle(s) occurs 
	through tree traversal and tests for 
	rectangle containment/overlap.


[Script]({{urls.media}}/gertz/rdb/04-indexing-3.pdf)
