# Garmin

from decimal import Decimal

from ... import nmea
from ... import nmea_utils


class ASH(nmea.ProprietarySentence):
    sentence_types = {}

    def __new__(_cls, manufacturer, data):
        name = manufacturer + data[0]
        cls = _cls.sentence_types.get(name, _cls)
        return super(ASH, cls).__new__(cls)

    def __init__(self, manufacturer, data):
        self.sentence_type = manufacturer + data[0]
        super(ASH, self).__init__(manufacturer, data)


class ASHR(ASH):
    """ Ashtech Heading, Pitch, Roll
    """
    fields = (
        ("Subtype", "subtype"),
        ("Timestamp", "timestamp", nmea_utils.timestamp),
        ("Heading", "heading", Decimal),
        ("True", "hdg_true"),
        ("Roll", "roll", Decimal),
        ("Pitch", "pitch", Decimal),
        ("Heave (m)", "heave", float),
        ("Roll StdDev", "roll_std", float),
        ("Pitch StdDev", "pitch_std", float),
        ("Heading StdDev", "hdg_std", float),
        ("Quality", "quality", int),
    )
