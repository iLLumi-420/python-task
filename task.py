import requests
from bs4 import BeautifulSoup
import json

def scrape(search_term, num_of_articles):
    articles = []
    page = get_latest_page()
    while len(articles)< num_of_articles:
        url = f'https://www.annapurnapost.com/search?q={search_term}&page={page}'
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            # print(soup)
            article_list = soup.select('.card__details')
            if not article_list:
                break
            for each in article_list[:num_of_articles]:
                title = each.select_one('.card__title')
                category = each.select_one('a')
                description = each.select_one('.card__desc')

                if title and category and description:

                    article_data = {

                        'title': title.text.strip(),
                        'category': category.text.strip(),
                        'description': description.text.strip(),
                        
                    }
                    articles.append(article_data)
                else:
                    print('Skipped cause incomplete data')
            page += 1
        else:
            print('Error ....')
            break

    save_latest_page(page)
    return articles[:num_of_articles]

def save_latest_page(page):
    with open('last_page.txt', 'w') as file:
        file.write(str(page))

def get_latest_page():
    try:
        with open('last_page.txt', 'r') as file:
            page = int(file.read())
            return page
    except FileNotFoundError:
        return 1
          
            

search_term = 'नेपाल'
number_of_articles = 30

articles = scrape(search_term, number_of_articles)

with open('articles.json', 'w', encoding='utf-8') as file:
    json.dump(articles, file, indent=4, ensure_ascii=False)