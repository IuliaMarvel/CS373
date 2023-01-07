# Write a program that will iteratively update and
# predict based on the location measurements 
# and inferred motions shown below. 

import math

def update(mean1, var1, mean2, var2):
    new_mean = float(var2 * mean1 + var1 * mean2) / (var1 + var2)
    new_var = 1./(1./var1 + 1./var2)
    return [new_mean, new_var]

def predict(mean1, var1, mean2, var2):
    new_mean = mean1 + mean2
    new_var = var1 + var2
    return [new_mean, new_var]

measurements = [5., 6., 7., 9., 10.]
motion = [1., 1., 2., 1., 1.]
measurement_sig = 4.
motion_sig = 2.
mu = 0.
sig = 10000.

def iterative_update(measuremens,motions,mu,var):
    for (motion,measure) in zip(motions,measurements):
        mu,var = update(mu,var,measure,measurement_sig)
        mu,var = predict(mu,var,motion,motion_sig)
    return mu,var

mu,sig = iterative_update(measurements,motion,mu,sig)
print [mu, sig]
