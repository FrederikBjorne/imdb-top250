from bs4 import BeautifulSoup
import requests
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from collections import Counter
import csv

source = requests.get('http://www.imdb.com/chart/top').text

soup = BeautifulSoup(source, 'html.parser')
results = soup.find_all('td',attrs={'class':'titleColumn'})

listy = []
for result in results:
    number = result.contents[0][7:-8]
    title = result.contents[1].text
    year = result.find('span').text[1:-1]
    listy.append((number, title, year))

df = pd.DataFrame(listy, columns=['number','title','year'])
df.to_csv('movielist.csv',index=False,encoding='utf-8')
print(df)

x = []

with open('movielist.csv','r') as df:
    plots = csv.reader(df, delimiter=',')
    for column in plots:
        x.append(column[2])


x.remove('year')
x2 = Counter(x)
counted = sorted(x2.items())

x,y = zip(*counted)

x = list(map(int,x))

sns.barplot(x,y)
plt.xticks(rotation=70)
plt.title('IMDB Top 250 by Year')
plt.xlabel('year')
plt.ylabel('number of movies in the top 250')
plt.tick_params(axis='x', which='major', labelsize=6)
plt.tight_layout()
fig_manager = plt.get_current_fig_manager()
if hasattr(fig_manager, 'window'):  # on mac osx window property does not exist
    fig_manager.window.showMaximized()
plt.show(block=False)

print(raw_input("Press enter to close"))

plt.close('all')
