# This generates the results of the bechmarking code

import Benchmarking


"""
Here are possible combinations of benchmarking user could try.
Unitaries: ['U_TTN', 'U2_equiv', 'U4_equiv', 'U_5', 'U_6', 'U_9', 'U_13', 'U_14', 'U_15', 'U_SO4', 'U_SU4', 'U_SU4_no_pooling', 'U_SU4_1D', 'U_9_1D']
U_num_params: [2, 10, 10, 2, 6, 6, 4, 6, 15, 15, 15, 2]
Encodings: ['img16x16x1','resize256', 'pca8', 'autoencoder8', 'pca16-compact', 'autoencoder16-compact', 'pca32-1', 'autoencoder32-1',
            'pca16-1', 'autoencoder16-1', 'pca30-1', 'autoencoder30-1', 'pca12-1', 'autoencoder12-1']
dataset: 'mnist' or 'fashion_mnist'
circuit: 'QCNN' or 'Hierarchical'
cost_fn: 'mse' or 'cross_entropy'
Note: when using 'mse' as cost_fn binary="True" is recommended, when using 'cross_entropy' as cost_fn must be binary="False".
"""


# invariant testings

# U4_equiv is not invariant with mse cost function
# U4_equiv is invariant only under reflections over Y and almost X using cross_entropy

# U2_equiv is invariant under p4m using MSE
# U2_equiv is invariant under reflections over X using cross_entropy 

Unitaries = ['U4_equiv','U2_equiv', "U_15"] #, 'U4_equiv', 'U_SU4', 'U_SU4_1D']

U_num_params = [6, 6, 15] #,6, 15, 15]
Encodings = ["img16x16x1"]
dataset = 'mnist'
classes = [0,1]
binary = True
cost_fn = 'mse'
Benchmarking.Benchmarking(dataset, classes, Unitaries, U_num_params, Encodings, circuit='QCNN', cost_fn=cost_fn, binary=binary)
#Benchmarking.Benchmarking(dataset, classes, Unitaries, U_num_params, Encodings, circuit='Hierarchical', cost_fn=cost_fn, binary=binary)

