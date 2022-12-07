#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    res = 0.0
    s_lis = list(l[0] * l[1] for l in my_list)
    w_lis = list(l[1] for l in my_list)
    res = sum(s_lis) / sum(w_lis)
    return res
