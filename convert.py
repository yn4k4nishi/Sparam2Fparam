#! /usr/bin/python3

import sys
import csv
import numpy as np


def main():
    
    with open(sys.argv[1]) as f:

        reader = csv.reader(f)
        
        header = reader.__next__()
        while header[0] != "Freq(Hz)":
            header = reader.__next__()
        
        print("freq[GHz], re(S11), im(S11), re(S12), im(S12) re(S21), im(S21), re(S22), im(S22)")
        for row in reader:
            if row[0] == "END":
                break

            print(row[0], end=',')

            S11 = np.power(10,float(row[1])/20)
            S21 = np.power(10,float(row[2])/20)
            S12 = np.power(10,float(row[3])/20)
            S22 = np.power(10,float(row[4])/20)

            S11 = S11 * np.cos(float(row[5])/180*np.pi) + 1j * S11 * np.sin(float(row[5])/180*np.pi)
            S21 = S21 * np.cos(float(row[6])/180*np.pi) + 1j * S21 * np.sin(float(row[6])/180*np.pi)
            S12 = S12 * np.cos(float(row[7])/180*np.pi) + 1j * S12 * np.sin(float(row[7])/180*np.pi)
            S22 = S22 * np.cos(float(row[8])/180*np.pi) + 1j * S22 * np.sin(float(row[8])/180*np.pi)

            print(S11.real, end=',')
            print(S11.imag, end=',')
            print(S12.real, end=',')
            print(S12.imag, end=',')
            print(S21.real, end=',')
            print(S21.imag, end=',')
            print(S22.real, end=',')
            print(S22.imag)


if __name__ == "__main__":
    main()