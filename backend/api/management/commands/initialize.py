from pathlib import Path
import pandas as pd
from django.core.management.base import BaseCommand
from backend import settings
from stores import models
from pyproj import Proj, transform


class Command(BaseCommand):
    help = "initialize database"
    DATA_DIR = Path(settings.BASE_DIR).parent.parent / "data"
    STORE_DATA = str(DATA_DIR / "stores.pkl")
    HOTEL_DATA = str(DATA_DIR / "hotels.pkl")
    DISTRICT_DATA = str(DATA_DIR / "district.csv")

    def _load_stores(self):
        try:
            print(Command.STORE_DATA)
            data = pd.read_pickle(Command.STORE_DATA)
        except:
            print(f"[-] Reading {Command.STORE_DATA} failed")
            exit(1)
        return data

    def _load_hotels(self):
        try:
            data = pd.read_pickle(Command.HOTEL_DATA)
        except:
            print(f"[-] Reading {Command.HOTEL_DATA} failed")
            exit(1)
        return data

    def _load_district(self):
        data = pd.read_csv(Command.DISTRICT_DATA, encoding='cp949')
        return data

    def _initialize(self):
        """
        Sub PJT 1에서 만든 Dataframe을 이용하여 DB를 초기화합니다.
        """
        print("[*] Loading data...")
        stores = self._load_stores()
        hotels = self._load_hotels()
        districts = self._load_district()

        print("[*] Initializing stores...")
        models.Store.objects.all().delete()

        stores_bulk = [
            models.Store(
                id=store.id,
                tel=store.tel,
                address1=store.address1,
                address2=store.address2,
                name=store.name,
                category=store.category,
                pos_x=store.pos_x,
                pos_y=store.pos_y,
            )
            for store in stores.itertuples()
        ]
        models.Store.objects.bulk_create(stores_bulk)

        print("[*] Initializing hotels...")
        models.Hotel.objects.all().delete()
        hotels_bulk = [
            models.Hotel(
                id=hotel.id,
                tel=hotel.tel,
                address1=hotel.address1,
                address2=hotel.address2,
                name=hotel.name,
                pos_x=hotel.pos_x,
                pos_y=hotel.pos_y,
            )
            for hotel in hotels.itertuples()
        ]
        models.Hotel.objects.bulk_create(hotels_bulk)

        print("[*] Initializing district...")
        models.District.objects.all().delete()
        districts_bulk = [
            models.District(
                sido=district.sido,
                gugun=district.gugun,
                dong=district.dong,
                payment_count=district.payment_count,
            )
            for district in districts.itertuples()
        ]
        models.District.objects.bulk_create(districts_bulk)

        print("[+] Done")

    def handle(self, *args, **kwargs):
        self._initialize()


    def trans(x1, y1):
        fromProjection = Proj(
            '+proj=tmerc +lat_0=38 +lon_0=127.0028902777778 +k=1 +x_0=200000 +y_0=500000 +ellps=bessel +units=m +no_defs +towgs84=-115.80,474.99,674.11,1.16,-2.31,-1.63,6.43')
        toProjection = Proj(init='epsg:4326')
        x2, y2 = transform(fromProjection, toProjection, x1, y1)
        return x2, y2
