# Computational methods in Physics
## Week 12
#### Prof. Michael Wood-Vasey
##### [based on materials from Prof. Brian D'Urso]
##### University of Pittsburgh, Department of Physics and Astronomy

#### ODE Initial Value Problems
We have been solving equations like:
\begin{equation*}
\frac{d\mathbf{y}(t)} {dt} =  \mathbf{f}(\mathbf{y}, t)
\end{equation*}
where:

* The function $\mathbf{f}(\mathbf{y}, t)$ is given.
* An initial condition is given, e.g. $y(0) = 1.0$.
* The problem is to find $\mathbf{y}(t)$ for a requested range of $t$.
* We refer to finding the solution $\mathbf{y}(t)$ as  
solving or integrating a  
first order  
ordinary differential equation (ODE)  
initial value problem. 



\section[PDEs]{Partial Differential Equations (PDEs)}

#### Partial Differential Equations (PDEs)

* PDEs contain derivatives with respect to multiple variables, e.g.: $\frac{\partial U}{\partial t}$, $\frac{\partial U}{\partial x}$, etc. 
* The solution to our PDE is a field, e.g. $U(x, y, z, t)$.
* $U$ might be a physical quantity e.g. ($T$, $P$) which varies continuously in $x$ and $t$.
* Changes in $U(x,y,z,t)$ affect $U$ nearby.
*  What about boundary conditions or initial conditions?
*  How do we solve PDEs numerically?

* Need to discretize multiple independent variables.




#### General Forms of 2-D PDEs
\begin{block}{\[
A\,  \frac{\partial^2 U}{\partial x^2}+ 2B \, \frac{\partial^2
U}{\partial x \partial y}+C  \,\frac{\partial^2 U}{\partial y^2} +
D\, \frac{\partial U}{\partial x}+E \,\frac{\partial U}{\partial
y} =F
\]}
\vspace{0.25cm}
\begin{footnotesize}
 \centering{\begin{tabular}{ccc}\hline
\alert{Elliptic} & \multicolumn{1}{c}{\alert{Parabolic}} &
\multicolumn{1}{c}{\alert{Hyperbolic}}\\*[0.5ex] \hline \\[-0.5ex]
$d=B^2-AC<0$ & $d=B^2-AC=0$ & $d=B^2-AC>0$\\[8pt]
$\nabla^2 U(x,y) = -4\pi\rho(x,y)$ & $\frac{\partial^2 U(x,t)}{\partial x^2}= a\,\frac{\partial U(x,t)}{\partial t}$  & $\frac{\partial^2 U(x,t)}{\partial x^2}=c^{-2}\frac{\partial^2 U}{\partial t^2}$\\[6pt]
\mbox{Poisson} & \mbox{Heat} & \mbox{Wave}\\ \hline
\end{tabular}}\end{footnotesize}
\vspace{0.5cm}

* Elliptic PDE:  All 2nd order, same signs.\\*[2ex]
* Parabolic PDE:  1st order and 2nd order derivatives.\\*[2ex]
* Hyperbolic PDE:  All 2nd order, opposite signs.\\*[2ex]

\end{block}


#### Relation to Boundary Conditions \& Uniqueness
\begin{footnotesize}
\begin{tabular}{@{}llll@{}}\hline
 \alert{Boundary}
&\multicolumn{1}{c}{\alert{Elliptic}}
&\multicolumn{1}{c}{\alert{Hyperbolic}}
&\multicolumn{1}{c}{\alert{Parabolic}} \\
 \alert{Condition} &\multicolumn{1}{c}{({\it Poisson})} &\multicolumn{1}{c}{({\it Wave})} &\multicolumn{1}{c}{({\it Heat})}\\ \hline
Dirichlet open $S$& Under & Under &
\emph{Unique \& stable (1-D)}\\[6.5pt]
Dirichlet closed $S$ & \emph{Unique \& stable} & Over &
Over\\[6.5pt]
Neumann open $S$&Under & Under & \emph{Unique \& Stable (1-D)} \\[6.5pt]
Neumann closed $S$ & \emph{Unique \& stable} & Over &Over \\[6.5pt]
Cauchy open $S$ & Nonphysical & \emph{Unique \& stable} &Over\\[6.5pt]
Cauchy closed $S$&Over & Over&
Over\\ \hline
\end{tabular}
\end{footnotesize}

* Boundary conditions: must be sufficient for unique solution.
* Dirichlet: value on surrounding closed $S$.
* Neumann: value normal derivative on surrounding $S$.
* Cauchy: both solution \& derivative on closed boundary.



