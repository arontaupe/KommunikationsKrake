from icalendar import Calendar, Event, vCalAddress, vText
import os
from pathlib import Path
from datetime import datetime, timedelta


def create_ics(name, desc, dtstart, dtend, organizer='MAILTO:info@sommerblut.de', location='Köln'):
    """

    :param name:
    :param desc:
    :param dtstart:
    :param dtend:
    :param organizer:
    :param location:
    """
    # init the calendar
    cal = Calendar()

    # Some properties are required to be compliant
    cal.add('prodid', '-//Eventkalender//sommerblut.de//')
    cal.add('version', '2.0')

    # Add subcomponents
    event = Event()
    event.add('name', name)
    event.add('summary', name)
    event.add('description', desc)
    event.add('dtstart', dtstart)
    event.add('dtend', dtend)

    # Add the organizer
    organizer = vCalAddress(organizer)

    event['organizer'] = organizer
    event['location'] = vText(location)

    # Add the event to the calendar
    cal.add_component(event)

    directory = Path.cwd() / 'events'

    f = open(os.path.join(directory, f'{name}.ics'), 'wb')
    f.write(cal.to_ical())
    f.close()
