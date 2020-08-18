import geopy
from geopy.geocoders import Nominatim

nom=Nominatim(user_agent="hulk")
n=nom.geocode("")
print(n.latitude,n.longitude)
