# Computational methods in Physics
## Week 6
#### Prof. Michael Wood-Vasey
##### [based on materials from Prof. Brian D'Urso]
##### University of Pittsburgh, Department of Physics and Astronomy

## Linear algebra

## Overview
This week's topics:
* Writing and reading arrays to/from files.
* Linear algebra and matrix methods.
* Multidimensional root finding and minimization.
* Curve fitting.


### Matrices

#### Creating Arrays in Numpy
* Creating arrays:
  * Online documentation:  
    http://docs.scipy.org/doc/numpy/reference/routines.array-creation.html
* Writing to a file:
  * Online documentation:
    http://docs.scipy.org/doc/numpy/reference/generated/numpy.savetxt.html
  * Python help:
  `help(numpy.savetxt)`
* Loading from a file:
  * Online documentation:
  http://docs.scipy.org/doc/numpy/reference/generated/numpy.loadtxt.html
  * Python help:
  `help(numpy.loadtxt)`
* There are other fileIO functions:
  e.g. `numpy.load` and `numpy.save`.
* and other formats (e.g., `hdf`) and frameworks (e.g., `astropy.Tables`).

#### Examples: Arrays and Files
* Setup:
```
import numpy as np
A = np.array([[0.0, 2.5, 3.2], 
              [1.0, 5.6, 8.9],
              [2.0, 7.1, 3.7],
              [3.0, 4.2, 9.3]]
```
* Save $\mathbf{A}$ to a file:
```
 np.savetxt('A_test.csv', A, 
            delimiter=',', fmt='%g')
```
* Load the array back from the file:
```
B = np.loadtxt('A_test.csv', 
               delimiter=',')
```


### Linear Algebra

#### Linear Algebra Problems
* The basic linear algebra problem is a set of $m$ simultaneous linear equations with $n$ unknowns:
\begin{equation*}
\begin{matrix}
 \alpha_{0,0}x_0   &+& \alpha_{0,1}x_1   &+& \cdots &+& \alpha_{0,n-1}x_{n-1}  &=& b_0
 \alpha_{1,0}x_0   &+& \alpha_{1,1}x_1   &+& \cdots &+& \alpha_{1,n-1}x_{n-1}  &=& b_1
 \vdots            &+& \vdots            &+& \ddots &+& \vdots                 &=& \vdots
 \alpha_{m-1,0}x_0 &+& \alpha_{m-1,1}x_1 &+& \cdots &+& \alpha_{m-1,n-1}x_{n-1}&=& b_{m-1} 
\end{matrix}
\end{equation*}
* Typically, we know $\alpha_{i,j}$ and $b_i$, and want to find $x_j$.
* If $m>n$, the system is overdetermined.
* If $m<n$, the system is underdetermined.
* We will look primarily at the case $n=m$.


#### Matrix Representation
* Computers are better able to handle equations as matrix equations.
* Matrix representation:
\begin{equation*}
\begin{pmatrix}
\alpha_{0,0}   & \alpha_{0,1}   & \cdots & \alpha_{0,n-1} 
\alpha_{1,0}   & \alpha_{1,1}   & \cdots & \alpha_{1,n-1} 
\vdots         & \vdots         & \ddots & \vdots 
\alpha_{m-1,0} & \alpha_{m-1,1} & \cdots & \alpha_{m-1,n-1} 
\end{pmatrix}
\begin{pmatrix}
x_0 
x_1 
\vdots 
x_{n-1}
\end{pmatrix}
=
\begin{pmatrix}
b_0 
b_1 
\vdots 
b_{n-1}
\end{pmatrix}
\end{equation*}
* We can write this set of equations in a compact form, writing the matrix as $\mathbf{A}$:
\begin{equation*}
\mathbf{A}\vec{x} = \vec{b}
\end{equation*}
* Here $\mathbf{A}$ is a square matrix.


#### Classes of Matrix Problems
$\mathbf{A}\vec{x}=\vec{b}$
* $\mathbf{A}$ is a known $N \times N$ matrix.
* $\vec{x}$ is an unknown vector of length $N$.
* $\vec{b}$ is a known vector of length $N$.
* Solve with Gaussian elimination  
 or lower-upper (LU) decomposition.
