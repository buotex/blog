{
  "title": "Paper Draft",
  "date": "2013-12-06",
  "categories": [
	"counting"	
  ]
}

{{#todo_block}}
##General issues {#Test}
- [+] Typos, missing words
- [ ] Switch cite-ing method
- Layout
- Perhaps slightly more text for the figures?
- [+] References are overlapping and ultra-ugly
- [ ] Rearrange some of the figures
- Take the bayer data into account? - No ground truth... and also worked with
  mask
- Update references?


##Improvements
- [ ] State heavily that we can use very easily computed pixelwise features.
	This improves the speed a lot.
- Refer to ilastik0.5 (or even 0.6) implementation?
- Stress that code is available, as the gui part is missing
{{/todo_block}}

##Design of counting paper

- 7 pages
- 1 page Introduction and Motivation
- 3.5 pages Model and Implementation details
- 1.5 pages Experiments and Results
- 0.5 page Summary + References


##Design of Lempitsky paper

- 8 pages
- 1.5 pages Introduction
- 0.5 pages Background and Contributions
- 2 pages Model and Implementation details
- 3 pages Experiments and Results
- 1 page Summary + References
- Blocks of text are similar in size


##Abstract

- Objective of counting:
In this work, we estimate the number of istances of a certain class in an image (e.g.
cells) by integrating over the prediction of a linear model for every pixel,
following \cite{lempitsky_12}.

For counting objects, the current state-of-the-art algorithms 
require the labeling of all relevant instances of an object (e.g.\ a cell) in a
region of interest.
Many of these may be redundant or uncertain, at the same time the user cannot receive intermediate feedback.
We therefore present an approach using \emph{partial} annotations, allowing the user to only label relevant objects
while looking at the current prediction.

Using a modification of the SVR model with a newly introduced background
class, we can obtain competitive results using standard pixel-features.
As another contribution, we introduce the concept of region labels, which allow
an additional source of input and show that our formulation, 
can still be solved with a standard quadratic solver such as CPLEX.
An open source implementation will be provided in the framework of
http://ilastik.org


##Introduction

This work focuses on a machine learning problem known as \emph{counting},
estimating the number of occurrences of a specific object type in a given dataset.

This recently popularized field has numerous uses in practice, recent works focus on handling
either people (e.g.\ pedestrians on a sidewalk) for monitoring purposes or
cells, which can used as a prior for \emph{tracking} procedures, both in still
images or video feeds.

The intuitive approach to counting, which is one of two general schools of thought, 
consists of first detecting individual instances, which renders the
remaining counting problem trivial.
In tasks which generally feature dense data such as cells, overlapping instances
numbering in the dozens become a common occurrence. 
At this point, the detection problem becomes intractable, requiring a different strategy.

Recent works, such as 
\cite{lempitsky_10_learning} and \cite{fiaschi_12_learning}, thus tried to handle
\emph{counting} on a more global level: instead of detecting instances directly, 
estimating the object density for individual pixels, based on the
local texture, proved to be successful.

But while the current state of the art already achieves very accurate
results for counting both cells and people, the algorithms still require
\emph{fully} annotated images, which means labeling every
single instance in a given region of interest, often in multiple training
images, which implies a lot of redundant work done by the human expert.
Our contribution consists of a framework, supplied with a graphical user
interface, which only requires \emph{partial} annotations, thus reducing the
manual workload tremendously while providing rapid feedback on the current
quality of the predictions.
- Rewrite introduction, as level for paper is higher


##Motivation

- Perhaps less from a user perspective?
