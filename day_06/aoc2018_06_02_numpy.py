# Advent of Code 2018
# Day 5: Alchemical Reduction -- Part 2 using numpy

import numpy as np
import matplotlib.pyplot as plt


coords = np.loadtxt('input.txt', delimiter=', ')

xvalues = np.arange(coords[:, 0].max())
yvalues = np.arange(coords[:, 1].max())
xx, yy = np.meshgrid(xvalues, yvalues)

layers = []
for coord in coords:
    mdists = np.abs(xx - coord[0]) + np.abs(yy - coord[1])
    layers.append(mdists)

dist_arr = np.array(layers)
# print(dist_arr.shape)

tot_dists = dist_arr.sum(axis=0)
print((tot_dists < 10000).sum())