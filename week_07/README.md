# Computational methods in Physics
## Week 7
#### Prof. Michael Wood-Vasey
##### [based on materials from Prof. Brian D'Urso]
##### University of Pittsburgh, Department of Physics and Astronomy

## Ordinary Differential Equations

\section{ODEs}

\begin{frame}[fragile=singleslide]
\frametitle{The Problem}
We will be looking at solving equations like:
\begin{equation*}
\frac{dy}{dt} = f(t, y)
\end{equation*}
\vfill
where:
\begin{itemize}
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
\frametitle{Order of an ODE}
The \textit{order} of an ODE is the highest degree of the derivative on the left hand side (LHS) of the equation.
\begin{itemize}
\vfill
\item The general form of a first order ODE is:
\begin{equation*}
\frac{dy}{dt} = f(t, y)
\end{equation*}
\vfill
\item The general form of a second order ODE is:
\begin{equation*}
\frac{d^2y}{dt^2}+ \lambda \frac{dy}{dt} = f\left(t, \frac{dy}{dt}, y\right)
\end{equation*}
\vfill
\item In each case:\\
\begin{itemize}
\vfill
\item $t$ is the \textit{independent} variable.\\
\vfill
\item $y$ is the \textit{dependent} variable.
\end{itemize}
\end{itemize}
\end{frame}


\begin{frame}[fragile=singleslide]
\frametitle{Ordinary and Partial Differential Equations}
\begin{itemize}
\item Ordinary differential equations (ODEs)\\ have one independent variable, e.g. $t$:
\vfill
\begin{equation*}
\frac{d^2y}{dt^2} = - k y 
\end{equation*}
\vfill
\item Partial differential equations (PDEs)\\ have multiple independent variables, e.g. $t$ and $x$:
\vfill
\begin{equation*}
\frac{\partial^2y}{\partial t^2} - c^2 \frac{\partial^2y}{\partial x^2} = 0
\end{equation*}
\vfill
\item For now, we will work only with ODEs.
\end{itemize}
\end{frame}


\begin{frame}[fragile=singleslide]
\frametitle{Linear and Nonlinear ODEs}
One advantage of numerical methods is that both\\ \textit{linear} and \textit{nonlinear} ODEs can generally be solved.
\begin{itemize}
\vfill
\item An ODE is \textit{linear} if $y$ and $\frac{d^n y}{dt^n}$\\ appear only to the first power.
\begin{itemize}
\vfill
\item For linear ODEs, any linear superposition\\ of solutions is also a solution.
\vfill
\item If $A(t)$ and $B(t)$ are solutions, then 
\begin{equation*}
y(t) = \alpha A(t) + \beta B(t)
\end{equation*}
is also a solution for any values of $\alpha$ and $\beta$.
\end{itemize}
\vfill
\item An ODE is \textit{nonlinear} if $y$ and $\frac{d^n y}{dt^n}$ appear\\ with powers $>1$ or in other nonlinear functions.
\begin{itemize}
\vfill
\item For nonlinear ODEs, linear superpositions\\ of solutions are not generally solutions.
\end{itemize}
\end{itemize}
\end{frame}


\begin{frame}[fragile=singleslide]
\frametitle{Initial and Boundary Value Problems}
\begin{itemize}
\item An ODE of order $n$ requires $n$ conditions to give a unique solution (one arbitrary constant is added for each integration step).
\vfill
\item If $n$ conditions are given at the same point in time, e.g:
$y(t_0)=\alpha$, $y^\prime (t_0)=\beta$, for some $t_0$, $\alpha$, and $\beta$, \\
they are called \textit{initial conditions} and the problem is an \textit{initial value problem}.
\vfill
\item If $n$ conditions are given at different points in time, e.g:
$y(t_1)=\alpha$, $y(t_2)=\beta$, for some $t_1 \neq t_2$, \\
they are called \textit{boundary conditions} and the problem is a \textit{boundary value problem}.
\end{itemize}
\end{frame}


\section{Solving}

\begin{frame}[fragile=singleslide]
\frametitle{Solving an ODE: General Strategy}
\begin{itemize}
\item Start with your equation, e.g.:
\begin{equation*}
\frac{dy}{dt} = f(t, y)
\end{equation*}
\vfill
\item Write it as a system of first order ODEs, if neccesary.\\
(We will discuss this in more detail next week.)
\vfill
\item Start at the initial condition, e.g. $y(t_0) = \alpha$.
\vfill
\item Use some method which evaluates $f(t, y)$\\ to find $y(t)$ at some other time $y(t+\delta t)$.
\vfill
\item Repeat to get an array of $(t, y(t))$ pairs.
\end{itemize}
\end{frame}


