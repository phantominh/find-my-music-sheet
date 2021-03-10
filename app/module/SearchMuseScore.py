from bs4 import BeautifulSoup


class SearchMuseScore:
    def __init__(self):
        # MuseScore search engine link builder
        self._search_link_builder = "https://musescore.com/sheetmusic?text="

    def search(self, driver, keyword):
        self._search_link_builder += keyword

        # Go to the requested link and get the needed html part
        driver.get(self._search_link_builder)
        html_doc = driver.find_element_by_xpath("/html/body/div[1]/div/section/section/main/div[2]").get_attribute("outerHTML")

        # Scrapping with BeautifulSoup
        html_soup = BeautifulSoup(html_doc, 'html.parser')
        for s in html_soup.find_all('article'):
            print(s)

"""
Json file includes:
- Title: Song's name
- Composer: Author
- Scoring: Piano Solo etc
- Views: Number/None
"""
