# cython: language_level=3

import sys
import traceback
sys.path.insert(0, '')

from predictor import predict

ctypedef public struct action:
    long double a1
    long double a2
    long double a3
    long double a4


cdef public action call_predict():
    try:
        lst = predict()
        acts = action(lst[0], lst[1], lst[2], lst[3])
    except:
        print("Predict failed. Traceback: ")
        traceback.print_exc()
    return acts