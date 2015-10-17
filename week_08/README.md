# Computational methods in Physics
## Week 8
#### Prof. Michael Wood-Vasey
##### [based on materials from Prof. Brian D'Urso]
##### University of Pittsburgh, Department of Physics and Astronomy

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



#### Solving an ODE: General Strategy

* Start with your equation, e.g.:
\begin{equation*}
\frac{d^2x}{dt^2} = -\frac{k}{m}x
\end{equation*}
* Write it as a system of first order ODEs:
\begin{equation*}
\frac{dx}{dt} = v \qquad \frac{dv}{dt} = -\frac{k}{m}x
\end{equation*}
* Write everything in vectorized form:
\begin{equation*}
\vec{y} = 
\begin{pmatrix}
x\\
v
\end{pmatrix}
\qquad
\frac{d\vec{y}}{dt} = \vec{f}(t, \vec{y}) = 
\begin{pmatrix}
v\\
-\tfrac{k}{m} x
\end{pmatrix}
\end{equation*}
* Start at the initial condition:
\begin{equation*}
x(t_0) = \alpha, \;
v(t_0) = \beta \;\rightarrow\;
\vec{y}(t_0) = \vec{y}_0 = 
\begin{pmatrix}
\alpha\\
\beta
\end{pmatrix}
\end{equation*}
* Use some method which evaluates $\vec{f}(t_0, \vec{y_0})$ to find $\vec{y}(t_0+\delta t)$. Repeat to increment $t$ by $\delta t$ at each step.



#### Rewriting an N$^{th$-Order ODE}

* We need to rewrite higher-order ODEs, e.g.:
\begin{equation*}
\frac{d^2 x(t)}{dt^2} + p(t, x) \frac{dx(t)}{dt}= q(t, x)
\end{equation*}
as a *system* of first-order ODEs.
* Define $v(t) = \tfrac{dx(t)}{dt}$ to get
\begin{equation*}
\frac{dx(t)}{dt} = v(t), \qquad \frac{dv(t)}{dt} = q(t, x) - p(t, x) v(t)
\end{equation*}
* The new variables may be derivatives of the original, but other choices may be better for error or ease of calculation.
* Often, each spatial coordinate $(x, y, z)$ and each velocity component $(v_x, v_y, v_z)$ of each object gets an equation and a variable.



#### Physics I Review

* Our most common equation to simulate is:
\begin{equation*}
\vec{F}(t) = m\vec{a}(t) = m \frac{d^2 \vec{r}(t)}{dt^2}
\end{equation*}
* Often our forces come from some potential energy function, which contains the physics:
\begin{equation*}
U(\vec{r}, t)
\end{equation*}
* Recall $\vec{F} = - \vec{\nabla} U$:
\begin{equation*}
F_x = -\frac{\partial U}{\partial x} \qquad
F_y = -\frac{\partial U}{\partial y} \qquad
F_z = -\frac{\partial U}{\partial z}
\end{equation*}
* Common non-conservative forces: friction, drag.



### Examples

#### Particle in a Box

* Consider a particle in the square potential well:
\begin{equation*}
U(x, y) = \tfrac{1}{m}(x^m+y^m)
\end{equation*}
* Then:
\begin{equation*}
\frac{d^2x}{dt^2} = -\frac{\partial U}{\partial x} = -x^{m-1} \qquad
\frac{d^2y}{dt^2} = -\frac{\partial U}{\partial y}= -y^{m-1}
\end{equation*}
* This can be rewritten as four first order ODEs:
\begin{align*}
&\frac{dx}{dt}= v_x \qquad\qquad &\frac{dv_x}{dt}=-x^{m-1}\\
&\frac{dy}{dt}= v_y \qquad\qquad &\frac{dv_y}{dt}=-y^{m-1}
\end{align*}
* Here, the $x$ and $y$ systems are actually decoupled.



#### Particle in a Circular Well

* Consider a particle in the circular potential well:
\begin{equation*}
U(x, y) = \tfrac{1}{m}(x^2+y^2)^{\tfrac{m}{2}}
\end{equation*}
* Then:
\begin{align*}
\frac{d^2x}{dt^2} &= -\frac{\partial U}{\partial x} = -x (x^2+y^2)^{\tfrac{m}{2}-1}\\
\frac{d^2y}{dt^2} &= -\frac{\partial U}{\partial y} = -y (x^2+y^2)^{\tfrac{m}{2}-1}
\end{align*}
* This can be rewritten as four first order ODEs:
\begin{align*}
&\frac{dx}{dt}= v_x \qquad\qquad &\frac{dv_x}{dt}= -x (x^2+y^2)^{\tfrac{m}{2}-1} \\
&\frac{dy}{dt}= v_y \qquad\qquad &\frac{dv_y}{dt}= -y (x^2+y^2)^{\tfrac{m}{2}-1}
\end{align*}
* Here, the $x$ and $y$ systems are coupled.



#### Molecular Dynamics
Consider $N$ interacting inert gas atoms.

* $\vec{F}=m\vec{a}$ applies to each atom.
* Each atom interacts with all other atoms.
* Contain the atoms in a box.

Forces:

* Attractive (long range):\\ van der Waals (dispersion) force.
* Repulsive (short range):\\ Pauli exclusion of electrons.
* An approximate potential is typically used,  
e.g. the Lennard-Jones potential  
(for noble gas atoms).



#### Lennard-Jones (6-12) Potential
\begin{equation*}
U_{LJ}(r) = \epsilon \left[\left(\frac{r_m}{r}\right)^{12} - 2\left(\frac{r_m}{r}\right)^{6}\right]
\end{equation*}

* $\epsilon$: depth of potential well.
* $r_m$: distance at which potential is minimal.

