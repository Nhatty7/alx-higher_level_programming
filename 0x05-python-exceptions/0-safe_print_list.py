#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        cnt = 0
        while cnt < x:
            print("{}".format(my_list[cnt]), end='')
            cnt += 1
        print()
        return cnt
    except IndexError:
        print()
        return cnt
        pass
