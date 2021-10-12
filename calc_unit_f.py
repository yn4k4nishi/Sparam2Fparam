#! /usr/bin/python3

import sys
import csv
import numpy as np
from scipy.linalg import sqrtm
from scipy.linalg import fractional_matrix_power

N = 5 # cell number

def main():

    freq = []  # frequency
    F_t = []    # transmission line
    F_p = []    # port

    with open(sys.argv[1]) as f:
        reader = csv.reader(f)
        header = reader.__next__()

        for row in reader:
            freq.append(row[0])

            A = float(row[1]) + 1j * float(row[2])
            B = float(row[3]) + 1j * float(row[4])
            C = float(row[5]) + 1j * float(row[6])
            D = float(row[7]) + 1j * float(row[8])

            F_t.append(np.matrix([[A,B],[C,D]]))
    
    with open(sys.argv[2]) as f:
        reader = csv.reader(f)
        header = reader.__next__()

        for row in reader:

            A = float(row[1]) + 1j * float(row[2])
            B = float(row[3]) + 1j * float(row[4])
            C = float(row[5]) + 1j * float(row[6])
            D = float(row[7]) + 1j * float(row[8])

            F_ps = np.matrix([[A,B],[C,D]])

            F_p.append(sqrtm(F_ps))



    print("freq[GHz], re(A), im(A), re(B), im(B), re(C), im(C), re(D), im(D)")

    for i in range(len(freq)):
        F_t[i] = np.linalg.inv(F_p[i]) * F_t[i] * np.linalg.inv(F_p[i])
        F_unit = fractional_matrix_power(F_t[i], 1/N)
        
        print(freq[i], end=',')
        print(F_unit[0][0].real, end=',')
        print(F_unit[0][0].imag, end=',')
        print(F_unit[0][1].real, end=',')
        print(F_unit[0][1].imag, end=',')
        print(F_unit[1][0].real, end=',')
        print(F_unit[1][0].imag, end=',')
        print(F_unit[1][1].real, end=',')
        print(F_unit[1][1].imag)


if __name__ == "__main__":
    main()