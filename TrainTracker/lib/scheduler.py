class Scheduler:
    """
    Refer: http://www.nncron.ru/help/EN/working/cron-format.htm

    * * * * * *
    | | | | | |
    | | | | | +-- Year              (range: 1900-3000)
    | | | | +---- Day of the Week   (range: 1-7, 1 standing for Monday)
    | | | +------ Month of the Year (range: 1-12)
    | | +-------- Day of the Month  (range: 1-31)
    | +---------- Hour              (range: 0-23)
    +------------ Minute            (range: 0-59)
    """

    def start(self):
        pass