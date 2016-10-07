# Computational methods in Physics
## Week 10
#### Prof. Michael Wood-Vasey
##### [based on materials from Prof. Brian D'Urso]
##### University of Pittsburgh, Department of Physics and Astronomy

* Analytical Fourier Series and Transforms
* Discrete Fourier Transforms

#### Fourier Series
For a periodic function $y(t)$ with period $T$:
\begin{equation*}
y(t) = \frac{a_{0}}{2} + \sum_{n=1}^{\infty} \left(a_{n} \cos
n\omega t + b_{n} \sin n\omega t
\right)
\end{equation*}
The Fourier coefficients can be determined with:
\begin{equation*}
{a_n\choose b_n}  =\frac{2}{T} \int _{0}^{T} dt {\cos n\omega
t\choose \sin n\omega t} y(t)
\end{equation*}
Notes:
* $a_{0} = 2 \left\langle y(t)\right\rangle$, $b_{0} = 0$.
* If $y(t)$ odd: $y(-t) = - y(t)$  $\Rightarrow$ $a_{n} \equiv 0$.
* If $y(t)$ even: $y(-t) = y(t)$ $\Rightarrow$ $b_{n} \equiv 0$.



#### Fourier Transforms
For a function $y(t)$ defined at all times:
\begin{equation*}
y(t)=\int_{-\infty}^{+\infty} d\omega\ Y(\omega)\, \frac{e^{+i\omega t}} {\sqrt{2\pi}}
\end{equation*}
Fourier transform $Y(\omega)$ can be determined with:
\begin{equation*}
Y(\omega)=\int_{-\infty}^{+\infty} dt\, \, y(t)\, \frac{e^{-i\omega t}} {\sqrt{2\pi}}
\end{equation*}
Notes:

* If $y(t)$ odd and real: $y(-t) = - y(t)$  \ $\Rightarrow$ \ $Y(\omega)$ is imaginary. 
* If $y(t)$ even and real: $y(-t) = y(t)$ \ $\Rightarrow$ \ $Y(\omega)$ is real.
* If $y(t)$ is purely real $\Rightarrow Y(-\omega)=\overline{Y(\omega)}$.
* Power Spectrum: $\propto \left| Y(\omega)\right|^{2}$, maybe $\log_{10}\left|Y\right|^{2}$.




\section[]{Discrete Fourier Transforms (DFT)}

#### Discrete Fourier Transforms (DFT)
For numerical evaluation, we have to use a finite range for $t$   
and $N$ discrete samples of $y(t)$:

* $y_{k} = y(t_{k})$, $k = 0, 1,\ldots, N-1$.
* Uniform time steps $\Delta t \rightarrow t_{k} = k \Delta t$.
* Assume periodicity $y(t+T) = y(t)$, $T=N\Delta t$.

The DFT will give us $Y(\omega)$ at $N$ discrete values $Y_k=Y(\omega_k)$:

* $\omega_k = k \Delta \omega, \qquad k = 0, 1, \ldots , N-1$.
* $\Delta \omega = \frac{2\pi}{T}=\frac{2\pi}{N\Delta t}$.
* $Y(\omega_k)$ is also periodic: $Y(\omega_{n+N})=Y(\omega_{n})$,  
	so we can also shift the range of $k$.



#### Discrete Fourier Transforms (DFT)
The formula for the forward DFT is:
\begin{equation*}
Y(\omega_{n}) = \sum_{k=0}^{N-1}\Delta t\, y(t_{k})\frac{e^{-i\omega_{n}t_{k}}}{\sqrt{2\pi}}
\end{equation*}

* $t_{k} = k \Delta t, \qquad k = 0, 1,\ldots, N-1$.

The inverse transform is:
\begin{equation*}
y(t) = \sum_{n=0}^{N-1}\frac{2\pi}{N\Delta t}\, \frac{e^{i \omega_{n}t}}{\sqrt{2\pi}} Y(\omega_{n})
\end{equation*}

* $\omega_k = k \Delta \omega, \qquad k = 0, 1, \ldots , N-1$.
* $\Delta \omega = \frac{2\pi}{T}=\frac{2\pi}{N\Delta t}$



#### Fast Fourier Transform (FFT)
The FFT is an efficient algorithm for computing the DFT  
when $N$ is an integer power of 2.  
FFTs in Numpy:

* `numpy.fft` module:

* Online documentation:  
http://docs.scipy.org/doc/numpy/reference/routines.fft.html
* Python help: `help(numpy.fft)`

* `numpy.fft` functions:

* `numpy.fft.fft` -- Discrete Fourier transform.
* `numpy.fft.ifft` -- Inverse discrete Fourier transform.
* `numpy.fft.rfft` -- Real discrete Fourier transform.
* `numpy.fft.irfft` -- Inverse real discrete Fourier transform.




#### Fast Fourier Transform (FFT)
In `numpy.fft`, the DFT is defined as:
\begin{equation*}
A_{k} = \sum_{n=0}^{N-1}a_n e^{-2\pi i n k/N} \qquad k=0, 1, \ldots, N-1 \qquad \Delta f = \tfrac{1}{N\Delta t}
\end{equation*}

* The values in the result follow "standard" order: If `A = numpy.fft.fft(a, N)` $\rightarrow$ `A[0]` contains the zero-frequency term, which is purely real for real inputs. 
* `A[1:N/2]` contains the positive-frequency terms, and `A[N/2+1:]` contains the negative-frequency terms, in order of decreasingly negative frequency. 
* For even $N$, `A[N/2]` represents both positive and negative Nyquist frequency, and is also real for real input. 
* For odd $N$, `A[(N-1)/2]` contains the largest positive frequency, while `A[(N+1)/2]` contains the largest negative frequency. 



#### Fast Fourier Transform (FFT)

* `numpy.fft.fftfreq(N)` returns an array giving the frequencies of corresponding elements in the output. 
* The routine `np.fft.fftshift(A)` shifts transforms and their frequencies to put the zero-frequency components in the middle, and `numpy.fft.ifftshift(A)` undoes that shift.

The inverse DFT is defined as:
\begin{equation*}
a_n = \frac{1}{N}\sum_{k=0}^{N-1}A_k e^{2\pi i n k/N} \qquad n=0, 1, \ldots, N-1
\end{equation*}

#### Additional Notes on Real FFTs

* If all the $a_k$ are real, the negative frequency terms are just the complex conjugates of the corresponding positive-frequency terms.
* `numpy.fft.rfft` does not compute the negative frequency terms, and the length of the output is `N/2+1`.
* If `A = numpy.fft.rfft(a)`, `A[0]` contains the zero-frequency term, which must be purely real.
* If `N` is even, `A[-1]` contains the term for frequencies `N/2` and `-N/2`, and must also be purely real.
* If `N` is odd, `A[-1]` contains the term for frequency `A[(N-1)/2]`, and is complex in the general case.



