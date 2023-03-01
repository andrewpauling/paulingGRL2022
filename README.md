paulingGRL2022
==============================
[![Build Status](https://github.com/andrewpauling/paulinggrl2022/workflows/Tests/badge.svg)](https://github.com/andrewpauling/paulinggrl2022/actions)
[![codecov](https://codecov.io/gh/andrewpauling/paulingGRL2022/branch/main/graph/badge.svg?token=ZMJO2T9246)](https://codecov.io/gh/andrewpauling/paulingGRL2022)
[![License:BSD-3-Clause](https://img.shields.io/badge/License-BSD%203--Clause-lightgray.svg?style=flt-square)](https://opensource.org/licenses/BSD-3-Clause)
[![pypi](https://img.shields.io/pypi/v/paulinggrl2022.svg)](https://pypi.org/project/paulinggrl2022)

Code to reproduce results from Pauling et al. "The climate response to the Mt Pinatubo eruption does not constrain climate sensitivity"

--------

#### Instructions

- Clone this repository
- Install the conda environment by running:
```
conda env create -f environment.yml
conda activate paulinggrl2022
```
- Install local code in to the environment by running:
```
python setup.py develop
```
- Download required model and observational output by running:
```
cd data
./getdata.sh
```

Running the notebook `wpi_vs_ecs.ipynb`requires a large amount of CMIP6 output. This can be obtained from various CMIP6 data repositories. See instructions within that notebook to get the right data.

<p><small>Project based on the <a target="_blank" href="https://github.com/jbusecke/cookiecutter-science-project">cookiecutter science project template</a>.</small></p>

The Jupyter notebooks to reproduce the results of the paper are in the notebooks subdirectory. The data needed for the figures can be obtained from the Zenodo repository [here](https://doi.org/10.5281/zenodo.7553001) and should be downloaded by the `getdata.sh`script..

The raw CMIP6 output needed to compute the warm pool index used in the Supporting Information (not provided) can be obtained from [here](https://esgf-node.llnl.gov/projects/esgf-llnl) and were downloaded using [cmip6_downloader](https://github.com/tloureiro/cmip6_downloader).

The equilibrium climate sensitivity (ECS) values were taken from the [Github repository](https://github.com/mzelinka/cmip56_forcing_feedback_ecs) of Mark Zelinka which was associated with [Zelinka et al., 2020](https://doi.org/10.1029/2019GL085782). These data are also downloaded by `getdata.sh`.
