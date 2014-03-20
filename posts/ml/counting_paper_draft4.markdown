{
  "title": "Counting paper draft 4",
  "date": "2014-03-18",
  "categories": [
    "counting"
  ],
  "tags": [
    
  ]
}


\subsection{Box constraints}
As an extension to pixelbased regression approaches for counting, we also propose an
additional type of label to integrate structural information.
Given a training image, we allow the user to fix regions of interest $R_j$ of his
choice to respective values $c_j$, stating the existence of e.g.\ 4 objects in an area without
providing their exact locations. 
To take these annotations into account, additional terms have to be added to the 
quadratic program \cref{}.

For simplicity, we will first look at the optimization of a single region R:

To fix the summed-up density over a region R to a specific value c, a single constraint of
the form 
$$\begin{equation} \sum_{i \in R}
max(f(x_i), 0) = c \label{eq:box} \end{equation}$$
is sufficient.

To prevent overfitting, we again relax those constraints to soft constraints by introducing slack variables $\beta$ in the following way:

$$
\begin{alignat}{2}
&\underset{\beta}{\text{minimize}} 
& &\lVert \beta \rVert \\
&\text{subject to} \quad 
& &\sum \limits_{i \in R} \max(f(x_i),0))  - c \leq \beta \\% \label{eq:bplus}\\ 
& & &c - \sum \limits_{i \in R} \max(f(x_i),0)) \leq \beta \\% \label{eq:bminus}
\end{alignat}
$$

Note that it is not possible to add these constraints directly into our quadratic program: the usage of the
$\max$-function is prohibited, so we need to derive a different formulation.

\paragraph*{Logical constraints} 

We propose the use of continuous non-negative latent 
variables $l_i$, replacing $\max(f(x_i),0)$ by $f(x_i) + l_i
\overset{!}{=} \max(f(x_i),0), l_i \geq 0$.\\*

Note that the latent variables $l_i$ can only take on two specific values, depending on $f(x_i)$: either be zero if $f(x_i) \geq 0$ and $-f(x_i)$ otherwise.
To select the correct value, we define binary variables $a_i := f(x_i) \geq 0$, these can also be
interpreted as indicator variables whether a pixel is likely to be foreground or background.
Now, depending on the value of $a_i$, we can state the value of $l_i$:
$a_i = 1 \Rightarrow l_i = 0$ and $a_i = 0
\Rightarrow l_i = -f(x_i)$ follow respectively.

The first implication can be modeled easily as we stated before that $l_i$ has to be non-negative:
$$
\begin{alignat}{4}
&\Delta (1 - a_i) &\geq \quad & l_i
\end{alignat}
$$

To achieve the second implication, we have to first take a look at how to set $a_i$ depending on $f(x_i)$, again a case study is required:
if $f(x_i) > 0$, one inequality is sufficient to set $a_i = 1$.

$$
\begin{alignat}{4}
&\Delta a_i &\geq \quad &f(x_i) 
\end{alignat}
$$

Now we have to model $f(x_i) < 0 \Rightarrow a_i = 0$:
This is done by a combination of the following:
$$
\begin{alignat}{4}
&f(x_i) + l_i \quad &\geq \quad& 0 \\
&\Delta (1 - a_i) &\geq \quad & l_i \\
\end{alignat}
$$
In the aforementationed case of $f(x_i) < 0$, the first inequality implies l_i > 0, 
which enforces $a_i = 0$ due to the second inequality.

The last inequality now forces $l_i$ to the exact value of $- f(x_i)$, as l_i gets bounded from
above.

$$
\begin{alignat}{4}
&a_i \quad &\geq \quad& l_i + f(x_i)
\end{alignat}
$$

Combined, this set of inequalities exactly models the behaviour stated in TODO, thus being an
adequate 
replacement for the $\max$-function

$$
\begin{alignat}{4}
&\Delta a_i &\geq \quad &f(x_i)  \\
&\Delta (1 - a_i) &\geq \quad & l_i \\
&a_i \quad &\geq \quad& l_i + f(x_i) \\
&f(x_i) + l_i \quad &\geq \quad& 0 \\
&l_i \quad &\geq \quad& 0\\
&&&a_i \in \{0,1\}
\end{alignat}
$$

