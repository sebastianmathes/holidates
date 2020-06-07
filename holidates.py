#!/usr/bin/env python3

from dateutil.easter import *
from datetime import timedelta
from datetime import date
from typing import List
from operator import itemgetter


def calc_holidays(year: int = date.today().year) -> List:
    """ calculates dates for holidays in the given year

    Parameters
    ----------
    year : int
        the year to calculate to holidays for, defaults to current year
    
    Returns
    -------
    holidates 
        a list containing the holidays with dates


    TODO: Add option to get holidays for other states than Hessen
    """
    # dates for static holidays
    holidates = [
            {'Name': 'Neujahr', 'Datum': date(year, 1, 1)},
            {'Name': '1ter Mai', 'Datum': date(year, 5, 1)},
            {'Name': 'Tag der dt. Einheit','Datum': date(year, 10, 3)},
            {'Name': '1ter Weihnachtstag', 'Datum': date(year, 12, 25)},
            {'Name': '2ter Weihnachtstag', 'Datum': date(year, 12, 26)}
            ]

    # timedeltas for easter dependent holidays
    deltas = {
            'Karfreitag': timedelta(days=-2),
            'Ostermontag': timedelta(days=1),
            'Himmelfahrt': timedelta(days=39),
            'Pfingstmontag': timedelta(days=50),
            'Fronleichnam': timedelta(days=60)  # only in BW,BY,HE,NW,RP,SL
            }

    for k, v in deltas.items():
        holiday = {'Name' : k, 'Datum': easter(year) + v }
        holidates.append(holiday)

    # sort output by date
    holidates = sorted(holidates, key=lambda dates : dates['Datum'])
    
    return holidates

if __name__ == "__main__":
    holi = calc_holidays()

    for day in holi:
        print(day['Name'], ":", day['Datum'])