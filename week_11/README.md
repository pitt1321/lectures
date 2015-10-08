# Computational methods in Physics
## Week 11
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

\date[Week 11]{Week 11}


\begin{document}

\lstset{language=Python, basicstyle=\footnotesize\ttfamily}

\begin{frame}
  \titlepage
\end{frame}

\section<article>{PHYS 1321: Notes and Homework \hfill Week 11}
\subsection<article>{Computational Methods in Physics}
\mode<article>{\vspace{3mm} \hrule \vspace{5mm}}


\begin{frame}
\frametitle<presentation>{Contents}
\tableofcontents
\end{frame}


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


\section{Magnets}

\begin{frame}{\textbf{Problem:} Explain  Thermal Behavior of Ferromagnets}

\pause\begin{block}{What are Magnets and How Do They Behave?}

  \begin{figure}
\centerline{\includegraphics[width=3.0in]{figures/Domains.pdf}
\includegraphics[width=0.85in]{figures/NdFeB-Domains.pdf}}
\end{figure}
\vspace{-1cm}
\bei
\i \pause Ferromagnets $= \sum$ finite \alert{domains} \\*[2ex]
\i  \pause Domain: all   atoms' spins aligned\\*[2ex]
\i  \pause External $\vec{B}$:  align domains \imply \alert{magnetized}\\*[2ex]
\i  \pause $T\ \uparrow: \ \sum$  magnetism $\downarrow$ (spins flip?)\\*[2ex]
\i  \pause @ $T_{curie}$: \alert{phase transition},  $\vec{M} \ =\ 0$ \\*[2ex]
\eni
\end{block}
\end{frame}

\section{Ising Model}

\begin{frame}{Ising Model:  $N$ Magnetic Dipoles on Linear Chain }

\uncover<2->{\begin{block}{Constrained Many Body Quantum System}}
\begin{figure}
\centerline{\uncover<2->{\includegraphics[width=1.75in]{figures/figure151c.pdf}}}
\end{figure}
\vspace{-3ex}
\begin{columns}
\column{0.5\textwidth}
\bei
\uncover<3->{ \i Same model 2-D, 3-D}
\uncover<4->{ \i Fixed \imply no movements}
\uncover<5->{\pause \i Spin dynamics\\*[2ex]}
\eni
 \column{0.5\textwidth}
 \bei
\uncover<6->{\i Particle $i$,  spin}
\uncover<7->{\i $s_{i} \equiv  s_{z,i} = \pm \frac{1}{2}$}
\uncover<8->{\i  $\Psi$:   $N$ spin values\\*[2ex]}
\eni
\end{columns}
\vspace{2ex}
\begin{footnotesize}
 \uncover<2->{\[
\left|\alpha_{j}\right \rangle  = \left|s_{1}, s_{2}, \ldots ,
s_{N} \right \rangle = \left\{\begin{array}{@{}c@{}} \displaystyle
\pm\frac{1}{2},\end{array}
\begin{array}{c}
 \displaystyle \pm\frac{1}{2},
\end{array}   \ldots \right\}, \quad
j=1,\ldots, 2^{N}
 \]}
 \end{footnotesize}
\end{block}
\end{frame}

\begin{frame}{Ising Model Continued}

\begin{block}{Quantum Interaction of $N$ Magnetic Dipoles}
%\begin{footnotesize}
%\end{footnotesize}
\begin{columns}
\column{0.45\textwidth}
%\vspace{-1ex}
\begin{figure}
\centerline{\includegraphics[width=1.75in]{figures/figure151c.pdf}}
\end{figure}
\vspace{-4ex}
\bei
\i $s_i = \uparrow, \downarrow$ \imply  $2^{N}$  states\\*[1.5ex]
\i Fixed \imply no exchange\\*[1.5ex]
\i Energy: $\vec{\mu}\cdot\vec{\mu}$ +  $\vec{\mu}\cdot\vec{B}$\\*[1.5ex]
\i $J$ = \alert{exchange energy}
\eni
\column{0.55\textwidth}
\[
\alert{V_{i} = - J\vec{s}_{i}\cdot\vec{s}_{i+1} - g \mu_b\,
\vec{s}_{i}\cdot \vec{B}}
\]
 \bei
 \i $J>0$:  \alert{ferromagnet} $\uparrow\uparrow\uparrow$\\*[1.5ex]
 \i $J<0$:    \alert{antiferromagnet} $\uparrow\downarrow\uparrow\downarrow$\\*[1.5ex]
