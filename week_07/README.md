# Computational methods in Physics
## Week 7
#### Prof. Michael Wood-Vasey
##### [based on materials from Prof. Brian D'Urso]
##### University of Pittsburgh, Department of Physics and Astronomy

## Ordinary Differential Equations

### ODEs

#### The Problem
We will be looking at solving equations like:
\begin{equation*}
\frac{dy}{dt} = f(t, y)
\end{equation*}
where:

* The function $f(t, y)$ is given.
* An initial condition is given, e.g. $y(0) = 1.0$.
* The problem is to find $y(t)$ for a requested range of $t$.
* We will refer to finding the solution $y(t)$ as  
solving or integrating a  
first order  
ordinary differential equation (ODE)  
initial value problem. 



#### Order of an ODE
The *order* of an ODE is the highest degree of the derivative on the left hand side (LHS) of the equation.

* The general form of a first order ODE is:
\begin{equation*}
\frac{dy}{dt} = f(t, y)
\end{equation*}
* The general form of a second order ODE is:
\begin{equation*}
\frac{d^2y}{dt^2}+ \lambda \frac{dy}{dt} = f\left(t, \frac{dy}{dt}, y\right)
\end{equation*}
* In each case:  

* $t$ is the *independent* variable.  
* $y$ is the *dependent* variable.




#### Ordinary and Partial Differential Equations

* Ordinary differential equations (ODEs)  
have one independent variable, e.g. $t$:
\begin{equation*}
\frac{d^2y}{dt^2} = - k y 
\end{equation*}
* Partial differential equations (PDEs)  
have multiple independent variables, e.g. $t$ and $x$:
\begin{equation*}
\frac{\partial^2y}{\partial t^2} - c^2 \frac{\partial^2y}{\partial x^2} = 0
\end{equation*}
* For now, we will work only with ODEs.



#### Linear and Nonlinear ODEs
One advantage of numerical methods is that both  
*linear* and *nonlinear* ODEs can generally be solved.

* An ODE is *linear* if $y$ and $\frac{d^n y}{dt^n}$  
appear only to the first power.

* For linear ODEs, any linear superposition  
of solutions is also a solution.
* If $A(t)$ and $B(t)$ are solutions, then 
\begin{equation*}
y(t) = \alpha A(t) + \beta B(t)
\end{equation*}
is also a solution for any values of $\alpha$ and $\beta$.

* An ODE is *nonlinear* if $y$ and $\frac{d^n y}{dt^n}$ appear  
with powers $>1$ or in other nonlinear functions.

* For nonlinear ODEs, linear superpositions  
of solutions are not generally solutions.




#### Initial and Boundary Value Problems

* An ODE of order $n$ requires $n$ conditions to give a unique solution (one arbitrary constant is added for each integration step).
* If $n$ conditions are given at the same point in time, e.g:
$y(t_0)=\alpha$, $y^\prime (t_0)=\beta$, for some $t_0$, $\alpha$, and $\beta$,   
they are called *initial conditions* and the problem is an *initial value problem*.
* If $n$ conditions are given at different points in time, e.g:
$y(t_1)=\alpha$, $y(t_2)=\beta$, for some $t_1 \neq t_2$,   
they are called *boundary conditions* and the problem is a *boundary value problem*.



### Solving

#### Solving an ODE: General Strategy

* Start with your equation, e.g.:
\begin{equation*}
\frac{dy}{dt} = f(t, y)
\end{equation*}
* Write it as a system of first order ODEs, if neccesary.  
(We will discuss this in more detail next week.)
* Start at the initial condition, e.g. $y(t_0) = \alpha$.
* Use some method which evaluates $f(t, y)$  
to find $y(t)$ at some other time $y(t+\delta t)$.
* Repeat to get an array of $(t, y(t))$ pairs.



#### Explicit Euler Method

* The simplest method of solution follows directly from the definition of the derivative:
\begin{equation*}
\frac{dy}{dt} = \lim_{\delta t \rightarrow 0} \frac{y(t+\delta t) - y(t)}{\delta t}
\end{equation*}
* So, if we go back to the equation, e.g.:
\begin{equation*}
\frac{dy}{dt} = f(t, y)
\end{equation*}
we can try:
\begin{equation*}
y(t+\delta t) = y(t) + \delta t \; f(t, y(t))
\end{equation*}
* This is the *explicit Euler method*.



#### Explicit Euler Method: Mass and Spring

* Consider the mass and spring system with $F=ma=-kx$:
\begin{equation*}
\frac{d^2x}{dt^2} = -\frac{k}{m}x
\end{equation*}
* This can be rewritten as two first order ODEs:
$\frac{dx}{dt} = v(t)$ and $\frac{dv}{dt} = -\frac{k}{m}x$.
* For simplicity, take $\frac{k}{m} = 1$.
* If we have initial conditions $x_0$ and $v_0$ at $t_0=0$,  
we can write:
\begin{align*}
x_{i+1} &= x_i + v_i \; \delta t  
v_{i+1} &= v_i - x_i \; \delta t
\end{align*}



#### Aside: Array Assignments
Check `a`, \verb$b$, \verb$a == b$, \verb$a is b$ at each step:

* `a = np.array([1, 2, 3])`
* `b = a`
* `a = np.array([4, 5, 6])`

Compare to *in place* assignment:

* `a = np.array([1, 2, 3]); b = a`
* `a[1] = 999`
* `a[:] = np.array([4, 5, 6])`

Combine with slicing in multi-dimensional arrays:

* `A = np.zeros((3,3))`
* `A[1,:] = a`
* `A = np.zeros((3,3))`
* `A[:,1] = a`



#### Explicit Euler Method Implementation

