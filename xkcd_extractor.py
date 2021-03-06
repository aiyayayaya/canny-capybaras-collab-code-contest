import csv
import json
import operator  # noqa: F401
import os

import requests
from bs4 import BeautifulSoup


class Container(object):
    """
    Container that contains 3 lists ('comics' for the list of comics that have been crawled,

    'titles' for the list of all comic's titles that have been crawled and
    'image_urls' for the list of all comic's image's url that have been crawled)
    """

    def __init__(self):
        self.comics = []
        self.titles = []
        self.image_urls = []

    def append(self, comic: list) -> None:
        """
        Append lists with comic's propreties

        :param comic
        """
        self.comics.append([comic[0], comic[1]])
        self.titles.append([comic[0], comic[1].title])
        self.image_urls.append([comic[0], comic[1].image_url])


class Comic(object):
    """Custom object that store the page number, title, scripts, image_url, comic_url, and the image_path of a comic"""

    def __init__(self, page: int, title: str, script: str, image_url: str, comic_url: str, image_path: str):
        self.page = page
        self.title = title
        self.script = script
        self.image_url = image_url
        self.comic_url = comic_url
        self.image_path = image_path


def parse_img(image_url: str, filename: str, item_dir: str) -> None:
    """
    Save image in the specified path

    :param image_url , image url obtained by scrapping
    :param filename , the name of the image file
    :param item_dir , the directory to be saved in
    """
    os.chdir(item_dir)
    with open(filename, 'wb') as f:
        f.write(requests.get(image_url).content)
    os.chdir("..\\")


def crawl(user_input: str, file_format: str = 'json', save_path: str = ".") -> Container:
    """
    Mode : list, must define the :param 'list_' with a list

    mode : range, must define the :param 'start' and the :param 'end' with integers

    :param user_input: the input for the comics to be scrapped
    :param file_format , by default 'json' ,can be changed to 'csv'
    :param save_path , in working directory by default, can by change by a str path
    """
    if '*' in user_input:
        html_text = requests.get('https://xkcd.com/')
        soup = BeautifulSoup(html_text.text, 'html.parser')
        lastest_comic = soup.find('meta', property="og:url")["content"].split('.com/')[1][:-1]
        user_input = user_input.replace('*', lastest_comic)
    user_input = user_input.split(',')
    for index_input, input_ in enumerate(user_input):
        if '-' in input_:
            split_input = input_.split('-')
            str_range = [str(int_) for int_ in range(int(split_input[0]), int(split_input[1]) + 1)]
            user_input[index_input:index_input] = str_range
            user_input.remove(input_)
    user_input = [int(input_) for input_ in user_input]
    comics_objs = Container()
    os.chdir(save_path)
    try:
        if not os.path.exists('output'):
            os.makedirs('output')
    except Exception as ex:
        print("Error: ", ex.__class__)
    os.chdir('output')
    for index, urls in enumerate(user_input):
        html_text = requests.get('https://xkcd.com/' + str(urls))
        soup = BeautifulSoup(html_text.text, 'html.parser')
        page = str(urls)

        # extract url
        comic_url = 'https://xkcd.com/' + str(urls)
        # extract title
        title = soup.find(id="ctitle").text
        try:
            # extract texts
            script = soup.find(id="comic").find("img")['title']
            # extract comic
            image_url = "https:" + soup.find(id="comic").find("img")['src']
        except Exception as ex:
            image_url, script = "https://uniim1.shutterfly.com/render/" \
                                "00-vOZRc1W66JnxNvciJy8U4krEZhJw8T6sbQ90aYWJRTIu1xZykVtCbeNYqPr02Q1" \
                                "KldMTLfbtJ__wYVBQ_4iTow?cn=THISLIFE&res=small", ""
            print("Error", ex.__class__, ": Found a special comic, empty script and image_url")

        # export to file
        filename = 'xkcd-' + page + '.png'
        item_dir = 'xkcd-' + page
        if not os.path.exists(item_dir):
            os.makedirs(item_dir)

        image_path = os.path.join('output', item_dir, filename)
        print(image_path)
        comics_objs.append([index, Comic(page, title, script, image_url, comic_url, image_path)])

        os.chdir(item_dir)
        if file_format == 'json':
            results = {'title': title, 'script': script, 'image_url': image_url, 'comic_url': comic_url}
            with open('xkcd-' + page + '.json', 'w') as f:
                json.dump(results, f)
        elif file_format == 'csv':
            with open('xkcd-' + page + '.csv', 'w', newline='') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow(['title', 'script', 'image_url', 'comic_url'])
                writer.writerow([title, script, image_url, comic_url])
        else:
            raise KeyError(file_format + "isn't a supported format")
        os.chdir("..\\")
        parse_img(image_url, filename, item_dir)

    for var_ in ['titles', 'comics', 'image_urls']:
        exec(f'comics_objs.{var_}.sort(key=operator.itemgetter(0))')   # noqa: S102
        exec(f'for list_ in comics_objs.{var_} :\n del list_[0]')  # noqa: S102
        exec(f'comics_objs.{var_} = [list_[0] for list_ in comics_objs.{var_}]')  # noqa: S102

    os.chdir("..\\")
    return comics_objs


if __name__ == "__main__":
    print(crawl(user_input='1,3', file_format="json").titles)
