{
  "title": "Shortest Path",
  "date": "2013-12-05",
  "categories": [

  ]
}

##Djikstra
**One to One**

##Bellman-Ford
**One to Many**
Correct(u,v)

##Floyd Warshall
**Many to Many**
Dynamic Programming
shortestPath(i,j,k+1) = min(shortestPath(i,k+1,k) + shortestPath(k+1,j,k), shortestPath(i,j,k))
