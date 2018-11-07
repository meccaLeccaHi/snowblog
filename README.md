# Welcome to Snowblog!


This app allows Jerry to keep track of his experiences at different ski resorts, and find new ones based on his location input! This is a beginner-friendly example of a simple Flask application, that is designed to help demonstrate the use of Flask, within the context of an introductory Python course. As such, the code in this repo is deliberately simplified and heavily-commented for clarity.

### Back-end
This app uses:
- a SQLite database of pre-scraped data from [Opensnow.com](https://opensnow.com/), which includes the name and state/province of every ski resort in America and Canada
- API calls to a [Python client library](https://github.com/googlemaps/google-maps-services-python) for Google Maps, allowing us to retrieve the latitude and longitude of each resort, as well as that of the user
- [Bootstrap](http://getbootstrap.com) as the CSS framework

### Views
_Home_ page displays existing notes on ski resorts visited by Jerry.
![Index View](./app/static/images/index_view.png)  

_Locate_ page finds and displays the nearest ski resort (based on euclidean distance).
![Locate View](./app/static/images/locate_view.png)  

_Comment_ page provides a way for the user (Jerry), to keep notes on his experiences at each resort.
![Comment View](./app/static/images/comment_view.png)