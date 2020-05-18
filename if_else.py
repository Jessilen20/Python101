#!/bin/python3

import math
import os
import random
import re
import sys

def analisis(n):
    if n%2==0:
        if 1<n<6:
           print("not weird")
        if 5<n<21:
           print("Weird")
        if 20<n:
           print("not wierd")      
    else:
       print ("Weird") 

if __name__ == '__main__':
    n = int(input().strip())
    analisis(n)