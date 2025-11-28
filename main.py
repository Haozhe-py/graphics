import pandas as pd
import argparse

# Initialize argument parser
parser = argparse.ArgumentParser(description='Draw a graphic from a CSV file.')
parser.add_argument('-f', '--file', help='File path of the CSV file')
parser.add_argument('-xkey', '--x-key', default='x', help='Key of the x-axis')
parser.add_argument('-ykey', '--y-key', default='y', help='Key of the y-axis')
parser.add_argument('-fmt', default='png', help='The format of output file')

