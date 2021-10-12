#! /usr/bin/python3

import sys
import csv
import numpy as np
import matplotlib.pyplot as plt


def main():

    freq = []
    beta_d = []
    Z_bloch = []

    with open(sys.argv[1]) as f:
        reader = csv.reader(f)
        header = reader.__next__()

        for row in reader:
            freq.append(float(row[0]))

            A = float(row[1]) + 1j * float(row[2])
            B = float(row[3]) + 1j * float(row[4])
            C = float(row[5]) + 1j * float(row[6])
            D = float(row[7]) + 1j * float(row[8])

            print(A+D)

            beta_d.append(np.arccos((A+D)/2))
            Z_bloch.append(np.sqrt(B/C))

    plt.figure(figsize=(24.0, 16.0))

    plt.subplot(1,2,1)
    plt.scatter(beta_d, freq)
    plt.scatter([ -i for i in beta_d], freq)

    plt.subplot(1,2,2)
    plt.scatter(freq, Z_bloch)

    plt.show()



if __name__ == "__main__":
    main()