# Computational methods in Physics
## Week 9
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

\date[Week 9]{Week 9}


\begin{document}

\lstset{language=Python, basicstyle=\footnotesize\ttfamily}

\begin{frame}
  \titlepage
\end{frame}

\section<article>{PHYS 1321: Notes and Homework \hfill Week 9}
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


\section[Transforms]{Analytical Fourier Series and Transforms}

\begin{frame}{Fourier Series}
For a periodic function $y(t)$ with period $T$:
\begin{equation*}
y(t) = \frac{a_{0}}{2} + \sum_{n=1}^{\infty} \left(a_{n} \cos
n\omega t + b_{n} \sin n\omega t
\right)
\end{equation*}
\vfill
The Fourier coefficients can be determined with:
\begin{equation*}
{a_n\choose b_n}  =\frac{2}{T} \int _{0}^{T} dt {\cos n\omega
t\choose \sin n\omega t} y(t)
\end{equation*}
\vfill
Notes:
\begin{itemize}[<+->]
\vfill
\item $a_{0} = 2 \left\langle y(t)\right\rangle$, $b_{0} = 0$.
\vfill
\item If $y(t)$ odd: $y(-t) = - y(t)$  \ $\Rightarrow$ \ $a_{n} \equiv 0$.
\vfill
\item If $y(t)$ even: $y(-t) = y(t)$ \ $\Rightarrow$ \ $b_{n} \equiv 0$.
\end{itemize}
\end{frame}


\begin{frame}{Fourier Transforms}
For a function $y(t)$ defined at all times:
\begin{equation*}
y(t)=\int_{-\infty}^{+\infty} d\omega\ Y(\omega)\, \frac{e^{+i\omega t}} {\sqrt{2\pi}}
\end{equation*}
\vfill
Fourier transform $Y(\omega)$ can be determined with:
\begin{equation*}
Y(\omega)=\int_{-\infty}^{+\infty} dt\, \, y(t)\, \frac{e^{-i\omega t}} {\sqrt{2\pi}}
\end{equation*}
\vfill
Notes:
\begin{itemize}
\vfill
\item If $y(t)$ odd and real: $y(-t) = - y(t)$  \ $\Rightarrow$ \ $Y(\omega)$ is imaginary. 
\vfill
\item If $y(t)$ even and real: $y(-t) = y(t)$ \ $\Rightarrow$ \ $Y(\omega)$ is real.
\vfill
\item If $y(t)$ is purely real $\Rightarrow Y(-\omega)=\overline{Y(\omega)}$.
\vfill
\item Power Spectrum: $\propto \left| Y(\omega)\right|^{2}$, maybe $\log_{10}\left|Y\right|^{2}$.
\end{itemize}
\end{frame}



\section[]{Discrete Fourier Transforms (DFT)}

\begin{frame}{Discrete Fourier Transforms (DFT)}
For numerical evaluation, we have to use a finite range for $t$ \\
and $N$ discrete samples of $y(t)$:
\begin{itemize}
\vfill
\item $y_{k} = y(t_{k})$, $k = 0, 1,\ldots, N-1$.
\vfill
\item Uniform time steps $\Delta t \rightarrow t_{k} = k \Delta t$.
\vfill
\item Assume periodicity $y(t+T) = y(t)$, $T=N\Delta t$.
\end{itemize}
\vfill
The DFT will give us $Y(\omega)$ at $N$ discrete values $Y_k=Y(\omega_k)$:
\begin{itemize}
\vfill
\item $\omega_k = k \Delta \omega, \qquad k = 0, 1, \ldots , N-1$.
\vfill
\item $\Delta \omega = \frac{2\pi}{T}=\frac{2\pi}{N\Delta t}$.
\vfill
\item $Y(\omega_k)$ is also periodic: $Y(\omega_{n+N})=Y(\omega_{n})$,\\
	so we can also shift the range of $k$.
\end{itemize}
\end{frame}


\begin{frame}{Discrete Fourier Transforms (DFT)}
The formula for the forward DFT is:
\begin{equation*}
Y(\omega_{n}) = \sum_{k=0}^{N-1}\Delta t\, y(t_{k})\frac{e^{-i\omega_{n}t_{k}}}{\sqrt{2\pi}}
\end{equation*}
\begin{itemize}
\item $t_{k} = k \Delta t, \qquad k = 0, 1,\ldots, N-1$.
\end{itemize}
\vfill
The inverse transform is:
\begin{equation*}
y(t) = \sum_{n=0}^{N-1}\frac{2\pi}{N\Delta t}\, \frac{e^{i \omega_{n}t}}{\sqrt{2\pi}} Y(\omega_{n})
\end{equation*}
\begin{itemize}
\item $\omega_k = k \Delta \omega, \qquad k = 0, 1, \ldots , N-1$.
\vfill
\item $\Delta \omega = \frac{2\pi}{T}=\frac{2\pi}{N\Delta t}$
\end{itemize}
\end{frame}


