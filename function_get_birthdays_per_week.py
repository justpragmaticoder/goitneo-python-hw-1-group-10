from datetime import datetime
from collections import defaultdict


def get_birthdays_per_week(users):
    if len(users) == 0:
        return []

    today = datetime.today().date()
    prepared_data = defaultdict(lambda: None)

    for user in users:
        name = user["name"]
        birthday = user["birthday"].date()
        birthday_this_year = birthday.replace(year=today.year)

        if birthday_this_year < today:
            birthday_this_year = birthday.replace(year=today.year + 1)

        delta_days = (birthday_this_year - today).days

        # skip if birhday is after week from today
        if delta_days >= 7:
            continue

        weekday = birthday_this_year.weekday()

        # check current weekday is weekend, move to the next monday
        if weekday in [5, 6]:
            prepared_data["Monday"] = (prepared_data["Monday"] or []) + [name]
        else:
            birthday = birthday_this_year.strftime("%A")
            prepared_data[birthday] = (prepared_data[birthday] or []) + [name]

    # simply print prepared birthday colleagues
    for day in prepared_data:
        birthday_colleagues = prepared_data[day]
        print(f"{day}: {', '.join(birthday_colleagues)}")

    # return prepared values just for unittest (plz, don't treat it as a wrong realization)
    return prepared_data
