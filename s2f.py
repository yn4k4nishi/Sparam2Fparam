#! /usr/bin/python3

import sys
import csv
import numpy as np

Z = 50 # ohm

def main():

    with open(sys.argv[1]) as f:

        reader = csv.reader(f)
        header = reader.__next__()

        print("freq[GHz], re(A), im(A), re(B), im(B), re(C), im(C), re(D), im(D)")
        
        for row in reader:
            print(row[0], end=',')
            
            S11 = float(row[1]) + 1j * float(row[2])
            S12 = float(row[3]) + 1j * float(row[4])
            S21 = float(row[5]) + 1j * float(row[6])
            S22 = float(row[7]) + 1j * float(row[8])

            k1 = 1/2/np.sqrt(Z) - S11/2/np.sqrt(Z)
            k2 = -np.sqrt(Z)/2 - np.sqrt(Z)/2*S11
            k3 = S12/2/np.sqrt(Z)
            k4 = -np.sqrt(Z)/2
            
            l1 = S21/2/np.sqrt(Z)
            l2 = np.sqrt(Z)*S21/2
            l3 = 1/2/np.sqrt(Z) - S22/2/np.sqrt(Z)
            l4 = np.sqrt(Z)/2 + np.sqrt(Z)*S22/2

            A = (k3-k2*l3/l2)/(k1-k2*l1/l2)
            B = (k4-k2*l4/l2)/(k1-k2*l1/l2)
            C =  l3/l2 - l1/l2 * (k3-k2*l3/l2)/(k1-k2*l1/l2)
            D =  l4/l2 - l1/l2 * (k4-k2*l4/l2)/(k1-k2*l1/l2)

            print(A.real, end=',')
            print(A.imag, end=',')
            print(B.real, end=',')
            print(B.imag, end=',')
            print(C.real, end=',')
            print(C.imag, end=',')
            print(D.real, end=',')
            print(D.imag)


if __name__ == "__main__":
    main()
