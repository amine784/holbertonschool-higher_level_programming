#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    for i in dir(hidden_4):
        delim = "__"
        if delim not in i:
            print("{:s}", format(i))
