from bs4 import BeautifulSoup
from fake_useragent import UserAgent
from requests import Session, Response


class Website:
    user_agent = UserAgent()

    def __init__(self, *, url: str, headers: dict, cookies: dict, params: dict):
        self.url: str = url
        self.headers: dict = headers
        self.cookies: dict = cookies
        self.params: dict = params

        ######
        self.__source = self.__spider = None

    @property
    def source(self):
        if not self.__source:
            with Session() as session:
                session.headers['User-Agent']: str = self.user_agent.random
    
                response: Response = session.get(url=self.url, cookies=self.cookies, params=self.params)
    
                markup: str = response.text
            
            self.__source = markup

        return self.__source
    
    @property
    def (self):
        return 


class Page:
    def __init__(self, *, markup: str):
        self.markup: str = markup
        self.spider: BeautifulSoup = BeautifulSoup(markup=self.markup, features='html.parser')

    def validate(self):
        is_valid = not self.spider.title.text.startswith('404')

        return is_valid

    def get_jokes(self):
        jokes = map(BeautifulSoup.get_text, self.spider.find_all(class_='text'))

        yield from jokes


class Scrapper:
    def __init__(self, *, url: str):
        self.url = url

    def main(self):
        page_number = 1

        while True:
            url = f'{self.url}{page_number}'

            markup = Website(url=url).source
            page = Page(markup=markup)

            if page.validate():
                jokes = page.get_jokes()

                for joke in jokes:
                    print(joke)
            else:
                break

            page_number += 1


if __name__ == '__main__':
    link = 'https://www.anekdot.ru/release/anekdot/year/2023/'

    scrapper = Scrapper(url=link)
    scrapper.main()
