import json
import secrets
import googlemaps


def make_request_using_cache_Google(params_geocode):

    if params_geocode not in CACHE_DICTION1:
        geocoding_results = gmaps.geocode(params_geocode)
        CACHE_DICTION1[params_geocode] = {'data': geocoding_results}
        cache_file = open('cache-google.json', 'w')
        cache_file.write(json.dumps(CACHE_DICTION1))
        cache_file.close()
        return CACHE_DICTION1[params_geocode]['data']
    else:
        return CACHE_DICTION1[params_geocode]['data']


def get_lat_and_long(ski_name, ski_state):
    '''
    Fetch latitude and longitude of a ski resort
    Usage: >>> get_lat_and_long('Beaver Creek', 'Colorado')
    '''
    
    gmaps = googlemaps.Client(key=secrets.google_places_key)
    params_geocode = ski_name+' '+ski_state
    
    # Geocoding an address
    geocoding_results = gmaps.geocode(params_geocode)
    latitude = geocoding_results[0]['geometry']['location']['lat']
    longitude = geocoding_results[0]['geometry']['location']['lng']

    return(latitude, longitude)
