#Задача №67.
#1. Создать новый столбец в таблице с
#пингвинами, который будет отвечать за
#показатель длины клюва пингвина.
#high - длинный(от 42)
#middle - средний(от 35 до 42)
#low - маленький(до 35)
#Чтобы подключить датасет с пингвинами, воспользуйтесь данным
#скриптом:
#penguins = sns.load_dataset("penguins")
#penguins.head()

from pandas import read_csv

penguins = read_csv('penguins.csv')

penguins.loc[penguins['bill_length_mm'] < 35, 'height_group'] = "low"
penguins.loc[(penguins['bill_length_mm'] > 35) & (penguins['bill_length_mm'] < 42), 'height_group'] = "middle"
penguins.loc[penguins['bill_length_mm'] > 42, 'height_group'] = "high"

penguins.to_csv('penguins.csv')