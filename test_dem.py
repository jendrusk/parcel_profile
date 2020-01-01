import unittest
from parcel import Parcel
from dem import DEM, Polygon


url_single = "https://services.gugik.gov.pl/nmt/?request=GetHByXY&x=486617&y=637928"
url_list = "https://services.gugik.gov.pl/nmt/?request=GetHByPointList&list=563800 243490,563950 243490,563950 243400"
url_polygon = "https://services.gugik.gov.pl/nmt/?request=GetMinMaxByPolygon&polygon=POLYGON((563800 243490 ... 563800 243490))&json"
url_volume = "https://integracja.gugik.gov.pl/nmt/?request=GetVolume&polygon=POLYGON((563800 243490 ... 563800 243490))&level=300&json"

class TestDEM(unittest.TestCase):
    def setUp(self) -> None:
        self.parcel = Parcel(addr="141201_1.0001.1867/2")
        self.dem = DEM()

    def test_dem_xy(self):
        res = self.dem.get_by_xy(
            x=self.parcel.geom.centroid.x,
            y=self.parcel.geom.centroid.y,
        )
        self.assertIsInstance(res, float)

    def test_dem_point(self):
        res = self.dem.get_by_point(point=self.parcel.geom.centroid)
        self.assertIsInstance(res, float)

    def test_dem_min_max_polygon(self):
        res = self.dem.get_min_max_by_polygon(polygon=self.parcel.geom)


if __name__ == '__main__':
    unittest.main()
