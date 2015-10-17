# Computational methods in Physics
## Week 13
#### Prof. Michael Wood-Vasey
##### [based on materials from Prof. Brian D'Urso]
##### University of Pittsburgh, Department of Physics and Astronomy

% #### Numerical Solution of Wave Equations
%
%\begin{block}{}
%
% 
% \pause * Many PDE Wave Equations $y(x,t)$
% \pause * First standard ``wave equation'', then beyond texts\\*[1.5ex]
% \pause * Again t-stepping, leapfrog algorithm\\*[1.5ex]
% \pause * Also quantum wave packets (complex), E\&M vector\\*[1.5ex]
% \pause * Also CFD:   dispersion,  shocks, solitons\\
%
%\end{block}
%%\begin{figure}
%%\includemovie[poster, controls,text={loading CatFrictionAnimate}] {6cm}{3cm}{figures/CatFrictionAnimate.mov}
%%\end{figure}
%

#### Theory: Hyperbolic Wave Equation
\begin{figure}
\includegraphics[width=19pc]{figures/Figure181leftc.png}
\end{figure}
\vspace{-0.75cm}
\begin{block}{}

* Recall standing \& travel wave demo (do!) \\*[1.25ex]
*  $L$ = length, fastened at  ends\\*[1.25ex]
* $\rho$ = density = mass/length = constant\\*[1.25ex]
* $T$ =   tension = constant = high, no $g$ sag\\*[1.25ex]
* No friction\\*[1.25ex]
* $y(x,t)$ = small vertical  displacement (1D)

\end{block}


#### Derive Hyperbolic (Linear) Wave Equation
\vspace{-0.25cm}
\begin{figure}
\includegraphics[width=9pc]{figures/Figure181leftc.png}\hspace{8ex}
\includegraphics[width=8pc]{figures/Figure181rightc.png}
\end{figure}

\begin{columns}
\column{0.5\textwidth}

\pause * Small $\frac{y}{L}$
\pause * Small slope $\frac{\partial y}{\partial x}$
\pause * {\footnotesize $\sin\theta \simeq \tan\theta =  \frac{\partial y}{\partial x}$}

\column{0.5\textwidth}

\pause * Isolate section $\Delta x$
\pause * Restoring force = $\Delta T_y$
\pause *   {\footnotesize $c  =  \sqrt{T/\rho} \neq$ string velocity $= \partial y/\partial t$}

\end{columns}

\begin{footnotesize}
\begin{align}
\uncover<8->{\sum F_y =}& \uncover<8->{\rho \, \Delta x \, \frac{\partial^2 y}{\partial
t^2}\quad\quad\quad\quad\quad (F=ma)}\\*[1.5ex]
\uncover<9->{\sum F_y  = T\sin\theta_{x+\Delta x} - T\sin\theta_x = }& \uncover<9->{T \left.
\frac{\partial y}{\partial x}\right|_{x+\Delta x} - T \left.
\frac{\partial y}{\partial x}\right|_x \simeq T \frac{\partial^2
y}{\partial x^2}\Delta x }\\*[1.5ex]
\uncover<10->{\Rightarrow \quad \alert{\frac{\partial^2 y(x,t)}{\partial x^2} =}}& \uncover<10->{
\alert{\frac{1}{c^2} \frac{\partial^2 y(x,t)}{\partial t^2}}}
\end{align}
\end{footnotesize}

#### Boundary \& Initial Conditions on Solution
\setcounter{equation}{0}
\beq
\alert{\frac{\partial^2 y(x,t)}{\partial x^2} =
\frac{1}{c^2} \frac{\partial^2 y(x,t)}{\partial t^2}}
\enq

\pause * PDE: two independent variables $x$ and $t$  \\*[1.5ex]
\pause * Initial condition = triangular  ``pluck'':
 \begin{footnotesize} \pause \beq
 y(x,t=0)= \begin{cases}
 1.25 x/L , &x\leq 0.8 L ,\\
 (5-5x/L), &x> 0.8 L,
 \end{cases}
 \enq
 \end{footnotesize}
\pause * $2^{nd}\ {\cal O}(t)$  \imply need  $2^{nd}$ IC\\*[1.5ex]
\pause * Released from rest:
 \begin{footnotesize} \beq
\frac{\partial y} {\partial t}(x,t=0) =0,\quad \mbox{(initial
condition 2)}
 \enq\end{footnotesize}
