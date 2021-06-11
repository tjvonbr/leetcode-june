""" 
Create a calendar that does not allow double booking.  If a pending event
conflicts with an already booked event, return False.  Otherwise, add the
event and return True.

Week of June 8th - 14th, 2021
"""
class MyCalendar:
    def __init__(self):
        self._calendar = []

    def book(self, start: int, end: int) -> bool:
        for booked_start, booked_end in self._calendar:
            if booked_start < end and start < booked_end:
                return False
        self._calendar.append((start, end))   
        return True 
        
# ACCEPTED