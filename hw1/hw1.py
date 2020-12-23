import random
import numpy as np


def main():
    f = open('hw1_train.dat','r')
    data_x = []
    data_y = []
    w = [0]*10
    data = f.readlines()
    output = [-1]*10
    N = 0
    
    for temp in data:
        temp = temp.splitlines()
        temp = temp[0].split("\t")
            
        data_x.append(temp[0:9])
        data_y.append(temp[10])
    
    while(N < 500):
        number = random.randint(0,99)
        N += 1
    

        

   
    
   






main()