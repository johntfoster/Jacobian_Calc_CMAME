Page 1
Computer Methods in Applied Mechanics and Engineering (CMAME) \
Referee Repor t \
Title: “A comparison of different methods for calculating
tangent-stiffness matrices in a massively \
parallel computational peridynamics code” \
Authors: M. D. Brothers, J. T. Foster, and H. R. Millwater \
Manuscript number: CMAME-D-13-01004 \
A. Summary \
This manuscript presents comparisons between different numerical
differentiation methods \
for the computation of entries of tangent-stiffness matrices, used in
Newton’s method for \
quasi-static nonlinear analysis of solid structures. The methods
include: automatic differen- \
tiation (AD), forward ﬁnite difference (FD), centered ﬁnite difference
(CD) and complex-step \
(CS). The authors perform the comparisons within the computational
peridynamics code \
Peridigm, where the authors implemented the CS method. Numerical results
include com- \
parisons of computational times between all the methods, as well as
comparisons of accu- \
racy between FD, CD, and CS, relative to AD. The results show that AD is
the fastest method \
in serial and FD in parallel, whereas CS is the slowest method. However,
the accuracy of \
CS is several orders of magnitude higher than the ﬁnite difference
methods (FD and CD). \
Consequently, although AD seems to be the best method in terms of
combined speed and \
accuracy, the results suggest that CS may represent a viable alternative
for cases where AD \
implementations are not practical. \
B. Evaluation \
This manuscript focuses on the CS method. This method and its comparison
to other ﬁnite- \
difference methods have been previously presented in the literature. For
example, the CS \
method has been described in [1], with a comparison between FD and CS.
Applications of \
the CS method to compute tangent matrices appear in [2, 3], with
comparisons between \
FD, CD, and CS. In addition, the CS method has been used for sensitivity
analysis in [5, 6], \
and in [4], a detailed description of the CS method and comparisons to
FD, CD, and AD are \
presented. Fur ther uses of the complex-step method appear in [7, 8, 9],
and extensions of \
the CS method are discussed in [10, 11]. \
However, this manuscript presents some aspects of the CS method which
seem novel. \
These are: \
1. comparisons between FD, CD, CS, and AD in terms of computational
time, \
2. implementation of the CS method in parallel, \
3. implementation of the CS method within Peridigm. \
In par ticular, the implementation in Peridigm is of strong interest to
researchers working with \
the peridynamic theory of solid mechanics. \
I believe this manuscript is of value to both the computational
mechanics community in gen- \
eral, and the peridynamic community in par ticular. \
I suggest it to be considered for pub- \
lication in the Computer Methods in Applied Mechanics and Engineering
journal, after the \
issues described below have been properly addressed. \
1 \
Page 2
C. Information to the authors \
I. Larger issues \
1. Some par ts of the manuscript suggest that the authors introduced a
new method, \
i.e., the complex-step (CS) method. For example, in the introduction,
they say \
“A goal of this study was to develop and evaluate a new, accurate, and
practical \
method ...” Another example appears in page 3, where the authors say
“The aim \
of this paper is not only to introduce the new complex-step method in
the context \
of evaluating tangent-stiffness matrices ..”. However, the CS method has
already \
appeared in many publications since 1998 [1]. Please revise the way you
refer to \
the CS method along the manuscript. \
2. The work presented focuses on a parallel computational peridynamic
code, and \
uses peridynamic models for mechanics. However, no detailed explanation
of the \
equations involved is presented. Although the tangent-stiffness
calculations are \
not specialized to Peridigm, the authors should include a shor t section
introducing \
the peridynamic theory and the speciﬁc constitutive model used, i.e.,
the elastic \
peridynamic solid. You may add this to the already included very brief
description \
of peridynamics in page 9 (lines 15-26). This will also help to explain
the concept \
of the peridynamic horizon in page 10. \
3. The manuscript seems to be written in a language more familiar to
computer scien- \
tists. I would encourage the authors to revise cer tain par ts of the
manuscript to be \
presented in a language more familiar to the computational mechanics
community. \
4. In Section 1.1.1, please include a more comprehensive literature
review for the CS \
method, including fur ther references (some of them are listed below). \
In par ticu- \
lar, specify what aspects of the CS method have been investigated in
each refer- \
ence. Then, you need to clearly mention your contribution within the CS
method, \
in contrast to the other references (some comments in this regard appear
in the \
manuscript in page 8). \
5. The comparisons of the different algorithms are only performed with
respect to the \
construction of tangent-stiffness matrices. In par ticular, the authors
always use the \
solution of AD at each time step to compute the entries of the
tangent-stiffness \
matrices, even for the FD, CD, and CS methods. However, the authors need
to \
demonstrate the performance of the CS method, in comparison to the other
ones, \
with respect to the solution of real, ideally non-linear problems. In
other words, how \
the solutions compare in terms of accuracy and speed between the methods
when \
solving given problems? Please include two examples of interest. The
authors \
suggest that two examples involving non-linear systems are already
included in the \
paper repository. \
The authors say in the Conclusion: “While the results showed that CS
produced \
more accurate tangent-stiffness matrices than CD and FD under the
parameters \
of the tests, it was not determined whether or not this is a clear
advantage of CS \
over FD in terms of accuracy of ﬁnal predicted displacements and speed
of conver- \
gence.” This needs to be studied and results in this regard added to
this manuscript. \
II. Smaller issues \
1. Pg. 2: In line 14, explain what does the term “algorithmically
consistent” mean. \
2. Pg. 2: In line 36, what do you mean by “discrimination”? \
3. Pg. 2: In line 37, explain what do you mean by “in-situ
instrumentation”. \
4. Pg. 3: In lines 19-29, specify the sections where each par t of the
manuscript is \
included. \
2 \
Page 3
5. Pg. 3: You may consider including the exact web address of the paper
repository. \
6. Pg. 3: Please include the forward and centered ﬁnite difference
expressions for \
easier comparison with (2); include the truncation error as well. You do
not have to \
derive these expressions though. \
7. Pg. 4: In Eq. (1), “ ∂ f 2 \
∂x2 ” should be “ ∂ 2 f \
∂x2 ”; similarly, for the third derivative. \
8. Pg. 4: You may consider writing Eq. (2) with the truncation error,
i.e., \
+ O(h2 ). \
(2) \
Im(f (x + ih)) \
h \
∂ f (x) \
= \
∂x \
In this case, one replaces “≈” by “=”. \
9. Pg. 6: In lines 9-11, please add references to the “Poisson problem”
and to the \
“mathematical optimization”. \
10. Pg. 7: Should Eqs. (4), (5), and (6) use “≈” instead of “=”? \
11. Pg. 7: In line 28, note that (cid:126)u is not the current
conﬁguration, but the displacement \
ﬁeld. Please revise the sentence. \
12. Pg. 7: Please provide an expression for F int \
in the model used. \
i \
13. Pg. 9: In line 26, please add the reference [12] below to “coupling
to molecular \
simulations [29].” \
14. Pg. 10: Please add an illustration of the block undergoing tension
in Section 2.2, \
for clarity. Also, clarify the displacement boundary conditions; are
they applied in a \
volumetric layer? \
15. Pg. 10: In line 40, you mentioned a bandwidth of 7. This seems to be
clear in 1D. \
Does this hold in higher dimensions? Please clarify. \
16. Pg. 10: In lines 47-49, you say “The speciﬁc parameters ... can be
found ... in the \
paper repository.” It seems a good idea to have the paper repository
with ﬁles that a \
user can eventually use. However, the content of the paper should be
independent \
of the repository. Please include a table with the parameters used.
Similarly, in \
page 11 (lines 11-13). \
17. Pg. 14: In line 55, is there any conclusion you can draw from the
power law index \
1.0 × 10−6? \
18. Pgs. 14-: Please clarify the value of the meshsize used on each of
the experiments. \
19. Pg. 16: Would it be possible to rescale Fig. 2, so that the
dependence of the time \
on the number of cores will look indeed linear? \
20. Pg. 16: In lines 54-56, you say “It should be pointed out that
compared to the (cid:96)2 - \
norms of any of the TS matrices by themselves, the magnitude of the
accuracy \
metric ... is relatively small.” Please include in the manuscript the
explicit informa- \
tion on the relative error. \
It seems that you already have such information in the \
paper repository. \
21. Pg. 17: Include the values of the probe distances h used for each
method. \
22. Pg. 17: In lines 53-54, you say “Accuracy trends matched those for
the single core \
tests.” Indeed, comparing Figs. 3 and 4, the results for FD seem to be
quite the \
same in serial and in parallel. For CS the accuracy seems higher in
serial. For CD, \
the accuracy is also higher in serial and, in serial, it has a
ﬂuctuating behavior. Can \
you comment on these observations? \
23. Pgs. 17-18: What are the units of K ? If F int in Eq. (4) etc. is
internal force, then K \
should have units of force/length. However, in Figs. 3 and 4 you use the
unit of \
MPa, which is force/length2 . Please clarify. \
24. Pg. 19: Are the units of the ver tical axis in Fig. 5 “seconds”, as
in Figs. 1 and 2? \
Please indicate that. Also, is the label of the ver tical axis in Fig. 6
correct? \
3 \
Page 4
25. Pg. 20: In lines 32-35, clarify what “byte-copyable” mean and why is
that impor tant. \
26. Pg. 21: Please include a section title for the references. \
27. Pg. 24: In line 23, you may add the truncation error O(h2 ) to the
expression. Oth- \
erwise, you may need to replace the “=” sign by the “≈” sign. However,
adding \
the error term would make more clear the limiting expression when h → 0.
Also, \
replace the comma by a period. \
28. Pg. 24: Why do we need S and X in Appendix B? \
29. Pgs. 25-26: Are the functions in the second column of the table in
2(c) (page 25) \
approximations? Why do you label the column “Approximates Function”?
Simi- \
larly, in line 16 (page 26) you say “approximated by the par tial
derivative”; is it an \
approximation? \
30. Pg. 26: Please clarify whether storage is needed in automatic
differentiation. For \
example, do we need to store w, v , and u? \
III. Typos/editing suggestions \
is \
1. Pg. 1: In line 43, remove “the” in “all the of the code”. \
2. Pg. 1: In line 46, replace “numeric differentiation” by “numerical
differentiation”. \
3. Pg. 2: In line 25, the sentence “The distinction of “accurate” is
deﬁned by ...” \
awkward. Please revise it. \
4. Pg. 2: In lines 32 and 48, “ﬁnite-difference” should be
“forward-difference”. \
5. Pg. 2: In lines 33, I believe “aide” should be “aid”. \
6. Pg. 3: In line 12, I would replace “such as required” by “such as
those required”. \
7. Pg. 3: In line 22, replace “with each the methods” by “with each of
the methods”. \
8. Pg. 3: In line 25, replace “implementing complex-step” by
“implementing the complex- \
step method”. \
9. Pg. 3: I would replace the title of Section 1.1, “Differentiation
Techniques” by “Dif- \
ferentiation techniques” for consistency, i.e., only capitalize the ﬁrst
letter of the ﬁrst \
word. Similarly, for the rest of the section titles. \
10. Pg. 4: In line 10, “be be made complex” should be “be made complex”.
\
11. Pg. 4: In Eq. (1), replace comma by period. \
12. Pg. 4: In line 22, you have an extra white space in “O (h2 )”. \
13. Pg. 4: I would check the proper use of hyphens along the manuscript.
For example, \
in the title of Section 1.1.2, I would replace
“Automatic-differentiation” by “Automatic \
differentiation” (i.e., no hyphen). \
14. Pg. 4: In line 42, replace “based the chain-rule” by “based on the
chain rule”. \
15. Pg. 4: In lines 45-46, “(add, multiply, power, transcendental and
the like)” should \
probably be “(addition, multiplication, exponentiation, and the like)”
or similar. \
16. Pg. 4: In line 47, I would replace “used in the study” by “used in
this study”. Similarly, \
in other instances of the manuscript. \
17. Pg. 5: In line 39, you may replace “the par tials” by “the par tial
derivatives”. Similarly \
in page 26. \
18. Pg. 5: I would replace the title of Section 1.2 “Tangent-stiffness”
by “Tangent-stiffness \
matrix”. Similarly, in line 50. \
19. Pg. 6: In line 14, “quasi-Newton’s method’s” should probably be
“quasi-Newton \
methods”. \
20. Pg. 6: In line 18, “about about a par ticular” should be “about a
par ticular”. \
21. Pg. 6: In line 51, you may replace “argument to F ” by “argument of
F ”. \
22. Pg. 7: In line 11, you may replace “single independent vector
component of the \
function” by “single independent vector component of the argument of the
function”. \
4 \
Page 5
23. Pg. 7: In line 24, replace “Where Kij is” by “where Kij is”. \
24. Pg. 7: In line 40, replace “in literature [19]” by “in the
literature [19]”. \
25. Pg. 8: Remove the period at the end of the titles of Sections 2 and
2.1, for consis- \
tency. Similarly, for the rest of the manuscript. Also, use italic font
for “Peridigm” in \
the title of §2.1. \
26. Pg. 9: In line 29, replace “Perdigm” by “Peridigm”. Similarly in
page 13 (line 44). \
27. Pg. 9: In line 37, replace “be simply be declared” by “be simply
declared”. \
28. Pg. 9: In line 55, I would replace “computational scientists” by
“computer scientists”. \
29. Pg. 10: In line 30, I would replace “The purpose of applying the
load” by “Applying \
the load”. \
30. Pg. 13: I would add a comma at the end of Eq. (8), and replace
“Where D is \
distance” by “where D is distance” in line 14. \
31. Pg. 13: In line 15, replace “based method, M is” by “based method,
and M is”. \
32. Pg. 13: In line 31, replace “correspond to” by “corresponds to”. \
33. Pg. 14: In lines 19-21, you have twice the word “nonzero” in “number
of nonzero \
tangent-stiffness (TS) non-zero matrix elements”. \
34. Pg. 14: In lines 22, I would replace “The units for accuracy are
derived equation (8) \
and the units used to deﬁne bulk material proper ties, mentioned in
Section 2.2.” by \
“The accuracy measure is given by equation (8) and the choice of elastic
moduli is \
mentioned in Section 2.2.” \
35. Pg. 15: In line 54, it seems that “yet still fall” should be “yet
still falls”. \
36. Pg. 17: In line 45 you say “h, cannot be too small,”. \
I understand that you mean \
that you can take h as small as possible. However, the way written may
have the \
opposite connotation. I would revise it for clarity. \
37. Pg. 18: In lines 35-36, replace “the number nonzero” by “the number
of nonzero”. \
38. Pg. 18: In line 39, replace “the the number of nonzero” by “the
number of nonzero”. \
39. Pg. 18: In line 50, I would replace “experimental results,” by
“computational experi- \
ments,”. Otherwise, it may give the impression of physical experiments.
\
40. Pg. 20: In line 13, is the use of the word “order” in “number of
iterations taken order \
to measure” correct? \
41. Pg. 20: In lines 26-27, replace “complex-step all of the methods” by
“complex-step \
in all of the methods”. \
42. Pg. 20: In line 50, you may either replace “to implement; It only”
by “to implement; \
it only”; or replace the semicolon by a period. \
43. Pgs. 21-23: You may capitalize the ﬁrst letters on the journal names
in your refer- \
ences [9, 20] \
44. Pg. 22: In your reference [10], you may replace “fr ´echet” by “Fr
´echet”. \
45. Pg. 23: Update your reference [21] (see the reference [3] in this
repor t). Also, \
update your reference [27]. \
46. Pg. 24: In line 18, replace the comma by a period. \
47. Pg. 24: I would replace the comma by a period in line 28, and
replace “using \
L’H ˆopital’s rule” by “Using l’H ˆopital’s rule” in line 31. \
48. Pg. 24: I would replace the comma by a period in line 34, and
replace “of course, \
as h → 0” by “As h → 0” in line 37. \
49. Pg. 24: I would replace the title of Appendix B “AD Example” by
“Automatic differ- \
entiation example”. \
50. Pg. 24: In line 45, you may replace “sin(cos(x))” by “sin(cos(x))”.
For that, use \\sin \
instead of sin, etc. (similarly in the bottom of the page and in page
25). Also, add \
a period at the end of the expression. \
5 \
Page 6
51. Pg. 25: In line 55, you may remove the “·” symbol in “ d \
dx · g(h(k(x)))”. \
52. Pgs. 25 and 26: I would number the table in 2(c) (page 25). Let’s
assume the \
number is “2”. Then, in line 13 (page 26), I would replace “chosen for
each function \
and held as constant” by “chosen for each function as in Table 2 and
held constant”. \
53. Pg. 26: In line 24, add a period at the end of the expression. \
References \
[1] W. Squire and G. Trapp, Using complex variables to estimate
derivatives of real functions, \
SIAM Rev. 40 (1998), pp. 110-112. \
[2] A. P ´erez-Foguet, A. Rodr´ıguez-Ferran, A. Huer ta, Numerical
differentiation for local and \
global tangent operators in computational plasticity, Comput. Methods
Appl. Mech. Engrg. \
189 (2000), pp. 277-296. \
[3] A. P ´erez-Foguet, A. Rodr´ıguez-Ferran, A. Huer ta, Numerical
differentiation for non-trivial con- \
sistent tangent matrices: an application to the MRS-Lade model, Int. J.
Numer. Meth. Engng \
48 (2000), pp. 159-184. \
[4] J. Mar tins, P. Sturdza, J. Alonso, The complex-step derivative
approximation, ACM Transac- \
tions on Mathematical Software (TOMS), ISSN 0098-3500, 09/2003, Volume
29, Issue 3, pp. \
245-262. \
[5] W. K. Anderson, J. C. Newman, D. L. Whitﬁeld, and E. J. Nielsen,
Sensitivity analysis for \
Navier–Stokes equations on unstructured meshes using complex variables,
AIAA Journal, \
ISSN 0001-1452, 01/2001, Volume 39, Issue 1, pp. 56-63. \
[6] J. C. Newman, W. K. Anderson, and L. D. Whitﬁeld, Multidisciplinary
sensitivity derivatives \
using complex variables, Tech. Rep. MSSU-COE-ERC-98-08 (July),
Computational Fluid Dy- \
namics Laboratory. \
[7] A. H. Al-Mohy and N. J. Higham, The complex step approximation to
the Fr ´echet derivative \
of a matrix function, Numer. Algor. 53 (2010), pp.133-148. \
[8] W. Jin, B. H. Dennis, and B. P. Wang, Improved sensitivity analysis
using a complex variable \
semi-analytical method, Struct. Multidisc. Optim. 41 (2010), pp.
433-439. \
[9] A. Voorhees, H. Millwater, and R. Bagley, Finite Elements in
Analysis and Design 47 (2011), \
pp. 1146-1156. \
[10] K.-L. Lai and J. L. Crassidis, Extensions of the ﬁrst and second
complex-step derivative ap- \
proximations, Journal of Computational and Applied Mathematics 219
(2008), pp. 276-293. \
[11] R. Abreu, D. Stich, and J. Morales, On the generalization of the
complex step method, Journal \
of Computational and Applied Mathematics 241 (2013), pp. 84-102. \
[12] P. Seleson, M. L. Parks, and M. Gunzburger, Peridynamic state-based
models and the \
embedded-atom model. Communications in Computational Physics, 15(1)
(2014), pp. 179- \
205. \
6 \
Page: [1](#1), [2](#2), [3](#3), [4](#4), [5](#5), [6](#6)