#! /usr/bin/python3

import sys
import csv
import numpy as np

Z = 50 # ohm

def main():
    freq = []
    
    S11_mag = []
    S12_mag = []
    S21_mag = []
    S22_mag = []

    S11_ang = []
    S12_ang = []
    S21_ang = []
    S22_ang = []

    S11 = []
    S12 = []
    S21 = []
    S22 = []

    A = []
    B = []
    C = []
    D = []

    # import S param magnitude [dB]
    with open(sys.argv[1]) as f:

        reader = csv.reader(f)
        header = reader.__next__()

        for row in reader:
            freq.append(float(row[0]))
            S11_mag.append(float(row[1]))
            S12_mag.append(float(row[2]))
            S21_mag.append(float(row[3]))
            S22_mag.append(float(row[4]))

    # import S param angle [degree]
    with open(sys.argv[2]) as f:
        reader = csv.reader(f)
        header = reader.__next__()

        for row in reader:
            S11_ang.append(float(row[1]))
            S12_ang.append(float(row[2]))
            S21_ang.append(float(row[3]))
            S22_ang.append(float(row[4]))
    
    # calc S param
    for i in range(len(freq)):
        S11.append( np.power(10, S11_mag[i] / 20) * ( np.cos( S11_ang[i] /180 *np.pi ) + 1j * np.sin( S11_ang[i] /180 *np.pi ) ) )
        S12.append( np.power(10, S12_mag[i] / 20) * ( np.cos( S12_ang[i] /180 *np.pi ) + 1j * np.sin( S12_ang[i] /180 *np.pi ) ) )
        S21.append( np.power(10, S21_mag[i] / 20) * ( np.cos( S21_ang[i] /180 *np.pi ) + 1j * np.sin( S21_ang[i] /180 *np.pi ) ) )
        S22.append( np.power(10, S22_mag[i] / 20) * ( np.cos( S22_ang[i] /180 *np.pi ) + 1j * np.sin( S22_ang[i] /180 *np.pi ) ) )

        k1 = 1/2/np.sqrt(Z) - S11[i]/2/np.ssqrt(Z)
        k2 = -np.sqrt(Z)/2 - np.sqrt(Z)/2*S11[i]
        k3 = S12[i]/2/np.sqrt(Z)
        k4 = -np.sqrt(Z)/2
        
        l1 = S21[i]/2/np.sqrt(Z)
        l2 = np.sqrt(Z)*S21[i]/2
        l3 = 1/2/np.sqrt(Z) - S22[i]/2/np.sqrt(Z)
        l4 = np.sqrt(Z)/2 + np.sqrt(Z)*S22[i]/2

        A.append((k3-k2*l3/l2)/(k1-k2*l1/l2))
        B.append((k4-k2*l4/l2)/(k1-k2*l1/l2))
        C.append( l3/l2 - l1/l2 * (k3-k2*l3/l2)/(k1-k2*l1/l2))
        D.append( l4/l2 - l1/l2 * (k4-k2*l4/l2)/(k1-k2*l1/l2))


if __name__ == "__main__":
    main()
