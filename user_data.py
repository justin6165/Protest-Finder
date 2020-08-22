import pickle
import notification
import scrapping
import os

# pickle.dump(LIST_NAME, open(".dat FILE_NAME", "wb"))
# pickle.load(open(".dat FILE_NAME", "rb"))

# executes on start-up
# checks to see if there are reminders for today
def check_reminders():
    events = pickle.load(open("saved_protests.dat", "rb"))

    if not events:
        for event in events:
            if (notification.check_alert(event.date)):
                notification.send_notification(event.title, event.link)
                events.remove(event)

# saves protest information into pre-existing list
def add_protest(title, date, link):
    events = pickle.load(open("saved_protests.dat", "rb"))
    protest_event = scrapping.Protest(title, date, link)
    events.append(protest_event)
    pickle.dump(events, open("saved_protests.dat", "wb"))

# returns a list containing the User's saved protests
def get_saved_protest_list():
    events = pickle.load(open("saved_protests.dat", "rb"))
    return events

# deletes a protest from the saved protest list given the protest title
def delete_protest(title):
    events = pickle.load(open("saved_protests.dat", "rb"))
    for event in events:
        if event.title == title:
            events.remove(event)

# saves the home address into a .dat file called "user_address.dat"
# if there already exists a home address. Overwrite the previous address
def add_home_address(address):
    if check_home_address() is False:
        pickle.dump(address, open("user_address.dat", "wb"))
    else:
        os.remove("user_address.dat")
        pickle.dump(address, open("user_address.dat", "wb"))


def check_home_address():
    try:
        pickle.load(open("user_address.dat", "rb"))
        return True
    except:
        return False

# returns the previously saved home address
def get_home_address():
    if check_home_address() is True:
        return pickle.load(open("user_address.dat", "rb"))
    else:
        return None
