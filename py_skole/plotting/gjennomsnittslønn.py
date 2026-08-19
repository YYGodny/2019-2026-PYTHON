import matplotlib.pyplot as plt
import numpy as np

with open('gjennomsnittlig-rslnn.csv', 'r') as f:
    innhold = f.read().split('\n')
    d = dict([tuple(i.split(';')) for i in innhold])
    print(d)