* Slower: solve by finding $\mathbf{A}^{-1}$, then $\vec{x}=\mathbf{A}^{-1}\vec{b}$.
$\mathbf{A}\vec{x}=\lambda\vec{x}$
* Eigenvector $\vec{x}$ is an unknown vector of length $N$.
* Eigenvalue $\lambda$ is an unknown parameter.
* $\mathbf{A}^{-1}$ doesn't help! Need specialized solver.
* Can shown that $\textrm{det}[\mathbf{A}-\lambda\mathbf{I}] = 0$ for eigenvalues $\lambda$.


#### Linear Algebra Routines
* We *will* solve linear algebra problems with "canned" routines.
* Eigensystems, matrix multiplication, inverses, determinants, etc.
* Many tested and optimized packages available:
NETLIB, LAPACK, SLATEC, BLAS, \ldots
* Writing custom solvers "from scratch" is not usually worthwhile for these.
* NumPy and SciPy wrap some of these.
* We will primarily use the NumPy routines in `numpy.linalg`.


#### Linear Algebra in Numpy
Common linear algebra functions available in `numpy`:
* Online documentation:  
  http://docs.scipy.org/doc/numpy/reference/routines.linalg.html
* Python help:  
  `help(numpy.linalg)`


#### Examples: Solving Linear Systems
* Setup matrices:  
```
import numpy as np
A = np.array([[ 1,  2,   3], 
              [22, 32,  42],
              [55, 66, 100]])
b = np.array([1, 2, 3])
```
* Solve $\mathbf{A}\vec{x}=\vec{b}$:
`x = np.linalg.solve(A, b)`
* Check accuracy of the solution by calculating $\mathbf{A}\vec{x}-\vec{b}$:
`np.dot(A, x) - b`
* Less efficient direct solution, $\vec{x}=\mathbf{A}^{-1}\vec{b}$:
```
A_inverse = np.linalg.inv(A)
np.dot(A_inverse, A)
x = np.dot(A_inverse, b)
```


#### Examples: Solving Eigensystems
Solve for the principle axes of a cube,  
where the moment of inertia tensor $\mathbf{I}$ is diagonal.
* Solve $\mathbf{I}\vec{\omega}= \lambda\vec{\omega}$ for eigenvectors $\vec{\omega}$ and eigenvalues $\lambda$.
* Setup:
```
import numpy as np
I = np.array([[ 2./3,-1./4,-1./4],
              [-1./4, 2./3,-1./4],
              [-1./4,-1./4, 2./3]])
```
* Solve eigensystem:
`evalues, evectors = np.linalg.eig(I)`
* Evaluate difference between RHS and LHS:
```
LHS = np.dot(I, evectors[:, 0])
RHS = evalues[0] * evectors[:, 0]
LHS - RHS
```


#### Multidimensional Nonlinear Root Finding
The general problem of finding roots of multiple nonlinear simultaneous equations $f(x, y)$ and $g(x, y)$ is difficult:  
(figures/multidimensional_root_finding.png)


#### Multidimensional Newton-Raphson
Consider $N$ nonlinear functions of $N$ variables, $F_i(x_1, x_2, \ldots , x_N)$. Find the $\vec{x}$ which gives $F_i(\vec{x}) = 0$  
 for all $i$.
* Taylor expansion:
\begin{equation*}
\vec{F}(\vec{x}+ \delta\vec{x}) = \vec{F}(\vec{x}) + \mathbf{J}\cdot \delta\vec{x} + \mathcal{O}(\delta\vec{x}^2)
\end{equation*}
where $\mathbf{J}$ is the Jacobian matrix with $J_{ij} = \frac{\partial F_i}{\partial x_j}$.
* Set $\vec{F}(\vec{x}+ \delta\vec{x})=0$ to get an approximate solution:
\begin{equation*}
\mathbf{J}\cdot \delta\vec{x} = -\vec{F}(\vec{x})
\end{equation*}
* Solve for $\delta\vec{x}$ to get the Newton-Raphson step:
\begin{equation*}
\vec{x}_{new} = \vec{x}_{old} + \delta\vec{x}
\end{equation*}
* Need to use matrix mathods (e.g. LU decomposition) to get $\delta\vec{x}$. 


