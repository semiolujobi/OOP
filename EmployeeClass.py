class Employee:

    def __init__(self, name, idnumber, department, jobtitle, monthlysalary):
        self.__name = name
        self.__idnumber = idnumber
        self.__department = department
        self.__jobtitle = jobtitle
        self.__monthlysalary = monthlysalary

    def get_name(self):
        return self.__name
    
    def get_idnumber(self):
        return self.__idnumber
    
    def get_department(self):
        return self.__department
    
    def get_jobtitle(self):
        return self.__jobtitle

    def get_monthlysalary(self):
        return self.__monthlysalary