#### Solving PDEs \& ODEs Is Different
No Standard PDE Solver

* Standard form for ODE:
\[
\frac{d\mathbf{y}(t)} {dt} =  \mathbf{f}(\mathbf{y}, t)
\]
* Single independent variable \imply standard algorithm  
(e.g. \texttt{rk4}).
* PDEs: several independent variables: $U(x,y,z,t)$.
* \imply  PDE solving is complicated:

*  More variables, more equations, more  ICs, BCs.
* Each PDE and particular BCs \imply particular algorithm.




### Heat Equation


#### Problem: How Does a Bar Cool?
\begin{figure}
\includegraphics[width=3.in]{figures/figure1712cFix.png}
\end{figure}
Insulated Metallic Bar Touching Ice

* Aluminum bar, $L=1$~m, $w$ along $x$.
* Insulated along length, ends in ice ($T=0^\circ$C).
* Initially $T=100^\circ$C.
* How does temperature vary in space and time?



#### The Parabolic Heat Equation (Theory)
\begin{columns}
\column{0.55\textwidth}
\begin{enumerate}
* Nature: heat flow  hot $\rightarrow$ cold  
$K$ = conductivity  
$C$ = sp heat  
$\rho$ = density\\*[2ex]
* $Q(t)$ = contained heat\\*[2ex]
* Heat Eqn: $\Delta T$ from flow\\*[2ex]
* Parabolic PDE in  $x$ \& $t$\\*[2ex]
* "Analytic" Solution  
Initial condition:  
$T(x,t=0) = 100^\circ$C  
Boundary conditions:  
$T(x=0) = T(x=L) = 0^\circ$C
\end{enumerate}
\column{0.6\textwidth}
\begin{footnotesize}
\begin{align}
\textbf{H} =& - K \,\mathbf{\nabla} T(\mathbf{x}, t)\\*[2ex]
Q(t) =& \int d\textbf{x}\, C \rho(\textbf{x}) \, T(\textbf{x}, t)\\*[2ex]
\frac{\partial T(\textbf{x}, t)}{\partial t} =& \frac{K}{C \rho} \nabla^2 T(\textbf{x}, t)\\*[2ex]
\frac{\partial T(x,t)}{\partial t} =& \frac{K}{C\rho}\frac{\partial ^2 T(x,t)}{\partial x^2}\\*[2ex]
T(x,t) =& \sum_{n=1,3,\ldots}^\infty  \frac{400\sin\,k_n x\,e^{-\alpha k_n^2 t}}{n\pi} \\*[2ex]
(k_n =& \frac{n\pi}{L}, \alpha = \frac{K}{C\rho})
\end{align}
\end{footnotesize}
\end{columns}


#### Solution Via Time Stepping
\setcounter{equation}{0}
\begin{columns}
\column{0.6\textwidth}
\vspace{-2ex}
\begin{figure}
\includegraphics[width=1.4in]{figures/figure1713c.png}
\end{figure}
\begin{footnotesize}
\begin{align*}
\frac{\partial T}{\partial t} \simeq & \frac{T(x,t+\Delta t)-T(x,t)}{\Delta t}\\*[1.5ex]
\frac{\partial^2 T}{\partial x^2} \simeq & \frac{T(x +\Delta x)+T(x-\Delta x)-2 T(x)}{(\Delta x)^2}
\end{align*}
\end{footnotesize}
\column{0.6\textwidth}
\vspace{-6ex}

\begin{footnotesize}
* Differential $\rightarrow$ difference equation.\\*[1.5ex]
* Solve at $x-t$ lattice sites.\\*[1.5ex]
* blue = BC\\*[1.5ex] row 0 = IC\\*[1.5ex]
* $\partial t$: forward difference\\*[1.5ex]
$\partial^2 x$: central difference\\*[1.5ex]
\imply  difference  heat equation\\*[1.5ex]
* Leapfrog $\downarrow$ one $t$ to next.\\*[1.5ex]
\end{footnotesize}

\end{columns}
\begin{footnotesize}
\begin{align}
\frac{T(x,t+ \Delta t)-T(x,t)}{\Delta t} =& \frac{K}{C\rho}\frac{T(x+\Delta x,t) +T(x-\Delta x,t) -2 T(x,t)}{\Delta x^2}\\*[1.5ex]
T_{i,j+1} =& T_{i,j}+ \eta \left[T_{i+1,j}+T_{i-1,j}-2T_{i,j}\right]
\end{align}
\end{footnotesize}

