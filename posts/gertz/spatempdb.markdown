{
  "title": "Spatio-temporal Databases",
  "date": "2014-01-24",
  "categories": [
    "databases"
  ],
  "tags": [
    
  ]
}

#Basics

##Queries

**Split by dimensionality**

- Moving point (point, sequence)
- Country borders (region/ period)
- Other combinations of point/region vs instance/sequence/period

**Split by querytype**

- NN queries
- Selection queries
- Aggregate queries
- Join queries
- SImilarity queries

##Data structures

- One Approach: 3D-R-Tree, but:
- Difficult to cluster
- Overlaps / empty spaces
- What is **now**

![3D RTree]({{urls.media}}/gertz/rdb/3dr_tree.png)

##Representations in 3D+t

- Moving points create **trajectories**, which can be modelled by e.g. linear interpolation


#References

- [Script]({{urls.media}}/06_std-3.pdf)
- [Script]({{urls.media}}/06_std-4.pdf)
