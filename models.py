from pymodm import fields, MongoModel


class User(MongoModel):
    # because primary_key is True, we will need to
    # query this field using the label_id
    email = fields.EmailField(primary_key=True)
    age = fields.IntegerField()
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
        if since_time is None:
            # logic to create new array with only relevant data
            for r in hr:
                continue
        return np.average(hr)
