# Computational methods in Physics
## Week 3
#### Prof. Michael Wood-Vasey
##### [based on materials from Prof. Brian D'Urso]
##### University of Pittsburgh, Department of Physics and Astronomy


## Random Numbers

### Deterministic Randomness
Some problems are physically unpredictable. Examples:
  * thermal motion
  * games of chance
  * radioactive decay

How do we deal with randomness numerically?
  * Computers are deterministic; no chance involved.
  * Always same output for same input; unless hardware error.
  * Generate pseudo-random numbers.
  * Monte Carlo calculations: simulate random events.
    - Solve equations statistically
    - Solve intractable problems

### Drawing Random Numbers
  * Python has a random module for drawing random numbers
  * `random.random()` 
draws random numbers in `[0, 1)` :  
`>>> import random`  
`>>> random.random()`  
`0.81550546885338104`  
`>>> random.random()`  
`0.44913326809029852`  
`>>> random.random()`  
`0.88320653116367454`  
  * The sequence of random numbers is produced by a
deterministic algorithm - the numbers just appear random.

### Distributions of Random Numbers}
  * `random.random()` generates random numbers that are uniformly
distributed in the interval $[0, 1)$.
  * `random.uniform(a, b)` generates random numbers uniformly
distributed in $[a, b)$.
  * "Uniformly distributed" means that if we generate a large set
of numbers, no part of $[a, b)$ gets more numbers than others.
  * See `random_distribution` demo.

### Vectorized Drawing of Random Numbers
  * `random.random()` generates one number at a time  
`r = random.random()` # one number
`r = random.uniform(-1, 10)` # one number  
  * `numpy` has a random module that efficiently generates a (large)
number of random numbers at a time:  
```
import numpy as np
r = np.random.random(size=1000) # array
r = np.random.uniform(-1, 10, size=1000) # array
```
  * Vectorized calculations are important for speeding up programs!

### Drawing Integers
  * Quite often we want to draw an integer from $[a, b]$ and not a
real number.
  * Python's `random` module and `numpy.random` have functions for
drawing uniformly distributed integers:
```
import random 
r = random.randint(a, b) # a, a+1, ..., b
```

```
import numpy as np
# b+1 is not included  
r = np.random.randint(a, b+1, N)  
# b is included  
r = np.random.random_integers(a, b, N)  
```

### Example: Throwing a Die; Vectorized Version
```
 import numpy as np  
 N = 10   
 eyes = np.random.randint(1, 7, N)   
 # True/False array   
 success = eyes == 6   
 # treats True as 1, False as 0   
 six = np.sum(success)   
 print 'Got six %d times out of %d' % (six, N) 
```
  * Important: use `numpy.sum` and not the default `sum` function! (The latter is slow.)

### Fixing the Seed Fixes the Random Sequence
  * Debugging programs with random numbers is difficult because
the numbers produced vary each time we run the program.
  * For debugging it is important that a new run reproduces the
sequence of random numbers in the last run.
  * This is possible by fixing the seed of the random module:  
`random.seed(121) # int argument`
  * Or the numpy module:
`np.random.seed(121) # int argument`
  * The value of the seed determines the random sequence:
```
 import numpy as np   
 np.random.seed(2)   
 np.random.random(3) 
```

### Distributions of Random Numbers
  * Sometimes we want uniformly distributed random numbers,
and sometimes not.
  * Example: it is more likely have normal (mean) blood pressure
than large deviations from the mean.
  * We can use the Gaussian (or "normal") distribution to get random
numbers clustered around a mean value:  
```
 import random   
 r = random.normalvariate(m, s)   
```
where `m`: mean value,  `s`: standard deviation
  * Vectorized drawing of $N$ Gaussian/normal numbers:  
```
 import numpy as np   
 samples = np.random.normal(m, s, N) 
```
  * We are using mostly uniformly distributed numbers.

### Probability via Monte Carlo Simulation
  * What is the probability that a certain event A happens?
    1. Simulate $N$ events
    2. Count how many times $M$ the event $A$