\pause * Boundary conditions for all times
\begin{footnotesize}\beq
y(0,t) \equiv 0, \quad y(L,t) \equiv 0
\enq\end{footnotesize}



### Normal-Modes

#### Normal-Mode Solution (Analytic but $\infty$)
%\quad %\href{figures/Jstrsin/Stseno.html}
%{\includegraphics[width=4pc]{figures/JavaApplet4.pdf}}} %--------------------------
\setcounter{equation}{0}

\begin{enumerate}
\pause * Assume  \bef\alert{$y(x,t) = X(x)T(t)$}\enf
\\*[1.5ex]
\pause * i) Substitute,\ \  ii) $\div y$,\ \  iii) iff:\\
 \pause \beq
\frac{d^2 T(t)}{dt^2} +\omega^2 T(t) = 0, \quad \frac{d^2
X(x)}{dx^2} +k^2 X(x) = 0,\quad k {\deq} \frac{\omega}{c}
 \enq
\pause * Determine     $\omega$ \& $k$ via BC
 \bef\pause \begin{align}
\Rightarrow \quad X_n(x) =& A_n \sin {k_n x}, \quad k_n = \frac
{\pi (n+1) } {L}, \quad  n = 0, 1, \ldots\\*[1.5ex]
T_n(t) =&  C_n \sin \omega_n t + D_n \,\cos \omega_n t
\end{align}\enf
\pause * Zero velocity IC2 \imply   $C_n = 0$; linear superposition
\end{enumerate}
\pause \bef\begin{align}
 \alert{y(x,t)=}& \alert{\sum_n^\infty B_n \,\sin k_n x\cos\omega_n t}\\
B_m=& 6.25 \; \sin(0.8 m\pi)/ {m^2 \pi^2}
 \end{align}\enf

### Algorithm

#### Algorithm: Discretized Wave Equation%---------------------------
\setcounter{equation}{0}
\begin{columns}
\column{0.5\textwidth}
\vspace{-0.5cm}
\begin{figure}
\includegraphics[width=12pc]{figures/figure182c.png}
\end{figure}
\column{0.65\textwidth}

\pause * Solve on space-time grid:
* $ (x,\ t)  =   (i \Delta x, \ j \Delta t) $
\pause* BC: vertical white dots
\pause* IC: top row white dots
\pause* Can't relax
\pause* Central-difference derivatives\\*[1.5ex]

\end{columns}
\vspace{0.5cm}
 \pause\beq
\frac{\partial^2 y }{\partial t^2} \simeq
\frac{y_{i,j+1}+y_{i,j-1}-2 y_{i,j}}{(\Delta t)^2}, \quad\quad
\frac{\partial^2 y}{\partial x^2} \simeq \frac{y_{i+1,j}
+y_{i-1,j}-2 y_{i,j}} {(\Delta x)^2}
 \enq
 
 \pause* Discretized (difference) wave equation:\\*[1.5ex]
 \beq
\alert{\frac{y_{i,j+1}+y_{i,j-1}-2 y_{i,j}} {c^2 (\Delta t)^2}  \ =\
\frac{y_{i+1,j}+y_{i-1,j}-2 y_{i,j}} {(\Delta x)^2}}
 \enq
 
 

 #### Wave Equation Algorithm: Time-Stepping%------------

 \setcounter{equation}{0}
\pause \beq
\frac{y_{i,j+1}+y_{i,j-1}-2 y_{i,j}} {c^2 (\Delta t)^2}  \ =\
\frac{y_{i+1,j}+y_{i-1,j}-2 y_{i,j}} {(\Delta x)^2}
 \enq
 \begin{columns}
 \column{0.5\textwidth}
\vspace{-0.5cm}
\begin{figure}
\includegraphics[width=9pc]{figures/figure182c.png}
\end{figure}
\column{0.65\textwidth}

