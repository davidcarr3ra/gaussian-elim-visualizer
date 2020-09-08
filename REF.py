#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  8 00:39:14 2020

@author: davidcarrera
"""

import numpy as np

def REF(input_matrix):
    ef_matrix = EF(input_matrix)
    
    # first pivot = leftmost nonzero element of lowest nonzero column. divide that row by pivot.
    # start at last row. go up until not all elements in it are zero.
    # then move from left to right until the next element is a nonzero. you are at the pivot. divide that row by pivot.
    # multiplier, row reduce
    # now, move up diagonal (--i, --j). leftmost nonzero element is the next pivot
    # repeat until the next pivot is at position 0,0. When that is the case, divide by pivot, return matrix.
    
    rows, columns = ef_matrix.shape
    for i in range(rows-1, -1, -1):
        if(not ef_matrix[i,:].any()):
            continue
        
        pivot = 0
        j = 0
        for j in range(columns):
            if(ef_matrix[i, j] != 0):
                # reached pivot. Scale to 1
                pivot = ef_matrix[i, j]
                ef_matrix[i,:] = ef_matrix[i,:]/pivot
                break

        if(i==0):
            output_matrix = ef_matrix
            return output_matrix
        
        # row reduce above
        row_above = i-1
        for row in range(row_above, -1, -1):
            multiplier = -ef_matrix[row_above, j]/ef_matrix[i, j]
            for column in range(columns):
                ef_matrix[row, column] = ef_matrix[row, column] + ef_matrix[i, column]*multiplier