{
  "title": "Metrics and Similarity",
  "date": "2014-01-13",
  "categories": [
    "databases",
    "maths"
  ],
  "tags": [
"euclidean"
    
  ]
}
#Metrics

##Basics
A metric space is an ordered pair $$(M,d)$$ where $$M$$ is a set and $$d$$ is a metric on $$M$$,
i.e., a function
$$d \colon M \times M \rightarrow \mathbb{R}$$
such that for any $$x, y, z \in M$$, the following holds:

- Non-negativity $$d(x,y) \ge 0$$
- Symmetry $$d(x,y) = 0\, iff x = y\$$
- Triangle inequality $$d(x,z) \le d(x,y) + d(y,z)$$

##Euclidean
$$\mathrm{d}(\mathbf{p},\mathbf{q}) = \mathrm{d}(\mathbf{q},\mathbf{p}) =
\sqrt{(q_1-p_1)^2 + (q_2-p_2)^2 + \cdots + (q_n-p_n)^2} = \sqrt{\sum_{i=1}^n
(q_i-p_i)^2}$$


##Manhattan
$$d_1(\mathbf{p}, \mathbf{q}) = \|\mathbf{p} - \mathbf{q}\|_1 = \sum_{i=1}^n
|p_i-q_i|$$

##Mahalanobis
The Mahalanobis distance of a multivariate vector $$x = ( x_1, x_2, x_3, \dots,
x_N )^T$$ from a group of values with mean $$\mu = ( \mu_1, \mu_2, \mu_3, \dots ,
\mu_N )^T$$ and covariance matrix S is defined as:
$$D_M(x) = \sqrt{(x - \mu)^T S^{-1} (x-\mu)}$$

#Similarities

##Cosine similarity
The cosine of two vectors can be derived by using the Euclidean dot product
formula:
$$\mathbf{a}\cdot\mathbf{b}
=\left\|\mathbf{a}\right\|\left\|\mathbf{b}\right\|\cos\theta$$
Given two vectors of attributes, A and B, the cosine similarity, cos(θ), is
represented using a dot product and magnitude as

$$\text{similarity} = \cos(\theta) = {A \cdot B \over \|A\| \|B\|} = \frac{
\sum\limits_{i=1}^{n}{A_i \times B_i} }{ \sqrt{\sum\limits_{i=1}^{n}{(A_i)^2}}
\times \sqrt{\sum\limits_{i=1}^{n}{(B_i)^2}} }$$
