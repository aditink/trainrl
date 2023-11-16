# cython: language_level=3

import sys
sys.path.insert(0, '')

from predictor import predict

cdef public void call_predict():
    predict()