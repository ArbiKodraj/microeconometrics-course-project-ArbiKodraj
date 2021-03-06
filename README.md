---
<font face="ITC Berkeley Oldstyle" size="3">Project for the course in Microeconometrics | Summer 2020, M.Sc. Economics, Bonn University | [Arbi Kodraj](https://github.com/ArbiKodraj/desktop-tutorial) </font><br/>


# Replication of Philip Oreopoulos (2011)


This notebook contains my replication of the results from the following paper:

> <font face="ITC Berkeley Oldstyle" size="4"> [Philip Oreopoulos (2011)](https://www.aeaweb.org/articles?id=10.1257/pol.3.4.148). "Why Do Skilled Immigrants Struggle in the Labor Market? A Field Experiment with Thirteen Thousand Resumes." American Economic Journal: Economic Policy 3, 148–171.</font><br />


Oreopoulos (2011) sent thousands of randomly manipulated resumes to employers who advertised open positions in Toronto. His aim was to find out why highly qualified immigrants have problems asserting themselves in the Canadian labor market. The study found significant discrimination in a variety of occupations against applicants with foreign working experience or applicants with Indian, Pakistani, Chinese and Greek names compared to English names. Listing additional competences such as fluency in languages, experience in multinational companies, training in very selective schools or extracurricular activities appear not to have offsetting effects. Recruiters justify this behavior with concerns about language skills, but were not able to adress compensatory skills.

- The original data provided by the author can be found [here](https://www.openicpsr.org/openicpsr/project/114770/version/V1/view) 

---

## Replication

In this notebook I concentrate on the essential results of the author. I follow its structure, additionally I draw on further studies to express some statements and findings. Furthermore, I strictly follow Oreopoulos procedures and apply the same methods as he does. I have changed some methods, such as the interactive regression with a time fixed effect, in favour of my replication. The reason for this is that on the one hand the results do not change much and differ only marginally from Oreopoulos results and on the other hand they allow me to replicate all results completely. This is explained in more detail in the notebook. 
Furthermore, I perform additional, own methods to check the robustness of the results. The resulting outputs are compared to the outputs of Oreopoulos. 
Finally, I will put the empirical findings into a political context and discuss Oreopoulos's suggestions for possible policy interventions and extend them with mine.   

The best way to access this notebook is by downloading it [here](https://github.com/ArbiKodraj/microeconometrics-course-project-ArbiKodraj) and open it locally via jupyter notebook. Alternatively, it can be viewed [here](https://github.com/ArbiKodraj/microeconometrics-course-project-ArbiKodraj/blob/master/ReplicationProject.ipynb), online on github. Other ways to view this notebook are binder [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/ArbiKodraj/microeconometrics-course-project-ArbiKodraj.git/master) or nbviewer <a href="https://nbviewer.jupyter.org/github/ArbiKodraj/microeconometrics-course-project-ArbiKodraj/blob/master/ReplicationProject.ipynb" 
   target="_parent">
   <img align="center" 
      src="https://raw.githubusercontent.com/jupyter/design/master/logos/Badges/nbviewer_badge.png" 
      width="109" height="20">
</a>, however these are not the preferred options, because when opening the notebook it can happen that some outputs are displayed incompletely.

> **Course Instructor:** [Philipp Eisenhauer](https://github.com/peisenha)


## Notebook's Structure

- **1. Introduction:** There, the author's question and its political relevance will be introduced  
- **2. Background:** In this section, I am going to list facts and numbers regarding the unemployment rate in Canada provided by the [Canadian Census](https://www12.statcan.gc.ca/census-recensement/index-eng.cfm) and the author itself
- **3. Theories of Job-Applicant Discrimination:** Here, I collect Oreopoulos opinion and possible explantions on job discrimination and contrast them with further opinions
- **4. Research Design:** This section deals with the design and procedure of the experiment 
- **5. Results:** There, I am going to replicate all results and extend them by further analysis and methods in order to check their robustness
- **6. Discussing Results with Recruiters:** This section shortly discusses the reactions and justifications of the recruiters after the author has confronted them with the results
- **7. Conclusion:** In order to return to the research question raised at the beginning, the results will be summarised again here and their consequences will be presented and classified politically

## Reproducibility

In order to ensure full reproducibility, I have set up a continous integration environment using [Travis Ci](https://travis-ci.com) which can be checked here: [![Build Status](https://travis-ci.com/ArbiKodraj/microeconometrics-course-project-ArbiKodraj.svg?branch=master)](https://travis-ci.com/ArbiKodraj/microeconometrics-course-project-ArbiKodraj) 


## Reference

- <b>Christian S. Crandall and Amy Eshleman (2003)</b>. *A Justification–Suppression Model of the Expression and Experience of Prejudice*. American Psychological Association, Vol. 129, No. 3, 414–446.


- <b>Edmund S. Phelps (1972)</b>. *The Statistical Theory of Racism and Sexism*. The American Economic Review, Vol. 62, No. 4, pp. 659- 661.


- <b>Gareth James, Daniela Witten, Trevor Hastie, Robert Tibshirani (2017)</b>. *An Introduction to Statistical Learning*. Springer New York Heidelberg Dordrecht London.


- <b>Jake VanderPlas (2017)</b>. *Python Data Science Handbook*. O’Reilly Media, Inc., 1005 Gravenstein Highway North, Sebastopol, CA 95472.


- <b>Marianne Bertrand and Sendhil Mullainathan (2004)</b>. *Are Emily and Greg More Employable Than Lakisha and Jamal? A Field Experiment on Labor Market Discrimination.* AMERICAN ECONOMIC REVIEW VOL. 94, NO. 4, 991-1013.


- <b>Philip Oreopoulos (2011)</b>. *Why do skilled immigrants struggle in the Labor Market? A Field Experiment with Thirteen Thousand Resumes*. American Economic Journal: Economic Policy 3: 148–171.


- <b>Robert C. M. Beyer (2017)</b>. *The Performance of Immigrants in the German Labor Market*. SOEPpapers on Multidisciplinary Panel Data Research at DIW Berlin.


- <b>Stephen Drinkwater (2017)</b>. *Why does unemployment differ for immigrants? Unemployment risk varies greatly across immigrant groups depending on language skills, culture, and religion* IZA World of Labor 2017: 376. 


- <b>Sendhil Mullainathan (2002)</b>. *Thinking Through Categories*. Working Paper, MIT, Cambridge, MA. 

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://github.com/HumanCapitalAnalysis/template-course-project/blob/master/LICENSE)

