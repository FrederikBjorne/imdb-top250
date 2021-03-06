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

interesting_imdb_params =
{
    'number' : lambda: result.contents[0][7:-8]
    'title'  : lambda: result.contents[1].text
    'year'   : lambda: result.find('span').text[1:-1]
}

listy = [(interesting_imdb_params['number'],
          interesting_imdb_params['title'],
          interesting_imdb_params['year']) for result in results]

df = pd.DataFrame(listy, columns=interesting_imdb_params.keys())
df.to_csv('movielist.csv', index=False, encoding='utf-8')
print(df)
print(input("Press enter to close"))

with open('movielist.csv','r') as df:
    plots = csv.reader(df, delimiter=',')
    x = [column[2] for column in plots].remove('year')

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
mng = plt.get_current_fig_manager()
mng.resize(*mng.window.maxsize())
plt.show()




