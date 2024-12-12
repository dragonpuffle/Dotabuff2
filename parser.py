import requests
from bs4 import BeautifulSoup as bs
import html5lib

def get_items():
    URL = 'https://liquipedia.net/dota2/Items'
    response = requests.get(URL)
    print('response =', response)
    soup = bs(response.content, "html5lib")
    items = soup.findAll('div','itemlist')
    items = items[0].findAllNext('div',limit=194)

    final_items = [item.a.get('title')[:-1:].split(' (') for item in items]
    final_items
    print(final_items)


def get_heroes():
    URL = 'https://liquipedia.net/dota2/Portal:Heroes'
    response = requests.get(URL)
    print('response =', response)
    soup = bs(response.content, "html5lib")
    heroes = soup.find('ul','heroes-panel__category-list')
    heroes = heroes.findAllNext('div','heroes-panel__hero-card__title', limit=130)
    final_heroes=[]
    for hero in heroes:
        hero_name=hero.a.get('title').replace(' ', '_')
        if hero_name != "Nature's_Prophet":
            final_heroes.append(hero_name)

    return final_heroes


def get_abilities(heroes):
    j = 0
    for hero in heroes:

        hero_abilities = []
        URL= 'https://liquipedia.net/dota2/' + hero + '#Abilities'
        response = requests.get(URL)
        soup = bs(response.content, "html5lib")
        abilities = soup.findAll(style="cursor:default; font-size:85%; font-weight:bold; color:#FFF; margin:-4px 0 2px 0; text-shadow:1px 1px 2px #000;;")
        abilities_desc = soup.findAll(style="vertical-align:top; padding-right:2px; padding-bottom:5px; font-size:85%;")
        i=0
        if len(abilities) == len(abilities_desc):
            for ability in abilities:
                hero_abilities.append((j,hero,ability.text,abilities_desc[i].text))
                i+=1
        print(hero_abilities)
        j+=1



#get_items()
heroes= get_heroes()
get_abilities(heroes)