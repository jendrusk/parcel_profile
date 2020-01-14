import unittest
from parcel import Parcel
from dem import DEM

class TestDEM(unittest.TestCase):
    def setUp(self) -> None:
        self.parcel = Parcel(addr="246101_1.0005.519")
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
        self.assertIsInstance(res, dict)
        self.assertTrue(float(res.get("Hmin")))
        self.assertTrue(float(res.get("Hmax")))

    def test_dem_volume(self):
        stats = self.dem.get_min_max_by_polygon(polygon=self.parcel.geom)
        avg_level = (stats["Hmin"] + stats["Hmax"])/2
        res = self.dem.get_volume(polygon=self.parcel.geom, level=avg_level)
        self.assertIsInstance(res, dict)
        self.assertTrue(float(res.get("Volume below")))
        self.assertTrue(float(res.get("Volume above")))


if __name__ == '__main__':
    unittest.main()
