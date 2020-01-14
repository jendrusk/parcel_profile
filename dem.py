import requests
from shapely.geometry import Point, LineString, Polygon
from logger import log
from time import sleep


class DEM:
    __BASE_URL = "https://services.gugik.gov.pl/nmt/"
    __RETRY_COUNT = 10
    __RETRY_BASE_DELAY = 2

    def __init__(self, base_url=None, retry_count=None, retry_base_delay=None):
        self.base_url = base_url or self.__BASE_URL
        self.retry_count = retry_count or self.__RETRY_COUNT
        self.retry_base_delay = retry_base_delay or self.__RETRY_BASE_DELAY

    def call_api(self, params):
        cnt = 0
        while True:
            try:
                api_res = requests.get(self.base_url, params=params)
                if api_res.status_code == 200:
                    res = api_res
                    break
                else:
                    log.error(f"Nie udało się pobrac danych DEM, code: {api_res.status_code}, res: {api_res.text}")

                if cnt >= self.retry_count:
                    log.error("Przekroczono maksymalną liczbę zapytań do API")
                    res = None
                    break
                else:
                    cnt += 1
                    sleep(cnt * self.retry_base_delay)

            except:
                log.exception("Nieobsłużony wyjątek podczas wykonywania zapytania do API")
        return res

    def get_by_xy(self, x: float, y: float) -> float or None:
        """
        Zwraca wysokość dla podanych współrzędnych (EPSG:2180)
        """
        params = {
            "x": x,
            "y": y,
            "request": "GetHByXY"
        }
        res = self.call_api(params)
        if res:
            return float(res.content)
        else:
            return None

    def get_by_point(self, point: Point) -> float or None:
        """
        Zwraca wysokość dla podanego punktu (obiekt typu punkt!)
        :param point:
        :return:
        """
        params = {
            "x": point.x,
            "y": point.y,
            "request": "GetHByXY"
        }
        res = self.call_api(params)
        if res:
            return float(res.content)
        else:
            return None

    def get_by_xy_list(self, point_list: list):
        log.warn("Not implemented")
        return None

    def get_by_line(self, line: LineString):
        log.warn("Not implemented")
        return None

    def get_min_max_by_polygon(self, polygon: Polygon):
        """
        Zwraca statystyki wysokości dla podanego polygon-u
        :param polygon:
        :return:
        """
        params = {
            "request": "GetMinMaxByPolygon",
            "polygon": polygon.wkt,
            "json": True
        }
        res = self.call_api(params)
        if res:
            return res.json()
        else:
            return None

    def get_volume(self, polygon: Polygon, level: float):
        """
        Zwraca objętość mas ziemnych dla podanego polygonu i wartości poziomu odniesienia
        :param polygon:
        :param level:
        :return:
        """
        params = {
            "request": "GetVolume",
            "polygon": polygon.wkt,
            "level": level,
            "json": True
        }
        res = self.call_api(params)
        if res:
            return res.json()
        else:
            return None
