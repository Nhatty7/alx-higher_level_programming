#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    cnt = 0
    err = 0
    while cnt < x:
        try:
            print("{:d}".format(my_list[cnt]), end='')
            cnt += 1
        except (ValueError, TypeError):
            cnt += 1
            err += 1
    cnt -= err
    print()
    return cnt