%
%#### Solution of Heat Equation
%
%\begin{figure}
%\includegraphics[width=1.5in]{figures/figure1712cFix.png}
% \includegraphics[width=2.5in]{figures/figure1714leftc.png}
%\end{figure}
%
%%\no\hyperbaseurl{./}
%% \href{run:../../eBookWorking/Codes/PythonCodes/EqHeat_03Mar09.py}{EqHeat.py
%%\includegraphics[scale=0.15]{figures/PythonCode1.pdf}}
%
%%\no\hyperbaseurl{./}
%% \href{run:../../eBookWorking/Codes/PythonCodes/EqHeat_Animate_20Sept08.py}{
%%EqHeat\_Animate.py\includegraphics[scale=0.15]{figures/PythonCode1.pdf}}
%

#### Von Neumann Stability Analysis
\setcounter{equation}{0}
\begin{footnotesize}
\beq T_{m,j+1} \ = \  T_{m,j}+ \eta
\left[T_{m+1,j}+T_{m-1,j}-2T_{m,j}\right], \qquad  x = m \Delta x,  \ \ t=j \Delta t
\enq
\end{footnotesize}
\vspace{-1ex}

* Is difference solution $\simeq$ PDE solution?\\*[1.25ex]

* Bad if difference diverges.\\*[1.25ex]

* Analysis of error behavior possible:\\*[1.25ex]

* Expand spatial variation of error in Fourier series.\\*[1.25ex]
* Examine time dependence of each term in series.\\*[1.25ex]
* For stability, all terms must decay exponentially with time $t$.\\*[1.25ex]

* Requirement for stability:
\begin{equation*}
\alert{\eta  = \frac{K\,\Delta t}{C\rho\,\Delta x^2}<\frac{1}{2} }
\end{equation*}
* \imply Smaller $\Delta t$ more stable\\*[1.25ex]
* To use $\downarrow$ $\Delta x$ must use $\downarrow$ $\Delta t$\\*[1.25ex]

%\begin{columns}
%\column{0.6\textwidth}
%
%* Difference solution  
$\simeq$ PDE solution?
%* Bad if difference  diverges.
%
%\begin{footnotesize}
%\begin{align}
%\uncover<4->{T_{m,j} \ = \ }&\uncover<4
%->{  \xi(k)^j \, e^{ikm\Delta x}\\*[1.7ex]}
%\uncover<7->{\Rightarrow\quad
%\xi(k) =}&\uncover<7->{ 1 + 2\eta [\cos(k\Delta x)-1]}\\*[1.7ex]
%\uncover<7->{|\xi(k)| \ < \ }& \uncover<7->{1 }\\*[1.7ex]
% \uncover<7->{\Rightarrow\ \alert{\eta  =}}&\uncover<7->{ \alert{\frac{K\,\Delta t}{C\rho\,\Delta x^2}
%<\frac{1}{2} }}
%\end{align}
%\end{footnotesize}
%\column{0.6\textwidth}
%
%* Assume $T_{m,j}$ = eigenmodes\\*[1.5ex]
%* $k$ = $2\pi/\lambda$ = ? \\*[1.5ex]
%* Stable if eigenmodes  stable\\*[1.5ex]
%* i.e. $|\xi(k)|<1$\\*[1.5ex]
%* Sub (3) into (1)\\*[1.5ex]
%* \imply Smaller $\Delta t$ more stable\\*[1.5ex]
%* $\downarrow$ $\Delta x$ must $\uparrow$ $\Delta t$\\*[1.5ex]
%
%\end{columns}


\section[Laplace]{Laplace Equation}


#### Problem: $V$ for Arbitrary Geometry \& BCs
\vspace{-2ex}
\begin{figure}
\centering{\includegraphics[width=4.0in]{figures/figure171c.png}}
\end{figure}
\begin{block}{Solve \alert{Inside} Charge-Free Square}

* Boundaries are conductors at fixed voltage.\\*[1.25ex]
* Closed boundary (insulate openings).\\*[1.25ex]
* \imply Neumann conditions on the boundary.\\*[1.25ex]
* \imply Unique \& stable solution.

\end{block}


#### Laplace \& Poisson Elliptic PDEs \ (Theory)


* Classical EM,  static charges, \alert{Poisson Equation}:
\[
\nabla^2 U(\textbf{x}) = - 4 \pi \rho(\textbf{x})
\]
* \alert{Laplace equation} if $\rho(\textbf{x})=0$:
\[
\nabla^2 U(\textbf{x}) = 0
\]
* Solve in 2-D rectangular coordinates:
 \[
\frac{\partial^2 U(x,y)}{\partial x^2}+ \frac{\partial^2
U(x,y)}{\partial y^2 } =
\begin{cases}
0, & \mbox{Laplace equation,}\\[4pt]
- 4 \pi \rho(\textbf{x}), & \mbox{Poisson equation}
\end{cases}
 \]
