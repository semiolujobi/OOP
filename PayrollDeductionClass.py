class Payroll:

    def __init__(self, description, date, charge, employeeid):
        self.__description = description
        self.__date = date
        self.__charge = charge
        self.__employeeid = employeeid

    def set_description(self, description):
        self.__description = description

    def set_date(self, date):
        self.__date = date

    def set_charge(self, charge):
        self.__charge = charge

    def set_employeeid(self, employeeid):
        self.__employeeid = employeeid

    def get_description(self):
        return self.__description

    def get_date(self):
        return self.__date

    def get_charge(self):
        return self.__charge

    def get_employeeid(self):
        return self.__employeeid
