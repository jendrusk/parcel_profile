import unittest
from parcel import Parcel, Polygon
import json


class TestParcelById(unittest.TestCase):
    def setUp(self) -> None:
        self.parcel = Parcel(addr="246101_1.0005.519")

    def test_parcel_geom(self):
        self.assertIsInstance(self.parcel.geom, Polygon)

    def test_parcel_proper(self):
        self.assertEqual(self.parcel.teryt, '246101_1.0005.519')


class TestParcelByXY(unittest.TestCase):
    def setUp(self) -> None:
        self.parcel = Parcel(y=217163.55,x=503635.97)

    def test_parcel_geom(self):
        self.assertIsInstance(self.parcel.geom, Polygon)

    def test_parcel_teryt(self):
        self.assertEqual(self.parcel.teryt, '246101_1.0005.519')

    def test_parcel_text_repr(self):
        self.assertIsInstance(self.parcel.text_repr, str)

    def test_parcel_json_repr(self):
        json.dumps(self.parcel.json_repr)

    def test_minmax_stats(self):
        self.assertIsInstance(self.parcel.minmax_stats, dict)
        self.assertEqual(self.parcel.minmax_stats.get("Hmin"), 311.6)
        self.assertEqual(self.parcel.minmax_stats.get("Hmax"), 312.8)

if __name__ == '__main__':
    unittest.main()
