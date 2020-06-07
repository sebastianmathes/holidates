#!/usr/bin/env python3

from dateutil.easter import *
from datetime import timedelta
from datetime import date
from typing import List


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
    # timedeltas for easter dependent holidays
    deltas = [
            ['Karfreitag', timedelta(days=-2)],
            ['Ostermontag', timedelta(days=1)],
            ['Himmelfahrt', timedelta(days=39)],
            ['Pfingstmontag', timedelta(days=50)],
            ['Fronleichnam', timedelta(days=60)]  # only in BW,BY,HE,NW,RP,SL
            ]

    # dates for static holidays
    holidates = [
            ['Neujahr', date(year, 1, 1)],
            ['1ter Mai', date(year, 5, 1)],
            ['Tag der dt. Einheit', date(year, 10, 3)],
            ['1ter Weihnachtstag', date(year, 12, 25)],
            ['2ter Weihnachtstag', date(year, 12, 26)]
            ]

    for k, v in deltas.items():
        holidates[k] = easter(year) + v
    
    return holidates

if __name__ == "__main__":
    x = calc_holidays()
    for k,v in x.items():
        print(k,":",v)
