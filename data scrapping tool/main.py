from src.gmaps import Gmaps



queries = [
   "malls in mumbai"
]

Gmaps.places(queries,max=5)