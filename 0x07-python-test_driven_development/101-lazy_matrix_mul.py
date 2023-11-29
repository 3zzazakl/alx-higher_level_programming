#!/usr/bin/python3
"""Define matrix function using numpy"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """"
    Return results of two matrics
    """
    return (np.matmul(m_a, m_b))