* See lecture demo `ODE_solver.py`.



#### Implicit Euler Method: Mass and Spring

* There is an asymmetry to our timestep.  
We could have chosen:
\begin{align*}
x_{i+1} &= x_i + v_{i+1} \; \delta t  
v_{i+1} &= v_i - x_{i+1} \; \delta t
\end{align*}
* This is the *implicit Euler method*.
* We need to solve a matrix equation at each time step  
to find $x_{i+1}$ and $v_{i+1}$:
\begin{equation*}
\begin{pmatrix}
1 & -\delta t  
\delta t & 1
\end{pmatrix}
\cdot
\begin{pmatrix}
x_{i+1}  
v_{i+1}
\end{pmatrix}
=
\begin{pmatrix}
x_{i}  
v_{i}
\end{pmatrix}
\end{equation*}
* This is harder for nonlinear problems, so implicit methods are not as common as explicit methods.



#### Conservation of Energy?

* Many methods do not conserve energy!
* Harmonic oscillator $(x, v)$ trajectories should trace out circles in phase space, since:
\begin{equation*}
E = \tfrac{1}{2}(x^2 + v^2)
\end{equation*}
* *Symplectic* methods ``almost'' exactly conserve energy.

* For Hamiltonian systems.
* Conserve ``volume'' in phase space.
* ``Conservation of pain'': Other errors are introduced.  
(a.k.a. the blanket principle: The blanket is always too short to cover both your feet and your head.)
* E.g. phase in harmonic oscillator is less accurate.




#### Symplectic Euler Method

* If the (classical) Hamiltonian is of the form:
\begin{equation*}
H = T(t, p) + V(t, q) \quad\textrm{e.g.}\quad H = \frac{p^2}{2} + V(q)
\end{equation*}
* Then the differential equations take the form:
\begin{align*}
\frac{dq}{dt} = \frac{\partial T}{\partial p} \quad &\Rightarrow \quad \frac{dx}{dt} = f(t, v)  
\frac{dp}{dt} = -\frac{\partial V}{\partial q} \quad &\Rightarrow \quad \frac{dv}{dt} = g(t, x)
\end{align*}
* If we have initial conditions $x_0$ and $v_0$ at $t_0$:
\begin{align*}
x_{i+1} &= x_i + f(t_i, v_i) \; \delta t  
v_{i+1} &= v_i + g(t_i, x_{i+1}) \; \delta t
\end{align*}
* For the mass and spring, these are:
\begin{align*}
x_{i+1} &= x_i + v_i \; \delta t  
v_{i+1} &= v_i - x_{i+1} \; \delta t
\end{align*}



#### Higher Order Methods

* Euler method evaluates $f$ at one endpoint of step.
* Euler method is first order: local error scales like $\delta t^2$.
\begin{align*}
y(t+\delta t) &= y(t) + \delta t \frac{dy}{dt} + \mathcal{O}(\delta t ^2)  
&= y(t) + \delta t \; f(y, t) + \mathcal{O}(\delta t ^2)
\end{align*}
* Global error is $\mathcal{O}(\delta t)$: smaller $\delta t\rightarrow$ more steps.
* Can we improve the scaling of the error?
* How about evaluating $f$ at the midpoint of the step?
\begin{figure}[!tbh]
\centering  
\includegraphics[width=3.0in]{figures/rk2.png}
\end{figure}



#### Second Order Runge-Kutta
If we aim to evaluate $f$ at the midpoint, we get a version of the *second order Runge-Kutta method*:
\begin{align*}
y(t+\delta t) &= y(t) + \delta t \; f\left[y(t)+\tfrac{\delta t}{2}f(y)\right]  
&= y(t) + \delta t \left(f[y(t)] + \tfrac{\delta t}{2} f[y(t)]\frac{df[y(t)]}{dx}+\mathcal{O}(\delta t ^2)\right)   
&= y(t) + \delta t \; f[y(t)] + \frac{\delta t^2}{2}\frac{df[y(t)]}{dt}+\mathcal{O}(\delta t ^3)
\end{align*}
Evaluate as:
\begin{align*}
y_{n+1} &= y_n + k_2  
k_2 &= \delta t \; f\left(t_n + \tfrac{\delta t}{2}, y_n + \tfrac{k_1}{2}\right)  
k_1 &= \delta t \; f(t_n, y_n)
\end{align*}


#### Fourth Order Runge-Kutta

* Schemes with $q$ intermediate steps are known as $(q+1)$-*stage Runge-Kutta*.
* Local error is $\mathcal{O}(\delta t^{q+1})$ only for $q \leq 4$.
* Sweet spot is fourth order Runge-Kutta ($q=4$)   
with local error $\mathcal{O}(\delta t^5)$. Evaluate as:

\begin{align*}
y_{n+1} &= y_n + \tfrac{1}{6}(k_1+2k_2+2k_3+k_4)  
k_1 &= \delta t \; f(t_n , y_n)  
k_2 &= \delta t \; f\left(t_n + \tfrac{\delta t}{2}, y_n + \tfrac{k_1}{2}\right)  
k_3 &= \delta t \; f\left(t_n + \tfrac{\delta t}{2}, y_n + \tfrac{k_2}{2}\right)  
k_4 &= \delta t \; f(t_n+\delta t, y_n+k_3)
\end{align*}

* A good general-purpose algorithm.



#### Other Methods

* Adaptive step size Runge-Kutta  
a.k.a. *Runge-Kutta-Fehlberg*:

* Changes step size based on an estimate of the error.
* Extra computational cost may or may not be worthwhile.

* Many other methods exist.
* Particular methods may be most appropriate for a given problem depending on behavior of equations and desired goal.



