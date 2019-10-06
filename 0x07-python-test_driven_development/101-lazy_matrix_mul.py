#!/usr/bin/python3
"""My function to multiply a two matrix"""


import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """My multiplication function
    Args:
        m_a: first matrix
        m_b: second matrix
    Returns:
        The return value. m_a * m_b
    """
    a = np.array(m_a)
    b = np.array(m_b)
    return a.dot(b)
