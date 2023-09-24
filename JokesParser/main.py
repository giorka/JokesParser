# -*- coding: utf-8 -*-
from .src.HTMLInspector import *


class Scrapper:
    url = 'https://www.anekdot.ru/release/anekdot/year/2023'

    @staticmethod
    def main():
        page_index = 1

        while True:
            url = f'{Scrapper.url}/{page_index}'
            page = Page(website=Website(url=url))

            if page.is_exists:
                for joke in page.jokes:
                    print(joke)
            else:
                break

            page_index += 1
