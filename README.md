<h1 align="center">
  <a href="https://github.com/pythonhealthdatascience"><img src="https://raw.githubusercontent.com/pythonhealthdatascience/stars_wp1_summary/main/images/stars_banner.png" alt="Markdownify"></a>
  <br>
  Computational Reproducibility Assessments: Summary
  <br>
</h1>

<p align="center">
  <i align="center">Summary of the eight computational reproducibility assessments conducted as part of STARS Work Package 1.</i>
</p>

<p align="center">
    <a target="_blank" href="https://doi.org/10.5281/zenodo.14267268"><img src="https://zenodo.org/badge/DOI/10.5281/zenodo.14267268.svg" alt="DOI 10.5281/zenodo.14267268"/></a>
    <!--<a href="#"><img src="https://img.shields.io/github/v/release/pythonhealthdatascience/stars_wp1_summary" alt="GitHub release" /></a>
    <a href="#"><img src="https://img.shields.io/github/release-date/pythonhealthdatascience/stars_wp1_summary" alt="GitHub release date" /></a>-->
    <a href="#"><img src="https://img.shields.io/github/last-commit/pythonhealthdatascience/stars_wp1_summary" alt="GitHub last commit" /></a>
    <a target="_blank" href="https://github.com/pythonhealthdatascience/stars_wp1_summary/blob/main/LICENSE"><img src="https://img.shields.io/badge/license-CC--BY--4.0-blue.svg" alt="MIT licence"/></a>
</p>

## Table of contents

