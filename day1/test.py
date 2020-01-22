"""模拟一次汽车的简单尝试"""
class Car():
    def __init__(self,make, model, year):
        """初始化汽车属性"""
        self.make = make
        self.model = model
        self.year = year


    def get_descriptive_name(self):
        """返回整洁性的描述性信息"""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name


my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())
