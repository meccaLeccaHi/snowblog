# Load libraries
import sqlite3
import extract_data

snow_list = extract_data.extract()

# Re-cast old data into new database
def insert_data(data):
	conn = sqlite3.connect('app.db')
	cur = conn.cursor()

	for state in data:
		for i in range(len(state['resorts'])):
			name = state['resorts'][i]
			state_name = state['state']
			lat = state['geocodes'][i][0]
			lng = state['geocodes'][i][1]
			url = state['urls'][i]
			insertion = (None, name, state_name, lat, lng, url)
			statement = 'INSERT INTO "Resort" '
			statement += 'VALUES (?, ?, ?, ?, ?, ?)'
			cur.execute(statement, insertion)
	conn.commit()
	conn.close()

insert_data(snow_list)
