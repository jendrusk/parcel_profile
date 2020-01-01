import requests
from shapely import wkb, wkt
from shapely.geometry import Point,LineString, Polygon
from logger import log


class DEM:
    _requests = ["GetHByXY", "GetHByPointList", "GetMinMaxByPolygon", "GetVolume"]
    _base_url = "https://services.gugik.gov.pl/nmt/"
    url_single = "https://services.gugik.gov.pl/nmt/?request=GetHByXY&x={x}&y={y}"
    url_list = "https://services.gugik.gov.pl/nmt/?request=GetHByPointList&list=563800 243490,563950 243490,563950 243400"
    url_polygon = "https://services.gugik.gov.pl/nmt/?request=GetMinMaxByPolygon&polygon={polygon_wkt}&json"
    url_volume = "https://integracja.gugik.gov.pl/nmt/?request=GetVolume&polygon=POLYGON((563800 243490 ... 563800 243490))&level=300&json"

    def call_api(self, params):
        api_res = requests.get(self._base_url, params=params)
        if api_res.status_code == 200:
            return api_res
        else:
            log.error(f"Nie udało się pobrac danych DEM, code: {api_res.status_code}, res: {api_res.text}")
            return None


    def get_by_xy(self, x, y):
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

    def get_by_point(self,point: Point):
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

    def get_by_point_list(self, point_list):
        log.warn("Not implemented")
        return None

    def get_by_line(self):
        log.warn("Not implemented")
        return None

    def get_min_max_by_polygon(self, polygon: Polygon):
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