* $U(x,y)$: two independent variables \imply PDE.\\*[1.25ex]
% * Laplace: charge indirectly generate BC
 


#### Fourier Series Solution As Algorithm
\begin{block}{Standard Textbook Solution Not Always Good}
\[
U(x,y)=\sum_{n=1,3,5,\ldots}^\infty \frac{400}{n\pi} \sin
\left(\frac{n\pi x}{L}\right)\, \frac{\sinh (n\pi y/L)}{\sinh
(n\pi)}
\]


* Sum not separable: $\neq \ X(x)\ Y(y)$. \\*[1.5ex]
* Sum = infinite; not true analytic solution.\\*[1.5ex]
* \alert{Algorithm: $\sum^{\infty} \simeq \sum^{N}$.}\\*[1.5ex]
* Painfully slow convergence \imply round-off error.\\*[1.5ex]
* $\sinh(n)$  overflow for large $n$.\\*[1.5ex]
%* 40,000 terms Fourier \emph{vs} 200 algorithm\\*[1.5ex]
* Converges in \emph{mean square}, Gibbs overshoot. $N\neq\infty$

\end{block}


#### Fourier-Gibb's Overshoot at Discontinuities
\begin{figure}
\centering{\includegraphics[width=3.5in]{figures/figure172c.png} }
\end{figure}


#### Finite-Difference Form of Poisson Equation
\begin{footnotesize}
\[
\frac{\partial^2 U(x,y)}{\partial x^2}+ \frac{\partial^2
U(x,y)}{\partial y^2 } =
\begin{cases}
0, & \mbox{Laplace equation,}\\[4pt]
- 4 \pi \rho(\textbf{x}), & \mbox{Poisson equation}
\end{cases}
\]
\end{footnotesize}
\begin{columns}
\column{0.5\textwidth}
\begin{figure}
\includegraphics[height=1.75in]{figures/figure173c.png}
\end{figure}
\column{0.6\textwidth}

* Form 2-D $x-y$ lattice.\\*[1.5ex]
* Solve for $U$ at each lattice site.\\*[1.5ex]
* Derivatives $\rightarrow$ \alert{finite-differences}.\\*[1.5ex]
* Or use finite-elements (non-square grid)\\*[1.5ex]
\imply more efficient, harder setup

\end{columns}


#### Finite-Difference Form of Poisson Equation
\setcounter{equation}{0}
\begin{enumerate}[1.]
* Forward difference $\partial/\partial x$:
\begin{footnotesize}
\begin{align*}
U(x +\Delta x, y) = &  U(x,y) + \frac{\partial U} {\partial x} \Delta x
+ \frac{1}{2} \frac{\partial^2 U} {\partial x^2}(\Delta x)^2 + \cdots \\[2pt]
U(x -\Delta x, y) = &  U(x,y) - \frac{\partial U}{\partial x}
\Delta x + \frac{1} {2} \frac{\partial^2 U}{\partial x^2} (\Delta
x)^2 - \cdots
\end{align*}
\end{footnotesize}
* Add series, odd terms cancel:
\end{enumerate}
\begin{footnotesize}
\begin{align*}
\frac{\partial^2 U(x,y)}{\partial x^2} \simeq&
\frac{U(x+\Delta x, y) + U(x-\Delta x, y) -2U(x,y)} {(\Delta x)^2}
\end{align*}
\end{footnotesize}
\imply Finite-difference Poisson PDE:
\begin{footnotesize}
\alert{\begin{align*}
&\frac{U(x+\Delta x,y) + U(x-\Delta x,y)-2 U(x,y)}{(\Delta x)^2}\\[8pt]
&\qquad + \frac{U(x,y+\Delta y) + U(x,y-\Delta y)-2
U(x,y)}{(\Delta y)^2} = -4\pi\rho
\end{align*}}
\end{footnotesize}


#### Solve Discrete Poisson Equation on Lattice
\vspace{-2ex}
\begin{footnotesize}
\begin{align}
- 4 \pi \rho(\textbf{x}) =& \frac{\partial^2 U(x,y)}{\partial x^2}+\frac{\partial^2 U(x,y)}{\partial y^2 }\\*[1ex]
-4\pi\rho_{i,j}\Delta^2 =& U_{i+1, j}  + U_{i-1, j}  +  U_{i, j+1} + U_{i, j-1} -4 U_{i,j} \\*[1ex]
\Rightarrow\quad U_{i,j} =& \frac{1}{4}\left[ U_{i+1,j}+U_{i-1,j}+U_{i,j+1}+U_{i,j-1} \right] + \pi\rho_{i,j} \Delta^2
\end{align}
\end{footnotesize}
 \begin{columns}
