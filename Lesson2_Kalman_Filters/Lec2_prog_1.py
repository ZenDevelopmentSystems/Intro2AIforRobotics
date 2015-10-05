# -*- coding: utf-8 -*-
"""
Created on Sat Sep 19 18:26:41 2015

@author: apollo
"""
from math import *

def f(mu, sigma2, x):
    return 1/sqrt(2.*pi*sigma2)*exp(-.5*(x-mu)**2/sigma2)
    
def new_mean(mu_pr, mu_meas, sig2_pr, sig2_meas):
    return (1/(sig2_pr+sig2_meas))*(sig2_meas*mu_pr+sig2_pr*mu_meas)
    
def new_sig2(sig2_pr, sig2_meas):
    return 1/((1/sig2_pr)+(1/sig2_meas))
    
def predict(mean1, var1, mean2, var2):
    new_mean = mean1 + mean2
    new_var = var1 + var2
    
#print( f(10., 4., 8.))
print(new_mean(2, 10, 2, 2))
print(new_sig2(2,2))