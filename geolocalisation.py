# -*- coding:utf-8 -*-

from geolocation.main  import GoogleMaps
from geolocation.distance_matrix.client  import DistanceMatrixApiClient

key = 'AIzaSyAr1BDyauV-BQzwduA1kQBIghgeOABJs-g'
maps = GoogleMaps(api_key=key)
class Geolocalisation(object):
    def geolocalisationAdresse(self,adresse):
        localisation = maps.search(location=adresse)
        localisation.all()
        adresse_localisation = localisation.first()
        
        ville = adresse_localisation.city
        route = adresse_localisation.route
        numero_rue = adresse_localisation.street_number
        code_postal = adresse_localisation.postal_code
        pays = adresse_localisation.country
        
        
        liste = [ville,route,numero_rue,code_postal,pays]
        
        for administrative_area  in adresse_localisation.administrative_area:
            liste.append(administrative_area.area_type)
            liste.append(administrative_area.name)
            
        latitude = adresse_localisation.lat
        longitude = adresse_localisation.lng
        
        liste.append(latitude)
        liste.append(longitude)
        
        return liste
    
    def GetModeVoiture(self,origine,destination):
        origins = [origine]
        destinations  = [destination]
        items =maps.distance(origins,destinations).all()
        liste = []
        for item in items:
            Distance_km = item.distance.kilometers
            Distance_m = item.distance.meters
            Duree = item.duration
            liste.append(Distance_km)
            liste.append(Distance_m)
            liste.append(Duree)
        return liste

    def GetModeVelo(self,origine,destination):
        origins = [origine]
        destinations = [destination]
        items = maps.distance(origins,destinations,DistanceMatrixApiClient.MODE_BICYCLING).all()
        liste = []
        
        for item in items:
            Distance_km = item.distance.kilometers
            Distance_m = item.distance.meters
            Duree = item.duration
            liste.append(Distance_km)
            liste.append(Distance_m)
            liste.append(Duree)
        return liste
    
    def GetModeMarcheAPied(self,origine,destination):
        origins = [origine]
        destinations = [destination]
        items = maps.distance(origins,destinations,DistanceMatrixApiClient.MODE_WALKING).all()
        
        liste = []
        
        for item in items:
            Distance_km = item.distance.kilometers
            Distance_m = item.distance.meters
            Duree = item.duration
            liste.append(Distance_km)
            liste.append(Distance_m)
            liste.append(Duree)
        return liste