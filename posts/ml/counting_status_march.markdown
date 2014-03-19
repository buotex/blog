{
  "title": "Counting status march",
  "date": "2014-03-12",
  "categories": [
    "unsorted"
  ],
  "tags": [
    
  ]
}

#Summary:

###Training Data

![]({{urls.media}}/counting/results/february/gt_gerlich1.jpg)

**~ 10 cells**

###Training with dots , high sigma:

<a href="{{urls.media}}/counting/results/february/training_dots.png"
class="lightview"><img
src="{{urls.media}}/counting/results/february/training_dots.png" >
</a>

###Skeleton:

<a href="{{urls.media}}/counting/results/february/skeleton_labels.png"
class="lightview"><img
src="{{urls.media}}/counting/results/february/skeleton_labels.png" >
</a>

###Training with skeletons, high sigma:

<a href="{{urls.media}}/counting/results/february/training_skeletons.png"
class="lightview"><img
src="{{urls.media}}/counting/results/february/training_skeletons.png" >
</a>


###Prediction Ground Truth

![]({{urls.media}}/counting/results/february/gt_gerlich.jpg)

####Prediction with Dots

![]({{urls.media}}/counting/results/february/dots_many_features.png)

Results: 
 
- predicted ~ 35 cells due to all the noise


###Prediction with Skeleton


<a href="{{urls.media}}/counting/results/february/prediction_skeleton.png"
class="lightview"><img
src="{{urls.media}}/counting/results/february/prediction_skeleton.png" >
</a>

**Prediction: 13.5**





#Bayer dataset:

###Confusion matrix of the region classification

![]({{urls.media}}/counting/results/february/confusion_matrix.png)

###Overlaid grid for cell data

![]({{urls.media}}/counting/results/february/bayer_grid_overlay.png)

Ground truth: 550
Predicted: 574

###Overlaid grid for cell data, dense

![]({{urls.media}}/counting/results/february/bayer_grid_overlay2.png)

![]({{urls.media}}/counting/results/february/confusion_matrix_bayer_2.png)

Ground truth: 2539
Predicted: 2726


#Blue cells:

###Confusion matrix of the region classification

![]({{urls.media}}/counting/results/february/confusion_matrix_blue.png)

Ground truth: 135
Predicted: 160







#Notes:

- Using all region features(minus global ones) produce terrible results in the bayer dataset
- Gives very good results in the blue cell dataset
- vigra: skewness is NaN for uniform region


#Experiment with stretching:

By stretching the image by a factor of two, along with the labels, the results are changed quite an
amount.
Now the question is, how _wrong_ are the results? And does using skeletons fix these problems? (i'm
really not sure about it)


#More notes:
- Region labels: We solve the problem of the maximum independent set (which is also inverse to the
maximum vertex cover), to select the best superpixels from the two sets.



#Iterated svr:
1. We use a heuristic to solve np-hard MIQP
2. This heuristic is likely to only find a local minimum (which may be good enough?)
3. Values are _very_ unlikely to actually hit 0
4. To circumvent this, I used an epsilon bound (thematically fitting), which gives everything a push
   to the other side, that came from one direction into the bound
5. Thought error? Currently, the result oscillates between 2 configurations.
6. Variable "step length" (in this case, epsilon bound) gives funny results

##Strategies for exchanging background/foreground:

- Use similar to simplex?
- variable epsilon bound

- Need 


#Footnotes/Data
[presentation_folder]({{urls.media}}/counting/presentation_bayer)


