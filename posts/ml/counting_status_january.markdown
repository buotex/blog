{
  "title": "Counting status January",
  "date": "2014-01-17",
  "categories": [
 "counting"   
  ],
  "tags": [
  "report"  
  ]
}


``sshfs luca:data/counting ~/data/counting``

#Abstract
For the Bayer project, we're trying to count different cell phenotypes, perhaps even at the same time.
While for easier datasets, a classification scheme may be preferred (and very doable), more difficult ones may require
the use of specific counting methods such as hours, as overlaps make the classification not feasible.

#Introduction

##Dataset

Our first experiments are done on the gerlich dataset, stored on the mip-server ( ssh://hci:/home/users/mip/data/gerlich )
![]({{urls.media}}/counting/results/gerlich.jpg)




#Methods

##Baseline

###Ex1

**Use huge sigma**

First results:
![]({{urls.media}}/counting/results/gerlich1.png)

Issue: It is not possible to reliably mark split-up cells using our current
method (with dots) logically - Thus, the only remaining method is to mark the
the gap inbetween while using a huge gaussian size.

Let's try to actually tackle this problem, we have about a month? (actually, more like 2)



###Ex2

**For a split-up cell, just mark both**

![]({{urls.media}}/counting/results/gerlich2.png)

When marking both, it is difficult to calibrate our prediction results, due to the (stretched) shape of the cells.
For these images, an approach via classification is probably better - there are no overlaps anyway.
The result is otherwise quite messy for this dataset.

##Ex3

**Just use the ilastik pixel classification as a baseline**

![]({{urls.media}}/counting/results/gerlich3.png)

The results are actually worse than expected, there is not enough contextual data to really separate split-up cells from
normal ones. Pixel-wise anything may be troublesome here?
In classification, it would be doable to just take the majority of the area and count that, along with some other
tricks, but it is surprisingly difficult.


##Ex4

Move away from dot annotations?
We could try to implement the pylon-thingy, such that instead of dot annotations, it'd only be necessary to click on one
of these pylons.

Resources:

- [Lempitsky - pylon]({{urls.media}}/counting/lempitsky_2011_pylon.pdf)
- [Segmentation Tree](http://www.eecs.berkeley.edu/Research/Projects/CS/vision/grouping/resources.html)


##Notes

Both of the structure features in ilastik are useful to discern split-up cells, at low filter sizes.

##Superpixels

- [Contour relaxed superpixels](http://www.vsi.cs.uni-frankfurt.de/research/current-projects/superpixel-segmentation/)

![]({{urls.media}}/counting/results/january/superpixels_boundaryOverlay.png)

``~/code/compareCounting/superpixels/contourRelaxedSuperpixels-0.1-r2/build/contourRelaxedSuperpixels
superpixels2.png 10 10``
~20 secs


![]({{urls.media}}/counting/results/january/superpixels2_boundaryOverlay.png)


#Todo

{{#todo_block}}
- [+] Ask U. about phone-conference
{{/todo_block}}
