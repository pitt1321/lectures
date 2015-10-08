# Computational methods in Physics
## Week 10
#### Prof. Michael Wood-Vasey
##### [based on materials from Prof. Brian D'Urso]
##### University of Pittsburgh, Department of Physics and Astronomy

%\documentclass{beamer}
%\mode<presentation>{\usetheme{Goettingen}}
\mode<presentation>{\usetheme{default}}

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

\date[Week 10]{Week 10}


\begin{document}

\lstset{language=Python, basicstyle=\footnotesize\ttfamily}

\begin{frame}
  \titlepage
\end{frame}

\section<article>{PHYS 1321: Notes and Homework \hfill Week 9}
\subsection<article>{Computational Methods in Physics}
\mode<article>{\vspace{3mm} \hrule \vspace{5mm}}


%\begin{frame}
%\frametitle<presentation>{Contents}
%\tableofcontents
%\end{frame}


%\section{Course Information}

%\subsection[First Subsection Name]{First Subsection Name}


\begin{frame}[plain]{Where to Go for Help}  
\begin{itemize}
\item I will be around during ``working time'' during each class after lecture time.
\vfill\vfill
\item Office hours: \\
\vfill
TO BE RESCHEDULED\\
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




\section{Problem}
\begin{frame}{Problem: Why Is Nature So Complicated?}

\begin{columns}
\column{0.5\textwidth}
\vspace{-10.0cm}
\bei
\i Insect populations, weather patterns
\i Complex behavior\\*[2ex]
\i Stable,  periodic,   chaotic, stable, \ldots\\*[2ex]
\i  \textbf{Problem:} can a simple, discrete law  produce such complicated
behavior?\\*[1ex]
\vspace{-10.0cm}
\eni
\column{0.5\textwidth}
\includegraphics[width=1.5in]{figures/BugPop.jpg}
\end{columns}
\end{frame}


\section{Logistic Map}
\begin{frame}{Model Realistic Problem: Bug Cycles}

\begin{block}{Bugs Reproduce Generation after Generation = $i$}
\begin{columns}
\column{0.5\textwidth}
\vspace{-17.0cm}
\bei
\i   $N_0\ \rightarrow \  N_1, N_2, \ldots  N_\infty$\\*[2ex]
\i  $N_i = f(i)?$\\*[2ex]
\i Seen discrete law,
\begin{align*}
\frac{\Delta N}{\Delta t} =\ & -\lambda N \\*[1ex]
\Rightarrow\   \simeq\ & e^{-\lambda t}
\end{align*}
\i   $-\lambda \rightarrow +\lambda$ \imply  growth
\vspace{-10.0cm}
\eni
\column{0.5\textwidth}
\includegraphics[width=1.75in]{figures/cockroach.jpg}
\vspace{10.0cm}
\[
\frac{\Delta N_i}{\Delta t} = \lambda \; N_i
\]
\end{columns}
\end{block}
\end{frame}


\begin{frame}{Refine Model: Maximum Population $N_{*}$}

\begin{block}{Incorporate Carrying Capacity into Rate}
\bei
\i Assume  breeding rate proportional to   number of bugs:
\[
\frac{\Delta N_i}{\Delta t} = \lambda \; N_i
\]
 \i Want growth rate   $\downarrow$  as  $N_i \rightarrow N_{*}$\\*[2ex]
 \i Assume $\lambda=\lambda' (N_*-N_i)$
