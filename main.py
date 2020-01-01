from dem import DEM
from parcel import Parcel
from logger import log
import argparse


parser = argparse.ArgumentParser()
parser.add_argument("-x", "--lon", type=float, help="Współrzędne działki w osi x")
parser.add_argument("-y", "--lat", type=float, help="Współrzędne działki w osi y")
parser.add_argument("-t", "--teryt", type=str, help="Pełny adres działki")
parser.add_argument("-f", "--format", type=str, help="Format danych wyjściowych: [text, json]", default="text")

args = parser.parse_args()

if args.lon and args.lat:
    parcel = Parcel(x=args.lon, y=args.lat)
elif args.teryt:
    parcel = Parcel(addr=args.teryt)
else:
    log.error("Musisz podać współrzędne lub adres działki")
    parcel = None
    exit(1)

if args.format == "text":
    print(parcel.text_repr)
else:
    print(parcel.json_repr)
