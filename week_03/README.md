# Computational methods in Physics
## Week 3
#### Prof. Michael Wood-Vasey
##### University of Pittsburgh, Department of Physics and Astronomy


\title[PHYS 1321] % (optional, use only with long paper titles)
{Computational Methods in Physics}

\subtitle{PHYS 1321: Notes and Homework}

\author[] % (optional, use only with lots of authors)
{Prof. Brian D'Urso}

\institute{University of Pittsburgh\\ Department of Physics and Astronomy}

\date[Week 3]{Week 3}


\begin{document}

\lstset{language=Python, basicstyle=\footnotesize\ttfamily}

\begin{frame}
  \titlepage
\end{frame}

\section<article>{PHYS 1321: Notes and Homework \hfill Week 3}
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


\section{Random Numbers}

\begin{frame}{Deterministic Randomness}  
Some problems appear physically uncertain. Examples:
\begin{itemize}
\item thermal motion
\item games of chance
\item radioactive decay
\end{itemize}
\vspace{5mm}
How do we deal with randomness numerically?
\begin{itemize}
\item Computers are deterministic; no chance involved.
\item Always same output for same input; unless error.
\item Generate pseudo-random numbers.
\item Monte Carlo calculations: simulate random events.
\begin{itemize}
\item Solve equations statistically
\item Solve intractable problems
\end{itemize}
\end{itemize}
\end{frame}


\begin{frame}[fragile=singleslide]
\frametitle{Drawing Random Numbers}
\begin{itemize}
\vfill
\item Python has a random module for drawing random numbers
\vfill
\item \verb$random.random()$\\ 
draws random numbers in $[0, 1)$:\\
\verb$>>> import random$\\
\verb$>>> random.random()$\\
\verb$0.81550546885338104$\\
\verb$>>> random.random()$\\
\verb$0.44913326809029852$\\
\verb$>>> random.random()$\\
\verb$0.88320653116367454$\\
\vfill
\item The sequence of random numbers is produced by a
deterministic algorithm - the numbers just appear random.
\vfill
\end{itemize}
\end{frame}


\begin{frame}[fragile=singleslide]
\frametitle{Distributions of Random Numbers}
\begin{itemize}
\vfill
\item \verb$random.random()$ generates random numbers that are uniformly
distributed in the interval $[0, 1)$.
\vfill
\item \verb$random.uniform(a, b)$ generates random numbers uniformly
distributed in $[a, b)$.
\vfill
\item ``Uniformly distributed'' means that if we generate a large set
of numbers, no part of $[a, b)$ gets more numbers than others.
\vfill
\item See \verb$random_distribution$ demo.
\vfill
\end{itemize}
\end{frame}


\begin{frame}[fragile=singleslide]
\frametitle{Vectorized Drawing of Random Numbers}
\begin{itemize}
\vfill
\item \verb$random.random()$ generates one number at a time
\verb$r = random.random() # one number$\\
\verb$r = random.uniform(-1, 10) # one number$
\vfill
\item \verb$numpy$ has a random module that efficiently generates a (large)
number of random numbers at a time:\\
\verb$import numpy as np$\\
\verb$r = np.random.random(size=1000) # array$\\
\verb$r = np.random.uniform(-1, 10, size=1000) # array$
\vfill
\item Vectorized calculations are important for speeding up programs!
\vfill
\end{itemize}
\end{frame}


\begin{frame}[fragile=singleslide]
\frametitle{Drawing Integers}
\begin{itemize}
\vfill
\item Quite often we want to draw an integer from $[a, b]$ and not a
real number.
\vfill
\item Python's \verb$random$ module and \verb$numpy.random$ have functions for
drawing uniformly distributed integers:
\vfill
\verb$import random$\\
\verb$r = random.randint(a, b) # a, a+1, ..., b$\\
\vfill
\verb$import numpy as np$\\
\verb$# b+1 is not included$\\
\verb$r = np.random.randint(a, b+1, N)$\\
\verb$# b is included$\\
\verb$r = np.random.random_integers(a, b, N)$
\vfill
\end{itemize}
\end{frame}


\begin{frame}[fragile=singleslide]
\frametitle{Example: Throwing a Die; Vectorized Version}
\begin{itemize}
\vfill
\item \verb$import numpy as np$\\
\verb$N = 10$\\
\verb$eyes = np.random.randint(1, 7, N)$\\
\verb$# True/False array$\\
\verb$success = eyes == 6$\\
\verb$# treats True as 1, False as 0$\\
\verb$six = np.sum(success)$\\
\verb$print 'Got six %d times out of %d' % (six, N)$
\vfill
\item Important: use \verb$sum$ from \verb$numpy$ and not Python's built-in \verb$sum$ function! (The latter is slow.)
\vfill
\end{itemize}
\end{frame}


\begin{frame}[fragile=singleslide]
\frametitle{Fixing the Seed Fixes the Random Sequence}
\begin{itemize}
\vfill
\item Debugging programs with random numbers is difficult because
the numbers produced vary each time we run the program.
\vfill
\item For debugging it is important that a new run reproduces the
sequence of random numbers in the last run.
\vfill
\item This is possible by fixing the seed of the random module:\\
\verb$random.seed(121) # int argument$
\vfill
\item Or the numpy module:
\verb$np.random.seed(121) # int argument$
\vfill
\item The value of the seed determines the random sequence:
\verb$import numpy as np$\\
\verb$np.random.seed(2)$\\
\verb$np.random.random(3)$
\vfill
\item By default, the seed is based on the current time.
\vfill
\end{itemize}
\end{frame}


\begin{frame}[fragile=singleslide]
\frametitle{Distributions of Random Numbers}
\begin{itemize}
\vfill
\item Sometimes we want uniformly distributed random numbers,
and sometimes not.
\vfill
\item Example: it is more likely have normal (mean) blood pressure
than large deviations from the mean.
\vfill
\item We can use the Gaussian or normal distribution to get random
numbers clustered around a mean value:\\
\verb$import random$\\
\verb$r = random.normalvariate(m, s)$\\
\verb$m$: mean value, \verb$s$: standard deviation
\vfill
\item Vectorized drawing of $N$ Gaussian/normal numbers:\\
\verb$import numpy as np$\\
\verb$samples = np.random.normal(m, s, N)$
\vfill
\item We are using mostly uniformly distributed numbers.
\vfill
\end{itemize}
\end{frame}


\begin{frame}[fragile=singleslide]
\frametitle{Probability via Monte Carlo Simulation}
\begin{itemize}
\vfill
\item What is the probability that a certain event A happens?
\vfill
\item Simulate $N$ events, count how many times $M$ the event $A$
happens, the probability of the event $A$ is then $M/N$ (as
$N \rightarrow \infty$).
\vfill
\item Example: what is the probability of getting 6 on two or more
dice if we throw 4 dice?\\
\verb$N = 100000 # no of experiments$\\
\verb$M = 0 # no of successful events$\\
\verb$for i in range(N):$\\
\verb$    six = 0 # count the no of dice with a six$\\
\verb$    r1 = random.randint(1, 6)$\\
\verb$    if r1 == 6: six += 1$\\
\verb$    ... same for dice 2, 3 and 4 ...$\\
\verb$    # successful event?$\\
\verb$    if six >= 2:$\\
\verb$        M += 1$\\
\verb$print 'probability:', float(M)/N$
\vfill
\end{itemize}
\end{frame}


\section{Random Walks}

\begin{frame}[fragile=singleslide]
\frametitle{Random Walk in One Spatial Dimension}
\begin{itemize}
\vfill
\item A particle moves to the left and right with equal probability
\vfill
\item $n$ particles start at $x = 0$ at time $t = 0$ - how do the particles
get distributed over time?
\vfill
\item This is called random walk and constitutes a simple model for
molecular motion.
\begin{itemize}
\item heat transport
\item quantum mechanics
\item polymer chains
\item population genetics
\item pricing of financial instruments
\item \ldots
\end{itemize}
\vfill
\item We'll make a program for simulating random walk.
\vfill
\end{itemize}
\end{frame}


\begin{frame}[fragile=singleslide]
\frametitle{Random Walk as a Difference Equation}
\begin{itemize}
\vfill
\item Let $x_n$ be the position of one particle at time $n$.
\vfill
\item Updating rule: $x_{n+1} = x_n + s$\\
where $s = 1$ or $s = -1$, both with probability $1/2$.
\vfill
\item For $n_p$ particles, we need $n_p$ such difference equations.
\vfill
\item Would like to calculate the statistics (mean position, ``width'' of the cluster of particles, how particles are distributed throughout space).
\vfill
\item Random walk in 2-D:
\begin{itemize}
\item $x_{n+1} = x_n + r_x$
\item $y_{n+1} = y_n + r_y$
\item $r_x = r \cos\theta$, $r_y = r \sin\theta$, with random $\theta$
\end{itemize}
\end{itemize}
\end{frame}


\begin{frame}[fragile=singleslide]
\frametitle{How Far After $N$ Steps (in 2-D)?}
\begin{itemize}
\vfill
\item Start at $(x, y) = (0, 0)$.
\vfill
\item After $N$ steps:\\
$R^2 = (\Delta x_1 + \cdots + \Delta x_N)^2 + (\Delta y_1 + \cdots + \Delta y_N)^2$
\vfill
\item Expand:\\
$R^2 = \Delta x_1^2 + \cdots + \Delta x_N^2 + 2 \Delta x_1 \Delta x_2 + \cdots  
+ \Delta y_1^2 + \cdots + \Delta y_N^2 + 2 \Delta y_1 \Delta y_2 + \cdots$
\vfill
\item Cross terms average to zero:\\
$R^2 \simeq \Delta x_1^2 + \cdots + \Delta x_N^2 + \Delta y_1^2 + \cdots + \Delta y_N^2$
\vfill
\item $\Rightarrow R^2 \simeq N \langle r^2 \rangle$
\vfill
\item $\Rightarrow R \simeq \sqrt{N} r_{RMS}$
\vfill
\end{itemize}
\end{frame}


\section{Radioactive Decay}
\begin{frame}[fragile=singleslide]
\frametitle{Spontaneous (e.g. Radioactive) Decay}
\begin{itemize}
\vfill
\item ``Spontaneous'' process $\rightarrow$ no external stimulus.
\vfill
\item Time of decay is random, independent of:
\begin{itemize}
\item How long it existed.
\item How many other are around.
\end{itemize}
\vfill
\item Describes nuclear decay, electronic relaxation, etc.
\vfill
\item Theory: probability of decay per $\Delta t$ per particle is:\\
\vfill
$P(t)=\lambda$ (constant)\\
\vfill
$\Rightarrow$ $N(t)$, $dN/dt$ decrease with time.
\vfill
\end{itemize}
\end{frame}


\begin{frame}[fragile=singleslide]
\frametitle{Model: Continuous Decay}
\begin{itemize}
\vfill
\item If $N\rightarrow \infty$, $\Delta t \rightarrow 0$:\\
\vfill
$\frac{\Delta N(t)}{\Delta t} \rightarrow \frac{dN(t)}{dt} = -\lambda N(t)$
\vfill
\item Can integrate differential equation:\\
\vfill
$N(t) = N(0) e^{-\lambda t} = N(0) e^{-t/\tau}$\\
\vfill
with $\lambda = 1/\tau$
\vfill
\item $\frac{dN}{dt}(t) = -\lambda N(0) e^{-\lambda t} = \frac{dN}{dt}(0) e^{-t/\tau}$
\vfill
\item But this is an approximation!\\
Nature can have small $N$, stochastic behavior.
\vfill
\end{itemize}
\end{frame}


\begin{frame}[fragile=singleslide]
\frametitle{Method: Decay Simulation}
\begin{itemize}
\vfill
\item Algorithm:\\
\vfill
Loop through remaining nuclei\\
\vfill
$r_i < \lambda$? $\Rightarrow$ decays\\
\vfill
$t = t + \Delta t$\\
\vfill
Repeat loop
\vfill
\item $r_i$ is random number in $[0, 1]$.
\vfill
\item Higher $\lambda\Rightarrow$ more frequent decays.
\vfill
\item See \verb$decay_simulator$ demonstration.
\vfill
\end{itemize}
\end{frame}


\section{Homework}
\begin{frame}{Homework 3}{Due 1/27/2013, 11:59pm}
Complete Problem Set 3. Turn in via CourseWeb:\\
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
\item The Python file \texttt{ps\_3.py} which generates the required results.
\vfill
\end{enumerate}
\end{frame}


%\end{document}


