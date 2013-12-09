#Counting Future

## cvpr2013: Learning to detect Partially Overlapped Instances
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

##pone.0001457 Identification of Novel Pro-Migratory....
- file://home/bxu/Dropbox/study/counting/journal.pone.0001457.pdf
- Migration-based?
- for that, images have to be clear enough so that cells leave tracks
- not much on our current data

##structured-domain-adaptation-nips.pdf 
- How 2D helps 3D interference
- Eventually, we want to learn a robust prediction model for the complex 3D problem using as little supervision as
possible. 
- First, we adopt domain adaptation to structured learning such that knowl-
edge from solving the 2D problem (source) can be transferred to the complex 3D one (target). 
-Second, we employ
learning from partial annotation [6] to further reduce the annotation cost in the complex target domain (annotation is
very expensive in 3D).