\i    $g$ = gyromagnetic ratio \\*[1.5ex]
\i $\vec{J} = g \vec{\mu}$\\*[1.5ex]
\i  $\mu_b = e\hbar/(2m_ec)$ \\*[1.5ex]
\eni
\end{columns}
\end{block}
\end{frame}

\begin{frame}{Many Body Problem ($N\ \geq \ 2, 3$ Unsolved)}
\pause \begin{block}{Beyond $N = $ 2, 3 Use Statistics, Approximations}
\begin{columns}
\column{0.5\textwidth}
\vspace{-0.5cm}
\begin{figure}
\centerline{\includegraphics[width=1.0in]{figures/figure151c.pdf}}
\end{figure}
\vspace{-5ex}
\bei
\pause \i   $2^{N}\ \rightarrow$ large  ($2^{20} > 10^6$)\\*[1.5ex]
\pause \i $10^{23}$: hah!\\*[1.5ex]
\pause \i $B_{ext}\rightarrow 0$ \imply no direction \\*[1.5ex]
 \pause \i \imply $<\vec{M}> = 0$ \\*[1.5ex]
 \pause \i Yet  spins aligned??\\*[1.5ex]
 \pause \i  Spontaneous reversal\\*[1.5ex]
\eni
\column{0.5\textwidth}
\begin{footnotesize}
 \[
E_{\alpha_k} =  -J \sum_{i=1}^{N-1} s_{i}s_{i+1} - B
\mu_b\sum_{i=1}^{N} s_{i}
 \]
 \end{footnotesize}
\bei
\pause \i Not equilibrium \alert{approach} \\*[1.5ex]
\pause \i  \alert{Curie Temperature:} $\vec{M}(T>T_c) \equiv 0$ \\*[1.5ex]
\pause \i $T<T_c$:  quantum  macroscopic order\\*[1.5ex]
\pause \i 1D: no phase transition \\*[1.5ex]
\eni
\end{columns}
\end{block}
\end{frame}


\section{Stat Mech}

\begin{frame}{Statistical Mechanics (Theory)}

\begin{block}{Microscopic Origin of Thermodynamics}
\bei
\i \pause Basis:  all configurations which satisfy constraints possible
\i \pause \emph{Microcanonical Ensemble}:  \alert{energy}  fixed
\i \pause \emph{Canonical Ensemble}: (here) $T,\ V,\ N$ fixed, not $E$
\i \pause \alert{``At temperature $T$'':} \ equilibrium  $\langle E\rangle \propto T$
\i \pause Equilibrium $\nRightarrow$ static  $\Rightarrow$ continual random fluctuates
\i \pause Canonical ensemble:  $E_{\alpha}$  vary via Boltzmann ($k_B$):
 \eni
 \begin{columns}
\column{0.5\textwidth}
\vspace{-0.5cm}
\begin{figure}
\centerline{\includegraphics[width=1.0in]{figures/figure151c.pdf}}
\end{figure}
\column{0.5\textwidth}
\vspace{-1ex}
   \begin{footnotesize}
  \pause \begin{align*}
\alert{\protect{\cal P}(E_{\alpha},T)\ =}&\  \alert{\frac{e^{-E_{\alpha}/k_BT}}
{Z(T)}}\\*[2ex]
Z(T)\ =&\ \sum_{\alpha}e^{-E_{\alpha}/k_BT}
 \end{align*}
 \end{footnotesize}
 \end{columns}
\bei
\pause \i Sum: individual states, not $g(E_{\alpha})$  weighted sum
\eni
\end{block}
\end{frame}

\section{Analytic}

\begin{frame}{Analytic Solutions $N\ \rightarrow\ \infty$ Ising Model}

  \textbf{1-D Ising}
  \begin{footnotesize}
