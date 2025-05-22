# Tangent Bundle Elastica

This repository contains the code implementation for the paper: **"Tangent Bundle Elastica and Computer Vision"** [TPAMI 2014](https://ieeexplore.ieee.org/abstract/document/6866207). The paper explores the mathematical framework of elastica in the tangent bundle and its applications in computer vision. The code provides functionalities for elastica calculations, visualization, and utility functions to support the concepts introduced in the paper.

## Table of Contents

- [Introduction](#introduction)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [Citation](#citation)

## Introduction

The **Tangent Bundle Elastica** framework introduces a novel approach to modeling and analyzing curves in the tangent bundle, with applications in computer vision tasks such as shape analysis and motion tracking. This repository provides the tools to reproduce the results and experiments presented in the paper, as well as utilities for further exploration of elastica-based methods.

## Installation

To install the required dependencies, run:

```
pip install -r requirements.txt
```

## Usage

The main functionality is provided in the `elastica.py` file located in the `src` directory. You can use the functions defined in this file to perform elastica calculations.

### Example

To see example usage, check the `sample_curves.py` file in the `src/examples` directory. This file demonstrates how to generate and visualize elastica curves.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue for any suggestions or improvements.

## Citation

If you use this code in your research, please cite the paper:

```
@article{tangent_bundle_elastica,
  title={Tangent bundle elastica and computer vision},
  author={Ben-Shahar, Ohad and Ben-Yosef, Guy},
  journal={IEEE Transactions on Pattern Analysis and Machine Intelligence},
  volume={37},
  number={1},
  pages={161--174},
  year={2014},
  publisher={IEEE}
}
```

For more details, you can read the paper [here](https://ieeexplore.ieee.org/abstract/document/6866207).