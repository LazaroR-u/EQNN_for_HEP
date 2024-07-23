# Equivariant Quantum Neural Networks for High Energy Physics Analysis at the LHC

<p align="center">
  <img src="https://github.com/LazaroR-u/EQNN/assets/80428982/63d3cc7b-f42f-4989-b203-4cce5eaff822" alt="image">
</p>


## Organization
[Machine Learning For Science (ML4SCI)](https://ml4sci.org/)

## Contributor
[Lazaro Diaz](https://www.linkedin.com/in/lazaro-raul-diaz-lievano/)

## Mentors
- [KC Kong](https://physics.ku.edu/people/kong-kyoungchul)
- [Konstantin Matchev](https://www.phys.ufl.edu/~matchev/)
- [Katia Matcheva](https://www.phys.ufl.edu/wp/index.php/people/faculty/katia-matcheva/)
- [Sergei Gleyzer](http://sergeigleyzer.com/)


[Equivariant Quantum Neural Networks for High Energy Physics Analysis at the LHC. Mid-Evaluation Report.](https://medium.com/@214lievano/equivariant-quantum-neural-networks-for-high-energy-physics-analysis-at-the-lhc-59b55ed3d43e)


## Introduction

The investigation of symmetries has long been a cornerstone in the analysis of physical systems. As formalized by Noether’s theorem, conserved quantities are inherently linked to the symmetries present within the system. In the realm of high-energy physics, the study of symmetries has played a pivotal role in shaping the Standard Model, which elucidates three of the four fundamental forces in nature. 

Recent research has showcased the efficacy of Equivariant Quantum Neural Networks (EQNNs) in leveraging symmetries within variational quantum machine learning (VQML), thereby augmenting model performance and efficiency. This project is dedicated to delving into a spectrum of symmetries, encompassing both discrete and continuous forms, to enrich the capabilities of EQNNs. The endeavor involves crafting a comprehensive framework for constructing Equivariant Quantum Convolutional Neural Networks (EQCNNs) tailored to image symmetries like rotations and reflections over the X and Y axes. By establishing such a framework, the creation and application of equivariant neural networks will be streamlined, thus facilitating their deployment in addressing challenges encountered in high-energy physics.

Specifically, this work aims to use the implemented EQCNN to classify quark-versus-gluon-initiated jet events from the dataset constructed by [Andrews et al.](https://www.sciencedirect.com/science/article/pii/S0168900220307002?via%3Dihub) and [electron-photon events](https://indico.cern.ch/event/567550/papers/2629451/files/7515-end-end-event_v4.pdf).

## Installation

````
git clone https://github.com/LazaroR-u/EQNN_for_HEP.git
cd Equivariant_QCNN
python3 -m venv env
source env/bin/activate
pip install -r ../requirements.txt
````

## References

1. Andrews, M., Alison, J., An, S., Bryant, P., Burkle, B., Gleyzer, S., Narain, M., Paulini, M., Poczos, B., & Usai, E. (2019). End-to-End Jet Classification of Quarks and Gluons with the CMS Open Data. Nucl. Instrum. Methods Phys. Res. A 977, 164304 (2020). [https://doi.org/10.1016/j.nima.2020.164304](https://doi.org/10.1016/j.nima.2020.164304)

2. Andrews, M., Paulini, M., Gleyzer, S., & Poczos, B. (2018). End-to-End Event Classification of High-Energy Physics Data. Journal of Physics: Conference Series, Volume 1085, Issue 4. [https://dx.doi.org/10.1088/1742-6596/1085/4/042022](https://dx.doi.org/10.1088/1742-6596/1085/4/042022)