\begin{frame}[fragile=singleslide]
\frametitle{Explicit Euler Method}
\begin{itemize}
\item The simplest method of solution follows directly from the definition of the derivative:
\vfill
\begin{equation*}
\frac{dy}{dt} = \lim_{\delta t \rightarrow 0} \frac{y(t+\delta t) - y(t)}{\delta t}
\end{equation*}
\vfill
\item So, if we go back to the equation, e.g.:
\vfill
\begin{equation*}
\frac{dy}{dt} = f(t, y)
\end{equation*}
\vfill
we can try:
\vfill
\begin{equation*}
y(t+\delta t) = y(t) + \delta t \; f(t, y(t))
\end{equation*}
\vfill
\item This is the \textit{explicit Euler method}.
\end{itemize}
\end{frame}


\begin{frame}[fragile=singleslide]
\frametitle{Explicit Euler Method: Mass and Spring}
\begin{itemize}
\item Consider the mass and spring system with $F=ma=-kx$:
\begin{equation*}
\frac{d^2x}{dt^2} = -\frac{k}{m}x
\end{equation*}
\vfill
\item This can be rewritten as two first order ODEs:
$\frac{dx}{dt} = v(t)$ and $\frac{dv}{dt} = -\frac{k}{m}x$.
\vfill
\item For simplicity, take $\frac{k}{m} = 1$.
\vfill
\item If we have initial conditions $x_0$ and $v_0$ at $t_0=0$,\\ we can write:
\begin{align*}
x_{i+1} &= x_i + v_i \; \delta t\\
v_{i+1} &= v_i - x_i \; \delta t
\end{align*}
\end{itemize}
\end{frame}


\begin{frame}[fragile=singleslide]
\frametitle{Aside: Array Assignments}
Check \verb$a$, \verb$b$, \verb$a == b$, \verb$a is b$ at each step:
\begin{itemize}
\item \verb$a = np.array([1, 2, 3])$
\item \verb$b = a$
\item \verb$a = np.array([4, 5, 6])$
\end{itemize}
\vfill
Compare to \textit{in place} assignment:
\begin{itemize}
\item \verb$a = np.array([1, 2, 3]); b = a$
\item \verb$a[1] = 999$
\item \verb$a[:] = np.array([4, 5, 6])$
\end{itemize}
\vfill
Combine with slicing in multi-dimensional arrays:
\begin{itemize}
\item \verb$A = np.zeros((3,3))$
\item \verb$A[1,:] = a$
\item \verb$A = np.zeros((3,3))$
\item \verb$A[:,1] = a$
\end{itemize}
\end{frame}


\begin{frame}[fragile=singleslide]
\frametitle{Explicit Euler Method Implementation}
\begin{itemize}
\item See lecture demo \verb$ODE_solver.py$.
\end{itemize}
\end{frame}


\begin{frame}[fragile=singleslide]
\frametitle{Implicit Euler Method: Mass and Spring}
\begin{itemize}
\item There is an asymmetry to our timestep.\\
We could have chosen:
\begin{align*}
x_{i+1} &= x_i + v_{i+1} \; \delta t\\
v_{i+1} &= v_i - x_{i+1} \; \delta t
\end{align*}
\vfill
\item This is the \textit{implicit Euler method}.
\vfill
\item We need to solve a matrix equation at each time step\\ to find $x_{i+1}$ and $v_{i+1}$:
\begin{equation*}
\begin{pmatrix}
1 & -\delta t\\
\delta t & 1
\end{pmatrix}
\cdot
\begin{pmatrix}
x_{i+1}\\
v_{i+1}
\end{pmatrix}
=
\begin{pmatrix}
x_{i}\\
v_{i}
\end{pmatrix}
\end{equation*}
\vfill
\item This is harder for nonlinear problems, so implicit methods are not as common as explicit methods.
\end{itemize}
\end{frame}


\begin{frame}[fragile=singleslide]
\frametitle{Conservation of Energy?}
\begin{itemize}
\item Many methods do not conserve energy!
\vfill
\item Harmonic oscillator $(x, v)$ trajectories should trace out circles in phase space, since:
\begin{equation*}
E = \tfrac{1}{2}(x^2 + v^2)
\end{equation*}
\vfill
\item \textit{Symplectic} methods ``almost'' exactly conserve energy.
\begin{itemize}
\vfill
\item For Hamiltonian systems.
\vfill
\item Conserve ``volume'' in phase space.
\vfill
\item ``Conservation of pain'': Other errors are introduced.\\ 
(a.k.a. the blanket principle: The blanket is always too short to cover both your feet and your head.)
\vfill
\item E.g. phase in harmonic oscillator is less accurate.
\end{itemize}
\end{itemize}
\end{frame}


