from module.SearchMuseScore import SearchMuseScore
from selenium import webdriver
import os

# Path to Firefox executable driver
GECKODRIVER_PATH = '/usr/bin/geckodriver'


class FindMyMusicSheet:
    def __init__(self):
        # Initialize search objects
        self._keyword = ""
        self._search_musescore = SearchMuseScore()
        # Initialize Selenium web driver to browse Firefox in headless mode and scrape data from dynamic websites
        options = webdriver.FirefoxOptions()
        options.add_argument('-headless')
        self._driver = webdriver.Firefox(executable_path=GECKODRIVER_PATH, options=options, service_log_path=os.devnull)

    # Command Line Interface
    def search_cli(self):
        # User input search keyword
        self._keyword = input()
        # Search result from MuseScore.com
        self._search_musescore.search(self._driver, self._keyword)

    def quit(self):
        self._driver.quit()


main = FindMyMusicSheet()
main.search_cli()
main.quit()