\column{0.6\textwidth}\vspace{-3ex}
\begin{figure}
 \uncover<3->{\includegraphics[height=1.6in]{figures/figure173c.png}}
\end{figure}
\column{0.6\textwidth}

* Solve (2): a \alert{big} matrix!\\*[1.5ex]
* \alert{Correct solution = average of 4 nearest neighbors.}\\*[1.5ex]
* Can we iterate to relax  
to the solution?\\*[1.5ex]
* Need to know if we arrive or fail.

\end{columns}


#### Relaxation Method
\begin{columns}
\column{0.35\textwidth} \vspace{-2.75ex}
\hspace{-3ex}
\begin{figure}
\includegraphics[height=1.4in]{figures/figure173c.png}
\end{figure}
\column{0.65\textwidth}
\begin{block}{How do we iterate towards a solution?}
\vspace{1.0ex}

* Jacobi: update $U$ after full sweep:\\*[1.0ex]

* Maintains symmetry of BC.\\*[2.0ex]

* Gauss--Seidel: always use latest $U$:
\begin{footnotesize} 
\begin{equation*}
U^{\rm(new)}_{i,j} = \frac{1}{4}\left[U^{\rm (old)}_{i+1,j} + U^{\rm (new)}_{i-1,j} + U^{\rm (old)}_{i,j+1} +  U^{\rm (new)}_{i,j-1} \right]
\end{equation*}
\end{footnotesize}

* Faster convergence \imply $\downarrow$ RO error.\\*[2.0ex]
* Decreased memory.\\*[2.0ex]
* Distorts symmetry of BCs.\\*[2.0ex]


\end{block}

\end{columns}


#### Successive Over Relaxation (SOR)
\setcounter{equation}{0}
\begin{block}{New = Old + Residual}
\begin{footnotesize}
\begin{align}
\uncover<2->{U^{\rm (new)}_{i,j}  = &} \uncover<2->{ U^{\rm (old)}_{i,j}  + r_{i,j}}\\[6pt]
\uncover<3->{r_{i,j}    \equiv &}\uncover<3->{ U^{\rm (new)}_{i,j} - U^{\rm (old)}_{i,j}
}\\[6pt]
\uncover<4->{ =&} \uncover<4->{\frac{1}{4}\left[U^{\rm (old)}_{i+1,j}
+ U^{\rm (new)}_{i-1,j} + U^{\rm (old)}_{i,j+1} +  U^{\rm (new)}_{i,j-1} \right]
-U^{\rm (old)}_{i,j}}
\end{align}
\end{footnotesize}
\vspace{-1ex}
\bei \uncover<5->{* \alert{Successive Over Relaxation}}
\begin{footnotesize} \uncover<5->{\beq
 \alert{U^{\rm (new)}_{i,j} = U^{\rm (old)}_{i,j} +
\omega \ r_{i,j}}
\enq}
\end{footnotesize}
\vspace{-2ex}
\begin{columns}
\column{0.5\textwidth}

\uncover<6->{* Gauss-Seidel: $\omega=1$}\\*[1.1ex]
\uncover<6->{* Over-relaxation: $\omega\ge 1$}\\*[1.1ex]
\uncover<6->{* Under-relaxation: $\omega <1$}

\column{0.5\textwidth}

\uncover<7->{* Unstable: $\omega \geq 2$}\\*[1.1ex]
\uncover<7->{* Determine $\omega$ empirically}

\end{columns}
\end{block}


#### Non Ideal Capacitors
\begin{block}{Small Plates, Large Gaps \imply Edge \& Fringe Effects}
\begin{columns}
\column{0.4\textwidth}
\begin{figure}
\includegraphics[width=2.0in,angle=-90] {figures/figure178c.png}
\end{figure}
\column{0.7\textwidth}

* $U=0$ boundary for uniqueness.\\*[2.0ex]
* Simple: thin plates $\pm 100$ V.\\*[2.0ex]
* Interest: thick plates, $\rho(x) =?$   
Laplace \imply $U(x,y)$  
 Poisson \imply $\rho(x,y)$\\*[2.0ex]
* Could have arbitrary BCs  
e.g. $U(x) = 100 \sin\left(\frac{2\pi x}{w}\right)$

\end{columns}
\end{block}


