# Computational methods in Physics
## Week 10
#### Prof. Michael Wood-Vasey
##### [based on materials from Prof. Brian D'Urso]
##### University of Pittsburgh, Department of Physics and Astronomy

### Problem
#### Problem: Why Is Nature So Complicated?

* Insect populations, weather patterns
* Complex behavior\\*[2ex]
* Stable,  periodic,   chaotic, stable, \ldots\\*[2ex]
*  \textbf{Problem:} can a simple, discrete law  produce such complicated
behavior?\\*[1ex]


### Logistic Map
#### Model Realistic Problem: Bug Cycles

##### Bugs Reproduce Generation after Generation = $i$

*   $N_0\ \rightarrow \  N_1, N_2, \ldots  N_\infty$\\*[2ex]
*  $N_i = f(i)?$\\*[2ex]
* Seen discrete law,
\begin{align*}
\frac{\Delta N}{\Delta t} =\ & -\lambda N \\*[1ex]
\Rightarrow\   \simeq\ & e^{-\lambda t}
\end{align*}
*   $-\lambda \rightarrow +\lambda$ \implies  growth

![](figures/cockroach.jpg)

$$
\frac{\Delta N_i}{\Delta t} = \lambda \; N_i
$$


#### Refine Model: Maximum Population $N_{*$}

##### Incorporate Carrying Capacity into Rate

* Assume  breeding rate proportional to   number of bugs:
$$
\frac{\Delta N_i}{\Delta t} = \lambda \; N_i
$$
 * Want growth rate   $\downarrow$  as  $N_i \rightarrow N_{*}$\\*[2ex]
 * Assume $\lambda=\lambda' (N_*-N_i)$
