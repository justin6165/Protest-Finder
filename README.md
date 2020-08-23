2020 Hack For The People
===========================
Protest Finder

by Justin Li, Alessandro Snyder, Lam Nguyen, Katie Park

This project is a Python based application that helps the user find protests and rallies based on their location. This is a submission for the 2020 Hack For The People Hackathon taking place from 08/21/2020 to 08/23/2020, under the Political category.


## Set up

## Program Capabilities
### Search for protests and rallies
The Protest Finder is able to look for protests based on what the user puts into the search bar. The user can narrow down their options by typing in city names or state names. After clicking Search, if the Protest Finder has found events happening in the specified location, it will generate a list containing the name and date of the event, a short description, as well as the event's poster.
It will also include a link which leads to the posting of this event from [rallylist.com](rallylist.com).

### Save protests
If the user is interested in following a certain event, they can save it into a predesignated list. The user can also see a list of saved protests by clicking on the Saves tab in the program.

### Remind user
If an event that the user has chosen to save is happnening today, the Protest Finder will send a notification in the system tray. The notification will also include the link to the posting in order to help the user review information such as the location and time of the protest.


## Built with
* Data from [rallylist.com](rallylist.com) - this is where we used web scrapping to get our protest data.
* [PyQt5](https://pypi.org/project/PyQt5/) - used to build the GUI
* [Win10Toast](https://pypi.org/project/win10toast/) - used to build the notification on the day of the event
* add extra stuff that i prob did not include

## Purpose
This Protest Finder was created in light of the events that took place in 2020. After George Floyd's passing, the people of the United States took to the streets to protest against police brutality. Additionally, the presidential election is set to take place in November 2020, and many are rallying to show support for their presidential candidate. Because of this, we decided to create the Protest Finder to help people find out about demonstations and events that may represent their interests near them. 