\begin{frame}[fragile=singleslide]
\frametitle{Fast Fourier Transform (FFT)}
The FFT is an efficient algorithm for computing the DFT\\ when $N$ is an integer power of 2.\\
\vfill
FFTs in Numpy:
\begin{itemize}
\vfill
\item \verb$numpy.fft$ module:
\begin{itemize}
\vfill
\item Online documentation:\\
\begin{scriptsize}http://docs.scipy.org/doc/numpy/reference/routines.fft.html\end{scriptsize}
\vfill
\item Python help: \verb$help(numpy.fft)$
\end{itemize}
\vfill
\item \verb$numpy.fft$ functions:
\begin{itemize}
\vfill
\item \verb$numpy.fft.fft$\\Discrete Fourier transform.
\vfill
\item \verb$numpy.fft.ifft$\\Inverse discrete Fourier transform.
\vfill
\item \verb$numpy.fft.rfft$\\Real discrete Fourier transform.
\vfill
\item \verb$numpy.fft.irfft$\\Inverse real discrete Fourier transform.
\end{itemize}
\end{itemize}
\end{frame}


\begin{frame}[fragile=singleslide]
\frametitle{Fast Fourier Transform (FFT)}
In \verb$numpy.fft$, the DFT is defined as:
\begin{equation*}
A_{k} = \sum_{n=0}^{N-1}a_n e^{-2\pi i n k/N} \qquad k=0, 1, \ldots, N-1 \qquad \Delta f = \tfrac{1}{N\Delta t}
\end{equation*}
\vspace{-3mm}
\begin{itemize}
\item The values in the result follow ``standard'' order: If \verb$A = numpy.fft.fft(a, N)$ $\rightarrow$ \verb$A[0]$ contains the zero-frequency term, which is purely real for real inputs. 
\vfill
\item \verb$A[1:N/2]$ contains the positive-frequency terms, and \verb$A[N/2+1:]$ contains the negative-frequency terms, in order of decreasingly negative frequency. 
\vfill
\item For even $N$, \verb$A[N/2]$ represents both positive and negative Nyquist frequency, and is also real for real input. 
\vfill
\item For odd $N$, \verb$A[(N-1)/2]$ contains the largest positive frequency, while \verb$A[(N+1)/2]$ contains the largest negative frequency. 
\end{itemize}
\end{frame}


\begin{frame}[fragile=singleslide]
\frametitle{Fast Fourier Transform (FFT)}
\begin{itemize}
\item \verb$numpy.fft.fftfreq(N)$ returns an array giving the frequencies of corresponding elements in the output. 
\vfill
\item The routine \verb$np.fft.fftshift(A)$ shifts transforms and their frequencies to put the zero-frequency components in the middle, and \verb$numpy.fft.ifftshift(A)$ undoes that shift.
\end{itemize}
\vfill
The inverse DFT is defined as:
\vfill
\begin{equation*}
a_n = \frac{1}{N}\sum_{k=0}^{N-1}A_k e^{2\pi i n k/N} \qquad n=0, 1, \ldots, N-1
\end{equation*}
\end{frame}

\begin{frame}[fragile=singleslide]
\frametitle{Additional Notes on Real FFTs}
\begin{itemize}
\item If all the $a_k$ are real, the negative frequency terms are just the complex conjugates of the corresponding positive-frequency terms.
\vfill
\item \verb$numpy.fft.rfft$ does not compute the negative frequency terms, and the length of the output is \verb$N/2+1$.
\vfill
\item If \verb$A = numpy.fft.rfft(a)$, \verb$A[0]$ contains the zero-frequency term, which must be purely real.
\vfill
\item If \verb$N$ is even, \verb$A[-1]$ contains the term for frequencies \verb$N/2$ and \verb$-N/2$, and must also be purely real.
\vfill
\item If \verb$N$ is odd, \verb$A[-1]$ contains the term for frequency \verb$A[(N-1)/2]$, and is complex in the general case.
\end{itemize}
\end{frame}


\section{Homework}

\begin{frame}{Homework 9}{Due 3/17/2013, 11:59pm}
Complete Problem Set 9. Turn in via CourseWeb:\\
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
\item The Python file \texttt{ps\_9.py} which generates the required results.
\vfill
\end{enumerate}
\end{frame}


%\end{document}


