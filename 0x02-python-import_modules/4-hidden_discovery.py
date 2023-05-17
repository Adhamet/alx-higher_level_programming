#!/usr/bin/python3
import hidden_4

if __name__ == "__main__":
    for ele in dir(hidden_4):
        if ele[:2] != "__":
            print("{}".format(ele))