\[
  \Rightarrow\ \ \alert{\frac{\Delta
N_i}{\Delta t} =
\lambda'(N_{*}-N_i)N_i} \quad \quad \mbox{(Logistic Map)}
 \]
* Small $N_i/N_*$ \implies exponential growth\\*[2ex]
*  $N_i \rightarrow N_*$  \implies slow growth, stable, decay

\end{block}

#### Logistic as Map in Dimensionless Variables

\begin{block}{As Population, Change Variables}
 \begin{align}
N_{i+1}  = & N_i + \lambda' \, \Delta t (N_{*}-N_i)N_i \\*[1ex]
 \alert{x_{i+1}} \ =\ & \alert{\mu x_{i}(1- x_{i}) \quad\quad\mbox{(Logistic Map)}}\\*[1ex]
\mu \deq\ & 1 + \lambda' \,\Delta  t N_{*}, \quad \quad x_{i} \deq
\frac{\lambda' \,  \Delta  t}{\mu} N_i\simeq
\frac{N_i}{N_{*}}\\*[1ex]
x_{i} \simeq \frac{N_i}{N_{*}} \  =& \  \mbox{fraction of max}
\end{align}
\begin{columns}
\column{0.5\textwidth}

*   $0 \leq x_{i} \leq 1$
*  Map: $x_{i+1} = f(x_i)$

\column{0.5\textwidth}

*  Quadratic,  1-D map
* $f(x) = \mu x(1-x)$

\end{columns}
\end{block}


### Properties
#### Properties of Nonlinear Maps (Theory)

\begin{block}{Empirical Study: Plot  $x_i$ \emph{vs}  $i$}
\vspace{-5.5cm}\hspace{-1.5ex}
\pgfimage[width=4.25in]{figures/Populations.pdf}
\vspace{-6.0cm}

* A: $\mu = \textrm{2.8}$, equilibration into single population\\*[2ex]
* B:  $\mu = \textrm{3.3}$, oscillation between 2 population levels\\*[2ex]
* C:  $\mu = \textrm{3.5}$ oscillation among 4 levels\\*[2ex]
* D:    chaos

\end{block}

### Attractors
#### Fixed Points
\begin{block}{$x_{i}$ Stays at $x_{*}$ or Returns}
\vspace{-5.5cm}\hspace{-1.5ex}
\pgfimage[width=4.0in]{figures/Populations.pdf}
\vspace{-5.5cm}
\beq
x_{i+1} = \mu x_i (1-x_i)
\enq
\vspace{-2ex}

*  One-cycle: $x_{i+1} = x_{i} = x_{*}$
 \begin{align}
\mu x_{*} (1-x_{*}) \ = &\  x_{*}\\*[1ex]
\Rightarrow\  x_{*}  \ =&\  0, \quad   x_{*} = \frac{\mu -
1}{\mu}
 \end{align}
  
  \end{block}
  
 #### Period Doubling, Attractors
\begin{block}{Unstable via  Bifurcation into 2-Cycle}
\vspace{-5.5cm}\hspace{-1.5ex}
\pgfimage[width=4.0in]{figures/Populations.pdf}
\vspace{-5.5cm}

* Attractors, cycle points
* Predict:  same population generation $i$, $i+2$
 \[
x_{i} = x_{i+2} = \mu x_{i+1}(1-x_{i+1})\enskip\Rightarrow\enskip
x_{*} = \frac{1+\mu \pm \sqrt{\mu^{2}-2\mu -
3}}{2\mu}
 \]
*   $\mu>3$: real solutions
* Continues 1 $\rightarrow$ 2 populations

\end{block}

\begin{columns}
  \column{0.5\textwidth}
\no\includegraphics[width=2.4in]{figures/bugcolor2.pdf}
  \column{0.5\textwidth}
 
 *  Can't vary intensity\\*[1ex]
 * Vary point density\\*[1ex]
 * Resolution $\sim$  300 DPI\\*[1ex]
 *  $3000 \times 3000 \simeq 10^7$ pts\\*[1ex]
 * Big, more = waste\\*[1ex]
 * Create 1000 bins   \\*[1ex]
 * $1 \leq \mu \leq 4$\\*[1ex]
 * Print $x_{*}$  3-4 decimal places\\*[1ex]
 * Remove duplicates\\*[1ex]
 * Enlarge:  \alert{self-similarity}\\*[1ex]
 *  Observe  windows
 
 \end{columns}
 


\begin{frame}[label=current]{Problem: Realistic Single or Double Pendulum}
\begin{block}{Simulate Nonlinear, Chaotic System}
 
   * Driven single pendulum \\*[1ex]
   * Free, double pendulum
   * Large oscillations, even over-the-top
   
\vspace{-1.0in}
\begin{center}
\includegraphics[height=4.0in]{figures/BothPends.pdf}
\end{center}
\end{block}

### ODE

#### Chaotic Pendulum ODE
\setcounter{equation}{0}

\begin{block}{Newton's Laws for Rotational Motion \hspace{3ex}  $\sum \tau \,=\, I \ \frac{d^2\theta}{dt^2}$ }

\begin{columns}
\hspace{-3cm}\column{0.3\textwidth}
\vspace{-2.5cm}
\includegraphics[height=3.5in]{figures/SinglePend.pdf}
\vspace{-3.5cm}
\column{0.7\textwidth}

 *  Gravitation $\tau$: \hspace{1ex} $-mgl\sin\theta$\\*[1.5ex]
 * Friction $\tau$: \hspace{3ex}  $-\beta\dot{\theta}$\\*[1.5ex]
 * External $\tau$:\hspace{3ex}  $\tau_0\cos \,\omega t$

 
\vspace{-1ex}
\begin{align}
I\, \frac{d^{2}\theta} {dt^{2}} = &   - {mgl}\, \sin\theta
 - \beta \, \frac{d\theta}{dt}
  + \tau_{0} \cos\omega t \\*[1.5ex]
 \alert{ \frac{d^{2}\theta} {dt^{2}}   =}  &
  \alert{-\omega_{0}^{2}  \,\sin \theta  -\alpha \,\frac{d\theta}{dt} +
f\cos\omega t} 
\end{align}
\begin{footnotesize}
  \[\omega_{0}    =  \frac{mgl}{I},\quad \alpha =
\frac{\beta}{I}, \quad f =\frac{\tau_0}{I} \]
\end{footnotesize}
\end{columns}
\end{block}
 
#### Chaotic Pendulum ODE
\setcounter{equation}{0}
\begin{block}{Standard ODE Form (rk4): $\quad \dot{\vec{y}} = \vec{f}(\vec{y}, t)$}
\begin{columns}
\hspace{-3cm}\column{0.35\textwidth}
\vspace{-3cm}
\includegraphics[height=3.75in]{figures/SinglePend.pdf}
\vspace{-3.5cm}
\column{0.65\textwidth}
  \beq \frac{d^{2}\theta}{dt^{2}}   =
-\omega_{0}^{2}  \,\sin \theta  -\alpha \,\frac{d\theta}{dt} +
f\cos\omega t
\enq

 * 2$^{nd}$ O t-dependent nonlinear ODE
* Nonlinearity: \hspace{1ex} $\sin\theta \simeq \theta -\theta^3/3! \cdots$
 * $ y^{(0)} =  \theta(t), \quad y^{(1)} = \frac{d\theta(t)}{dt}$

\end{columns}
  \begin{align}
\alert{\frac{dy^{(0)}}{dt} \ =\ }&  \alert{y^{(1)}}\\*[1.5ex]
\alert{\frac{dy^{(1)}}{dt}  \ =\  }& \alert{- \omega_{0}^{2} \sin y^{(0)} - \alpha
y^{(1)} + f\cos\omega t}
\end{align}
\end{block}


### Free Pend
\setcounter{equation}{0}

#### Start Simply: Free Oscillations (Test Algorithm \& Physics)
\begin{block}{Ignore Friction \& External Torques \hspace{3ex}($f= \alpha = 0$)}
\begin{columns}
\hspace{-3cm}\column{0.35\textwidth}
\vspace{-4cm}
\includegraphics[height=4.5in]{figures/FreePend.pdf}
\vspace{-3.5cm}
\column{0.65\textwidth}
\vspace{-1cm}
  \begin{align}
 \alert{\ddot{\theta}  =} & \alert{-\omega_{0}^{2} \sin \theta }  \label{6}\\*[2ex]
  \ddot{\theta} \  \simeq\  & -\omega_0^2 \theta \quad\quad \mbox{(linear,  $\theta\simeq 0$)}\nonumber\\*[2ex]
 \Rightarrow \enskip\theta(t) \ =\  & \theta_{0} \sin(\omega_{0} t
+ \phi)
\end{align}
\end{columns}
(\ref{6}):\hspace{2ex}  ''Analytic solution''; sort of:

\begin{footnotesize}
\beq
 T  \propto
\int_{0}^{\theta_m}\frac{d\theta}{ \left[\sin^{2}({\theta_m}/{2})
- \sin^{2}({\theta}/{2})\right]^{1/2}}
\enq
\end{footnotesize}
 \end{block}

#### Visualization: Phase Space Orbits
\setcounter{equation}{0}

 \begin{block}{Abstract Space: $v(t)$ vs $x(t)\ $ ($x$ vs $t$, $v$ vs $t$= Complicated)}
 \vspace{-5.4cm}
\no\includegraphics[width=4.25in]{figures/Fig127Mod.pdf}
 \vspace{-5cm}
 \begin{columns}
 \column{0.45\textwidth}
 
* Geometry easy to ``see''
* SHM: Ellipse, $E\rightarrow$ size
* Anharmonic:  + corners

 \column{0.55\textwidth}
 
 * Ossc \implies CW Closed
 * Non Ossc, repulse = open

\end{columns}
\begin{footnotesize}
\begin{align}
x(t)=&  A \sin(\omega t),\quad v(t)   = \omega A
\cos(\omega t)\quad (SHM)\\*[1ex]
E  = & {\rm KE} + {\rm PE} =   m \alert{v^{2}}/2 +
 \omega^{2}m^{2}\alert{x^{2}}/2=  \mbox{ellipse}
\end{align}
\end{footnotesize}
\end{block}

 #### Undriven, Frictionless Pendulum in Phase Space
\setcounter{equation}{0}

\begin{block}{Separatrix  Separates Open \& Closed Orbits}
\centerline{\includegraphics[width=3.25in]{figures/Fig128leftMod.pdf}}
 \vspace{-1.5cm}
 \begin{columns}
 \column{0.5\textwidth}
 
  * Closed: oscillation
  * Open: rotation
  * Both: periodic
 *  Orbits do not cross

 \column{0.5\textwidth}
 
 *  Open orbits touch
 * Hyperbolic points
 * Unstable equilibrium

\end{columns}
\end{block}

 #### Include Friction, Driving Torque (small t steps)
\setcounter{equation}{0}
\begin{block}{Geometry Tends to Remain}
\vspace{-3.5cm}
\includegraphics[height=4.5in]{figures/Limit.pdf}
 \vspace{-4.5cm}
 \begin{columns}
 \column{0.5\textwidth}
 
 *  Friction \implies $\downarrow$ E\\*[1.5ex]
 *  Inward Spiral\\*[1.5ex]
 * $\tau_{ext}$ can put $E$ back\\*[1.5ex]

 \column{0.5\textwidth}
 
 * Limit cycle = Balance \\*[1.5ex]
 * $<\tau_{ext}> \ = \ <\mbox{friction}> $ \\*[1.5ex]

\end{columns}
\end{block}


#### Chaos As Viewed in Phase Space (Full Solution)
\setcounter{equation}{0}

\begin{block}{Look for in Your Simulations}
\begin{footnotesize}
\begin{columns}
 \column{0.5\textwidth}
 \includegraphics[height=1.75in]{figures/PSplotPend.pdf}
 \vspace{-0.5cm}
 
  * Complex $\leq$ Chaos $\leq$ Rand\\*[1.5ex]
  * Fixed Params, all $x_0$, $t$s:  flows \\*[2.0ex]
 
 \column{0.5\textwidth}

 * Chaos complex $\neq$ mess\\*[2.0ex]
 * Figs distort, remains\\*[2.0ex]
 * Closed = periodic \\*[2.0ex]
 * Simplicity in chaos [PS, $\neq \theta(t)$]\\*[2.0ex]
  * $\rightarrow$ attractors (return)\\*[2.0ex]
  * Random = cloud fill $E$ \\*[2.0ex]
  * \alert{Bands} \implies continuity, sequential\\*[2.0ex]
  * \implies hypersensitive $\theta(t)$\\*[2.0ex]
  * Tools measure chaos\\*[2.0ex]
 
 \end{columns}
 \end{footnotesize}
 \end{block}





### Double Pendulum
#### Double Pendulum: Alternative Problem
\setcounter{equation}{0}

\begin{block}{Chaos without External Torque or Friction}
\begin{columns}
\column{0.6\textwidth}
\vspace{-2.5cm}\hspace{1.1cm}
\begin{figure}
\centerline{\includegraphics[width=15pc]{figures/DoublePendPhoto.pdf}}
\end{figure}
\column{0.4\textwidth}
\vspace{-3.5cm}

* No small-$\theta$\\*[1.5ex]
* Coupling = extra degree freedom\\*[1.5ex]
* Small $\theta$: in-$\phi$, out-$\phi$

\end{columns}
\vspace{-3.5cm}
\begin{footnotesize}
 \begin{align}
L =& {\rm KE}-{\rm PE} =  (m_1+m_2) l_1^2
\dot{\theta_1}^2/2 +  m_2l_2^2\dot{\theta_2}^2/2\\
& +\, m_2l_1l_2
\dot{\theta_1}\dot{\theta_2}\cos(\theta_1-\theta_2) +(m_1+m_2)g
l_1\cos\theta_1 + m_2g l_2\cos\theta_2 \nonumber\\*[2ex]
\Rightarrow\quad & (m_1+m_2)l_1\ddot{\theta_1} +
m_2l_2\ddot{\theta_2}\cos(\theta_1-\theta_2) + m_2 l_2 \dot{\theta_2}^2
\sin(\theta_1-\theta_2)\\[4pt]
&\quad + g(m_1+m_2)\sin\theta_1 = 0  \nonumber\\
&m_2l_2\ddot{\theta_2}+m_2l_1\ddot{\theta_1}\cos(\theta_1-\theta_2)-
m_2l_1\dot{\theta_1}^2\sin(\theta_1-\theta_2)  +  mg\sin\theta_2 =
0
 \end{align}
\end{footnotesize}
\end{block}

#### Double Pendulum: Bifurcations
\vspace{-8cm}
 \begin{figure}
 \centerline{\includegraphics[width=17pc]{figures/DoublePend.pdf} \vspace{-10cm}
 \includegraphics[width=20pc]{figures/DoublePendBifur.pdf} }
\end{figure}


