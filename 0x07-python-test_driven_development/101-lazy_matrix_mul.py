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
    if type(m_a) != list:
        raise TypeError("m_a must be a list")
    if type(m_b) != list:
        raise TypeError("m_b must be a list")
    a = np.array(m_a)
    b = np.array(m_b)
    return a.dot(b)