\begin{figure}[!tbh]
\centering  
\includegraphics[width=3.0in]{figures/Lennard-Jones-Potential.png}
\end{figure}


#### Forces from Lennard-Jones Potential
Rewrite in 2-D cartesian coordinates for $N$ particles:
\begin{align*}
U_{LJ} = \sum_{i < j} \epsilon &\left[\frac{r_m^{12}}{[(x_j - x_i)^2 + (y_j - y_i)^2]^6}\right.\\ 
- &\left. 2\frac{r_m^{6}}{[(x_j - x_i)^2 + (y_j - y_i)^2]^3}\right]
\end{align*}
So, the force in the $x$ direction on the $i^{th}$ particle is:
\begin{align*}
F_{xi} = -\sum_{i \neq j} 12\epsilon &\left[\frac{r_m^{12}(x_j - x_i)}{[(x_j - x_i)^2 + (y_j - y_i)^2]^7}\right.\\ 
- &\left. \frac{r_m^{6}(x_j - x_i)}{[(x_j - x_i)^2 + (y_j - y_i)^2]^4}\right]
\end{align*}
and similar for $F_{yi}$.


#### Equations for Molecular Dynamics
We have four sets of coupled equations. Taking $m=1$:
\begin{equation*}
\begin{matrix}
\frac{dx_i}{dt}=v_{xi} & \frac{dv_{xi}}{dt}=F_{xi} & \frac{dy_i}{dt}=v_{yi} & \frac{dv_{yi}}{dt}=F_{yi}
\end{matrix}
\end{equation*}
Vectorize for $N$ particles:
\begin{equation*}
\vec{y}(t) = 
\begin{pmatrix}
x_1\\
v_{x1}\\
y_1\\
v_{y_1}\\
\vdots \\
x_N\\
v_{xN}\\
y_N\\
v_{y_N}
\end{pmatrix}
\qquad
\vec{y}(0) = 
\begin{pmatrix}
*grid*\\
*random*\\
*grid*\\
*random*\\
\vdots\\
*grid*\\
*random*\\
*grid*\\
*random*
\end{pmatrix}
\qquad
\frac{d\vec{y}}{dt} =  
\begin{pmatrix}
v_{x1}\\
F_{x1}\\
v_{y1}\\
F_{y1}\\
\vdots\\
v_{xN}\\
F_{xN}\\
v_{yN}\\
F_{yN}
\end{pmatrix}
\end{equation*}


#### Velocity Verlet Method

* The *Velocity Verlet* method is a symplectic method which looks like a cross between the symplectic Euler method and the midpoint method:
\begin{enumerate}
* $\vec{v}\left(t + \tfrac{1}{2} \delta t\right) = \vec{v}(t) + \tfrac{1}{2}\vec{a}(t) \delta t$
* $\vec{x}(t + \delta t) = \vec{x}(t) + \vec{v}\left(t + \tfrac{1}{2} \delta t\right)\delta t$
* Use $\vec{f}\left(\vec{x}(t+\delta t)\right)$ to get $\vec{a}(t+\delta t)$
* $\vec{v}(t + \delta t) = \vec{v}\left(t + \tfrac{1}{2} \delta t\right) + \tfrac{1}{2}\vec{a}(t+\delta t) \delta t$
\end{enumerate}
* The global error is $\mathcal{O}\left(\delta t^2\right)$.

* Same order error as midpoint method (RK2).
* One order higher than Euler or symplectic Euler.

* This method is commonly used for molecular dynamics because it is simple, fast, and stable.



### Homework Hints

#### Projectile Motion with Air Resistance
Equations of motion (2-D):
\begin{equation*}
\frac{d^2x}{dt^2} = F_{Dx}(\vec{v}) \qquad
\frac{d^2y}{dt^2} = F_{Dy}(\vec{v})-mg
\end{equation*}
Forms of air resistance:

* At low speed (laminar flow): $\vec{F}_{D}=-b\vec{v}$

* $b=6\pi\eta r$ is the drag constant for a sphere
* $r=$ radius of sphere
* $\eta=$ fluid viscosity

* At high speed (turbulent flow): $\vec{F}_{D}=-\tfrac{1}{2}\rho v^2 C_d A \hat{v}$

* $\rho=$ density of fluid
* $C_d=$ is the drag coefficient\\ (a dimensionless parameter)
* $A=$ cross sectional area of object




#### Gravity and Celestial Motion

* Consider $N$ objects moving in 2-D with:

* masses $m_i$
* positions $(x_i, y_i)$
* velocities $(v_{xi}, v_{yi})$.

* The objects move in a gravitational potential:
\begin{align*}
U_{G} = \sum_{i < j} \frac{-G m_i m_j}{\sqrt{(x_j - x_i)^2 + (y_j - y_i)^2}}
\end{align*}
* So we end up with the equations:

\begin{equation*}
\begin{matrix}
\frac{dx_1}{dt}=v_{x1} & \frac{dv_{x1}}{dt}=-\frac{1}{m_1}\frac{\partial U_G}{\partial x_1} & \frac{dy_1}{dt}=v_{y1} & \frac{dv_{y1}}{dt}=-\frac{1}{m_1}\frac{\partial U_G}{\partial y_1} \\
\vdots & \vdots & \vdots & \vdots \\
\frac{dx_N}{dt}=v_{xN} & \frac{dv_{xN}}{dt}=-\frac{1}{m_N}\frac{\partial U_G}{\partial x_N} & \frac{dy_N}{dt}=v_{yN} & \frac{dv_{yN}}{dt}=-\frac{1}{m_N}\frac{\partial U_G}{\partial y_N} \\
\end{matrix}
\end{equation*}


