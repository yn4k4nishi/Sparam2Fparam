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

            A = 1/2 * ((1-S22)/S21 + S12)
            B = Z/2 * ((1+S22)/S21 - S12)
            C = 1/2/Z * ((1-S22)/S21 - S12)
            D = 1/2 * ((1+S22)/S21 + S12)

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
