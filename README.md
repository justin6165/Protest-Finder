2020 Hack For The People - Protest Finder Application
===========================
This project is a Python based application that helps the user find protests and rallies based on their location. This is a submission for the 2020 Hack For The People Hackathon taking place from 08/21/2020 to 08/23/2020, under the Political category. See below for information on setting things up, the different functionalities of the program, what the program was built with, and who contributed to the project!

## Set up
Currently, in order to set up the application, you must download all of the python files in the repository above and must have their dependencies installed (i.e, you must pip install PyQt5, for example. See the "Built With" section to see all of the dependency libraries needed). Afterwards, you must have python installed and then you simply just run "main.py." In the future, we plan on packaging the python files into an executable for users to use. Through an executable, you won't have to install the dependency libraries or python directly; downloading the executable would be all that you need!

## Program Capabilities
### Search for protests and rallies
The Protest Finder is able to look for protests based on what the user puts into the search bar. The user can narrow down their options by typing in city names or state names. After clicking Search, if the Protest Finder has found events happening in the specified location, it will generate a list containing the name and date of the event, a short description, as well as the event's poster.

It will also include a link which leads to the posting of this event from [rallylis.com](rallylist.com).

![](https://user-images.githubusercontent.com/46146906/90983252-52e3ae80-e532-11ea-99ed-277b05265a89.png)

### Set a home address
The user can set their home address including the city and state they currently live in, as seen in the example below.
![](https://user-images.githubusercontent.com/46146906/90983248-5119eb00-e532-11ea-9bba-56ae197a914d.png)

### Save protests postings
If the user is interested in following a certain event, they can save it into a predesignated list. The user can also see a list of saved protests by clicking on the 'Saves' tab in the program. Below is an example of the saved protests tab.

![](https://user-images.githubusercontent.com/46146906/90983249-524b1800-e532-11ea-9bcd-063836c13f4b.png)

### Remind user of saved protests
If an event that the user has chosen to save is happening today, the Protest Finder will send a notification in the system tray. The notification will also include the link to the posting in order to help the user review important information, such as the location and time of the protest.

![](https://user-images.githubusercontent.com/46146906/90983250-52e3ae80-e532-11ea-8857-d5f7896405a3.png)

## Notify user of new protests in the area
Once the user has set a home address, the Protest Finder will automatically send the user a notification whenever it detects new protest posts in your area.

![](https://user-images.githubusercontent.com/46146906/90983251-52e3ae80-e532-11ea-87f8-4646c1590f79.png)

## Built with
* [Requests](https://pypi.org/project/requests/2.7.0/) - used to make GET requests in order to grab the HTML of web pages
* [Beautiful Soup](https://pypi.org/project/beautifulsoup4/) -  used to web scrape. 
* Data from [rallylist.com](rallylist.com) - the source from which we retrieved the protest data by web scrapping.
* [PyQt5](https://pypi.org/project/PyQt5/) - used to build the GUI/user interface
* [Win10Toast](https://pypi.org/project/win10toast/) - used to build the notification on the day of the event.
* [Pickle](https://github.com/python/cpython/blob/3.8/Lib/pickle.py) - used to saving data onto a .dat file.
* [DateTime](https://docs.python.org/3/library/datetime.html#module-datetime) - used in building the protest notification.

## Purpose
This Protest Finder was created in light of the events that took place in 2020. After George Floyd's passing, the people of the United States took to the streets to protest against police brutality. Additionally, the presidential election is set to take place in November 2020, and many are rallying to show support for their presidential candidate. Because of this, we decided to create the Protest Finder to help people find out about demonstations and events that may represent their interests near them. 

## Contributors
* Justin Li
* Alessandro Snyder 
* Lam Nguyen 
* Katie Park

