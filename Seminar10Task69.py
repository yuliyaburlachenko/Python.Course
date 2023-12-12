#Задача №69. 
#1. Изобразить гистограмму по flipper_length_mm
#с оттенком height_group. Сделать анализ
from pandas import read_csv
from seaborn import histplot
from matplotlib.pyplot import show

penguins = read_csv('penguins.csv')

histplot(penguins, x='flipper_length_mm', hue='height_group')

show()