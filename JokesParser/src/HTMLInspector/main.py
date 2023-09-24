# -*- coding: utf-8 -*-
from ..HTMLCrawler import *


class Page:
    __slots__ = ('spider', '__is_exists')

    def __init__(self, *, website: Website):
        self.spider = website.spider

        ######
        self.__is_exists = None

    @property
    def jokes(self):
        yield from (joke for joke in map(BeautifulSoup.get_text, self.spider.find_all(class_='text')))

    @property
    def is_exists(self):
        if not self.__is_exists:
            self.__is_exists = not self.spider.title.text.startswith('404')

        return self.__is_exists
