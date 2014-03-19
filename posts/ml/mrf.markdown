{
  "title": "Markov Random Field",
  "date": "2014-02-24",
  "categories": [
    "unsorted"
  ],
  "tags": [
    
  ]
}

#Markov Random Field

**models $$p(x,o) = p(x \vert) p(o)$$** (cmp. [CRF](/posts/ml/crf))

**A MRF is a countable set of random variables (often indexed by spatial position)**

#Keywords

- Ising model
- Potts model
- clique[^clique]


#Abstract

#Ingredients

- set of random variables
- undirected hypergraph [^hypergraph] on this set of RV
- range of RVs
- potentials

#Notes

- A specific hypergraph represents a family of distributions that all factorize as 

Compatibility
: $$p(x_1, x_2, x_3) = \frac{1}{Z} \prod_{c \in E} \Phi_C(X_C)$$

If such a probability distribution is positive ( > 0 over its entire domain), then it can be
represented as a Gibbs[^gibbsm] measure

Gibbs measure
: $$p(x) = \frac{1}{Z} exp(-Ene(x))$$

$$Ene(x) = \sum_{C \in E} \Psi_C(x_C)$$

$$\Psi$$ is **potential** on clique C and equal to $$-log \Phi_C$$, the **compatibility**

Markov property
:	$$p(x_A \vert x_{-A}) = p(x_A \vert  x_{\delta(A)})$$

Markov blanket
:	$$\delta(A) = \{ x_i \vert x_i \not \in A, \{x_i, x_j \in A\} \in C \in E \}$$

A subset of RVs $$A$$ is conditionally independent of all others given its Markov blanket, which can
be stated as follows:

$$A \vert \delta(A) \perp X_{-A-\delta(A)}$$



##Example:

**Discrete random fields**

###Ising model:

Usage
: Binary random variables, foreground/background segmentation.

1. One RV per pixel
2. Graph: 4-neighbourhood
3. RVs: $${0,1}^n$$
4. Single-site potentials 

	- for unlabeled pixels

	- $$\psi_i(0) = o_i$$ (some observation, for example gray value of pixel)
	- $$\psi_i(1) = 255 - o_i$$ (some observation, for example gray value of pixel)

	- or labeled pixels.

	- $$\psi_i(0) = 0$$, if labeled as background
	- $$\psi_i(1) = \inf$$.

	- $$\psi_i(0) = \inf$$, if labeled as foreground
	- $$\psi_i(1) = 0$$.

5. pairwise potentials

  - $$\psi_{i,j}(x_i,x_j) = \Theta_1 \vert x_i, x_j\vert \exp \left(- \frac{(o_i - o_j)^2}{2 \Theta_2^2}\right) $$.


Optimization function:
: $$Ene(image) = \Sigma_i\psi_i(x_i, o_i) + \Sigma_{i,j, (i,j) \in E}(\psi_{i,j}(x_i, x_j, o_i, o_j))$$

Probability:
: $$p(X) = \frac{1}{Z}\exp(-Ene(X))$$

###Potts model

Usage
: integer RVs, depth perception, assign one depth to every pixel.

3. the range is now $$x_i \in \{-d,-d+1,..., d\}$$
4. Single-site: $$\psi_i(l) = SAD$$[^sad]$$(o^{left}_i, o^{right}_{i-l})$$
whereas each observation is a vectorized patch around pixel i and i-l respectively
5. Pairwise:
$$ \psi_{i,j} = \Theta * (1 - \delta(x_i,x_j))$$
If label is the same, then 0-penalty, otherwise it's $$\Theta$$


#Gaussian Markov Random Field
**Continuous valued markov random field**

For zero mean:

$$p(x) \propto \vert Q \vert^{0.5} \exp( -0.5 x^t Q x)$$

Q: precision matrix [^precisionmat] 

Theorem
: $$Q_{ij} = 0 \Leftrightarrow x_i \perp x_j \vert x_{-ij}$$

x is a GMRF wrt graph G = (V,E) with mean $$\mu$$ and with precision matrix Q iff

Gaussian Markov Random Field
: $$p(x) \propto \vert Q \vert^{0.5} \exp( -0.5 (x-\mu)^t Q (x-\mu))$$
: $$Q_{ij} \neq 0 \Leftrightarrow (i,j) \in E \ \forall i \neq j$$

Conditional density $$V = A \cup B; A \cap B = \emptyset$$

$$x = [x_A, x_B]^t; \mu = [\mu_A, \mu_B]^t$$

$$x_A \vert x_B$$ is still a GMRF wrt subgraph $$G^A = (A, E^A)$$
so every subgraph is also a GMRF with new parameters $$\mu_{A \vert B} and Q_{A \vert B} = Q_{AA}$$

<a href="{{urls.media}}/ml/gmrf.png" class="lightview"
>Handwritten notes</a>


Sample from GMRF:
To sample $$x \sim N(o, Q^{-1}), do

- Find L so that $$Q = LL^t$$[^cholesky]
- Sample $$z \sim N(o,I)
- Solve $$L^tx = z$$ for x

x has desired distribution because 

$$Cov(x) =$$[^cov1] $$Cov(L^{-t}z) = L^{-t} Cov(z) L^{-1} = (L L^t)^{-1} = Q^{-1}$$

##Example

![]({{urls.media}}/ml/gmrf2.png)

The precision matrix is only a triband matrix, thus only a 4-relationship has to be defined.
On the other hand, all nodes are correlated, as in general the covariance matrix (as the inverse of
the precision matrix) is dense.

#Intrinsic Gaussian Markov Random Field

**If the matrix is not of full rank (singular)**

- Can model very long-range correlations, but is specified only through purely local interactions
- Can model stochastic processes whose *increments* are a stationary GMRF
- Can model ... with polynomial trend (linearly growing mean, for example)

Intrinsic Gaussian Markov Random Field
: $$p(x) \propto \vert Q \vert_{gen}^{0.5} \exp( -0.5 (x-\mu)^t Q (x-\mu))$$

- Now we use a generalized determinant
- Covariance matrix does not exist anymore, as Q is not be invertible

IGMRF of first order: rank n-1 and $$Q\vec{1} = 0$$

##Example

###Random Walker

**An example for IRF-1**


#Gaussian Conditional Random Field

**Generalization of Random Walker**

matrix constraint: $$M_i has to be circulant[^circulant]$$
$$M_i = F_i^t F_i$$

Homogenous GMRF
: $$\min 0.5 \sum \theta_i F_i^t F_i)x - t^t x$$

Inhomogenous Gaussian *conditional* RF
: $$\min 0.5 \sum f_i(o) F_i^t F_i)x - t^t x$$

- use observations o in a function instead of static \theta_i


#Factor Graphs

**Bipartite graph**

<a class="lightview" href="{{urls.media}}/ml/GraphicalModels.pdf#page=91">Graphical models</a>

Order
: The number of neighbours a factor is connected to

##Notes

- Higher-order factors can be modelled via helper variables (exponentially many)

#Summary

The beauty of the MRF is that it's possible to only specify local unary/binary potentials, instead of
global ones in a "normal" probabilistic model, which makes the whole problem tractable.


#Footnotes

[^hypergraph]: a generalization of a graph in which an edge can
	 connect any number of vertices, think of cluster/clique 

[^clique]: All vertices in a clique are connected to each other

[^sad]: Sum of absolute deviations

[^precisionmat]: Also known as concentration matrix, it is the inverse of the covariance matrix

[^cholesky]: [Basics](/posts/basics/matrix)

[^cov1]: [Covariance properties](/posts/basics/matrix)

[^circulant]: [Circulent](/posts/basics/matrix)
