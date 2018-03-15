from pymodm import fields, MongoModel


class User(MongoModel):
    # because primary_key is True, we will need to
    # query this field using the label_id
    email = fields.EmailField(primary_key=True)
    age = fields.IntegerField()
    age_units = fields.CharField()
    heart_rate = fields.ListField(field=fields.IntegerField())
    heart_rate_times = fields.ListField(field=fields.DateTimeField())

    def vals(self):
        """
        Returns dictionary of attributes for object

        :return: dictionary of attributes
        :rtype: dict
        """
        vals = {
            "user_email": self.email,
            "user_age": self.age,
            "age_units": self.age_units,
            "heart_rates": self.heart_rate,
            "heart_rate_times": self.heart_rate_times
            }
        return vals

    def average_hr(self, since_time=None):
        """
        Returns average of all stored heart rates for user
        since some time if given

        :return: average heart rate
        :rtype: float
        """
        try:
            import numpy as np
        except ImportError as e:
            print("Necessary import failed: {}".format(e))
            return None
        hr = np.array(self.heart_rate)
        if since_time is not None:
            hr_adjusted = np.array([])
            for index, rate in enumerate(hr):
                t = self.heart_rate_times[index]
                if t >= since_time:
                    hr_adjusted = np.append(hr_adjusted, rate)
            return np.average(hr_adjusted)
        return np.average(hr)

    def adjust_age(self):
        """
        Adjust age and age units to ranges
        """
        if self.age_units == "day":
            if self.age < 7:
                return
            elif self.age < 30:
                self.age = self.age%7
                self.age_units = "week"
            elif self.age < 365:
                self.age = self.age%30
                self.age_units = "month"
            else:
                self.age = self.age%365
                self.age_units = "year"
        elif self.age_units == "week":
            if self.age < 4:
                return
            elif self.age < 52:
                self.age = self.age%4
                self.age_units = "month"
            else:
                self.age = self.age%52
                self.age_units = "year"
        elif self.age_units == "month":
            if self.age < 12:
                return
            else:
                self.age = self.age%12
                self.age_units = "year"


    def tachycardic_range(self):
        """
        Determines lower bound for tachycardia given age of User

        :return: lower bound for tachycardia
        :rtype: int
        """
        pass
