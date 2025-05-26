# Tangent Bundle Elastica for Contour Completion

This repository contains the code implementation for the paper: **"Tangent Bundle Elastica and Computer Vision"** [TPAMI 2014](https://ieeexplore.ieee.org/abstract/document/6866207). The paper explores the mathematical framework of elastica in the tangent bundle and its applications in computer vision. The code provides functionalities for elastica calculations, visualization, and utility functions to support the concepts introduced in the paper.

## Introduction

The **Tangent Bundle Elastica** framework introduces a novel approach to modeling and analyzing curves in the tangent bundle, with applications in computer vision tasks for contour completion. This repository provides the tools to reproduce the results and experiments presented in the paper, as well as utilities for further exploration of methods related to elastica in tangent bundle.

## Installation

To install the required dependencies, run:

```
pip install -r requirements.txt
```

## Usage

The main functionality is provided in the `elastica.py` file located in the `src` directory. You can use the functions defined in this file to perform elastica calculations.

### Example Usage

To see example usage, check the `ElasticaTB_Examples.ipynb` file in the `notebooks/` directory. This file demonstrates how to generate and visualize elastica curves. Other notebooks in the `notebooks/` directory provide additional examples and visualizations of the elastica framework.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue for any suggestions or improvements.

## Realted paper

For more details on the mathematical framework and applications, refer to the original paper: 
* [Ohad Ben-Shahar, Guy Ben-Yosef, "Tangent Bundle Elastica and Computer Vision", IEEE Transactions on Pattern Analysis and Machine Intelligence (PAMI), 2014](https://ieeexplore.ieee.org/abstract/document/6866207). 

Other related paper on contour completion using tangent bundle theory:
* [Guy Ben-Yosef, Ohad Ben-Shahar, "A Tangent Bundle Theory for Visual Curve Completion", IEEE Transactions on Pattern Analysis and Machine Intelligence (PAMI), 2012](https://ieeexplore.ieee.org/abstract/document/6112765).
* [Guy Ben-Yosef, Ohad Ben-Shahar, "Minimum length in the tangent bundle as a model for curve completion", IEEE Computer Vision and Pattern Recognition (CVPR), 2010, (oral presentation)](https://ieeexplore.ieee.org/abstract/document/5539930).
* [Guy Ben-Yosef, Ohad Ben-Shahar, "Tangent Bundle Curve Completion with Locally Connected Parallel Networks", Neural Computation, 2012](https://direct.mit.edu/neco/article-abstract/24/12/3277/7834/Tangent-Bundle-Curve-Completion-with-Locally).
* [Guy Ben-Yosef, Ohad Ben-Shahar, "A Biologically-Inspired Theory for Non-axiomatic Parametric Curve Completion", Asian Conference on Computer Vision  (ACCV), 2010](https://link.springer.com/chapter/10.1007/978-3-642-19309-5_27)

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
## Related Repositories:

For a detailed implementation of the **Minimum Length in the Tangent Bundle** model, please visit the following repository:

- [Minimum Length in the Tangent Bundle (MLTB)](https://github.com/guybenyosef/MLTB): This repository provides the code and resources for the Minimum Length in the Tangent Bundle model, as described in the related paper: *"Minimum length in the tangent bundle as a model for curve completion" (CVPR 2010)*, and *"A Tangent Bundle Theory for Visual Curve Completion" (PAMI 2012)*. It includes implementations of the model, experiments, and visualizations.

