from abc import ABC, abstractmethod
from typing import Generator
from crawlers.unit import Unit


class Crawler(ABC):
    @abstractmethod
    def crawl(self) -> Generator[Unit, None, None]:
        pass