\pause * NB: only 3 times enter\\*[1.5ex]
\pause * \bef(j+1, j, j-1)\enf = (future, present, past)\\*[1.5ex]
\pause * Predict future:

 \end{columns}
 \pause \beq
   \alert{y_{i,j+1}  = 2 y_{i,j}-y_{i,j-1}+ \frac{c^2 }
{c'^{2}} \left [ y_{i+1,j}+y_{i-1,j}-2 y_{i,j}\right]}
 \enq
 
 \pause \i
 $c' \deq  \Delta x/\Delta t$
 *  $\frac{c'}{c}$  determines
stability



#### Discussion: Time Stepping Algorithm%--------------

\setcounter{equation}{0}
\begin{columns}
 \column{0.5\textwidth}
\vspace{-0.5cm}
\begin{figure}
\includegraphics[width=12pc]{figures/figure182c.png}
\end{figure}
\column{0.6\textwidth}
\pause \begin{block}{Generalities}

\pause * Leapfrog \em{vs}  relaxation\\*[2ex]
\pause * Store only 3 time values\\*[2ex]
\pause * Very small $\Delta t$ for high precision\\*[2ex]
\pause * Starting requires $t<0$\\*[2ex]
\pause * "At rest" IC + CD:\\*[2ex]

\bef\pause \begin{align*}
\frac{\partial y}{\partial t}(x,0) \simeq& \frac{y(x, \Delta t)- y(x,
-\Delta t)}{2\Delta t}=0\\*[1.5ex]
  \Rightarrow \quad y_{i, 0} = & y_{i,2}
\end{align*}\enf
\end{block}
 \end{columns}



#### von Neumann (Courant) Stability Condition%----------------

\setcounter{equation}{0}
\pause \beq
\frac{y_{i,j+1}+y_{i,j-1}-2 y_{i,j}} {c^2 (\Delta t)^2}  \ =\
\frac{y_{i+1,j}+y_{i-1,j}-2 y_{i,j}} {(\Delta x)^2}
 \enq
 \pause \begin{block}{General Truth:  Can't pick arbitrary $\Delta x, \ \Delta t$}

\pause * Substitute into (1) \alert{$y_{m,j} = \xi^j\ \exp(i k m\ \Delta x) $} \\*[1.5ex]
\pause * Avoid exponential growth in time $|\xi|>1$ (unstable)\\*[1.5ex]
\pause * True generally for  transport equations (Press):
\pause \beq
\alert{c \leq  c'  = \frac{\Delta x }{\Delta t}} \quad\quad\mbox{(Courant
condition)}
\enq
\pause * Better: smaller $\Delta t$; worse smaller $\Delta x$\\*[1.5ex]
\pause * (1) = symmetric, yet IC, BC $\neq$ symmetric

\end{block}


%#### Non Computational Exercises%-----------------------------------
%
%\ben
%\pause * Suggest an algorithm to solve wave equation in 1 step.\\*[2ex]
%\ben
%\pause * How much memory is required?\\*[2ex]
%\pause * How does this compare with the memory required for the leapfrog method?
%\enn
%\pause \i
%Suggest an algorithm to solve the wave equation via relaxation (like Laplace's equation).
%\ben
%\pause *  What would you take as the initial guess?\\*[2ex]
%\pause * How would you know when the procedure has converged?\\*[2ex]
%\pause * How would you know  if the solution is correct?
%\enn
%\enn
%

%\section[Implementation]{Wave Equation Implementation}
%
%#### Wave Equation Implementation%----------------------
%
%\begin{block}{
%\href{figures/Jvibstr.html}{\vspace{2.5cm}
%\includegraphics[width=4pc]{figures/JavaApplet4.pdf}}
%\hyperbaseurl{./}
%\href{run:figures/EqStringAnimate_05Mar09.py}{
%\includegraphics[scale=0.2]{figures/PythonCode1.pdf}}
%\hyperbaseurl{./}
%\href{figures/EqString.html}{
%\includegraphics[scale=0.4]{figures/Code2.pdf}}
%\vspace{-10ex}}
%
%
%\pause *   Study \texttt{EqString.py}, outlining the structure\\*[2ex]
%\pause * You will need to modify this code to add new physics.\\*[2ex]
%\pause * NB: $L=1$ \imply $y/L\ll 1$ not OK  ($L=1000$ better)\\*[2ex]
%\pause * $\rho=0.01\,\hbox{kg/m}$, $T=40\,\hbox{N}$, $\D=
%0.01\,\hbox{cm}$
%
%\end{block}
% 

%   ### Assessment
%\begin{frame}[label=current]{Assessment}%-----------------------------------
%
%\begin{columns}
%\column{0.4\textwidth}
%
%\begin{figure}
%\includegraphics[width=15pc]{figures/Figure183c.pdf}
%\end{figure}
%\column{0.7\textwidth}
%\begin{enumerate}
%\pause \item
%Solve   wave equation
%\pause * Make surface or animation $y(x,t)$
%
%\pause \item
%Explore $\Delta x$ \& $\Delta t$ combos
%
%\pause *  Is  stability condition obeyed?
%
%\pause \item
%Compare   "analytic"  vs numeric solutions
%
%\pause \item
%Estimate $c$ via graphs, compare $\sqrt{\frac{T}{\rho}}$
%
%\pause \item
%Choose IC for single normal mode:
% \beq\nonumber
%y(x,t=0) =  0.001\, \sin 2\pi x, \quad\frac{\partial y}{\partial
%t}(x,t=0) =0
% \enq
%
%\pause * Do 2 near modes beat?
%
%\pause \item
%Interference if plucked in middle?
%
%\end{enumerate}
%
%\end{columns}
%
%


### Friction


#### Including Friction (Easy Numerically)

\begin{figure}
\includegraphics[width=10pc]{figures/Figure181leftc.png}\hspace{8ex}
\includegraphics[width=8pc]{figures/Figure181rightc.png}
\end{figure}

\begin{block}{How Include Friction in Wave Equation?}

   \uncover<2->{ * Observation: Real strings don't vibrate forever}
  \uncover<3->{ * Model: String element in viscous fluid ($\kappa$)}
  \uncover<4->{ * Frictional force opposes motion,    $\propto v, \Delta x$:
 \beq
F_f \simeq -2\kappa\ \Delta x\ \frac{\partial y} {\partial
t}
 \enq}
 \uncover<5->{* Modified wave equation (Additional RHS Force)
\beq
\alert{\frac{\partial^2y}{\partial t^2}= c^2\, \frac{\partial^2
y}{\partial x^2} - \frac{2\kappa}{\rho}\, \frac{\partial
y}{\partial t}}
  \enq}

\end{block}


%#### Exercise%---------------------------------------------
%
%\begin{block}{Do On Your Own}
%\begin{enumerate}
%\pause \i
% Generalize   wave equation algorithm   to include friction\\*[1.5ex]
% \pause \i
% Solve wave equation\\*[1.5ex]
% \pause * Check that wave decays, or not ($\kappa=0$)\\*[1.5ex]
%\pause * Unstable: $\kappa <0$? \\*[1.5ex]
%\pause  * Pick large enough $\kappa$ to see effect; if too large?
% \end{enumerate}
%\end{block}
%\begin{figure}
%\includemovie[poster, controls,text={loading CatFrictionAnimate}] {6cm}{3cm}{figures/CatFrictionAnimate.mov}
%\end{figure}
%
### $T(x)$


%%-------------------------------------------------------------------
%#### Another Extension:  Variable Tension, Density
%\vspace{-2ex}
%\begin{figure}
%\includegraphics[width=10pc]{figures/Figure181leftc.png}\hspace{8ex}
%\includegraphics[width=8pc]{figures/Figure181rightc.png}
%\end{figure}
%\vspace{-2ex}
%\begin{block}{}
%\begin{columns}
%\column{0.5\textwidth}
%
%\pause *  \bef $c=\sqrt{T/\rho}$;\enf constant $T$, $\rho$
%\pause * \imply fast \& slow; adiabatic
%\pause *  $g$, $\rho(x)$ \imply $T(x)$, $c(x)$
%
%\column{0.5\textwidth}
%
%\pause * $\uparrow \rho \Rightarrow \uparrow T$ to accelerate
%\pause * Thick chain ends; $g$
%\pause *  Newton for element:
%
%\end{columns} 
%\bef\begin{align}
%\uncover<8->{F \ =\  }& \uncover<8->{m a }\\*[1.5ex]
%\uncover<9->{\frac{\partial}{\partial x}\left[T(x) \,
%\frac{\partial y(x,t)}{\partial x}\right]\Delta x \ =\ } & \uncover<9->{\rho(x)\Delta
%x\,\frac{\partial^2 y(x,t)} {\partial t^2}}\\*[2.0ex]
%\uncover<10->{\alert{\frac{\partial
%T(x)}{\partial x}\, \frac{\partial y(x,t)}{\partial x} +T(x)
%\,\frac{\partial^2 y(x,t)}{\partial x^2}\ =\  }&\alert{\rho(x)\,
%\frac{\partial^2 y(x,t)}{\partial
%t^2}}}
%\end{align}\enf
%\end{block}
% %
% #### Discretized Wave Equation with $T(x)$
%
% \setcounter{equation}{0}
% \pause \begin{block}{\alert{Trial Case: \ } $\rho(x) \ =\  \rho_0 e^{\alpha x}, \quad T = T_O e^{\alpha x}$}
%  \pause \beq
%  \rho(x)\,
%\frac{\partial^2 y(x,t)}{\partial t^2}  \ =\    \frac{\partial
%T(x)}{ \partial x}\, \frac{\partial y(x,t)}{\partial x} +T(x)
%\,\frac{\partial^2 y(x,t)}{\partial x^2}
% \enq
% 
%\pause * Difference equation  via central-difference derivatives:\\*[1.5ex]
% \pause \beq
%y_{i,2} = y_{i,1}+ \frac{c^2}{c'^2}[y_{i+1,1}+y_{i-1,1}
%-2y_{i,1}] + \frac{\alpha c^2 (\Delta t)^2 } {2\Delta
%x}[y_{i+1,1}-y_{i,1}]
% \enq
% \mbox{}
% \pause * Try standing waves $y(x,t) = A \cos(\omega t)\sin(k x)$\\*[1.5ex]
% \pause \item
%Verify  $\omega \le \omega_{cut}$ \imply no solution
%
%\end{block}
%%
%### Catenary
%#### Hanging String at Rest: Derivation of \alert{Catenary} %============
%
%\begin{figure}
%\includegraphics[width=18pc]{figures/figure185c.png}
%\end{figure}
%
%\begin{block}{}
%\begin{columns}
%\column{0.5\textwidth}
%
%\pause * Chains sag\\*[1.5ex] 
%\pause * $T(x)$: ends support middle  \\*[1.5ex]
%\pause * $u(x)$ = equilibrium shape, $y(x)$ = disturbance
%
%\column{0.5\textwidth}
%
%\pause * $u(x)$, $T(x)$ =?\\*[1.5ex]
%\pause * Free-body diagram  \\*[1.5ex]
%\pause *  $W$ =section weight = $T_y$\\*[1.5ex]
%\pause * $s$ = arc length:
%
%\end{columns}
%\end{block}
%%
%#### Hanging String: Derivation of Catenary (Cont)%=============================
%
%\setcounter{equation}{0}
%
%\begin{figure}
%\includegraphics[width=15pc]{figures/figure185c.png}
%\end{figure}
%\bef
%\begin{align}
%T(x)\sin\theta  = & W = \rho g s, \quad T(x)\cos\theta = T_0,
%\\
%\Rightarrow \quad \tan\theta = & {\rho g s} /{T_0}
% \end{align}\enf
% \vspace{-2ex}
% \uncover<2->{\begin{block}{Trick:  convert  to ODE, solve ODE (see text)} }
%\bef\begin{align}
% \uncover<3->{\alert{u(x) \ =}} & \uncover<3->{ \  \alert{D \cosh \frac{x} {D}}
%  \quad\quad\mbox{NB Special Orgin)}}\\
%   \uncover<4->{ T(x) \ =} & \uncover<4->{ \   T_0 \cosh\,\frac{x}{D}, \quad D  \ \deq  \  {T_0 / \rho g}}
% \end{align}\enf
%\uncover<5->{Now know $T(x)$ for wave equation
% \beq
% \frac{\partial
%T(x)}{\partial x}\, \frac{\partial y(x,t)}{\partial x} +T(x)
%\,\frac{\partial^2 y(x,t)}{\partial x^2}\ =\   \rho(x)\,
%\frac{\partial^2 y(x,t)}{\partial
%t^2}
%\enq}
%\end{block}
% %
%%#### Implementation: Catenary and Frictional Waves%======================
%%
%%\begin{enumerate}
%%\pause * Modify EqString.py to include friction and $g$  
%%\pause \item
%%Look for interesting cases, create surface plots
%%\pause \item
%%Point out non uniform damping.
%%\pause \item
%%Are standing waves (normal modes) possible?
%%\pause \bef\[
%%u(x,t) = A \cos(\omega t)\sin(\gamma x)
%% \]\enf
%%\end{enumerate}
%%\begin{figure}
%%\includegraphics[width=1.4in]{figures/figure186C.pdf}
%%(Get to work!)
%%\end{figure}
%% 



%\end{document}


