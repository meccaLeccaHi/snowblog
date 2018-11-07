# Welcome to Snowblog!


This is an example Flask application that makes use of multiple elements including:
- Pre-scraped data from [Opensnow.com](www.opensnow.com), which includes the name and state/province of every ski resort in America and Canada
- API calls to retrieve the latitude and longitude of each of those resorts, as well as that of the user, using a [Python client library](https://github.com/googlemaps/google-maps-services-python) for Google Maps API
- GET/POST calls to SQLite database, allowing users to keep notes on experiences at each resort (/comment view), review those notes (/index view), and find the closest resorts (/locate view)
- Uses [Bootstrap](http://getbootstrap.com) as the CSS framework
