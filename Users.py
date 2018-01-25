class Users():
    def __init__(self,user,type,name,saving,month,year):
        self.__user = user
        self.__type = type
        self.__name = name
        self.__saving = saving
        self.__month = month
        self.__year = year

    def get_user(self):
        return self.__user
    def get_type(self):
        return self.__type
    def get_name(self):
        return self.__name
    def get_saving(self):
        return self.__saving
    def get_month(self):
        return self.__month
    def get_year(self):
        return self.__year


    def set_user(self, user):
        self.__user = user
    def set_type(self, type):
        self.__type = type
    def set_name(self, name):
        self.__name = name
    def set_saving(self,saving):
        self.__saving = saving
    def set_month(self,month):
        self.__month = month
    def set_year(self,year):
        self.__year = year

