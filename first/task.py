import requests
from bs4 import BeautifulSoup
import json

def scrape(search_term, num_of_articles):
    new_articles = []
    prev_articles = []
    last_page = 1
    print(new_articles, 'start')

    try: 
        with open('articles.json', 'r' , encoding='utf-8') as file:
            data = json.load(file)
            prev_articles = data['articles']
            last_page = data['last_page']
        print(prev_articles, 'file read')
    except FileNotFoundError:
        pass

    while(len(new_articles)< num_of_articles):
        url = f'https://www.annapurnapost.com/search?q={search_term}&page={last_page}'
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            article_list = soup.select('.card__details')
            if not article_list:
                break
            else:
                for each in article_list:
                    title = each.select_one('.card__title')
                    category = each.select_one('a')
                    description = each.select_one('.card__desc')

                    article_data = {
                        'title': title.text.strip() if title else '',
                        'category': category.text.strip() if category else '',
                        'description': description.text.strip() if description else '',
                    }
                    new_articles.append(article_data)
  
        else:
            print('Error occurred while fetching data.')
            break

        last_page += 1

    data = {
        'articles' : prev_articles + new_articles,
        'last_page': last_page,
    }
    with open('articles.json', 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)


search_term = 'नेपाल'
number_of_articles = 30

scrape(search_term, number_of_articles)

