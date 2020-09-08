#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  8 00:38:04 2020

@author: davidcarrera
"""


import numpy as np

def EF(input_matrix): # reduces a numpy matrix (2d np.array) to echelon form
    input_matrix = input_matrix.astype('float64')
    rows, columns = input_matrix.shape
    for i in range(rows):
        j = i
        pivot = 0
        
        # if the row has all zeros, attempt exchange. otherwise, return matrix
        count = i+1
        while(not input_matrix[i,:].any()):
            if(count == rows):
                output_matrix = input_matrix
                return output_matrix
            # otherwise, swap
            temp = input_matrix[i,:].copy()
            input_matrix[i,:] = input_matrix[count,:]
            input_matrix[count,:] = temp
            count += 1
        
        # if all elements in this column are zero, move to the right.
        while(not input_matrix[i:, j].any()):
            j += 1
        
        # choose first nonzero element encountered to be the pivot.
        for row in range(i, rows):
            if(input_matrix[row, j] == 0):
                continue
            else:
                pivot = input_matrix[row, j]
                # swap
                temp = input_matrix[row,:].copy()
                input_matrix[row,:] = input_matrix[i,:]
                input_matrix[i,:] = temp
                break
        pivot_row = i
        row_below = i+1
        for i in range(row_below, rows):
            multiplier = -input_matrix[i, j]/pivot
            # row reduce. replace each element in column below with column above*multiplier + column below
            for column in range(columns):
                input_matrix[i, column] = input_matrix[i, column] + input_matrix[pivot_row, column]*multiplier
    output_matrix = input_matrix
    return output_matrix

