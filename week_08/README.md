# Computational methods in Physics
## Week 8
#### Prof. Michael Wood-Vasey
##### [based on materials from Prof. Brian D'Urso]
##### University of Pittsburgh, Department of Physics and Astronomy

%\documentclass{beamer}
\mode<presentation>{\usetheme{Goettingen}}

\usepackage[latin1]{inputenc}
\usepackage{listings}
\usepackage{times}
%\usepackage[T1]{fontenc}
% Or whatever. Note that the encoding and the font should match. If T1
% does not look nice, try deleting the line with the fontenc.


\title[PHYS 1321] % (optional, use only with long paper titles)
{Computational Methods in Physics}

\subtitle{PHYS 1321: Notes and Homework}

\author[] % (optional, use only with lots of authors)
{Prof. Brian D'Urso}

\institute{University of Pittsburgh\\ Department of Physics and Astronomy}

\date[Week 8]{Week 8}


\begin{document}

\lstset{language=Python, basicstyle=\footnotesize\ttfamily}

\begin{frame}
  \titlepage
\end{frame}

\section<article>{PHYS 1321: Notes and Homework \hfill Week 8}
\subsection<article>{Computational Methods in Physics}
\mode<article>{\vspace{3mm} \hrule \vspace{5mm}}


\section{Course Information}

%\subsection[First Subsection Name]{First Subsection Name}


\begin{frame}{Where to Go for Help}  
\begin{itemize}
\item I will be around during ``working time'' during each class after lecture time.
\vfill\vfill
\item Office hours: \\
\vfill
Wednesday 12:00 to 2:00 pm\\
\vfill
210 Thaw Hall
\vfill\vfill
\item Make an appointment to meet with me.
\vfill\vfill
\item Lots of Python help available online!
\begin{itemize}
\vfill
\item http://www.python.org/
\vfill
\item http://numpy.scipy.org/
\end{itemize}
\end{itemize}
\end{frame}


\section{ODEs}

\begin{frame}[fragile=singleslide]
\frametitle{The Problem}
We will be looking at solving equations like:
\begin{equation*}
\frac{dy}{dt} = f(t, y)
\end{equation*}
where:
\begin{itemize}
\vfill
\item The function $f(t, y)$ is given.
\vfill
\item An initial condition is given, e.g. $y(0) = 1.0$.
\vfill
\item The problem is to find $y(t)$ for a requested range of $t$.
\vfill
\item We will refer to finding the solution $y(t)$ as\\
solving or integrating a\\
first order\\ 
ordinary differential equation (ODE)\\
initial value problem. 
\end{itemize}
\end{frame}


\begin{frame}[fragile=singleslide]
\frametitle{Solving an ODE: General Strategy}
\begin{itemize}
\item Start with your equation, e.g.:
\begin{equation*}
\frac{d^2x}{dt^2} = -\frac{k}{m}x
\end{equation*}
\item Write it as a system of first order ODEs:
\begin{equation*}
\frac{dx}{dt} = v \qquad \frac{dv}{dt} = -\frac{k}{m}x
\end{equation*}
\item Write everything in vectorized form:
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
\item Start at the initial condition:
\begin{equation*}
x(t_0) = \alpha, \;
v(t_0) = \beta \;\rightarrow\;
\vec{y}(t_0) = \vec{y}_0 = 
\begin{pmatrix}
\alpha\\
\beta
\end{pmatrix}
\end{equation*}
\item Use some method which evaluates $\vec{f}(t_0, \vec{y_0})$ to find $\vec{y}(t_0+\delta t)$. Repeat to increment $t$ by $\delta t$ at each step.
\end{itemize}
\end{frame}


\begin{frame}[fragile=singleslide]
\frametitle{Rewriting an N$^{th}$-Order ODE}
\begin{itemize}
\item We need to rewrite higher-order ODEs, e.g.:
\begin{equation*}
\frac{d^2 x(t)}{dt^2} + p(t, x) \frac{dx(t)}{dt}= q(t, x)
\end{equation*}
as a \textit{system} of first-order ODEs.
\vfill
\item Define $v(t) = \tfrac{dx(t)}{dt}$ to get
\begin{equation*}
\frac{dx(t)}{dt} = v(t), \qquad \frac{dv(t)}{dt} = q(t, x) - p(t, x) v(t)
\end{equation*}
\vfill
\item The new variables may be derivatives of the original, but other choices may be better for error or ease of calculation.
\vfill
\item Often, each spatial coordinate $(x, y, z)$ and each velocity component $(v_x, v_y, v_z)$ of each object gets an equation and a variable.
\end{itemize}
\end{frame}


\begin{frame}[fragile=singleslide]
\frametitle{Physics I Review}
\begin{itemize}
\item Our most common equation to simulate is:
\begin{equation*}
\vec{F}(t) = m\vec{a}(t) = m \frac{d^2 \vec{r}(t)}{dt^2}
\end{equation*}
\vfill
\item Often our forces come from some potential energy function, which contains the physics:
\begin{equation*}
U(\vec{r}, t)
\end{equation*}
\vfill
\item Recall $\vec{F} = - \vec{\nabla} U$:
\begin{equation*}
F_x = -\frac{\partial U}{\partial x} \qquad
F_y = -\frac{\partial U}{\partial y} \qquad
F_z = -\frac{\partial U}{\partial z}
\end{equation*}
\vfill
\item Common non-conservative forces: friction, drag.
\end{itemize}
\end{frame}


\section{Examples}

\begin{frame}[fragile=singleslide]
\frametitle{Particle in a Box}
\begin{itemize}
\item Consider a particle in the square potential well:
\begin{equation*}
U(x, y) = \tfrac{1}{m}(x^m+y^m)
\end{equation*}
\vfill
\item Then:
\begin{equation*}
\frac{d^2x}{dt^2} = -\frac{\partial U}{\partial x} = -x^{m-1} \qquad
\frac{d^2y}{dt^2} = -\frac{\partial U}{\partial y}= -y^{m-1}
\end{equation*}
\vfill
\item This can be rewritten as four first order ODEs:
\begin{align*}
&\frac{dx}{dt}= v_x \qquad\qquad &\frac{dv_x}{dt}=-x^{m-1}\\
&\frac{dy}{dt}= v_y \qquad\qquad &\frac{dv_y}{dt}=-y^{m-1}
\end{align*}
\vfill
\item Here, the $x$ and $y$ systems are actually decoupled.
\end{itemize}
\end{frame}


\begin{frame}[fragile=singleslide]
\frametitle{Particle in a Circular Well}
\begin{itemize}
\item Consider a particle in the circular potential well:
\begin{equation*}
U(x, y) = \tfrac{1}{m}(x^2+y^2)^{\tfrac{m}{2}}
\end{equation*}
\vfill
\item Then:
\begin{align*}
\frac{d^2x}{dt^2} &= -\frac{\partial U}{\partial x} = -x (x^2+y^2)^{\tfrac{m}{2}-1}\\
\frac{d^2y}{dt^2} &= -\frac{\partial U}{\partial y} = -y (x^2+y^2)^{\tfrac{m}{2}-1}
\end{align*}
\vfill
\item This can be rewritten as four first order ODEs:
\begin{align*}
&\frac{dx}{dt}= v_x \qquad\qquad &\frac{dv_x}{dt}= -x (x^2+y^2)^{\tfrac{m}{2}-1} \\
&\frac{dy}{dt}= v_y \qquad\qquad &\frac{dv_y}{dt}= -y (x^2+y^2)^{\tfrac{m}{2}-1}
\end{align*}
\vfill
\item Here, the $x$ and $y$ systems are coupled.
\end{itemize}
\end{frame}


\begin{frame}[fragile=singleslide]
\frametitle{Molecular Dynamics}
Consider $N$ interacting inert gas atoms.
\begin{itemize}
\vfill
\item $\vec{F}=m\vec{a}$ applies to each atom.
\vfill
\item Each atom interacts with all other atoms.
\vfill
\item Contain the atoms in a box.
\end{itemize}
\vfill
Forces:
\begin{itemize}
\vfill
\item Attractive (long range):\\ van der Waals (dispersion) force.
\vfill
\item Repulsive (short range):\\ Pauli exclusion of electrons.
\vfill
\item An approximate potential is typically used,\\
e.g. the Lennard-Jones potential\\ 
(for noble gas atoms).
\end{itemize}
\end{frame}


\begin{frame}[fragile=singleslide]
\frametitle{Lennard-Jones (6-12) Potential}
\begin{equation*}
U_{LJ}(r) = \epsilon \left[\left(\frac{r_m}{r}\right)^{12} - 2\left(\frac{r_m}{r}\right)^{6}\right]
\end{equation*}
\begin{itemize}
\item $\epsilon$: depth of potential well.
\vfill
\item $r_m$: distance at which potential is minimal.
\end{itemize}
\begin{figure}[!tbh]
\centering  
\includegraphics[width=3.0in]{figures/Lennard-Jones-Potential.png}
\end{figure}
\end{frame}


\begin{frame}[fragile=singleslide]
\frametitle{Forces from Lennard-Jones Potential}
Rewrite in 2-D cartesian coordinates for $N$ particles:
\begin{align*}
U_{LJ} = \sum_{i < j} \epsilon &\left[\frac{r_m^{12}}{[(x_j - x_i)^2 + (y_j - y_i)^2]^6}\right.\\ 
- &\left. 2\frac{r_m^{6}}{[(x_j - x_i)^2 + (y_j - y_i)^2]^3}\right]
\end{align*}
\vfill
So, the force in the $x$ direction on the $i^{th}$ particle is:
\begin{align*}
F_{xi} = -\sum_{i \neq j} 12\epsilon &\left[\frac{r_m^{12}(x_j - x_i)}{[(x_j - x_i)^2 + (y_j - y_i)^2]^7}\right.\\ 
- &\left. \frac{r_m^{6}(x_j - x_i)}{[(x_j - x_i)^2 + (y_j - y_i)^2]^4}\right]
\end{align*}
and similar for $F_{yi}$.
\end{frame}


\begin{frame}[fragile=singleslide]
\frametitle{Equations for Molecular Dynamics}
We have four sets of coupled equations. Taking $m=1$:
\begin{equation*}
\begin{matrix}
\frac{dx_i}{dt}=v_{xi} & \frac{dv_{xi}}{dt}=F_{xi} & \frac{dy_i}{dt}=v_{yi} & \frac{dv_{yi}}{dt}=F_{yi}
\end{matrix}
\end{equation*}
\vfill
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
\textit{grid}\\
\textit{random}\\
\textit{grid}\\
\textit{random}\\
\vdots\\
\textit{grid}\\
\textit{random}\\
\textit{grid}\\
\textit{random}
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
\end{frame}


\begin{frame}[fragile=singleslide]
\frametitle{Velocity Verlet Method}
\begin{itemize}
\item The \textit{Velocity Verlet} method is a symplectic method which looks like a cross between the symplectic Euler method and the midpoint method:
\begin{enumerate}
\vfill
\item $\vec{v}\left(t + \tfrac{1}{2} \delta t\right) = \vec{v}(t) + \tfrac{1}{2}\vec{a}(t) \delta t$
\vfill
\item $\vec{x}(t + \delta t) = \vec{x}(t) + \vec{v}\left(t + \tfrac{1}{2} \delta t\right)\delta t$
\vfill
\item Use $\vec{f}\left(\vec{x}(t+\delta t)\right)$ to get $\vec{a}(t+\delta t)$
\vfill
\item $\vec{v}(t + \delta t) = \vec{v}\left(t + \tfrac{1}{2} \delta t\right) + \tfrac{1}{2}\vec{a}(t+\delta t) \delta t$
\end{enumerate}
\vfill
\item The global error is $\mathcal{O}\left(\delta t^2\right)$.
\begin{itemize}
\vfill
\item Same order error as midpoint method (RK2).
\vfill
\item One order higher than Euler or symplectic Euler.
\end{itemize}
\vfill
\item This method is commonly used for molecular dynamics because it is simple, fast, and stable.
\end{itemize}
\end{frame}


\section{Homework Hints}

\begin{frame}[fragile=singleslide]
\frametitle{Projectile Motion with Air Resistance}
Equations of motion (2-D):
\begin{equation*}
\frac{d^2x}{dt^2} = F_{Dx}(\vec{v}) \qquad
\frac{d^2y}{dt^2} = F_{Dy}(\vec{v})-mg
\end{equation*}
\vfill
Forms of air resistance:
\begin{itemize}
\vfill
\item At low speed (laminar flow): $\vec{F}_{D}=-b\vec{v}$
\begin{itemize}
\vfill
\item $b=6\pi\eta r$ is the drag constant for a sphere
\vfill
\item $r=$ radius of sphere
\vfill
\item $\eta=$ fluid viscosity
\end{itemize}
\vfill
\item At high speed (turbulent flow): $\vec{F}_{D}=-\tfrac{1}{2}\rho v^2 C_d A \hat{v}$
\begin{itemize}
\vfill
\item $\rho=$ density of fluid
\vfill
\item $C_d=$ is the drag coefficient\\ (a dimensionless parameter)
\vfill
\item $A=$ cross sectional area of object
\end{itemize}
\end{itemize}
\end{frame}


\begin{frame}[fragile=singleslide]
\frametitle{Gravity and Celestial Motion}
\begin{itemize}
\item Consider $N$ objects moving in 2-D with:
\begin{itemize}
\vfill
\item masses $m_i$
\vfill
\item positions $(x_i, y_i)$
\vfill
\item velocities $(v_{xi}, v_{yi})$.
\end{itemize}
\vfill
\item The objects move in a gravitational potential:
\begin{align*}
U_{G} = \sum_{i < j} \frac{-G m_i m_j}{\sqrt{(x_j - x_i)^2 + (y_j - y_i)^2}}
\end{align*}
\vfill
\item So we end up with the equations:
\end{itemize}
\begin{equation*}
\begin{matrix}
\frac{dx_1}{dt}=v_{x1} & \frac{dv_{x1}}{dt}=-\frac{1}{m_1}\frac{\partial U_G}{\partial x_1} & \frac{dy_1}{dt}=v_{y1} & \frac{dv_{y1}}{dt}=-\frac{1}{m_1}\frac{\partial U_G}{\partial y_1} \\
\vdots & \vdots & \vdots & \vdots \\
\frac{dx_N}{dt}=v_{xN} & \frac{dv_{xN}}{dt}=-\frac{1}{m_N}\frac{\partial U_G}{\partial x_N} & \frac{dy_N}{dt}=v_{yN} & \frac{dv_{yN}}{dt}=-\frac{1}{m_N}\frac{\partial U_G}{\partial y_N} \\
\end{matrix}
\end{equation*}
\end{frame}


\section{Homework}

\begin{frame}{Homework 8}{Due 3/3/2013, 11:59pm}
Complete Problem Set 8. Turn in via CourseWeb:\\
\begin{enumerate}
\vfill
\item A .pdf file with:
\begin{enumerate}
\vfill
\item Your written answers.
\vfill
\item Copy and pasted program output\\ (typically from Pythics).
\vfill
\item Images of plots (right click on plots).\
\vfill
\item Assemble it all in MS Word, \LaTeX, or other and convert to pdf.
\end{enumerate}
\vfill
\item The Python file \texttt{ps\_8.py} which generates the required results.
\vfill
\end{enumerate}
\end{frame}

%\end{document}


