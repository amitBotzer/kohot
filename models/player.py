from datetime import datetime
from dateutil.relativedelta import relativedelta

class Player:
    """

    Represent player who uses the application

    """

    def __init__(self, nickname, fullname, data_of_birth, hometown):
        """

        nickname is unique id among all players and it should be verified in the
        instantiator of this object.

        date_of_birth should be datetime typed

        """
        self._nickname = nickname
        self._fullname = fullname
        self._date_of_birth = data_of_birth
        self._hometown = hometown

    def get_age(self):
        """
        """
        nowtime = datetime.now()
        difference_in_years = relativedelta(nowtime, self._date_of_birth).years
        return difference_in_years
