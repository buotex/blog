{
  "title": "Douglas Peucker",
  "date": "2013-12-09",
  "categories": [
	"database/spatial"    
  ],
  "tags": [
	"algorithm"
  ]
}

[Wiki](http://en.wikipedia.org/wiki/Ramer%E2%80%93Douglas%E2%80%93Peucker_algorithm)

~~~lua

function DouglasPeucker(PointList[], epsilon)
    // Find the point with the maximum distance
    dmax = 0
    index = 0
    end = length(PointList)
    for i = 2 to ( end - 1) {
        d = shortestDistanceToSegment(PointList[i], Line(PointList[1], PointList[end])) 
        if ( d > dmax ) {
            index = i
            dmax = d
        }
    }
    // If max distance is greater than epsilon, recursively simplify
    if ( dmax > epsilon ) {
        // Recursive call
        recResults1[] = DouglasPeucker(PointList[1...index], epsilon)
        recResults2[] = DouglasPeucker(PointList[index...end], epsilon)
 
        // Build the result list
        ResultList[] = {recResults1[1...end-1] recResults2[1...end]}
    } else {
        ResultList[] = {PointList[1], PointList[end]}
    }
    // Return the result
    return ResultList[]
end

~~~    

![Animated algorithm]({{urls.media}}/gertz/rdb/Douglas-Peucker_animated.gif)

### Complexity:

- Average case: $$O(n \log n)$$ due to application of the [Master Theorem](/posts/algorithms/master_theorem) on the recursive formulation $$T(n) = 2T(n/2) + O(n)$$
- Worst case: $$O(n^2)$$ 

### Analysis:

- Worst case: No simplification possible, worst points in linear order. (So the
  outer loop is (1-n), (2-n), (3-n) etc.
- Average case: Worst point in the middle, therefore problem getting split up
  $$(T(n/2))$$, though each half has to be worked on, so $$2(\cdot)$$ along with
  $$O(n)$$ to iterate over every point to check if it is the worst one.


### Optimality:

Does it present the _best_ solution, i.e. is the problem convex?
Actually, no! The order of things is important here.

Counter-example:

![Counter example]({{urls.media}}/gertz/rdb/Douglas_Peucker.png)
