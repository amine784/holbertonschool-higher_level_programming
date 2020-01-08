def list_division(my_list_1, my_list_2, list_length):
    res = []
    check = 0
    for i in range(list_length):
        try:
            check = (my_list_1[i] / my_list_2[i])
        except ZeroDivisionError:
            print("division by 0")
            check = 0
        except TypeError:
            print("wrong type")
            check = 0
        except IndexError:
            print("out of range")
            check = 0
        finally:
            res.append(check)
    return(res)