\begin{eqnarray}
&\displaystyle  U = \langle E \rangle &\\[3pt]
 &\displaystyle   \frac{U}{J} = - N \tanh \frac{J}{k_BT} =
-N\frac{e^{J/k_BT} -e^{-J/k_BT}}{e^{J/k_BT}+e^{-J/k_BT}}   =
 \begin{cases}
   N, &   k_BT\rightarrow 0 ,\\[6pt]
   0, &   k_BT\rightarrow \infty \end{cases}&
\end{eqnarray}
  \begin{eqnarray}
M(k_BT) & = &   \frac{N e^{J/k_BT}\sinh (B/k_BT)}{
\sqrt{e^{2J/k_BT}\sinh^2(B/k_BT) + e^{-2J/k_BT}} } .
 \end{eqnarray}
  \textbf{\large 2-D Ising}
   \begin{eqnarray}
 \protect{\cal M}(T) &=& \begin{cases} 0, &  T>T_c\\[8pt]
   \frac{(1+z^2)^{1/4}(1-6z^2+z^4)^{1/8}} {\sqrt{1-z^2}}, &   T<T_c
   ,\end{cases}\\[4pt]
k T_c &\ \simeq\ & 2.269185 J, \quad z= e^{-2J/k_BT},
   \end{eqnarray}
  \end{footnotesize}
\end{frame}

\section{Metropolis}

\begin{frame} {Metropolis Algorithm (A Top 10 Pick)}

\begin{block}{Basic Concepts (Mystery That It Works)}
\bei
\pause \i Boltzmann $\ \nRightarrow\ $ system remain  lowest $E$ state\\*[1.5ex]
\pause \i Boltzmann \imply  higher $E$ less likely than lower $E$\\*[1.5ex]
\pause \i $T \rightarrow 0$: only lowest $E$\\*[2ex]
\pause \i Finite $T$: $\ \Delta E \ \sim \ k_BT$  fluctuations $\sim$  equilibrium\\*[1.5ex]
\pause \i Metropolis,  Rosenbluth, Teller \& Teller: $n$ transport\\*[1.5ex]
\pause \i Clever way improve Monte Carlo averages\\*[1.5ex]
\pause \i Simulates thermal equilibrium fluctuations\\*[1.5ex]
\pause \i Randomly change spins,   $\langle$follows$\rangle\ \simeq$ Boltzmann\\*[1.5ex]
\pause \i Combo:   variance reduction \& von Neumann rejection\\*[1.5ex]
\pause \i Random, most likely predominant\\*[1.5ex]
\eni
\end{block}
\end{frame}

\begin{frame}{Metropolis Algorithm Implementation}

\begin{block}{Number of Steps, Multiple Paths to Equilibrium Configuration}

\begin{enumerate}
\pause \i
Start: fixed $T$,  arbitrary $\alpha_{k}=\{s_1,
s_2, \ldots, s_N\}, E_{\alpha_k}$\\*[1.25ex]

\pause \i  Trial:   flip random spin(s), calculate $E_{trial}$\\*[1.25ex]


\pause \i
If $E_{trial} \leq E_{\alpha_{k}}$, accept: $\alpha_{k+1} = \alpha_{trial}$\\*[1.25ex]

\pause \i
If $E_{trial} > E_{\alpha_k}$, accept + relative probable $\protect{\cal R}
= e^{-\frac{\Delta E}{k_BT}}$:\\*[1.25ex]

\begin{itemize}
\pause \i    Choose  uniform  $0 \leq r_i \leq 1$
\pause \i    \begin{footnotesize} Set $\alpha_{k+1} =    \begin{cases}
\alpha_{trial}, & \mbox{if} \ \ \protect{\cal R} \geq r_j  \ \
\mbox{(accept)},\\[6pt]
\alpha_{k}, & \mbox{if}\ \ \protect{\cal R} < r_j \ \
\mbox{(reject)}.
\end{cases}$\end{footnotesize}
 \end{itemize}
 \pause \i Iterate, equilibrate (wait ${\simeq}10N$)\\*[1.25ex]

 \pause \i Physics = fluctuations $\rightarrow$ $M(T)$, $U(T)$\\*[1.25ex]

 \pause \i Change $T$, repeat\\*[1.25ex]