* [👋 About the repository](#-about-the-repository)
* [📍 Locating tables and figures from the article](#-locating-tables-and-figures-from-the-article)
* [📖 View book locally](#-view-book-locally)
* [📝 Citation](#-citation)
* [💰 Funding](#-funding)

<br>
<br>

## 👋 About the repository

In work package 1, we assessed the computational reproducibility of eight discrete-event simulation papers with models in Python and R. The reproductions and findings are summarised at: <https://pythonhealthdatascience.github.io/stars_wp1_summary/>.

[![Python](https://img.shields.io/badge/-python-black?style=for-the-badge&logoColor=white&logo=python&color=3776AB)](https://www.python.org/)
[![R](https://img.shields.io/badge/-r-black?style=for-the-badge&logoColor=white&logo=r&color=276DC3)](https://www.r-project.org/)

Relevant GitHub repositories:

| Repository | Description |
| --- | --- |
| [stars-reproduction-protocol](https://github.com/pythonhealthdatascience/stars_reproduction_protocol) | Latex files for reproduction protocol |
| [stars-reproduce-allen-2020](https://github.com/pythonhealthdatascience/stars-reproduce-allen-2020) |Test run of reproducibility protocol on Allen et al. 2020 |
| [stars-reproduction-template](https://github.com/pythonhealthdatascience/stars_reproduction_template) | Template for assessment of computational reproducibility |
| [stars-reproduce-shoaib-2022](https://github.com/pythonhealthdatascience/stars-reproduce-shoaib-2022) | Reproduction study 1: Shoaib and Ramamohan 2022 (Python) |
| [stars-reproduce-huang-2019](https://github.com/pythonhealthdatascience/stars-reproduce-huang-2019) | Reproduction study 2: Huang et al. 2019 (R) |
| [stars-reproduce-lim-2020](https://github.com/pythonhealthdatascience/stars-reproduce-lim-2020) | Reproduction study 3: Lim et al. 2020 (Python) |
| [stars-reproduce-kim-2021](https://github.com/pythonhealthdatascience/stars-reproduce-kim-2021) | Reproduction study 4: Kim et al. 2021 (R) |
| [stars-reproduce-anagnostou-2022](https://github.com/pythonhealthdatascience/stars-reproduce-anagnostou-2022) | Reproduction study 5: Anagnostou et al. 2022 (Python) |
| [stars-reproduce-johnson-2021](https://github.com/pythonhealthdatascience/stars-reproduce-johnson-2021) | Reproduction study 6: Johnson et al. 2021 (R) |
| [stars-reproduce-hernandez-2015](https://github.com/pythonhealthdatascience/stars-reproduce-hernandez-2015) | Reproduction study 7: Hernandez et al. 2015 (Python + R) |
| [stars-reproduce-wood-2021](https://github.com/pythonhealthdatascience/stars-reproduce-wood-2021) | Reproduction study 8: Wood et al. 2021 (R) |

Process followed for each study:

![Workflow](./images/stars_wp1_workflow.png)

<br>
<br>

## 📍 Locating tables and figures from the article

| Figure/Table | Method | Location |
| - | - | - |
| **Figure 1.** Five standards that scientific code should strive to achieve, and the benefits of doing so | Inkscape | `images/5rs.svg` |
| **Figure 2.** Time to complete items in scope for each reproduction, inspired by figure in Krafczyk et al. 2021 | Matplotlib | Created within `pages/reproduction.qmd`, saved as `images/article_times.png` |
| **Figure 3.** Recommendations to support reproduction, with stars to highlight five recommendations considered to have the greatest potential impact. | Inkscape | `images/reproduction_wheel.svg`|
| **Figure 4.** Recommendations to support troubleshooting and reuse | Inkscape | `images/troubleshooting_wheel.svg` |
| **Figure 5.** Of the eight healthcare DES studies evaluated, proportion that met each recommendation in the current STARS framework. | Plotly express | Created within `pages/repo_evaluation.qmd`, saved as `images/stars_criteria.png` |
| **Figure 6.** Of the eight healthcare DES studies evaluated, proportion that met each item in the current STRESS-DES criteria. | Plotly express | Created within `pages/paper_evaluation.qmd`, saved as `stress_criteria.png` |
| **Figure 7.** Of the eight healthcare DES studies evaluated, proportion that met each criteria in the general reporting checklist for DES | Plotly express | Created within `pages/paper_evaluation.qmd`, saved as `ispor_criteria.png` |
| **Table 2.** Evaluation of repositories against ACM badge criteria. | - | Created within `pages/repo_evaluation.qmd`, saved as `data/badges_table.csv` (and Table 2 is an extract from that table) |
| **Table 3.** Proportion of applicable criteria that were fully met, from evaluation of repository or article, alongside the proportion of items reproduced from each study. | - | Combination of two tables: (1) `data/applicable_stars.csv` created within `pages/repo_evaluation.qmd`, and (2) `data/applicable_report.csv` created within `pages/paper_evaluation.qmd` |
| **Table D1.** Evaluation of studies against badge criteria - grouped into three themes, as defined by NISO. | - | Created within `pages/repo_evaluation.qmd`, saved as `data/badges_table.csv` |

The remaining tables were created directly in the Latex article, rather than in this repository, as they are not describing results from reproduction:

* **Table 1.** Description of the included studies.
* **Table 4.** Simple checklists to assist reviewers in assessing the openness, longevity, and reproducibility of DES models during peer review.
* **Table B1.** Links for reproduction and evaluation.
* **Table B2.** Links to original study repositories.

<br>
<br>

## 📖 View book locally

The [website](https://pythonhealthdatascience.github.io/stars_wp1_summary/) is a quarto book hosted with GitHub pages. If you want to view the book locally on your own machine you will need to:

1. Clone GitHub repository

```
git clone https://github.com/pythonhealthdatascience/stars_wp1_summary.git
```

2. Create the virtual environment

```
virtualenv stars_wp1_summary
source stars_wp1_summary/bin/activate
pip install -r requirements.txt
```

3. Create the book

```
quarto render
```

4. Open the book in your browser (open the `_book/index.html` file).

<br>
<br>

## 📝 Citation

This repository has been archived on Zenodo and can be cited as:

> Heather, A., Monks, T., & Harper, A. (2025). Computational Reproducibility Assessments: Summary. Zenodo. <https://doi.org/10.5281/zenodo.14267268>.

If you wish to cite this repository on GitHub, please refer to the citation file `CITATION.cff`, and the auto-generated alternatives `citation_apalike.apa` and `citation_bibtex.bib`. Authors:

| Member | ORCID | GitHub |
| --- | --- | --- |
| Amy Heather | [![ORCID: Heather](https://img.shields.io/badge/ORCID-0000--0002--6596--3479-brightgreen)](https://orcid.org/0000-0002-6596-3479) | https://github.com/amyheather |
| Thomas Monks | [![ORCID: Monks](https://img.shields.io/badge/ORCID-0000--0003--2631--4481-brightgreen)](https://orcid.org/0000-0003-2631-4481) | https://github.com/TomMonks |
| Alison Harper | [![ORCID: Harper](https://img.shields.io/badge/ORCID-0000--0001--5274--5037-brightgreen)](https://orcid.org/0000-0001-5274-5037) | https://github.com/AliHarp |

<br>
<br>

## 💰 Funding

This project is supported by the Medical Research Council [grant number [MR/Z503915/1](https://gtr.ukri.org/projects?ref=MR%2FZ503915%2F1)].
