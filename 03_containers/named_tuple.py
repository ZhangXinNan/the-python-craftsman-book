
from typing import NamedTuple


class Address(NamedTuple):
    country: str
    province: str
    city: str


def latlon_to_address(lat, lon):
    return Address(country=lat, province=lon, city="")


addr = latlon_to_address('China', 'Shandong')
print(addr)
print(addr.country, addr.province)