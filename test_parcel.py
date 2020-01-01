import unittest
from parcel import Parcel, Polygon
import json


class TestParcelById(unittest.TestCase):
    def setUp(self) -> None:
        self.parcel = Parcel(addr="141201_1.0001.1867/2")

    def test_parcel_geom(self):
        self.assertIsInstance(self.parcel.geom, Polygon)


class TestParcelByXY(unittest.TestCase):
    def setUp(self) -> None:
        self.parcel = Parcel(y=222714.54, x=501360.87)

    def test_parcel_geom(self):
        self.assertIsInstance(self.parcel.geom, Polygon)

    def test_parcel_teryt(self):
        self.assertEqual(self.parcel.teryt, '240204_4.0001.2841/2')

    def test_parcel_text_repr(self):
        self.assertIsInstance(self.parcel.text_repr, str)

    def test_parcel_json_repr(self):
        json.dumps(self.parcel.json_repr)

    def test_minmax_stats(self):
        self.assertIsInstance(self.parcel.minmax_stats, dict)


if __name__ == '__main__':
    unittest.main()
