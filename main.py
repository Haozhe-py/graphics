import pandas as pd
import argparse
import numpy as np
import matplotlib.pyplot as plt
import sys

# Initialize argument parser
parser = argparse.ArgumentParser(description='Draw a graphic from a CSV file.')
parser.add_argument('-f', '--file', help='File path of the CSV file')
parser.add_argument('-xkey', '--x-key', default='x', help='Key of the x-axis')
parser.add_argument('-ykey', '--y-key', default='y', help='Key of the y-axis')
parser.add_argument('-fmt', default='png', help='The format of output file')

# Solve problems of Matplotlib
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False  

# Main function
def main(file, xkey, ykey, fmt):
    print(file, xkey, ykey, fmt)

    data = pd.read_csv(file)

    xs = np.array(data[xkey])
    ys = np.array(data[ykey])

    plt.set_xlabel(xkey, fontsize=12)
    plt.set_ylabel(ykey, fontsize=12)

    output_name = f'output{"." if fmt[0]!="." else ""}{fmt}'
    plt.plot(xs, ys)
    plt.savefig(output_name, bbox_inches='tight')
    print(f'Graphic saved to {output_name} successfully. ')

    return

# Run
if __name__ == '__main__':
    args = parser.parse_args()
    main(vars(args).values())
    sys.exit(0)