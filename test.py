import unittest
from datetime import datetime, timedelta
from collections import defaultdict

from function_get_birthdays_per_week import get_birthdays_per_week
from bot import *


def on_day(date, day):
    days = (day - date.weekday() + 7) % 7
    return date + timedelta(days=days)


class Test(unittest.TestCase):
    def test_birthdays_per_week(self):
        today = datetime.today().date()
        next_sunday = on_day(today, 5)
        next_saturday = on_day(today, 6)
        next_tuesday = on_day(today, 1)
        next_wednesday = on_day(today, 2)
        next_thursday = on_day(today, 3)
        arnold_birthday_month = (
            today.month - 1 if today.month == 12 else today.month + 1
        )
        fake_collegues = [
            {
                "name": "Bill Gates",
                "birthday": datetime(
                    1955, next_sunday.month, next_sunday.day
                ),  # next saturday
            },
            {
                "name": "Johnny Depp",
                "birthday": datetime(
                    1955, next_saturday.month, next_saturday.day
                ),  # next sunday
            },
            {
                "name": "Arnold Schwarzenegger",
                "birthday": datetime(1955, arnold_birthday_month, 17),
            },
            {
                "name": "Jim Carrey",
                "birthday": datetime(1955, next_tuesday.month, next_tuesday.day),
            },
            {
                "name": "Emma Watson",
                "birthday": datetime(1955, next_wednesday.month, next_wednesday.day),
            },
            {
                "name": "Daniel Radcliffe",
                "birthday": datetime(1955, next_thursday.month, next_thursday.day),
            },
        ]
        result = get_birthdays_per_week(fake_collegues)

        self.assertEqual(result["Monday"], ["Bill Gates", "Johnny Depp"])
        self.assertEqual(result["Tuesday"], ["Jim Carrey"])
        self.assertEqual(result["Wednesday"], ["Emma Watson"])
        self.assertEqual(result["Thursday"], ["Daniel Radcliffe"])

    def test_add_contact_happy_flow(self):
        contacts = {}
        result = add_contact(["John", 12341231], contacts)

        self.assertEqual(contacts, {"John": 12341231})
        self.assertEqual(result, "Contact added.")

    def test_change_contact_happy_flow(self):
        contacts = {"John": 12341231}
        result = change_contact(["John", 99999999], contacts)

        self.assertEqual(contacts, {"John": 99999999})
        self.assertEqual(result, "Contact updated.")

    def test_change_contact_not_found(self):
        contacts = {"Joshua": 12341231}
        result = change_contact(["John", 99999999], contacts)

        self.assertEqual(result, "Contact was not found.")

    def test_show_phone_happy_flow(self):
        contacts = {"Joshua": 12341231}
        result = show_phone(["Joshua"], contacts)

        self.assertEqual(result, 12341231)

    def test_show_phone_not_found(self):
        contacts = {"Joshua": 12341231}
        result = show_phone(["John"], contacts)

        self.assertEqual(result, "Contact was not found.")

    def test_show_all(self):
        contacts = {"Joshua": 12341231, "Steve": 2857371}
        result = show_all(contacts)

        self.assertEqual(result, "Joshua: 12341231\nSteve: 2857371")