Regrettably, the introduction of logical (binary) variables converts the QP into a MLQP (Mixed Logical
/ Quadratic Program), which are generally NP-hard to solve. Due to the number of
required constraints (one per pixel in a box), the problem quickly becomes intractable.
We present a simple heuristic to fix the binary variables $a_i$ beforehand, thus removing the
need to optimize integral variables. But first we state the whole formulation, combining both the
exact pixelbased annotations and the regions:

$$
\begin{alignat*}{6}
&\text{min} 
& &\frac{1}{2} \lVert w \rVert + C \sum \limits_{i\in F}
\lVert \xi^{f}_i \rVert + C \sum \limits_{i \in B} \lVert \xi^{b}_i \rVert +\\
&&&C \sum \limits_{\Box \in \mathcal{B}}\lVert \beta_i \rVert\\
\end{alignat*}
$$
such that

$$
\begin{alignat*}{4}
\xi^{b}_i + \epsilon \quad &\geq&\quad  &\langle w,x_i \rangle + b - y_i  &\forall i \in B\\
\xi^{f}_i  + \epsilon \quad &\geq&\quad & \langle w,x_i \rangle + b - y_i  &\forall i \in F\\
\xi^{f}_i +\epsilon\quad  &\geq&\quad   &y_i - \langle w,x_i \rangle - b &\forall i \in F\\
%\beta \quad &\geq& \quad &\sum \limits_{i \in R_j}  \langle w,x_i \rangle + b+l_i - c_{R_j} \quad &\forall R_j \in \mathcal{R} \\
\beta \quad &\geq& \quad &c_{R_j} - \sum \limits_{i \in R_j} \langle w,x_i \rangle + b + l_i \quad &\forall R_j \in \mathcal{R}\\
\beta \quad &\geq& \quad &-\left[ c_{R_j} - \sum \limits_{i \in R_j} \langle w,x_i \rangle + b + l_i \right] \quad &\forall R_j \in \mathcal{R}\\
\Delta a_i \quad &\geq&\quad  &f(x_i) &\forall i \in R_j, \forall R_j \in \mathcal{R}\\
\Delta (1 - a_i)\quad  &\geq&\quad   &l_i &\forall i \in R_j, \forall R_j \in \mathcal{R}\\
a_i \quad &\geq&\quad  &l_i + f(x_i) &\forall i \in R_j, \forall R_j \in \mathcal{R}\\
f(x_i) + l_i \quad &\geq&\quad  &0 &\forall i \in R_j, \forall R_j \in \mathcal{R} \\
l_i \quad &\geq&\quad   &0 &\forall i \in R_j, \forall R_j \in \mathcal{R}
\end{alignat*}
$$

\subsection{Setting the binary variables}

As the active variables $a_i$ are only used to differentiate foreground from
background samples, this step can be regarded as a classification problem.
By optimizing the previous formulation presented in \eqref{array:svm21} and \eqref{array:svm2},
we can obtain a preliminary solution $f_1$ and thus a weight vector $w_1$ and
bias $b_1$,
the prediction can then be thresholded to obtain $\tilde{a}_i \overset{!}{=}
(\left \langle w_1,\phi(x_i) \right \rangle + b_1 \geq 0)$.
By fixing the variables $a_i$ to these values, we can turn the optimization problem into a
non-integer
QP, which is solvable to optimality, given our precomputed $a_i$.

Note that due to the constraints used in the formulation, 
it is not possible to learn parameters $w_1,b_1$ which contradict the binary variables.
This means that any pixels (which belong to annotated regions) that were predicted to have positive density beforehand retain the 
same state even when learning new parameters $w_2,b_2$ by taking the box annotations into
account. Therefore, additional iterations to learn new parameters using the same threshold approach will yield the same results - namely just $w_2, b_2$.