\begin{frame}[fragile=singleslide]
\frametitle{Symplectic Euler Method}
\begin{itemize}
\item If the (classical) Hamiltonian is of the form:
\begin{equation*}
H = T(t, p) + V(t, q) \quad\textrm{e.g.}\quad H = \frac{p^2}{2} + V(q)
\end{equation*}
\vfill
\item Then the differential equations take the form:
\begin{align*}
\frac{dq}{dt} = \frac{\partial T}{\partial p} \quad &\Rightarrow \quad \frac{dx}{dt} = f(t, v)\\
\frac{dp}{dt} = -\frac{\partial V}{\partial q} \quad &\Rightarrow \quad \frac{dv}{dt} = g(t, x)
\end{align*}
\vfill
\item If we have initial conditions $x_0$ and $v_0$ at $t_0$:
\begin{align*}
x_{i+1} &= x_i + f(t_i, v_i) \; \delta t\\
v_{i+1} &= v_i + g(t_i, x_{i+1}) \; \delta t
\end{align*}
\vfill
\item For the mass and spring, these are:
\begin{align*}
x_{i+1} &= x_i + v_i \; \delta t\\
v_{i+1} &= v_i - x_{i+1} \; \delta t
\end{align*}
\end{itemize}
\end{frame}


\begin{frame}[fragile=singleslide]
\frametitle{Higher Order Methods}
\begin{itemize}
\item Euler method evaluates $f$ at one endpoint of step.
\vfill
\item Euler method is first order: local error scales like $\delta t^2$.
\begin{align*}
y(t+\delta t) &= y(t) + \delta t \frac{dy}{dt} + \mathcal{O}(\delta t ^2)\\
&= y(t) + \delta t \; f(y, t) + \mathcal{O}(\delta t ^2)
\end{align*}
\vfill
\item Global error is $\mathcal{O}(\delta t)$: smaller $\delta t\rightarrow$ more steps.
\vfill
\item Can we improve the scaling of the error?
\vfill
\item How about evaluating $f$ at the midpoint of the step?
\begin{figure}[!tbh]
\centering  
\includegraphics[width=3.0in]{figures/rk2.png}
\end{figure}
\end{itemize}
\end{frame}


\begin{frame}[fragile=singleslide]
\frametitle{Second Order Runge-Kutta}
If we aim to evaluate $f$ at the midpoint, we get a version of the \textit{second order Runge-Kutta method}:
\vfill
\begin{align*}
y(t+\delta t) &= y(t) + \delta t \; f\left[y(t)+\tfrac{\delta t}{2}f(y)\right]\\
&= y(t) + \delta t \left(f[y(t)] + \tfrac{\delta t}{2} f[y(t)]\frac{df[y(t)]}{dx}+\mathcal{O}(\delta t ^2)\right) \\
&= y(t) + \delta t \; f[y(t)] + \frac{\delta t^2}{2}\frac{df[y(t)]}{dt}+\mathcal{O}(\delta t ^3)
\end{align*}
\vfill
Evaluate as:
\begin{align*}
y_{n+1} &= y_n + k_2\\
k_2 &= \delta t \; f\left(t_n + \tfrac{\delta t}{2}, y_n + \tfrac{k_1}{2}\right)\\
k_1 &= \delta t \; f(t_n, y_n)
\end{align*}
\end{frame}


\begin{frame}[fragile=singleslide]
\frametitle{Fourth Order Runge-Kutta}
\begin{itemize}
\item Schemes with $q$ intermediate steps are known as $(q+1)$-\textit{stage Runge-Kutta}.
\vfill
\item Local error is $\mathcal{O}(\delta t^{q+1})$ only for $q \leq 4$.
\vfill
\item Sweet spot is fourth order Runge-Kutta ($q=4$) \\ 
with local error $\mathcal{O}(\delta t^5)$. Evaluate as:
\end{itemize}
\begin{align*}
y_{n+1} &= y_n + \tfrac{1}{6}(k_1+2k_2+2k_3+k_4)\\
k_1 &= \delta t \; f(t_n , y_n)\\
k_2 &= \delta t \; f\left(t_n + \tfrac{\delta t}{2}, y_n + \tfrac{k_1}{2}\right)\\
k_3 &= \delta t \; f\left(t_n + \tfrac{\delta t}{2}, y_n + \tfrac{k_2}{2}\right)\\
k_4 &= \delta t \; f(t_n+\delta t, y_n+k_3)
\end{align*}
\begin{itemize}
\item A good general-purpose algorithm.
\end{itemize}
\end{frame}


\begin{frame}[fragile=singleslide]
\frametitle{Other Methods}
\begin{itemize}
\item Adaptive step size Runge-Kutta\\ a.k.a. \textit{Runge-Kutta-Fehlberg}:
\begin{itemize}
\vfill
\item Changes step size based on an estimate of the error.
\vfill
\item Extra computational cost may or may not be worthwhile.
\end{itemize}
\vfill
\item Many other methods exist.
\vfill
\item Particular methods may be most appropriate for a given problem depending on behavior of equations and desired goal.
\end{itemize}
\end{frame}


%\section{Examples}

    
\section{Homework}
\begin{frame}{Homework 7}{Due 2/24/2013, 11:59pm}
Complete Problem Set 7. Turn in via CourseWeb:\\
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
\item The Python file \texttt{ps\_7.py} which generates the required results.
\vfill
\end{enumerate}
\end{frame}


%\end{document}


