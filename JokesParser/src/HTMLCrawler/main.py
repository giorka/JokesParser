# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
from requests import Response, Session


class Website:
    __slots__ = ('url', 'headers', 'cookies', 'params', '__source', '__spider')

    user_agent = UserAgent()
    features = 'lxml'

    def __init__(self, *, url: str, headers: dict = None, cookies: dict = None, params: dict = None) -> None:
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
    def spider(self):
        if not self.__spider:
            self.__spider = BeautifulSoup(markup=self.source, features=self.features)

        return self.__spider