\end{enumerate}
\end{block}
\end{frame}


\begin{frame}{Metropolis Algorithm Implementation (\texttt{\small IsingViz.py})}
\begin{block}{}
\begin{figure}
\centerline{\includegraphics[width=1.75in]{figures/figure152c.pdf} }
\end{figure}
\vspace{-2.5ex}
\begin{columns}
\column{0.45\textwidth}
\vspace{-0.75cm}
\begin{itemize}
\pause \i Hot start: random
\pause \i Cold start: parallel, anti
\pause \i $>10N$ iterates no matter
\pause \i More averages better
 \i
Data structure = \texttt{\small s[N]}
\pause \i Print   $+$, $-$  ea site
\pause \i  Periodic BC
\end{itemize}
\column{0.55\textwidth}
\vspace{-1cm}
\begin{itemize}
\pause \i  1st $J=k_BT=1$, $N \leq 20$
\pause \i  Watch equilibrate: $\Delta$ starts
\pause \i  Large flucts: $\uparrow$ $T$, $\downarrow$ $N$
\pause \i Large $k_BT$: instabilities
\pause \i Small $k_BT$: slow equilibrate
\pause \i  Domain formation \& total $E$ ($E>0$: $\uparrow\downarrow$, $\downarrow\uparrow$)
\end{itemize}
\end{columns}
\end{block}
\end{frame}

\begin{frame}{Calculate Thermodynamic Properties
}%\no\hyperbaseurl{./}
%\href{run:../../eBookWorking/Codes/PythonCodes/VIsing28Nov09.py}{
%\includegraphics[scale=0.1]{BeamerFigs/PythonCode1.pdf}}
%\hyperbaseurl{./}
%\href{../../eBookWorking/html/Ising.html}{
%\includegraphics[scale=0.2]{BeamerFigs/Code2.pdf}}}

\begin{block}{Average in Equilibrium 100 spins}
\begin{figure}
\centerline{\includegraphics[width=18pc]{figures/figure153cMod.pdf}
}
\end{figure}
\vspace{-0.5cm}
%\begin{footnotesize}
\[
\uncover<2->{E_{\alpha_j} = - J\sum_{i=1} ^{N-1} s_{i}s_{i+1}},
\quad\quad \uncover<3->{{\cal M}_{j} =  \sum_{i=1}^{N} s_{i}},  \quad\quad \uncover<4->{C_{simple}  =    \frac{1}{N} \frac{d\langle E \rangle}{dT}}
\]
%\end{footnotesize}
\begin{columns}
\column{0.5\textwidth}
\bei
\uncover<5->{\i  $\vec{M}(k_bT \rightarrow \infty) \rightarrow 0$}
\eni
\column{0.5\textwidth}
\bei
\uncover<6->{\i $\vec{M}(k_bT \rightarrow 0) \rightarrow N/2$}
\eni
\end{columns}
\end{block}
\end{frame}


\begin{frame}{Simulated Annealing}
Adapt the Metropolis Algorithm to ``solve'' \\
optimization problems.
\begin{itemize}
\vfill
\item Try to minimize an ``energy'' (or ``cost'') function $f$ over some parameter range or some space.
\vfill
\item Take Metropolis steps, starting at high $T$ and slowly decreasing $T$.
\vfill
\item The ``solution'' forms as the system cools - similar to annealing a metal.
\vfill
\item Not guaranteed to give global minimum.
\vfill
\item Can solve some problems with few other approaches.
\vfill
\item Easy to implement.
\vfill
\item Application: the ``Traveling Salesman'' problem.
\end{itemize}
\end{frame}


\section{Homework}

\begin{frame}{Homework 11}{Due 3/31/2013, 11:59pm}
Complete Problem Set 11. Turn in via CourseWeb:\\
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
\item The Python file \texttt{ps\_11.py} which generates the required results.
\vfill
\end{enumerate}
\end{frame}


%\end{document}


