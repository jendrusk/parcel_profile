import requests
from shapely import wkt
from shapely.geometry import Point,LineString, Polygon
import json
from logger import log
from dem import DEM

dem = DEM()

class Parcel:
    base_url = "https://uldk.gugik.gov.pl/"
    fields =  ["geom_wkt", "teryt", "voivodeship", "county", "commune", "region", "parcel"]
    requests = ["GetParcelById", "GetParcelByXY"]

    @property
    def xy(self):
        if self.x and self.y:
            return ",".join([str(self.x), str(self.y)])
        else:
            return None

    @property
    def params(self)-> dict:
        params = dict()
        if self.addr:
            params["request"] = "GetParcelById"
            params["id"] = self.addr
        elif self.xy:
            params["request"] = "GetParcelByXY"
            params["xy"] = self.xy
        else:
            log.error("Musisz podać numer działki lub współrzędnie punktu wewnątrz działki")
            exit(1)
        params["result"] = ",".join(self.fields)
        return params

    @property
    def minmax_stats(self):
        if not self._minmax_stats:
            self._minmax_stats = dem.get_min_max_by_polygon(self.geom)
        return self._minmax_stats

    @property
    def text_repr(parcel):
        res = F"""
Adres działki: {parcel.teryt}
Powierzchnia: {parcel.minmax_stats.get("Polygon area")}
Wysokość maksymalna: {parcel.minmax_stats.get("Hmax")}
Wysokość minimalna: {parcel.minmax_stats.get("Hmin")}    
        """
        return res

    @property
    def json_repr(self):
        res = {
            "teryt": self.teryt,
            "area": self.minmax_stats.get("Polygon area"),
            "Hmax": self.minmax_stats.get("Hmax"),
            "Hmin": self.minmax_stats.get("Hmin")
        }
        return json.dumps(res)

    def __init__(self, addr=None, x=None, y=None):
        self.addr = addr
        self.x = x
        self.y = y
        self.geom = None
        self.geom_wkt = None
        self._minmax_stats = None

        # known fields from API
        self.geom_wkt = None
        self.teryt = None
        self.voivodeship = None
        self.county = None
        self.commune = None
        self.region = None
        self.parcel = None

        self.__api_get__()

    def __parse_result__(self,result):
        result_exp = result.split("|")
        for key, value in zip(self.fields, result_exp):
            if key == "geom_wkt":
                if ";" in value:
                    setattr(self, key, wkt.loads(value.split(";")[1]))
                else:
                    setattr(self, key, wkt.loads(value))
                setattr(self, "geom", self.geom_wkt)
            else:
                setattr(self, key, value)

    def __api_get__(self):
        url = self.base_url
        api_res = requests.get(url, params=self.params)
        if api_res.status_code == 200:
            log.debug("Prawidłowo pobrano właściwości działki")
            api_res_split = api_res.text.split("\n")
            self.__parse_result__(api_res_split[1])
        else:
            log.error(f"Nie udało się pobrac właściwości działki, code: {api_res.status_code}, res: {api_res.text}")

