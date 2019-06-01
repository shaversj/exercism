import datetime


class Clock(object):
    def __init__(self, hour, minute):
        self.hour = hour
        self.minute = minute
        self.time_in_seconds = (self.hour * 3600) + (self.minute * 60)

    def __repr__(self):
        delta = datetime.timedelta(seconds=self.time_in_seconds)
        if delta.days != 0:
            days_to_seconds = int(delta.days) * 86400
            delta = delta - datetime.timedelta(seconds=days_to_seconds)

        formatted_delta = "{:0>8}".format(str(delta))

        return formatted_delta[:-3]

    def __eq__(self, other):
        return str(self) == str(other)

    def __add__(self, minutes):
        delta = datetime.timedelta(seconds=self.time_in_seconds)
        delta2 = datetime.timedelta(seconds=(minutes * 60))
        if delta.days != 0:
            days_to_seconds = int(delta.days) * 86400
            delta = delta - datetime.timedelta(seconds=days_to_seconds)

        result = delta + delta2

        if result.days != 0:
            days_to_seconds = int(result.days) * 86400
            result = result - datetime.timedelta(seconds=days_to_seconds)

        formatted_result = "{:0>8}".format(str(result))

        return formatted_result[:-3]

    def __sub__(self, minutes):
        delta = datetime.timedelta(seconds=self.time_in_seconds)
        delta2 = datetime.timedelta(seconds=(minutes * 60))
        if delta.days != 0:
            days_to_seconds = int(delta.days) * 86400
            delta = delta - datetime.timedelta(seconds=days_to_seconds)

        result = delta - delta2

        if result.days != 0:
            days_to_seconds = int(result.days) * 86400
            result = result - datetime.timedelta(seconds=days_to_seconds)

        formatted_result = "{:0>8}".format(str(result))

        return formatted_result[:-3]
