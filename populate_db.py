# Load libraries
import pickle
import secrets
import google_api
import sqlite3


# Un-pickle snow data
infile = open('snow_data','rb')
data = pickle.load(infile)
infile.close()

# Extract data of interest from old database
def extract_data():
	snow_list = []
	for i in range(5,len(data)):
		resorts = list(data[i][1].keys())
		state = data[i][2]
		urls = [data[i][1][resort]['URL'] for resort in resorts]
		geocodes = [google_api.get_lat_and_long(resort, state) for resort in resorts]
		snow_dic = {'state': state, 'resorts': resorts, 'urls': urls, 'geocodes': geocodes}
		snow_list.append(snow_dic)
	return snow_list

snow_list = extract_data()

# Re-cast old data into new database
def insert_data(data):
	conn = sqlite3.connect('app.db')
	cur = conn.cursor()

	for state in data:
		for i in range(len(state['resorts'])):
			name = state['resorts'][i]
			state_name = state['state']
			lat = state['geocodes'][i][0]
			long = state['geocodes'][i][1]
			url = state['urls'][i]
			insertion = (None, name, state_name, lat, long, url)
			statement = 'INSERT INTO "Resort" '
			statement += 'VALUES (?, ?, ?, ?, ?, ?)'
			cur.execute(statement, insertion)
	conn.commit()
	conn.close()

insert_data(snow_list)