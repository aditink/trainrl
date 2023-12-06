# cython: language_level=3

import sys
import traceback
sys.path.insert(0, '')

from predictor import predict
from predictor import init

ctypedef public struct action:
    long double a1
    long double a2
    long double a3
    long double a4

ctypedef public struct state:
    long double train1pos
    long double train2pos
    long double train1vel
    long double train2vel
    int ma1start
    int ma2start
    int ma1end
    int ma2end

cdef public action call_predict(state obs):
    try:
        lst = predict(obs)
        acts = action(lst[0], lst[1], lst[2], lst[3])
    except:
        print("Predict failed. Traceback: ")
        traceback.print_exc()
    return acts

cdef public void call_init():
    try:
        init()
    except:
        print("Init failed. Traceback: ")
        traceback.print_exc()