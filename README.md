<h1 align="center">
  <a href="https://github.com/pythonhealthdatascience"><img src="https://raw.githubusercontent.com/pythonhealthdatascience/stars_wp1_summary/main/images/stars_banner.png" alt="Markdownify"></a>
  <br>
  STARS Work Package 1 Summary
  <br>
</h1>

<p align="center">
  <i align="center">Summary of the six computational reproducibility assessments conducted as part of STARS Work Package 1.</i>
</p>

<p align="center">
    <!--<a href="#"><img src="https://img.shields.io/github/v/release/pythonhealthdatascience/stars_wp1_summary" alt="GitHub release" /></a>
    <a href="#"><img src="https://img.shields.io/github/release-date/pythonhealthdatascience/stars_wp1_summary" alt="GitHub release date" /></a>-->
    <a href="#"><img src="https://img.shields.io/github/last-commit/pythonhealthdatascience/stars_wp1_summary" alt="GitHub last commit" /></a>
    <a target="_blank" href="https://github.com/pythonhealthdatascience/stars_wp1_summary/blob/main/LICENSE"><img src="https://img.shields.io/badge/license-CC--BY--4.0-blue.svg" alt="MIT licence"/></a>
    <a href="#"><img src="https://github.com/pythonhealthdatascience/stars_wp1_summary/actions/workflows/cff_validation.yaml/badge.svg" alt="Valid CITATION.cff" /></a>
</p>

## Table of contents

* [👋 About the repository](#-about-the-repository)
* [📖 View book locally](#-view-book-locally)
* [📝 Citation](#-citation)
* [💰 Funding](#-funding)

<br>
<br>

## 👋 About the repository

In work package 1, we assessed the computational reproducibility of six discrete-event simulation papers with models in Python and R. The reproductions and findings are summarised at: <https://pythonhealthdatascience.github.io/stars_wp1_summary/>.

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

If you wish to cite this repository, please refer to the citation file `CITATION.cff`, and the auto-generated alternatives `citation_apalike.apa` and `citation_bibtex.bib`. Authors:

| Member | ORCID | GitHub |
| --- | --- | --- |
| Amy Heather | [![ORCID: Heather](https://img.shields.io/badge/ORCID-0000--0002--6596--3479-brightgreen)](https://orcid.org/0000-0002-6596-3479) | https://github.com/amyheather |
| Thomas Monks | [![ORCID: Monks](https://img.shields.io/badge/ORCID-0000--0003--2631--4481-brightgreen)](https://orcid.org/0000-0003-2631-4481) | https://github.com/TomMonks |
| Alison Harper | [![ORCID: Harper](https://img.shields.io/badge/ORCID-0000--0001--5274--5037-brightgreen)](https://orcid.org/0000-0001-5274-5037) | https://github.com/AliHarp |

<br>
<br>

## 💰 Funding

This project is supported by the Medical Research Council [grant number [MR/Z503915/1](https://gtr.ukri.org/projects?ref=MR%2FZ503915%2F1)].
