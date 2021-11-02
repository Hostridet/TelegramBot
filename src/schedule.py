import calendar
from datetime import datetime, timedelta


class Schedule:
    def __init__(self):
        self.now = datetime.now()

    def get_num_weeks(self):
        sep = datetime(self.now.year if self.now.month >= 9 else self.now.year - 1, 9, 1)
        d1 = sep - timedelta(days=sep.weekday())
        d2 = self.now - timedelta(days=self.now.weekday())
        parity = ((d2 - d1).days // 7) % 2
        if parity:
            return "even"
        else:
            return "odd"

    def get_number_of_day(self):
        day = datetime.today()
        name_week = calendar.day_name[day.weekday()]
        day_code = 0
        code_to_day = {
            "Monday": 1,
            "Tuesday": 2,
            "Wednesday": 3,
            "Thursday": 4,
            "Friday": 5,
            "Saturday": 6,
            "Sunday": 7
        }
        if name_week in code_to_day:
            day_code = code_to_day[name_week]
        return day_code

    def get_name_of_day(self, day_code):
        return 'static/' + self.get_num_weeks() + '/' + str(day_code) + '.PNG'

    def get_week(self, day_code):
        week = ''
        weeks_ru = {
            1: "Понедельник",
            2: "Вторник",
            3: "Среда",
            4: "Четверг",
            5: "Пятница",
            6: "Суббота",
            7: "Воскресенье"
        }
        if day_code in weeks_ru:
            week = weeks_ru[day_code]
        return week

    def get_day(self):
        return datetime.now().day

    def get_day_tomorrow(self):
        return (datetime.now() + timedelta(days=1)).day

    def get_month(self):
        month_ru = {
            "October": "октября",
            "November": "ноября",
            "December": "декабря",
            "January": "января",
            "February": "февраля",
            "April": "апреля",
            "March": "марта",
            "May": "мая",
            "June": "июня",
            "July": "июля",
            "August": "августа",
            "September": "сентября",
        }
        if calendar.month_name[datetime.today().month] in month_ru:
            return month_ru[calendar.month_name[datetime.today().month]]