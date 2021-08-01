# Используя ссылки в конце данного урока, ознакомьтесь с таким средством инкапсуляции как свойства.
# Ознакомьтесь с декоратором property в Python. Создайте класс, описывающий температуру и
# позволяющий задавать и получать температуру по шкале Цельсия и Фаренгейта, причём данные могут
# быть заданы в одной шкале, а получены в другой.

class Temperature:

    def __init__(self, temperature):
        self.temperature = temperature

    def to_fahrenheit(self):
        return self.temperature * 1.8 + 32

    def to_celsius(self):
        return (self.temperature - 32) / 1.8

    # @property
    # def temperature(self):
    #     return self.__temperature
    #
    # @temperature.setter
    # def temperature(self, value):
    #     self.__temperature = value


temp = Temperature(float(input("Set Celsius: ")))
temp1 = Temperature(float(input("Set Fahrenheit: ")))
print("Celsius: ", temp.temperature)
print("Celsius to Fahrenheit: ", temp.to_fahrenheit())
print("Fahrenheit: ",temp1.temperature)
print("Fahrenheit to Celsius: ", temp1.to_celsius())


