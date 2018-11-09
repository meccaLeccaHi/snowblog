import pickle
import googlemaps
from config import Config

def get_lat_and_long(ski_name, ski_state):
    '''
    Fetch latitude and longitude of a ski resort
    Usage: >>> get_lat_and_long('Beaver Creek', 'Colorado')
    '''
    
    gmaps = googlemaps.Client(key=Config.GOOGLE_KEY)
    params_geocode = ski_name+' '+ski_state
    
    # Geocoding an address
    geocoding_results = gmaps.geocode(params_geocode)
    latitude = geocoding_results[0]['geometry']['location']['lat']
    longitude = geocoding_results[0]['geometry']['location']['lng']

    return(latitude, longitude)


def extract():
	''' Extract data of interest from old database '''

	# Un-pickle snow data
	infile = open('snow_data','rb')
	data = pickle.load(infile)
	infile.close()
	
	# Insert into new database
	resort_list = []
	for i in range(5,7): #len(data)
		resorts = list(data[i][1].keys())
		print(resorts)
		state = data[i][2]
		urls = [data[i][1][resort]['URL'] for resort in resorts]
		geocodes = [get_lat_and_long(resort, state) for resort in resorts]
		snow_dic = {'state': state, 'resorts': resorts, 'urls': urls, 'geocodes': geocodes}
		resort_list.append(snow_dic)

	return resort_list
