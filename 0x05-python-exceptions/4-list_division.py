#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    for i in range(0, list_length):
        try:
            res = my_list_1[i] / my_list_2[i]
        except TypeError:
                print("Wrong Input")
                res = 0
        except ZeroDivisionError:
                print("Divison cannot be done with 0")
                res = 0
        except IndexError:
                print("Wrong Range")
                res = 0
        finally:
            new_list.append(res)
    return new_list