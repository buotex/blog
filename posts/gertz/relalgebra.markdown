{
  "title": "Relational Algebra",
  "date": "2014-01-23",
  "categories": [
   "database" 
  ],
  "tags": [
    "data structure"
  ]
}

#Operators

Select operator
: $$\Sigma_{GPA > 3}$$
: Subscript is a list of conditions combined by $$\land, \lor$$

Project operator
: $$\Pi_{Student}$$
: Subscript is a list of attributes
: affixed by relationname

Cross product
: $$ Rel1 x Rel2$$
: Rel1.attrib = Rel2.attrib if they have the same name
: cartesian product of the relations

Natural join
: $$\Join$$
: Enforce equality on all attributes
: Eliminate duplicates
: Can have the same number of results as cartesian product

Theta join
: $$\Join_{\theta}$$
: $$\theta$$ is a list of conditions
: $$Rel1 \Join_{\theta} Rel2 = \Sigma_{\theta}(Rel1 x Rel2)$$ 
: Theta is often not said explicitly, sometimes just known as the normal join

Union
: $$\Cup$$
: combine vertically

Difference
: $$-$$

Intersection
: $$\Cap$$
: Can be expressed by the Difference operator

Rename
: $$\Rho$$
: $$\Rho_{Relname(attrname1, attrname2, ...)}$$
: Very useful for self-joins
: removes ambiguity
: Preparation for union / natural joins etc., by renaming to the same columns

Semi-Join
: Like natural join, but only keep the columns of the left (or right) operand


#Tricks

Backjoin
- First extract the columns, 
- do some set operation on them (e.g. union, difference etc.)
- do a natural join of the result and the original source of those columns
- Example: $$(\Pi_A Students \Cap \Pi_A Apply) \Join Students to get students that have applied

First you can use a filter operation on 