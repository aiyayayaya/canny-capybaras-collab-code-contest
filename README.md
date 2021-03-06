# XKCD Webscraping TUI
> A software to scrape comic title, id, url, image url and the alternative text from the website [xkcd](https://xkcd.com/) in form of a [TUI](https://en.wikipedia.org/wiki/Text-based_user_interface), Text-/Terminal-based User Interface

![](https://img.shields.io/badge/License-MIT-idk?style=flat&logo=windows-curses&logoColor=white&color=ff00)

## Tools & Technologies
+ Python 3.9
+ [Beautiful Soup 4](https://pypi.org/project/beautifulsoup4/) ~= 4.8.0
+ [psutil](https://pypi.org/project/psutil/) ~= 5.8.0
+ [img2text](https://pypi.org/project/img2text/) ~= 0.0.2
+ [windows-curses](https://pypi.org/project/windows-curses/) ~= 2.2
+ [requests](https://pypi.org/project/requests/) ~= 2.26.0

## Features
+ scrape comic title, id, url, image url and the alternative text from [xkcd](https://xkcd.com/)
+ scrape a specific queue with comic id's from [xkcd](https://xkcd.com/) (800-1000)
+ save scraped comic data in a json/csv file
+ CPU usage

## How it works?
+ go to field `Comic ID(s):` and enter the number of your comic id's
  + input format for **one** ID `1000`
  + input format for more specific ID's `1, 800, 1000`
  + input format for several comic ID's `800-1000`
  + input format for **one** specific ID and several ID's in a range `1, 800-1000`
  + input format for several queues of ID's `1-50, 800-1000`
  + input can also be `2488-*`, which will start at comic 2488 and finish at the latest comic, or `1-*`, which will scrape all available comics
+ to select the file format of the output click on the text behind `File Format:`
  + can change between JSON or CSV
+ click on `START` to start crawling process
+ click on `Show Image` to show the image in console in ASCII art (picture 2&3)
+ click on 'Open Folder' to open the folder where the scraped comic is located
+ with buttons `Back` & `Next` you can switch between results
+ see the magic

![](/images/start_tui.png)
![](/images/executed_tui.png)
![](/images/ASCII_image_tui.png)

## Theme Interpretation (Think Inside the Box)
Our interpretation of the theme was that "thinking inside the box" should imply that it does not require broad thinking. For example, something that is simple to understand, execute, and obtain the results of. We decided to go for a basic TUI style which is self-contained in a single menu (a box if you will). We also chose xkcd to scrape out of all websites because of [this comic titled "AI-Box Experiment"](https://xkcd.com/1450/).

## Other

Some [xkcd](https://xkcd.com) comics are `build-yourself`, so some if the information to be scraped will not be available, but your output will indicate on whether it is a `build-yourself` comic

## Installation

Clone this repository

```bash
  git clone git@github.com:aiyayayaya/canny-capybaras-collab-code-contest.git
```

Create a virtual environment (in this example  we will be using [pipenv](https://pypi.org/project/pipenv/))

```bash
  pipenv --python 3.9
```

Install the required packages

```bash
  pipenv install -r requirement.txt

  pipenv install -d dev-requirements.txt  # is not really needed
```

Run the project

```bash
  pipenv run py __main__
```

Scraped comics will be placed in a folder within the `output` folder. Folder naming is done according to the comic number

## Authors

- [@aiyayayaya](https://www.github.com/aiyayayaya)
- [@miladog](https://www.github.com/miladog)
- [@mariothedog](https://www.github.com/mariothedog)
- [@paulchen5](https://www.github.com/paulchen5)
- [@voidoffi](https://www.github.com/voidoffi)
- [@marty321](https://www.github.com/marty321)

## Known Issues
+ Making the window too small results in a crash and resizing it too fast may result in a weird-looking TUI
+ Scraping [comic 404](https://xkcd.com/404) will result in a crash (this includes scraping ranges that include comic 404 such as `1-*` which would scrape all the comics)
+ If you try to scrape a comic that doesn't exist the program will crash
+ Scraping choose-your-own-adventure comics (such as 1350) will result in incorrect and weird information being displayed
