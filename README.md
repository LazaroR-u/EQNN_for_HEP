# Equivariant Quantum Neural Networks


## Summary

So far, we have successfully implemented an equivariant quantum convolutional neural network (EQCNN) that maintains invariance under the p4m symmetry group, which includes rotations of 90° and reflections over the X and Y axes. The model has demonstrated strong performance on both benchmark datasets: MNIST and Fashion MNIST.

## Introduction

The investigation of symmetries has long been a cornerstone in the analysis of physical systems. As formalized by Noether’s theorem, conserved quantities are inherently linked to the symmetries present within the system. In the field of high-energy physics, the study of symmetries has played a key role in shaping the Standard Model, which describes three of the four fundamental forces in nature. 

New studies have demonstrated the effectiveness of Equivariant Quantum Neural Networks (EQNNs) in utilizing symmetries in quantum machine learning (QML). The project focuses on exploring various symmetries present in image datasets, such as reflections, rotations, and translations. The goal is to develop a comprehensive framework for building Equivariant Quantum Convolutional Neural Networks (EQCNNs) specifically designed for image symmetries as roto-rotation symmetry, which consists of rotations by 90° and reflections along the X and Y axes. By establishing this framework, we aim to simplify the creation and use of equivariant neural networks, making it easier to apply them to address challenges in high-energy physics.


## Datasets

- **MNIST**: A large database of handwritten digits commonly used for training and testing various image processing systems. It consists of 60,000 training images and 10,000 testing images, each of size 28x28 pixels in grayscale.

- **Fashion MNIST**: Similar to the MNIST dataset but contains images of clothing items such as shirts, trousers, and shoes. It also consists of 60,000 training images and 10,000 testing images, each of size 28x28 pixels in grayscale.

## Structure

### Equivariant_QCNN/
It Contains the modules to develop Equivariant Quantum Convolutional Neural Networks (EQCNN) and generic Quantum Convolutional Neural Networks (QCNN) with different quantum convolutional filters.

Modules:
- **data.py**: defines a function to load and process datasets.
- **embedding.py**: matches the embedding type to encode classical data into quantum states.
- **unitary.py**: contains the set of convolutional filters and pooling layers.
- **QCNN_circuit.py**: constructs the EQCNN and QCNN architectures.
- **Training.py**: defines cost functions (MSE and BCE) and trains the model for a given architecture, dataset, and hyperparameters.
- **prueba.py**: module just for testing.
- **Benchmarking.py**: defines the accuracy and a function to benchmark different given models.
- **result.py**: executes the benchmarking function for a given set of models, types of encodings, a dataset, and a cost function. Returns the loss history and accuracy for each model and setting.
- **CNN.py**: performs benchmarking for different settings for classical Convolutional Neural Networks.
- **hep_dataset_processing.py**: loads and preprocesses the HEP datasets.

Notebooks:
- **Fashion_MNIST_EQCNN.ipynb**
- **MNIST_EQCNN.ipynb**
- **results_benchmark_EQCNNvsQCNN.ipynb**

## demos_notebooks/
Here we have the same Jupyter Notebook examples of EQCNN to perform binary classification on MNIST and Fashion MNIST datasets.

## test/
Here you can find Jupyter notebooks that run on Google Colab:
- **p4m_EQCNN_mnist.ipynb** 
- **REFLECTION_EQNN_mnist.ipynb**
- **Quark_gluon_study_CNN_testing.ipynb** (to get the dataset, send me an email)

Additional:
- **requirements.txt**: Lists all the necessary packages to run the code.




## References

1. Andrews, M., Alison, J., An, S., Bryant, P., Burkle, B., Gleyzer, S., Narain, M., Paulini, M., Poczos, B., & Usai, E. (2019). End-to-End Jet Classification of Quarks and Gluons with the CMS Open Data. Nucl. Instrum. Methods Phys. Res. A 977, 164304 (2020). [https://doi.org/10.1016/j.nima.2020.164304](https://doi.org/10.1016/j.nima.2020.164304)

2. Andrews, M., Paulini, M., Gleyzer, S., & Poczos, B. (2018). End-to-End Event Classification of High-Energy Physics Data. Journal of Physics: Conference Series, Volume 1085, Issue 4. [https://dx.doi.org/10.1088/1742-6596/1085/4/042022](https://dx.doi.org/10.1088/1742-6596/1085/4/042022)

3. Chang, Su Yeon, Michele Grossi, Bertrand Le Saux, y Sofia Vallecorsa. Approximately Equivariant Quantum Neural Network for $p4m$ Group Symmetries in Images. En 2023 IEEE International Conference on Quantum Computing and Engineering (QCE), 229-35, 2023. [https://doi.org/10.1109/QCE57702.2023.00033](https://doi.org/10.1109/QCE57702.2023.00033).

4. Hur, Tak, Leeseok Kim, y Daniel K. Park. Quantum convolutional neural network for classical data classification. Quantum Machine Intelligence 4, n.o 1 (junio de 2022): 3. [https://doi.org/10.1007/s42484-021-00061-x](https://doi.org/10.1007/s42484-021-00061-x).

5. West, Maxwell T., Martin Sevior, y Muhammad Usman. Reflection Equivariant Quantum Neural Networks for Enhanced Image Classification. Machine Learning: Science and Technology 4, n.o 3 (1 de septiembre de 2023): 035027. [https://doi.org/10.1088/2632-2153/acf096](https://doi.org/10.1088/2632-2153/acf096).

6.  Nguyen, Quynh T., Louis Schatzki, Paolo Braccia, Michael Ragone, Patrick J. Coles, Frederic Sauvage, Martin Larocca, y M. Cerezo. Theory for Equivariant Quantum Neural Networks. PRX Quantum 5, n.o 2 (6 de mayo de 2024): 020328. [https://doi.org/10.1103/PRXQuantum.5.020328](https://doi.org/10.1103/PRXQuantum.5.020328).



