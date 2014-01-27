{
  "title": "References",
  "date": "2014-01-24",
  "categories": [
	"counting"    
  ],
  "tags": [
    "references"
  ]
}

###[Learning to Count with Regression Forest and Structured Labels]({{urls.media}}/counting/fiaschi_12_learning.pdf)
- Random Forest on structured labels
- Training / Prediction on overlapping **patches**
- Dot annotations, gaussian smoothing applied
- Sensitive to different sizes of objects (not functioning)
- Implementation not working for 3D
- experiments on Pedestrians / Cells
- Fully annotated data

###[Learning-based Mitotic Cell Detection in Histopathological Images]({{urls.media}}/counting/sommer_12_learning-based.pdf)
- 2 step model
- Pixel classification into candidates (foreground / background) via ilastik
- classification of candidate cells into mitotic/non-mitotic via cellcognition

###[Weakly Supervised Learning for Image Quality Control]({{urls.media}}/counting/lou_12_quality.pdf)
- classifying **images**
- weakly-supervised
- outlier-detection via one-class svm

### cvpr2013: Learning to detect Partially Overlapped Instances 
- [Publication]({{urls.media}}/counting/cvpr2013.pdf)
- Arteta/Lempitsky/Noble/Zisserman
- Detection-based / **Classification**
- Every region is assigned a label corresponding to number of objects (~1-5)
- Model considers a pool of nested regions 
- Extremal region detection MSER
- Non-overlapping constraint for regions
- Solution: Linear program
- Too slow for us (30 sec for 400 x 400) due to feature computation
- Could be made to work for partial annotations? Still full
- Pedestrians / Cells
- Dataset: available at http://www.robots.ox.ac.uk/~vgg/research/cell_detection/ has matlab code and demo dataset

###pone.0001457 Identification of Novel Pro-Migratory....
- [Publication]({{urls.media}}/counting/journal.pone.0001457.pdf)
- Migration-based?
- for that, images have to be clear enough so that cells leave tracks
- not much on our current data

###structured-domain-adaptation-nips.pdf 
- [Publication]({{urls.media}}/counting/structured-domain-adaptation-nips.pdf)
- How 2D helps 3D interference
- Eventually, we want to learn a robust prediction model for the complex 3D problem using as little supervision as
possible. 
- First, we adopt domain adaptation to structured learning such that knowl-
edge from solving the 2D problem (source) can be transferred to the complex 3D one (target). 
-Second, we employ
learning from partial annotation [6] to further reduce the annotation cost in the complex target domain (annotation is
very expensive in 3D).

#Status:

- [November](/posts/ml/counting_status_november)
- [December](/posts/ml/counting_status_december)
- [January](/posts/ml/counting_status_january)
