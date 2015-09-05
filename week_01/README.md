# Computational methods in Physics
## Week 1
#### Prof. Michael Wood-Vasey
##### University of Pittsburgh, Department of Physics and Astronomy

## Course Information

### Course Structure
* All course materials available on GitHub page: https://github.com/pitt1321/
* Syllabus at http://github.com/pitt1321/syllabus
* Lectures at http://github.com/pitt1321/lectures
* Reading at lectures page http://github.com/pitt1321/lectures/README.md
  - But this README.md is automatically displayed when you just go to `lectures`
* Organized by week:
  - Lecture and lab time each Monday and Wednesday.
  - More focus on lab time on Friday.  Bring questions!
  - Assignments due Friday.  What time do you want?
* Lecture and lab time will be interactive:
  - Introduction of new material.
  - Interactive demonstrations.
  - Start your assignment.
  - I will clarify topics as needed.
  - Try not to miss classes; they will be hard to make up.
* Assignments:
  - Each assignment will be provided as a GitHub repository under.
    https://github.com/pitt1321/assignments/
  - To complete each assignment:
    1. [**fork** the repository][forking] to your own account.
    2. [**Clone**][ref-clone] the repository to your computer.
    3. Work on assignments in lab and on your own time.
    4. Regularly [**commit**][ref-commit] and push your work.
    5. [**Push**][ref-push]/sync the changes up to GitHub.
    6. [Create a **pull request**][pull-request] on the original repository to turn in the assignment.
  - Notes:
    * Create [**Issues**][issues] to ask for help or feedback or just to track your own progress.
    * Discussion is encouraged,\\ but all code entry must be your own!
    * Understand all the code you write!
* Final Project:
  - Culmination of course.
  - Start looking for a topic early!
  - I will help with coding in lab time.

## Where to Go for Help
* I will be around during working time during each class after lecture time.
* Office hours: Wednesday, 11:00 to 12:00
* Make an appointment to meet with me.
* Lots of Python and GitHub help available online!

## Course Outline
* Week 1: Introduction to Python.
* Week 2: Python arrays and plotting.
* Week 3: Random numbers, Monte Carlo simulation.
* Week 4: Numerical integration.
* Week 5: Solving equations, root finding.
* Week 6: NumPy and SciPy, matrix methods.
* Week 7: Ordinary differential equations (ODEs).
* Week 8: Solving systems of ODEs.
* Week 9: Fourier Transforms.
* Week 10: Discrete/continuous nonlinear problems.
* Week 11: Thermodynamic simulations.
* Week 12: Partial differential equations (PDEs).
* Week 13: PDEs continued.
* Week 14: Final project presentations.

## Python is 
* A high-level language.
  - Built-in high level data structures.
  - Object oriented with some inspiration from functional languages.
* An interpreted language.
  - You don't compile your programs.
  - Exception framework with tracebacks
  - Automatic memory management
  - Dynamic typing, dynamic binding.
* Huge standard library with all sorts of functionality.
* Extensible and embeddable.
* Cross-platform and free.
* Great as both a scripting/glue language and for full-blown application development.

## Python Installation Options
* Computer options:
  - Use lab computers with pre-installed Python and 
    * Clone and commit/push back to GitHub for each session.
    * store your data on a flash drive.
    * You can try Box, but sadly Box doesn't always work the best with `git`.
    * Use your own computer and install software yourself.
    * I will provide some support, but your colleagues and the wider web will be the best resources.
* For your personal machine, I recommend the Anaconda Python distribution:
  - https://store.continuum.io/cshop/anaconda/
  - This is a distribution aimed at the Scientific Python users, which is us!
  - It includes the key main packages `numpy`, `scipy`, `matplotlib`, and `iPython`; and also provides the increasingly popular `pandas` data processing framework.
* The Entought Canopy distribution is also a popular one
  - Pros: 
    * Comes with an Integrated Development Environment (IDE) which some people really like.  
    * It's what is actually installed on the Thaw 210 lab computers.
  - Cons: 
    * Is currently restricted to Python 2.7.
    * Is nominally not free, but is free for academic use (i.e., for .edu email addresses).


## Running Python
There are many ways Python can be used:
* Interactively:
  - Run the python program with no arguments and get:
  ```
Python 2.7.10 (default, Jul 24 2015, 10:36:25) 
[GCC 4.2.1 Compatible Apple LLVM 6.1.0 (clang-602.0.53)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> 
  ```
  - Useful for tests, debugging, and for demonstrations.
  - This is where we'll start today.
* Non-interactively:
  - Write a script (a text file) and run it.
  - We will not use this, but it may be useful.
* Using iPython Notebook:
  - Present code, text, and results in one file.
  - Allows interactive analysis
  - Encourages integration of explanation, code, and results.
  - This is where we'll end up.

## Introduction to iPython/Jupyter
* iPython is a useful and improved interface over the base python interactive command line.
* iPython Notebook is a web-browser-based interface that uses ``Notebook''s to present content, code, and results in an integrated file.
* From the command line type the following to open up a web browser that you will use to interact with iPython.
`ipython notebook`
  - Main site: http://ipython.org/
  - Quick demo: https://youtu.be/H6dLGQw9yFQ
  - It's nice to see code and results together when developing
  - The integrated help and auto-completion is really useful.
  - Can save the notebook including results
  - Can export the code to a separate Python file for reuse by other programs.
  - Lots of videos and demos, including at http://ipython.org/videos.html.  Check them out and come up to speed.
  - Tutorials and example notebook:  http://nbviewer.ipython.org/github/ipython/ipython/blob/master/examples/Notebook/Index.ipynb
  - ``A gallery of interesting iPython Notebooks'' https://github.com/ipython/ipython/wiki/A-gallery-of-interesting-IPython-Notebooks
  - NBViewer:  A service that you can publish read-only versions of iPython notebooks.  http://nbviewer.ipython.org
  - More later.

## Homework 1 - Due 2015-09-05, at 23:59
* Create a GitHub account and tell me (we should have just done this in class)
* Install Python and iPython on your computer.
  - Python version 3.4 or later.
  - If you are already up and running with Python 2.7, you can keep running that but please be aware of the differences and submit code that runs under Python 3 using the ``__future__`` module: https://docs.python.org/2/library/__future__.html
* Complete Problem Set 1. Turn in your code via GitHub.
  - An iPython file with:
    * Your written answers.
    * Your code.
    * Your output.
    * Images of plots as required.



<!-- Links -->
[create-repo]: https://help.github.com/articles/create-a-repo
[private-repos]: /guide/private_repos
[add-to-team-action]: https://github.com/education/teachers_pet/#giving-others-access
[teachers-pet]: https://github.com/education/teachers_pet
[help-add-to-team]: https://help.github.com/articles/adding-organization-members-to-a-team
[help-access-control]: https://help.github.com/articles/what-are-the-different-access-permissions#organization-accounts
[forking]: https://guides.github.com/activities/forking/
[issues]: https://guides.github.com/features/issues/
[ref-clone]: http://gitref.org/creating/#clone
[ref-commit]: http://gitref.org/basic/#commit
[ref-push]: http://gitref.org/remotes/#push
[pull-request]: https://help.github.com/articles/creating-a-pull-request
[raw]: https://raw.githubusercontent.com/education/guide/master/docs/forks.md
