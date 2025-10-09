class Car:
    def __init__(self, brand, fuel_level, engin_status):
        self.brand = brand
        self._fuel_level = 0
        self.__engine_status = False

    def start_engine(self):
        if self._fuel_level > 0:
            self.__engine_status = True
            print("Двигатель запущен!")
        else:
            print("Невозможно завести двигатель — нет топлива!")

    def stop_engine(self):
        self.__engine_status = False
        print("Двигатель остановлен.")

    def drive(self, distance):
        fuel_needed = distance * 0.1
        if self.__check_fuel(fuel_needed):
            self._fuel_level -= fuel_needed
            print(f"Проехали {distance} км, осталось {self._fuel_level:} литров топлива.")
        else:
            print("Недостаточно топлива для поездки!")

    def refuel(self, amount):
        self._fuel_level += amount
        print(f"Добавлено {amount} литров топлива. Текущий уровень: {self._fuel_level:.1f} литров.")

    def get_status(self):
        engine_state = "включен" if self.__engine_status else "выключен"
        return f"Марка: {self.brand} | Топливо: {self._fuel_level:} | Двигатель: {engine_state}"

    def __check_fuel(self, required):
        return self._fuel_level >= required


car = Car("Toyota", 10, 1)
car.refuel(10)
car.start_engine()
car.drive(5)
print(car.get_status())