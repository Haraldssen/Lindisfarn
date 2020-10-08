import pytest
import time
import requests
import urllib


# декоратор, кторый умеет измерять время исполннения функции

def benchmark(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(end-start)
        assert end - start <= 1
        return result
    return wrapper

class TestRebelStar:

    def setup_class(self):
        self.domain = 'https://rebelstar.ru/'
        self.timeout = 3.0  # в секундах

    @benchmark
    def callUrl(self, part=None, params=None):
        try:
            url = self.domain
            if part:
                url +=part
            if params:
                url += '?' + urllib.parse.urlencode(params)
            return requests.get(url.lower(), timeout=self.timeout)
        except ValueError as err:
            return False

    # проверить, что домен вообще доступен
    def test_domain(self):
        result = self.callUrl()
        assert result.status_code == 200

    # https://rebelstar.ru/RS1/index.html?raider=false&operative=true&fog=false


    @pytest.mark.parametrize("raider, operative, fog",
                             [(True, True, True), (True, True, False),
                             (True, False, True), (True, False, False),
                             (False, False, True), (False, False, False)]
                            )
    def test_method(self, raider, operative, fog):
        part = 'RS1/index.html'
        params = dict(raider=raider, operative=operative, fog=fog)
        result = self.callUrl(part, params)
        assert result.status_code == 200
