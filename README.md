![test-suite](https://github.com/Sparrow0hawk/walkers/workflows/test-suite/badge.svg) 
[![codecov](https://codecov.io/gh/Sparrow0hawk/walkers/branch/master/graph/badge.svg)](https://codecov.io/gh/Sparrow0hawk/walkers)
[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=Sparrow0hawk_walkers&metric=alert_status)](https://sonarcloud.io/dashboard?id=Sparrow0hawk_walkers)

# Walkers a Python random walker implementation with GUI

![Hundreds of walkers](https://github.com/Sparrow0hawk/walkers/blob/develop/examples/outputs/hundreds.png)

An object orientated dummy world and agents model. This repository includes tools for creating worlds populated with agents that randomly walk around.

## Installing

This package can be installed from source and required [conda package manager](https://docs.conda.io/en/latest/) to recreate the working environment for runtime.

```bash
$ git clone https://github.com/Sparrow0hawk/walkers.git

$ cd walkers

$ conda env create -f environment.yml && conda activate myenv

$ python setup.py install

$ pytest

```

# Example(s)

You can find an example program using this package in the [examples](https://github.com/Sparrow0hawk/walkers/tree/master/examples) folder including use of matplotlib to visualise outputs.

# TODO

- [ ] Implementing a GUI
