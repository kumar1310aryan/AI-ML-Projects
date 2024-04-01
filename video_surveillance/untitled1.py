class pwskills:
    def __init__(self,course_price,course_name):
        self.__course_price=course_price
        self.course_name=course_name
        
    @property 
    def course_price_access(self):
        return self.__course_price
    
    @course_price_access.setter 
    def course_price_set(self,price):
        if price>=3500:
            pass
        else:
            self.__course_price=price
    
    @course_price_access.deleter 
    def course_price_delete(self):
        del self.__course_price
        
pw=pwskills(3500, "data science")


pw.course_price_set=2500
pw.course_price_access
del pw.course_price_delete 
pw.course_price_access 