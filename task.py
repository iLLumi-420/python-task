import requests
from bs4 import BeautifulSoup
import json

def scrape(search_term, num_of_articles):
    articles = []
    page = 1
    while len(articles)< num_of_articles:
        url = f'https://www.annapurnapost.com/search?q={search_term}&page={page}'
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            # print(soup)
            article_list = soup.select('.card__details')
            for each in article_list[0:2]:
                article_data = {
                    'title': each.select_one('.card__title').text,
                    'category': each.select_one('a').text  ,
                    'description': each.select_one('.card__desc').text,
                }
                articles.append(article_data)
        else:
            print('Error ....')
            break

    return articles[:num_of_articles]
          
            

search_term = 'नेपाल'
number_of_articles = 30

articles = scrape(search_term, number_of_articles)
print(articles)

with open('articles.json', 'w') as file:
    json.dump(articles, file, indent=4)