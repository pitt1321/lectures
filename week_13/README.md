# Computational methods in Physics
## Week 13
#### Prof. Michael Wood-Vasey
##### [based on materials from Prof. Brian D'Urso]
##### University of Pittsburgh, Department of Physics and Astronomy

%\documentclass{beamer}
%\mode<presentation>{\usetheme{Goettingen}}
\mode<presentation>{\usetheme{default}}

\usepackage[latin1]{inputenc}
%\usepackage{listings}
\usepackage{times}
%\usepackage[T1]{fontenc}
% Or whatever. Note that the encoding and the font should match. If T1
% does not look nice, try deleting the line with the fontenc.


%\def\file{\protect\pbtt} % font for file names in commands
% defines from papers
\def\bra#1{\left\langle #1\right|}  %\bra{\psi}
\def\ket#1{\left| #1\right\rangle}  %\ket{\psi}
\def\sumint {\sum\hspace{-3ex}\int} %\sum-integral
% braket
\newcommand{\braket}[2]{\left\langle{#1}\left|{#2}\right.\right\rangle}
%\newcommand{\braket}[2]{\left\langle{#1}\right|\left.{#2}\right\rangle}
% matrix element, expectation value
\newcommand{\xval}[3]{\left\langle{#1}\left|{#2}\right|{#3}\right\rangle}
\newcommand{\F}{\mathbf{F}}
\newcommand{\rv}{\mathbf{r}}
\newcommand{\fv}{\mathbf{f}}

\newcommand{\e}{\mathbf{e}}
% Bold face greek chars (also to get caps)-now back to old way too
\def\bfgreek#1{\mbox{\boldmath$#1$}}
\def\r {\bfgreek{r}}
\def\x {\bfgreek{x}}
\def\O {\bfgreek{\Omega}}
\def\p {\bfgreek{p}}
\def\P {\bfgreek{P}}
\def\e {\bfgreek{e}}
\def\f {\bfgreek{f}}
\def\F {\bfgreek{F}}
\def\R {\bfgreek{R}}
\def\D {\Delta}
\def\k {\bfgreek{k}}
\def\v {\mathbf{v}}
\def\u {\mathbf{u}}
\def\w {\mathbf{w}}
%\def\bfgreek#1{\bf #1}

% Re & Im for math mode
\def\Re {\mbox{Re}}
\def\Im{\mbox{Im}}
% Dirac slash
\def\slash {/\!\!\! }
% \def\slash {\not }
% definition
\def\deq{\stackrel{\rm def}{\ =\ } }
% Angstrom
\def\A{\stackrel{\cdot}{\rm A} }

%shorthand for equation begin, end
\def\beq {\begin{footnotesize}\begin{equation}}
\def\enq {\end{equation}\end{footnotesize}}
\def\bef {\begin{footnotesize}}
\def\enf {\end{footnotesize}}

%shorthand for lists begin end
\def\bei {\begin{itemize}}
\def\eni {\end{itemize}}
\def\ben {\begin{enumerate}}
\def\enn {\end{enumerate}}
\def\i {\item}
% noindent
\def\no {\noindent}

% imply
\def\imply {$\ \Rightarrow\ $}

% horizontal line to set off tex
\def\line{\rule{3in}{0.1cm}\\*[1ex]}


%place bullet in margin, next to line
\newcommand{\bull}{
\vspace{1ex} \noindent \hspace{+3ex} $\bullet$
}
%--------------------------







\title[PHYS 1321] % (optional, use only with long paper titles)
{Computational Methods in Physics}

\subtitle{PHYS 1321: Notes and Homework}

\author[] % (optional, use only with lots of authors)
{Prof. Brian D'Urso}

\institute{University of Pittsburgh\\ Department of Physics and Astronomy}

\date[Week 13]{Week 13}


\begin{document}

%\lstset{language=Python, basicstyle=\footnotesize\ttfamily}

\begin{frame}
  \titlepage
\end{frame}

\section<article>{PHYS 1321: Notes and Homework \hfill Week 13}
\subsection<article>{Computational Methods in Physics}
\mode<article>{\vspace{3mm} \hrule \vspace{5mm}}


%\begin{frame}
%\frametitle<presentation>{Contents}
%\tableofcontents
%\end{frame}


%\section{Course Information}

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





% \begin{frame}{Numerical Solution of Wave Equations}
%
%\begin{block}{}
%
% \bei
% \pause \i Many PDE Wave Equations $y(x,t)$
% \pause \i First standard ``wave equation'', then beyond texts\\*[1.5ex]
% \pause \i Again t-stepping, leapfrog algorithm\\*[1.5ex]
% \pause \i Also quantum wave packets (complex), E\&M vector\\*[1.5ex]
% \pause \i Also CFD:   dispersion,  shocks, solitons\\
%\eni
%\end{block}
%%\begin{figure}
%%\includemovie[poster, controls,text={loading CatFrictionAnimate}] {6cm}{3cm}{figures/CatFrictionAnimate.mov}
%%\end{figure}
%\end{frame}


\begin{frame}{Theory: Hyperbolic Wave Equation}
\begin{figure}
\includegraphics[width=19pc]{figures/Figure181leftc.png}
\end{figure}
\vspace{-0.75cm}
\begin{block}{}
\bei
\i Recall standing \& travel wave demo (do!) \\*[1.25ex]
\i  $L$ = length, fastened at  ends\\*[1.25ex]
\i $\rho$ = density = mass/length = constant\\*[1.25ex]
\i $T$ =   tension = constant = high, no $g$ sag\\*[1.25ex]
\i No friction\\*[1.25ex]
\i $y(x,t)$ = small vertical  displacement (1D)
\eni
\end{block}
\end{frame}


\begin{frame}{Derive Hyperbolic (Linear) Wave Equation}
\vspace{-0.25cm}
\begin{figure}
\includegraphics[width=9pc]{figures/Figure181leftc.png}\hspace{8ex}
\includegraphics[width=8pc]{figures/Figure181rightc.png}
\end{figure}

\begin{columns}
\column{0.5\textwidth}
\bei
\pause \i Small $\frac{y}{L}$
\pause \i Small slope $\frac{\partial y}{\partial x}$
\pause \i {\footnotesize $\sin\theta \simeq \tan\theta =  \frac{\partial y}{\partial x}$}
\eni
\column{0.5\textwidth}
\bei
\pause \i Isolate section $\Delta x$
\pause \i Restoring force = $\Delta T_y$
\pause \i   {\footnotesize $c  =  \sqrt{T/\rho} \neq$ string velocity $= \partial y/\partial t$}
\eni
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
\end{frame}

\begin{frame}{Boundary \& Initial Conditions on Solution}
\setcounter{equation}{0}
\beq
\alert{\frac{\partial^2 y(x,t)}{\partial x^2} =
\frac{1}{c^2} \frac{\partial^2 y(x,t)}{\partial t^2}}
\enq
\bei
\pause \i PDE: two independent variables $x$ and $t$  \\*[1.5ex]
\pause \i Initial condition = triangular  ``pluck'':
 \begin{footnotesize} \pause \beq
 y(x,t=0)= \begin{cases}
 1.25 x/L , &x\leq 0.8 L ,\\
 (5-5x/L), &x> 0.8 L,
 \end{cases}
 \enq
 \end{footnotesize}
\pause \i $2^{nd}\ {\cal O}(t)$  \imply need  $2^{nd}$ IC\\*[1.5ex]
\pause \i Released from rest:
 \begin{footnotesize} \beq
\frac{\partial y} {\partial t}(x,t=0) =0,\quad \mbox{(initial
condition 2)}
 \enq\end{footnotesize}
\pause \i Boundary conditions for all times
\begin{footnotesize}\beq
y(0,t) \equiv 0, \quad y(L,t) \equiv 0
\enq\end{footnotesize}
\eni
\end{frame}


\section{Normal-Modes}

\begin{frame}{Normal-Mode Solution (Analytic but $\infty$)}
%\quad %\href{figures/Jstrsin/Stseno.html}
%{\includegraphics[width=4pc]{figures/JavaApplet4.pdf}}} %--------------------------
\setcounter{equation}{0}

\begin{enumerate}
\pause \i Assume  \bef\alert{$y(x,t) = X(x)T(t)$}\enf
\\*[1.5ex]
\pause \i i) Substitute,\ \  ii) $\div y$,\ \  iii) iff:\\
 \pause \beq
\frac{d^2 T(t)}{dt^2} +\omega^2 T(t) = 0, \quad \frac{d^2
X(x)}{dx^2} +k^2 X(x) = 0,\quad k {\deq} \frac{\omega}{c}
 \enq
\pause \i Determine     $\omega$ \& $k$ via BC
 \bef\pause \begin{align}
\Rightarrow \quad X_n(x) =& A_n \sin {k_n x}, \quad k_n = \frac
{\pi (n+1) } {L}, \quad  n = 0, 1, \ldots\\*[1.5ex]
T_n(t) =&  C_n \sin \omega_n t + D_n \,\cos \omega_n t
\end{align}\enf
\pause \i Zero velocity IC2 \imply   $C_n = 0$; linear superposition
\end{enumerate}
\pause \bef\begin{align}
 \alert{y(x,t)=}& \alert{\sum_n^\infty B_n \,\sin k_n x\cos\omega_n t}\\
B_m=& 6.25 \; \sin(0.8 m\pi)/ {m^2 \pi^2}
 \end{align}\enf
\end{frame}

\section{Algorithm}

\begin{frame}{Algorithm: Discretized Wave Equation}%---------------------------
\setcounter{equation}{0}
\begin{columns}
\column{0.5\textwidth}
\vspace{-0.5cm}
\begin{figure}
\includegraphics[width=12pc]{figures/figure182c.png}
\end{figure}
\column{0.65\textwidth}
\bei
\pause \i Solve on space-time grid:
\i $ (x,\ t)  =   (i \Delta x, \ j \Delta t) $
\pause\i BC: vertical white dots
\pause\i IC: top row white dots
\pause\i Can't relax
\pause\i Central-difference derivatives\\*[1.5ex]
\eni
\end{columns}
\vspace{0.5cm}
 \pause\beq
\frac{\partial^2 y }{\partial t^2} \simeq
\frac{y_{i,j+1}+y_{i,j-1}-2 y_{i,j}}{(\Delta t)^2}, \quad\quad
\frac{\partial^2 y}{\partial x^2} \simeq \frac{y_{i+1,j}
+y_{i-1,j}-2 y_{i,j}} {(\Delta x)^2}
 \enq
 \bei
 \pause\i Discretized (difference) wave equation:\\*[1.5ex]
 \beq
\alert{\frac{y_{i,j+1}+y_{i,j-1}-2 y_{i,j}} {c^2 (\Delta t)^2}  \ =\
\frac{y_{i+1,j}+y_{i-1,j}-2 y_{i,j}} {(\Delta x)^2}}
 \enq
 \eni
 \end{frame}


 \begin{frame}{Wave Equation Algorithm: Time-Stepping}%------------

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
\bei
\pause \i NB: only 3 times enter\\*[1.5ex]
\pause \i \bef(j+1, j, j-1)\enf = (future, present, past)\\*[1.5ex]
\pause \i Predict future:
\eni
 \end{columns}
 \pause \beq
   \alert{y_{i,j+1}  = 2 y_{i,j}-y_{i,j-1}+ \frac{c^2 }
{c'^{2}} \left [ y_{i+1,j}+y_{i-1,j}-2 y_{i,j}\right]}
 \enq
 \bei
 \pause \i
 $c' \deq  \Delta x/\Delta t$
 \i  $\frac{c'}{c}$  determines
stability
\eni
\end{frame}


\begin{frame}{Discussion: Time Stepping Algorithm}%--------------

\setcounter{equation}{0}
\begin{columns}
 \column{0.5\textwidth}
\vspace{-0.5cm}
\begin{figure}
\includegraphics[width=12pc]{figures/figure182c.png}
\end{figure}
\column{0.6\textwidth}
\pause \begin{block}{Generalities}
\bei
\pause \i Leapfrog \em{vs}  relaxation\\*[2ex]
\pause \i Store only 3 time values\\*[2ex]
\pause \i Very small $\Delta t$ for high precision\\*[2ex]
\pause \i Starting requires $t<0$\\*[2ex]
\pause \i ``At rest'' IC + CD:\\*[2ex]
\eni
\bef\pause \begin{align*}
\frac{\partial y}{\partial t}(x,0) \simeq& \frac{y(x, \Delta t)- y(x,
-\Delta t)}{2\Delta t}=0\\*[1.5ex]
  \Rightarrow \quad y_{i, 0} = & y_{i,2}
\end{align*}\enf
\end{block}
 \end{columns}

\end{frame}


\begin{frame}{von Neumann (Courant) Stability Condition}%----------------

\setcounter{equation}{0}
\pause \beq
\frac{y_{i,j+1}+y_{i,j-1}-2 y_{i,j}} {c^2 (\Delta t)^2}  \ =\
\frac{y_{i+1,j}+y_{i-1,j}-2 y_{i,j}} {(\Delta x)^2}
 \enq
 \pause \begin{block}{General Truth:  Can't pick arbitrary $\Delta x, \ \Delta t$}
\bei
\pause \i Substitute into (1) \alert{$y_{m,j} = \xi^j\ \exp(i k m\ \Delta x) $} \\*[1.5ex]
\pause \i Avoid exponential growth in time $|\xi|>1$ (unstable)\\*[1.5ex]
\pause \i True generally for  transport equations (Press):
\pause \beq
\alert{c \leq  c'  = \frac{\Delta x }{\Delta t}} \quad\quad\mbox{(Courant
condition)}
\enq
\pause \i Better: smaller $\Delta t$; worse smaller $\Delta x$\\*[1.5ex]
\pause \i (1) = symmetric, yet IC, BC $\neq$ symmetric
\eni
\end{block}
\end{frame}


%\begin{frame}{Non Computational Exercises}%-----------------------------------
%
%\ben
%\pause \i Suggest an algorithm to solve wave equation in 1 step.\\*[2ex]
%\ben
%\pause \i How much memory is required?\\*[2ex]
%\pause \i How does this compare with the memory required for the leapfrog method?
%\enn
%\pause \i
%Suggest an algorithm to solve the wave equation via relaxation (like Laplace's equation).
%\ben
%\pause \i  What would you take as the initial guess?\\*[2ex]
%\pause \i How would you know when the procedure has converged?\\*[2ex]
%\pause \i How would you know  if the solution is correct?
%\enn
%\enn
%\end{frame}


%\section[Implementation]{Wave Equation Implementation}
%
%\begin{frame}{Wave Equation Implementation}%----------------------
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
%\bei
%\pause \i   Study \texttt{EqString.py}, outlining the structure\\*[2ex]
%\pause \i You will need to modify this code to add new physics.\\*[2ex]
%\pause \i NB: $L=1$ \imply $y/L\ll 1$ not OK  ($L=1000$ better)\\*[2ex]
%\pause \i $\rho=0.01\,\hbox{kg/m}$, $T=40\,\hbox{N}$, $\D=
%0.01\,\hbox{cm}$
%\eni
%\end{block}
% \end{frame}


%   \section{Assessment}
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
%\pause \i Make surface or animation $y(x,t)$
%
%\pause \item
%Explore $\Delta x$ \& $\Delta t$ combos
%
%\pause \i  Is  stability condition obeyed?
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
%\pause \item Do 2 near modes beat?
%
%\pause \item
%Interference if plucked in middle?
%
%\end{enumerate}
%
%\end{columns}
%
%\end{frame}



\section{Friction}


\begin{frame}{Including Friction (Easy Numerically)}

\begin{figure}
\includegraphics[width=10pc]{figures/Figure181leftc.png}\hspace{8ex}
\includegraphics[width=8pc]{figures/Figure181rightc.png}
\end{figure}

\begin{block}{How Include Friction in Wave Equation?}
\bei
   \uncover<2->{ \i Observation: Real strings don't vibrate forever}
  \uncover<3->{ \i Model: String element in viscous fluid ($\kappa$)}
  \uncover<4->{ \i Frictional force opposes motion,    $\propto v, \Delta x$:
 \beq
F_f \simeq -2\kappa\ \Delta x\ \frac{\partial y} {\partial
t}
 \enq}
 \uncover<5->{\i Modified wave equation (Additional RHS Force)
\beq
\alert{\frac{\partial^2y}{\partial t^2}= c^2\, \frac{\partial^2
y}{\partial x^2} - \frac{2\kappa}{\rho}\, \frac{\partial
y}{\partial t}}
  \enq}
\eni
\end{block}
\end{frame}


%\begin{frame}{Exercise}%---------------------------------------------
%
%\begin{block}{Do On Your Own}
%\begin{enumerate}
%\pause \i
% Generalize   wave equation algorithm   to include friction\\*[1.5ex]
% \pause \i
% Solve wave equation\\*[1.5ex]
% \pause \i Check that wave decays, or not ($\kappa=0$)\\*[1.5ex]
%\pause \i Unstable: $\kappa <0$? \\*[1.5ex]
%\pause  \i Pick large enough $\kappa$ to see effect; if too large?
% \end{enumerate}
%\end{block}
%\begin{figure}
%\includemovie[poster, controls,text={loading CatFrictionAnimate}] {6cm}{3cm}{figures/CatFrictionAnimate.mov}
%\end{figure}
%\end{frame}

\section{$T(x)$}


%%-------------------------------------------------------------------
%\begin{frame}{Another Extension:  Variable Tension, Density}
%\vspace{-2ex}
%\begin{figure}
%\includegraphics[width=10pc]{figures/Figure181leftc.png}\hspace{8ex}
%\includegraphics[width=8pc]{figures/Figure181rightc.png}
%\end{figure}
%\vspace{-2ex}
%\begin{block}{}
%\begin{columns}
%\column{0.5\textwidth}
%\bei
%\pause \i  \bef $c=\sqrt{T/\rho}$;\enf constant $T$, $\rho$
%\pause \i \imply fast \& slow; adiabatic
%\pause \i  $g$, $\rho(x)$ \imply $T(x)$, $c(x)$
%\eni
%\column{0.5\textwidth}
%\bei
%\pause \i $\uparrow \rho \Rightarrow \uparrow T$ to accelerate
%\pause \i Thick chain ends; $g$
%\pause \i  Newton for element:
%\eni
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
% \end{frame}
%
% \begin{frame}{Discretized Wave Equation with $T(x)$}
%
% \setcounter{equation}{0}
% \pause \begin{block}{\alert{Trial Case: \ } $\rho(x) \ =\  \rho_0 e^{\alpha x}, \quad T = T_O e^{\alpha x}$}
%  \pause \beq
%  \rho(x)\,
%\frac{\partial^2 y(x,t)}{\partial t^2}  \ =\    \frac{\partial
%T(x)}{ \partial x}\, \frac{\partial y(x,t)}{\partial x} +T(x)
%\,\frac{\partial^2 y(x,t)}{\partial x^2}
% \enq
% \bei
%\pause \i Difference equation  via central-difference derivatives:\\*[1.5ex]
% \pause \beq
%y_{i,2} = y_{i,1}+ \frac{c^2}{c'^2}[y_{i+1,1}+y_{i-1,1}
%-2y_{i,1}] + \frac{\alpha c^2 (\Delta t)^2 } {2\Delta
%x}[y_{i+1,1}-y_{i,1}]
% \enq
% \mbox{}
% \pause \i Try standing waves $y(x,t) = A \cos(\omega t)\sin(k x)$\\*[1.5ex]
% \pause \item
%Verify  $\omega \le \omega_{cut}$ \imply no solution
%\eni
%\end{block}
%\end{frame}
%
%\section{Catenary}
%\begin{frame}{Hanging String at Rest: Derivation of \alert{Catenary}} %============
%
%\begin{figure}
%\includegraphics[width=18pc]{figures/figure185c.png}
%\end{figure}
%
%\begin{block}{}
%\begin{columns}
%\column{0.5\textwidth}
%\bei
%\pause \i Chains sag\\*[1.5ex] 
%\pause \i $T(x)$: ends support middle  \\*[1.5ex]
%\pause \i $u(x)$ = equilibrium shape, $y(x)$ = disturbance
%\eni
%\column{0.5\textwidth}
%\bei
%\pause \i $u(x)$, $T(x)$ =?\\*[1.5ex]
%\pause \i Free-body diagram  \\*[1.5ex]
%\pause \i  $W$ =section weight = $T_y$\\*[1.5ex]
%\pause \i $s$ = arc length:
%\eni
%\end{columns}
%\end{block}
%\end{frame}
%
%\begin{frame}{Hanging String: Derivation of Catenary (Cont)}%=============================
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
% \end{frame}
%
%%\begin{frame}{Implementation: Catenary and Frictional Waves}%======================
%%
%%\begin{enumerate}
%%\pause \i Modify EqString.py to include friction and $g$  
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
%% \end{frame}




%\end{document}


