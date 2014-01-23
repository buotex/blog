{
  "title": "B+-Tree",
  "date": "2014-01-23",
  "categories": [
   "database" 
  ],
  "tags": [
    "data structure"
  ]
}


#Multi-Version BTree (MVBT)

##Basics

- Store all versions of the state of a B-Tree
- Modifications are applied to the present version and increase the version number of the whole tree
- Queries have additional parameter: **version**
- Cost is a constant factor in time an space for the additional version handling
- each B-Tree root represents an interval of versions

##Properties and Subroutines:

Live/Dead
: a block is live if it is the head-copy, otherwise it's dead

Version split!
: Copy the block and remove all but the current version entries form copy
: Can cause strong version underflow

Split by key
: Create 2 new blocks, split up old block into both of them

Merge sibling blocks
: merge blocks with only current version entries, may require Version split

##Parameters:

b
: Maximum number of entries in a single block

d
: minimum number of current version entries, if an entry is deleted we get a 
**weak version underflow**

$$\epsilon$$
: Required for the Strong version condition, controlling the number of current version entries

##Constraints:

Weak version condition!
: We require that every block has either 0 or d entries of every version.

   - underflow: Do Version split

Strong version condition!
: The number of current version entries after a version split must be in $$[(1 +
\epsilon)*d, (k-\epsilon)*d]$$

   - underflow: Merge sibling blocks
   - overflow: split by key values

Split-constraint
: $$(1/2)(1+\epsilon)d \leq SVC_high+1$$
: Guarantee that after a split both of the resulting blocks are not overfilled wregarding the Strong
condition.

Merge-constraint
: $$2d-1 \geq SVC_low$$: The blocks to be merged need a minimum number of entries so that the
resulting block is bigger than required for the Strong condition.



###References

- [Script]({{urls.media}}/gertz/rdb/04-indexing-1.pdf#page=5)
- [MultiVersion]({{urls.media}}/gertz/rdb/06_std-1.pdf)