happens
    3. The probability of the event $A$ is then $M/N$ (as $N \rightarrow \infty$).
  * Example: what is the probability of getting 6 on two or more
dice if we throw 4 dice?  
```
 N = 100000 # number of experiments   
 M = 0 # number of successful events   
 for i in range(N):   
     six = 0 # count the number of dice with a six   
     r1 = random.randint(1, 6)   
     if r1 == 6: six += 1   
     ... same for dice 2, 3 and 4 ...   
     # successful event?   
     if six >= 2:   
         M += 1   
 print 'probability:', float(M)/N 
```

## Random Walks

### Random Walk in One Spatial Dimension
  * A particle moves to the left and right with equal probability
  * $n$ particles start at $x = 0$ at time $t = 0$ - how do the particles
get distributed over time?
  * This is called a random walk and constitutes a simple model for
molecular motion in many situations:
    - heat transport
    - quantum mechanics
    - polymer chains
    - population genetics
    - pricing of financial instruments
    - ...
  * We'll make a program for simulating random walk.

### Random Walk as a Difference Equation
  * Let $x_n$ be the position of one particle at time $n$.
  * Updating rule: $x_{n+1} = x_n + s$  
where $s = 1$ or $s = -1$, both with probability $1/2$.
  * For $n_p$ particles, we need $n_p$ such difference equations.
  * Would like to calculate the statistics (mean position, ``width'' of the cluster of particles, how particles are distributed throughout space).
  * Random walk in 2-D:
    - $x_{n+1} = x_n + r_x$
    - $y_{n+1} = y_n + r_y$
    - $r_x = r \cos\theta$, $r_y = r \sin\theta$, with random $\theta$

### How Far After $N$ Steps (in 2-D)?
  * Start at $(x, y) = (0, 0)$.
  * After $N$ steps:  
$R^2 = (\Delta x_1 + \cdots + \Delta x_N)^2 + (\Delta y_1 + \cdots + \Delta y_N)^2$
  * Expand:  
$R^2 = \Delta x_1^2 + \cdots + \Delta x_N^2 + 2 \Delta x_1 \Delta x_2 + \cdots  
+ \Delta y_1^2 + \cdots + \Delta y_N^2 + 2 \Delta y_1 \Delta y_2 + \cdots$
  * Cross terms average to zero:  
$R^2 \simeq \Delta x_1^2 + \cdots + \Delta x_N^2 + \Delta y_1^2 + \cdots + \Delta y_N^2$
  * $\Rightarrow R^2 \simeq N \langle r^2 \rangle$
  * $\Rightarrow R \simeq \sqrt{N} r_{RMS}$

## Radioactive Decay
### Spontaneous (e.g. Radioactive) Decay
  * "Spontaneous" process $\rightarrow$ no external stimulus.
  * Time of decay is random, independent of:
    - How long it existed.
    - How many other are around.
  * Describes nuclear decay, electronic relaxation, etc.
  * Theory: probability of decay per $\Delta t$ per particle is:   
$P(t)=\lambda$ (constant)    
$\Rightarrow$ $N(t)$, $dN/dt$ decrease with time.  

### Model: Continuous Decay
  * If $N\rightarrow \infty$, $\Delta t \rightarrow 0$:  
$\frac{\Delta N(t)}{\Delta t} \rightarrow \frac{dN(t)}{dt} = -\lambda N(t)$
  * Can integrate differential equation:  
$N(t) = N(0) e^{-\lambda t} = N(0) e^{-t/\tau}$  
with $\lambda = 1/\tau$
  * $\frac{dN}{dt}(t) = -\lambda N(0) e^{-\lambda t} = \frac{dN}{dt}(0) e^{-t/\tau}$
  * But this is an approximation!  
Nature can have small $N$, stochastic behavior.

### Method: Decay Simulation
  * Algorithm:  
Loop through remaining nuclei   
$r_i < \lambda$? $\Rightarrow$ decays   
$t = t + \Delta t$   
Repeat loop  
  * $r_i$ is random number in $[0, 1]$.
  * Higher $\lambda\Rightarrow$ more frequent decays.
  * See `decay_simulator` demonstration.

