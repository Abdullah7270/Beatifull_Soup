import pandas as pd
from string import ascii_uppercase as alphabet
import pickle

all_tables = pd.read_html('https://en.wikipedia.org/wiki/2022_FIFA_World_Cup')

print(all_tables[11])
print(all_tables[18])
print(all_tables[25])
print(all_tables[60])

dict_table ={}
for letter, i in zip(alphabet, range(11, 67,7)):
	df = all_tables[i]
	dict_table[f'Group{letter}']= df
print(dict_table.keys())

with open('dict_table', 'wb') as output:
	pickle.dump(dict_table, output)
