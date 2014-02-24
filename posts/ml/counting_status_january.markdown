{
  "title": "Counting status January",
  "date": "2014-02-07",
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

##Datasets

Our first experiments are done on the gerlich dataset, stored on the mip-server ( ssh://hci:/home/users/mip/data/gerlich )
![]({{urls.media}}/counting/results/gerlich.jpg)

####Notes

- orange: just before split
- purple: splitting
- green: boring
- yellow: merging

- WARNING: DON'T USE .values() for region features - THINGS WILL BREAK



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
- [Springerlink](http://link.springer.com/chapter/10.1007%2F978-3-642-40395-8_21)
- Gibbs-Markov random field model

![]({{urls.media}}/counting/results/january/superpixels_boundaryOverlay.png)

``~/code/compareCounting/superpixels/contourRelaxedSuperpixels-0.1-r2/build/contourRelaxedSuperpixels
superpixels2.png 10 10``
~20 secs

![]({{urls.media}}/counting/results/january/superpixels2_boundaryOverlay.png)

####Evaluation:

- Performs well compared to a previous watershed approach, though it is also magnitudes slower.
- Biggest difference: borders are much smoother and most sizes are homogeneous.

Proposal of modification: Instead of placing gaussians on top of the dot-marks, we can instead let
consider the dot as a seed for a region - such that the whole region can be used as an annotation.
Of course, this is only viable if the number of overlaps is small and thus this segmentation is
feasible.

Given the scale of the bayer data, for example, this would be impossible for dense regions - there,
dots are still the best solution. On the other hand, is it possible to differentiate cells with that
resolution?

<!---
##Ex5

- Do superpixel segmentation
- foreground/background segmentation / unsupervised perhaps? 
- Calculate features for superpixel 
- integrate vigra stuff?
- clusterization
- place seeds
- bleed seeds out into regions
- training / prediction
-->

##Ex5

- Prediction / Training for superpixels
- Contour-relaxed superpixels
- Using vigra region-features

####Result
![]({{urls.media}}/counting/results/january/superpixeltraining.png)
![]({{urls.media}}/counting/results/january/superpixelprediction.png)

- Left: Ground truth, Right: Prediction, Top: Training
- Number of samples: 16 Superpixels
- Every superpixel is assigned a count, blueish for low counts (down to 0), red for higher values (up
to 4 in this set).
- Foreground/background segmentation is working passably, but the counts are still bad
- Features used: ['Mean', 'Minimum', 'Maximum', 'Count', 'Covariance', 'Principal<PowerSum<2> >']
- 135 gt, 180 predicted, 76% of the superpixels were predicted correctly, similar results over
 multiple runs

##Ex6



- Get more ground truth by using multiple parameters for the superpixels - bit close to multigrid
 approach
- First test using 2 layers
- Pyramid graphical model scheme
- Solve with ???
- Combine either pylon or contour approach with structured forest
- How do we enter a cost matrix into the forest?
- Suggestion: Tune the random forest to purity with regards to classes in its leaves
- Suggestion: For the number of elements, do something elaborate?

![]({{urls.media}}/counting/results/january/superpixelgrid.png)
Better results due to using 2 layers, numbers:
- 135 gt, 160 predicted, less noise, 78-80% superpixels correct
- foreground/background segmentation now correct

Approach:



#Todo

{{#todo_block}}
- [+] Ask U. about phone-conference
- [] Implement ilastik-gui option to take advantage of the segmentation? - unlikely
- [] Prepare console workflow again, this time based on superpixels!
- [+] Find decent superpixel features
{{/todo_block}}

#References
[Mitosis detection on gerlich data]({{urls.media}}/counting/sommer_12_learning-based.pdf)
