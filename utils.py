import requests
from bs4 import BeautifulSoup

def get_movie_info(url_receive):
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
    data = requests.get(url_receive, headers=headers)
    soup = BeautifulSoup(data.text, 'html.parser')
    title_tag = soup.select_one('title')
    title = title_tag.text
    return title