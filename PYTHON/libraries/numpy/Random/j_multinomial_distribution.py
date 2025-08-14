# This is a generalisation of binomial distrbution
# It decsribes outcomes of multinomial scenarios unlike binomial where scenarios must be only one of two e.g. blood type of a population, dice roll outcome

# It has three parameters:
# n - number of times to run the experiment
# pvals - list of probabilities of outcomes
# size - The shape of the returned array

from numpy import random

x = random.multinomial(n=6, pvals=[1/6,1/6,1/6,1/6,1/6,1/6])
print(x)