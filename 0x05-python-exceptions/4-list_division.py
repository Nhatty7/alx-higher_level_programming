#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    cnt = 0
    len = []
    while cnt < list_length:
        try:
            res = my_list_1[cnt] / my_list_2[cnt]
        except ZeroDivisionError:
            res = 0
            print("division by 0")
        except TypeError:
            res = 0
            print("wrong type")
        except IndexError:
            res = 0
            print("out of range")
        finally:
            cnt += 1
            len.append(res)
    return len