\[
  \Rightarrow\ \ \alert{\frac{\Delta
N_i}{\Delta t} =
\lambda'(N_{*}-N_i)N_i} \quad \quad \mbox{(Logistic Map)}
 \]
\i Small $N_i/N_*$ \imply exponential growth\\*[2ex]
\i  $N_i \rightarrow N_*$  \imply slow growth, stable, decay
\eni
\end{block}
\end{frame}

\begin{frame}{Logistic as Map in Dimensionless Variables}

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
\bei
\i   $0 \leq x_{i} \leq 1$
\i  Map: $x_{i+1} = f(x_i)$
\eni
\column{0.5\textwidth}
\bei
\i  Quadratic,  1-D map
\i $f(x) = \mu x(1-x)$
\eni
\end{columns}
\end{block}
\end{frame}


\section{Properties}
\begin{frame}{Properties of Nonlinear Maps (Theory)}

\begin{block}{Empirical Study: Plot  $x_i$ \emph{vs}  $i$}
\vspace{-5.5cm}\hspace{-1.5ex}
\pgfimage[width=4.25in]{figures/Populations.pdf}
\vspace{-6.0cm}
\bei
\i A: $\mu = \textrm{2.8}$, equilibration into single population\\*[2ex]
\i B:  $\mu = \textrm{3.3}$, oscillation between 2 population levels\\*[2ex]
\i C:  $\mu = \textrm{3.5}$ oscillation among 4 levels\\*[2ex]
\i D:    chaos
\eni
\end{block}
\end{frame}

\section{Attractors}
\begin{frame}{Fixed Points}
\begin{block}{$x_{i}$ Stays at $x_{*}$ or Returns}
\vspace{-5.5cm}\hspace{-1.5ex}
\pgfimage[width=4.0in]{figures/Populations.pdf}
\vspace{-5.5cm}
\beq
x_{i+1} = \mu x_i (1-x_i)
\enq
\vspace{-2ex}
\bei
\i  One-cycle: $x_{i+1} = x_{i} = x_{*}$
 \begin{align}
\mu x_{*} (1-x_{*}) \ = &\  x_{*}\\*[1ex]
\Rightarrow\  x_{*}  \ =&\  0, \quad   x_{*} = \frac{\mu -
1}{\mu}
 \end{align}
  \eni
  \end{block}
  \end{frame}

 \begin{frame}{Period Doubling, Attractors}
\begin{block}{Unstable via  Bifurcation into 2-Cycle}
\vspace{-5.5cm}\hspace{-1.5ex}
\pgfimage[width=4.0in]{figures/Populations.pdf}
\vspace{-5.5cm}
\bei
\i Attractors, cycle points
\i Predict:  same population generation $i$, $i+2$
 \[
x_{i} = x_{i+2} = \mu x_{i+1}(1-x_{i+1})\enskip\Rightarrow\enskip
x_{*} = \frac{1+\mu \pm \sqrt{\mu^{2}-2\mu -
3}}{2\mu}
 \]
\i   $\mu>3$: real solutions
\i Continues 1 $\rightarrow$ 2 populations
\eni
\end{block}
\end{frame}

%\section{Exercise 1}
%\begin{frame}{Exercise 1}
%\begin{block}{Produce sequence  $x_{i}$}
%\begin{enumerate}
%\i Confirm  behavior patterns A, B, C, D\\
%\i Identify the  following:
%\begin{description}
%\item [Transients ]
%\i [Asymptotes ]
%\i [Extinction ]
%\i [Stable states ]
%\i [Multiple cycles ]
%\i [Four-cycle ]
%\item [Intermittency ]   $ 3.8264 < \mu <
%3.8304$
%\i [Chaos ]  deterministic irregularity; hypersensitivity \imply nonpredictable,  $\mu = 4,\  4(1 -
%\epsilon)$
% \end{description}
%\end{enumerate}
%\end{block}
%\end{frame}

%\section{Bifurcations}
%\begin{frame}{Bifurcation Diagram}
%\begin{block}{Concentrate on Attractors}
%\begin{columns}
%\column{0.6\textwidth}
%\no \hspace{6ex}\includegraphics[width=2.25in]{figures/bugcolor2.pdf}
%\column{0.4\textwidth}
%\bei
%\i Simplicity in chaos\\*[2ex]
% \i Attractors  as   $f(\mu)$\\*[2ex]
% \i Scan $x_0$, $\mu$\\*[2ex]
%\i Let transients die\\*[2ex]
%\i Output  $(\mu,x_{*})s$\\*[2ex]
%\i $n$ cycle = $n$ values\\*[2ex]
%\i See enlargements
%\eni
%\end{columns}
%\end{block}
% \end{frame}
%
%\begin{frame}[label=current]{Detailed Bifurcation Diagram}
%\framezoom<1><2>[border](0.1cm,0.5cm)(2cm,4cm)
%\framezoom<1><3>[border](0.1cm,2cm)(2cm,2cm)
%\framezoom<1><4>[border](5cm,0.5cm)(2cm,2cm)
%
%\no\hspace{-1cm}\includegraphics[width=5.5in]{figures/bugcolorCrop.jpg}
%\end{frame}


%\begin{frame}{Bifurcation Diagram Sonification}
%  \hyperbaseurl{./}
%  \begin{block}{Play Bifurcation Diagram}
%  \begin{columns}
%  \column{0.5\textwidth}
%  \bei
%  \i  \href{figures/BUG.AU}{\alert{Hear each bifurcation}}
%  \i Each branch = one $\omega$
%  \eni
%  \column{0.5\textwidth}
%  \bei
%    \i  $\omega \propto x^*$
%  \i Bifurcation = new $\omega$, cord
%  \eni
%  \end{columns}
%\vspace{-0.85cm} \no\includegraphics[width=3.05in]{figures/bugcolor2.pdf}
%\end{block}
%\end{frame}
%
%\section{Exercise 2}
\begin{frame}[label=current]{Bifurcation Diagram }

\begin{columns}
  \column{0.5\textwidth}
\no\includegraphics[width=2.4in]{figures/bugcolor2.pdf}
  \column{0.5\textwidth}
 \bei
 \i  Can't vary intensity\\*[1ex]
 \i Vary point density\\*[1ex]
 \i Resolution $\sim$  300 DPI\\*[1ex]
 \i  $3000 \times 3000 \simeq 10^7$ pts\\*[1ex]
 \i Big, more = waste\\*[1ex]
 \i Create 1000 bins   \\*[1ex]
 \i $1 \leq \mu \leq 4$\\*[1ex]
 \i Print $x_{*}$  3-4 decimal places\\*[1ex]
 \i Remove duplicates\\*[1ex]
 \i Enlarge:  \alert{self-similarity}\\*[1ex]
 \i  Observe  windows
 \eni
 \end{columns}
 \end{frame}

%\section{Conclusion}
%\begin{frame}{Summary \& Conclusion}
%
%\begin{block}{Simplicity \& Beauty within Chaos}
%
%\bei
%\i Yes, simple discrete maps can lead to complexity\\*[1ex]
%\i Models of real world complexity\\*[1ex]
%\i Complexity related to \alert{nonlinearity} ($x^2$)\\*[1ex]
%\i Computation crucial for nonlinear systems\\*[1ex]
%\i Signals of simplicity, chaos
%\begin{description}
%\i [Bifurcation Diagram]\mbox{} \\*[1ex]
%\i  [Feigenbaum Constants]\mbox{}\\*[1ex]
%\i [Lyapunov Coefficients]\mbox{}\\*[1ex]
%\i [Shannon Entropy]\mbox{}\\*[1ex]
%\i [Fractal Dimension]
%\end{description}
%\eni
%\end{block}
%   \end{frame}




\begin{frame}[label=current]{Problem: Realistic Single or Double Pendulum}
\begin{block}{Simulate Nonlinear, Chaotic System}
 \bei
   \i Driven single pendulum \\*[1ex]
   \i Free, double pendulum
   \i Large oscillations, even over-the-top
   \eni
\vspace{-1.0in}
\begin{center}
\includegraphics[height=4.0in]{figures/BothPends.pdf}
\end{center}
\end{block}
\end{frame}

\section{ODE}

\begin{frame}{Chaotic Pendulum ODE}
\setcounter{equation}{0}

\begin{block}{Newton's Laws for Rotational Motion \hspace{3ex}  $\sum \tau \,=\, I \ \frac{d^2\theta}{dt^2}$ }

\begin{columns}
\hspace{-3cm}\column{0.3\textwidth}
\vspace{-2.5cm}
\includegraphics[height=3.5in]{figures/SinglePend.pdf}
\vspace{-3.5cm}
\column{0.7\textwidth}
\bei
 \i  Gravitation $\tau$: \hspace{1ex} $-mgl\sin\theta$\\*[1.5ex]
 \i Friction $\tau$: \hspace{3ex}  $-\beta\dot{\theta}$\\*[1.5ex]
 \i External $\tau$:\hspace{3ex}  $\tau_0\cos \,\omega t$
\eni
%------------------------------------------
 
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
\end{frame}
 
\begin{frame}{Chaotic Pendulum ODE}
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
\bei
 \i 2$^{nd}$ O t-dependent nonlinear ODE
\i Nonlinearity: \hspace{1ex} $\sin\theta \simeq \theta -\theta^3/3! \cdots$
 \i $ y^{(0)} =  \theta(t), \quad y^{(1)} = \frac{d\theta(t)}{dt}$
\eni
\end{columns}
  \begin{align}
\alert{\frac{dy^{(0)}}{dt} \ =\ }&  \alert{y^{(1)}}\\*[1.5ex]
\alert{\frac{dy^{(1)}}{dt}  \ =\  }& \alert{- \omega_{0}^{2} \sin y^{(0)} - \alpha
y^{(1)} + f\cos\omega t}
\end{align}
\end{block}
\end{frame}


\section{Free Pend}
\setcounter{equation}{0}

\begin{frame}{Start Simply: Free Oscillations (Test Algorithm \& Physics)}
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
\end{frame}

%\begin{frame}{Free Pendulum Implementation \hspace{4ex} $\ddot{\theta}  =   -\omega_{0}^{2} \sin \theta$}
%\setcounter{equation}{0}
%
%\begin{block}{Solve \hspace{4ex}ODE \hspace{4ex} with rk4}
%\begin{enumerate}
% \i
%Initial conditions: \{$\theta=0$, $\dot{\theta}(0)\neq 0$\};\  increase  $\dot{\theta}(0)$\\*[1.5ex]
% \i Verify SHM $\ \ddot{\theta}  =   -\omega_{0}^{2} \theta$ \imply $\omega=\omega_{0}= 2\pi/T$ = constant\\*[1.5ex]
%  \i
%Devise algorithm to determine period $T$ ( $3\times \theta=0$)\\*[1.5ex]
%  \i
%Determine $T(\theta)$ for realistic pendulum, compare\\*[1.5ex]
% \i
%Verify   as  $KE(0) \ \leq\ 2mgl$: non harmonic oscillations\\*[1.5ex]
% \i Verify   \imply separatrix ($KE(0) \ \rightarrow \ 2mgl$), $T\rightarrow \infty$\\*[1.5ex]
% \i Listen harmonic \& anharmonic motion \hyperbaseurl{./}
%\href{../../../Sound/index.html}{\alert{(Hear now)}}\\*[1.5ex]
% \i \hyperbaseurl{./} \href{../../../Applets/nacphy/bert/index.html}{\alert{\textit{Hear Data} applet}}
%\end{enumerate}
%\end{block}
%\end{frame}

\section{Phase Space}

\begin{frame}{Visualization: Phase Space Orbits}
\setcounter{equation}{0}

 \begin{block}{Abstract Space: $v(t)$ vs $x(t)\ $ ($x$ vs $t$, $v$ vs $t$= Complicated)}
 \vspace{-5.4cm}
\no\includegraphics[width=4.25in]{figures/Fig127Mod.pdf}
 \vspace{-5cm}
 \begin{columns}
 \column{0.45\textwidth}
 \bei
\i Geometry easy to ``see''
\i SHM: Ellipse, $E\rightarrow$ size
\i Anharmonic:  + corners
\eni
 \column{0.55\textwidth}
 \bei
 \i Ossc \imply CW Closed
 \i Non Ossc, repulse = open
\eni
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
\end{frame}

 \begin{frame}{Undriven, Frictionless Pendulum in Phase Space}
\setcounter{equation}{0}

\begin{block}{Separatrix  Separates Open \& Closed Orbits}
\centerline{\includegraphics[width=3.25in]{figures/Fig128leftMod.pdf}}
 \vspace{-1.5cm}
 \begin{columns}
 \column{0.5\textwidth}
 \bei
  \i Closed: oscillation
  \i Open: rotation
  \i Both: periodic
 \i  Orbits do not cross
\eni
 \column{0.5\textwidth}
 \bei
 \i  Open orbits touch
 \i Hyperbolic points
 \i Unstable equilibrium
\eni
\end{columns}
\end{block}
\end{frame}

 \begin{frame}{Include Friction, Driving Torque (small t steps)}
\setcounter{equation}{0}
\begin{block}{Geometry Tends to Remain}
\vspace{-3.5cm}
\includegraphics[height=4.5in]{figures/Limit.pdf}
 \vspace{-4.5cm}
 \begin{columns}
 \column{0.5\textwidth}
 \bei
 \i  Friction \imply $\downarrow$ E\\*[1.5ex]
 \i  Inward Spiral\\*[1.5ex]
 \i $\tau_{ext}$ can put $E$ back\\*[1.5ex]
\eni
 \column{0.5\textwidth}
 \bei
 \i Limit cycle = Balance \\*[1.5ex]
 \i $<\tau_{ext}> \ = \ <\mbox{friction}> $ \\*[1.5ex]
\eni
\end{columns}
\end{block}
\end{frame}


\begin{frame}{Chaos As Viewed in Phase Space (Full Solution)}
\setcounter{equation}{0}

\begin{block}{Look for in Your Simulations}
\begin{footnotesize}
\begin{columns}
 \column{0.5\textwidth}
 \includegraphics[height=1.75in]{figures/PSplotPend.pdf}
 \vspace{-0.5cm}
 \bei
  \i Complex $\leq$ Chaos $\leq$ Rand\\*[1.5ex]
  \i Fixed Params, all $x_0$, $t$s:  flows \\*[2.0ex]
 \eni
 \column{0.5\textwidth}
\bei
 \i Chaos complex $\neq$ mess\\*[2.0ex]
 \i Figs distort, remains\\*[2.0ex]
 \i Closed = periodic \\*[2.0ex]
 \i Simplicity in chaos [PS, $\neq \theta(t)$]\\*[2.0ex]
  \i $\rightarrow$ attractors (return)\\*[2.0ex]
  \i Random = cloud fill $E$ \\*[2.0ex]
  \i \alert{Bands} \imply continuity, sequential\\*[2.0ex]
  \i \imply hypersensitive $\theta(t)$\\*[2.0ex]
  \i Tools measure chaos\\*[2.0ex]
 \eni
 \end{columns}
 \end{footnotesize}
 \end{block}
\end{frame}



%\begin{frame}{Examples of What You Should See}
%\setcounter{equation}{0}
%
%\begin{block}{Applets of Pendulums in Phase Space (Hans Kowallik)}
%\begin{columns}
%\column{0.6\textwidth}
%\bei
%\i Do with your program (text path)\\*[2ex]
%\i Reproduce standard features\\*[2ex]
%\i Beware: 4-D parameter space\vspace{-1cm}\\
%\includegraphics[height=1.75in]{figures/SinglePend.pdf}
%\vspace{-1.5cm}
%\i \hyperbaseurl{./}
%\href{../../../Applets/nacphy/JAVA_pend/COMP/index.html}{\alert{Complicated Behavior Applet}}\\*[2ex]
%\i \hyperbaseurl{./}
%\href{../../../Applets/nacphy/JAVA_pend/CHAOS/index.html}{\alert{Chaos Comparison Applet}}\\*[2ex]
%\eni
%\column{0.4\textwidth}
%\begin{figure}\includegraphics[height=2.0in]{figures/PendApplets.pdf}\end{figure}
%\end{columns}
%\end{block}
%\end{frame}
%
%\begin{frame}{Assessment in Phase Space}
%\setcounter{equation}{0}
%
%\begin{block}{Start with Free Pendulum As Your Lab}
%\vspace{-1.5ex}
%\begin{columns}
%\column{0.5\textwidth}
%\bei
% \i Add friction: spirals\\*[1.25ex]
% \i Small $\tau_{ext}$ ($\sim$ellipse)\\*[1.25ex]
%  \i $\omega \simeq \omega_0$, beats\\*[1.25ex]
%  \i NL resonance  ($\phi$ matters)\\*[1.25ex]
% \i ID transients, 1, 2, 3  cycle\\*[1.25ex]
% \i ID running solutions\\*[1.25ex]
% \i Explore chaos (small $h$)\\*[1.25ex]
% \i ID  hypersensitive details  \\*[1.25ex]
%  \i OK not reproduce us\\*[1.25ex]
% \eni
% \column{0.5\textwidth}
% \begin{figure}\includegraphics[height=2.4in]{figures/figure1210c.jpg}
% %\includegraphics[height=2.4in]{figures/Fig1210Mod.pdf}
% \end{figure}
% \end{columns}
% \end{block}
% \end{frame}
%
%\section{Bifurcations}
%
%\begin{frame}{Bifurcations of Chaotic Pendulum}
%\setcounter{equation}{0}
%
%\begin{block}{How \& When Do $\omega_i$s Occur?}
%\vspace{-1.5ex}
%\begin{columns}
%\column{0.45\textwidth}
%\bei
% \i Saw bugs bifurcate\\*[1.25ex]
% \i Saw pendulum  jump  $\omega_i$ \\*[1.25ex]
%  \i \imply  $\omega_i$ sequential\\*[1.25ex]
%  \i Linear: $\omega_i$ simultaneous\\*[1.25ex]
% \i For 150 $t_i$ plot $(|\dot{\theta}(t_i)|, f)$\\*[1.25ex]
% \i Samples instantaneous $\dot{\theta}=d\theta/dt$\\*[1.25ex]
% \i Dominant $\omega_i$ = attractors\\*[1.25ex]
% \eni
% \column{0.55\textwidth}
% \vspace{-2cm}\begin{figure}
% \includegraphics[height=2in]{figures/SinglePSpend.pdf}\\
% \vspace{-2cm}\includegraphics[height=1.75in]{figures/BifurPend.pdf}
% \end{figure}
% \end{columns}
% \end{block}
%\end{frame}




\section{Double Pendulum}
\begin{frame}{Double Pendulum: Alternative Problem}
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
\bei
\i No small-$\theta$\\*[1.5ex]
\i Coupling = extra degree freedom\\*[1.5ex]
\i Small $\theta$: in-$\phi$, out-$\phi$
\eni
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
\end{frame}

\begin{frame}{Double Pendulum: Bifurcations}
\vspace{-8cm}
 \begin{figure}
 \centerline{\includegraphics[width=17pc]{figures/DoublePend.pdf} \vspace{-10cm}
 \includegraphics[width=20pc]{figures/DoublePendBifur.pdf} }
\end{figure}
\end{frame}


%\begin{frame}  {Double Pendulum: Movies In-Phase, Out-Phase}
%\includemovie[poster,controls,text={loading mode1}] {5.0cm}{6.0cm}{./figures/Movies/mode1.mpg}
%\includemovie[poster,controls,text={loading mode2}] {5.0cm}{6.0cm}{./figures/Movies/mode2.mpg}
%\end{frame}
%
%\begin{frame} [label=current]{Double Pendulum: Movie: Combined Large Oscillation}
%
%\includemovie[poster,controls,text={loading neat}] {8.0cm}{6.0cm}{./figures/Movies/neat.mpg}
%\end{frame}


\section{Homework}

\begin{frame}{Homework 10}{Due 3/24/2013, 11:59pm}
Complete Problem Set 10. Turn in via CourseWeb:\\
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
\item The Python file \texttt{ps\_10.py} which generates the required results.
\vfill
\end{enumerate}
\end{frame}

%\end{document}