\paragraph{Iterative approach \label{iter}}
To improve the solution, we thus propose the following threshold mechanism:
Let $f_t(x) = \left \langle w_t,x \right \rangle + b_t$, the prediction for a pixel x in the t-th iteration. 
We want to learn $a_{t + 1}$ for the next iteration step.
In the previous thresholding method which is used to get the initial values for the variables a, only the current prediction 
($f_t(x) \rightarrow a_{t+1}$) is taken into account.
To produce better better solutions, we have to look at the difference between the previous and the current prediction instead:
Let $\epsilon > 0$, assume for a pixel x that $f_t(x) < -epsilon \rightarrow a_t = 0$. After learning a new $f_{t+1}$ using $a_t$, we may now predict 
$- \epsilon< f_{t+1}(x) \leq 0$, which can be taken as evidence that our previous assumption of $a_t = 0$ may be wrong - we therefore set $a_{t+1} = 1$, 
which flips the sign of the density for the specific pixel $x$.
By selecting a reasonably small $\epsilon$, we can then iterate to better solutions of the original MIQP.


\subsection{Removal of the slack variables}

Let us re-investigate the role of the slack variables $l_i$: 
they only serve to model $\sum \max(f(x_i,0)$ correctly, such that every term in the sum is non-negative in the MIQP formulation.
For an annotated region R_j, we precompute the binary variables $a_i$, but if $a_i = 0$ we already know that $f(x_i) \leq 0$ due to the constraints, 
therefore the density of the pixel $x_i$ will not make any contribution to the sum.
Instead of relying on the slack variables $l_i$ to force $f(x_i) + l_i = 0$, we can remove both the slack variable and the term from the sum instead.
As a result, removes the need for the slack variables in the practical implementation, which speeds up the optimization as can be seen in \ref{fig:benchmark}.
Now, we only have to take into account pixels where we assumed $a_i = 1$, this can be expressed by 
replacing $\max(f(x_i),0)$ with $a_i f(x_i)$.
Note that $a_i$ can be considered a constant in the actual QP that we will solve, as we precompute the value. The formulation is now 

\figref{fig:benchmark}. 
\begin{figure}[htb]
%\includegraphics[width = 1.0\linewidth]{images2/benchmark.png}
\includegraphics[width = 1.0\linewidth]{images2/heuristics.png}
\caption{By taking into account the implications of the binary variables, we can optimize out the
helper variables and thus save a lot of time.
\label{fig:benchmark}}
\end{figure}


$$
\begin{alignat*}{4}
&\text{min} 
& &\frac{1}{2} \lVert w \rVert + C \sum \limits_{i\in F}
\lVert \xi^{f}_i \rVert + C \sum \limits_{i \in B} \lVert \xi^{b}_i \rVert +\\
&&&C \sum \limits_{\Box \in \mathcal{B}}\lVert \beta_\Box^{+} \rVert + \lVert
\beta_\Box^{-}\rVert\\
&\text{s.t.} 
&&\xi^{b}_i + \epsilon \geq \langle w,x_i \rangle + b - y_i  &\forall i \in B\\
&&&\xi^{f}_i  + \epsilon \geq \langle w,x_i \rangle + b - y_i  &\forall i \in F\\
&&&\xi^{f}_i +\epsilon \geq  y_i - \langle w,x_i \rangle - b &\forall i \in F\\
&&& {a_\Box}_i \geq f ({x_\Box}_i) &\forall i \in \Box, \Box \in \mathcal{B} \\%\label{eq:enabling}\\
&&& (2{a_\Box}_i - 1)f({x_\Box}_i) \geq 0 &\forall i \in \Box, \Box \in
\mathcal{B}  \\
&&& \beta_\Box^{+} \geq \sum \limits_{\nu \in \Box} {a_\Box}_\nu \left[ \langle
w,{x_\Box}_\nu \rangle + b \right] -y_{\Box}&\forall \Box \in \mathcal{B}\\
&&& \beta_\Box^{-} \geq y_{\Box} - \sum \limits_{\nu \in \Box} {a_\Box}_\nu \left[ \langle
w,{x_\Box}_\nu \rangle + b \right] &\forall \Box \in \mathcal{B}\\
&&&\xi^f_i, \xi^b_i, \beta^{+}_\Box, \beta^{-}_\Box \geq 0\\
%&&&{a_\Box}_\nu \in {0,1}
\end{alignat*}
$$


Our software implementation uses this formulation to provide a heuristic solution to the stated MIQP, which can 
be further improved by the iterative approach as stated in \ref{iter}.