#### Function Minimization
What if the problem is to minimize a function instead of finding a zero?
* There are routines similar to the bisection and Newton-Raphson methods for minimization.
* Multidimensional minimization (optimization) is better behaved than multidimensional root finding.
%* See `scipy.optimize` help for a wide range of routines for minimizing functions over one or many variables, with or without constraints.
* Many Scipy optimization routines:
  * Online documentation:  
  http://docs.scipy.org/doc/scipy/reference/optimize.html\end{scriptsize}
  * Python help:  
  `help(scipy.optimize)`
  * Many trade-offs between speed, memory use, robustness, \ldots
  * Ideal technique is problem-dependent.


### Curve Fitting

#### Curve Fitting
Find the parameters $\vec{a}=(a_1, a_2, \ldots, a_M)$ that make the function $f(x, \vec{a})$ fit the data $(x_i, y_i)$ with standard deviations (errors) $\sigma_i$ as well as possible.
* A common approach is to adjust $\vec{a}$ to minimize the sum of the squares of the weighted errors, called $\chi^2$:
\begin{equation*}
\chi^2 = \sum_{i=0}^{N} \left[\frac{y_i - f(x_i, \vec{a})}{\sigma_i}\right]^2
\end{equation*}
* For normally distributed data,  
 minimum $\chi^2 \Rightarrow$ maximum likelihood.
* $1/\sigma_i^2$ = weighting $\Rightarrow$ large errors contribute least.
* Smaller $\chi^2 \Rightarrow$ better fit.
* $\chi^2 \approx N - M =$ \# degrees freedom, good.
* Good fit: misses $\sim 1/3$ of points.
* $\chi^2 = 0 \Rightarrow$ theory passes through all data points.


#### Example: Linear Regression
Fitting data to a line (called Linear Regression) is particularly easy. e.g. fit a line,
$y = mx + c$, through some noisy data-points:
* Setup and make some data:
`import numpy as np`
`x = np.array([0, 1, 2, 3])`
`y = np.array([-1, 0.2, 0.9, 2.1])`
* By examining the coefficients, we see that the line should have a slope of roughly $1$ and cut the y-axis at, more or less, $-1$.
* We can rewrite the line equation as $\vec{y} = \mathbf{A}\vec{p}$,  
 where `A = [[x 1]]` and `p = [[m], [c]]`.
Now use `lstsq` to solve for `p`:
`A = np.column_stack([x, np.ones(len(x))])`
`m, c = np.linalg.lstsq(A, y)[0]`


#### Example: Linear Regression, Plotting
* Setup the plots for the data and line:
`plot.new_curve('data', line_style='',`
`               marker_style='o',`
`               marker_color='blue')`
`plot.new_curve('fit',`
`               line_style='-',`
`               line_color='red')`
* Plot the data along with the fitted line:
`plot.set_data('data', np.column_stack((x, y)))`
`plot.set_data('fit', np.column_stack((x, m*x + c)))`


#### Example: Nonlinear Curve Fitting
* Setup:
```
import numpy as np
import scipy.optimize
```
* The function to fit:
```
def f(x, a, b, c):`
    return a*x**2 + b*x + c
```
* Generate some simulated data:
```
x = np.linspace(0.0, 4.0, 50)
y = f(x, 2.5, 1.3, 0.5)
yn = y + 0.2*np.random.normal(size=len(x))
```
* Fit the data:
`scipy.optimize.curve_fit(f, x, yn)`


#### Uncertainties in Fit Parameters
How do we estimate the uncertainties in the fit parameters $\vec{a}=(a_1, a_2, \ldots, a_M)$?
* `scipy.optimize.curve_fit` returns:
  * `popt`: array
Optimal values for the parameters so that the sum of the squared error is minimized.
  * `pcov`: 2d array
The estimated covariance of `popt`. The diagonals provide the variance of the parameter estimate.
* The standard deviation of $a_i$ is $\sigma_i = \sqrt{C_{ii}}$.
  * The 68\% confidence interval for $a_i$ is $\pm \sigma_i$.
  * The 95\% confidence interval for $a_i$ is $\pm 2\sigma_i$.
  * etc.


#### Example: Nonlinear Curve Fitting, Continued
The results of the fit:
```
import math
popt, pcov = scipy.optimize.curve_fit(f, x, yn)
for i in range(len(popt)):
    params = (i, popt[i], pcov[i,i])
    print '%d: %g +/- %g' % params
```

    
