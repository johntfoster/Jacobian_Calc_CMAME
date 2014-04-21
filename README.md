Jacobian_Calc_CMAME
===================

Collaborative CMAME journal paper


To clone:

````
git clone https://github.com/johntfoster/Jacobian_Calc_CMAME.git
````

After making changes in your local repository, commit then _locally_ with:

````
git commit -a -m "A Commit Message"
````

the `-a` option adds all currently tracked files to the local commit.  The `-m` 
option allows for an inline commit message, if omitted it will open up an
editor for you to include a longer commit message.

When your ready to push your changes to the github repo:

````
git push origin master
````

`origin` is the default name given to the remote github repository when the
initial clone is done.  `master` is the default branch.

To sync your local repo with `origin master` on github:

````
git pull
````

### To build the paper ###
Make sure you have a current LaTeX installation in your `$PATH`, then just
type `make`.  The included `Makefile` will correctly typeset and update
references, cross-references, bibliography, etc. You can also type `make clean`
to remove all the auxiliary files in the directory.

### Creating a LaTeX diff from the repository

````
latexdiff-vc -c ld.cfg -r 9ee7554 --math-markup=0 jacobian_calc_CMAME.tex
````

where `9ee7554` should be replaced with the correct `git` commit.
