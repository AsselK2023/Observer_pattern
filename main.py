from abc import ABC, abstractmethod

class Observer(ABC):
    @abstractmethod
    def update(self, temperature, humidity):
        pass

class WeatherData:
    def __init__(self):
        self._observers = []
        self._temperature = 0
        self._humidity = 0

    def add_observer(self, observer):
        self._observers.append(observer)

    def remove_observer(self, observer):
        self._observers.remove(observer)

    def set_measurements(self, temperature, humidity):
        self._temperature = temperature
        self._humidity = humidity
        self.notify_observers()

    def notify_observers(self):
        for observer in self._observers:
            observer.update(self._temperature, self._humidity)

class WeatherDisplay(Observer):
    def update(self, temperature, humidity):
        print(f"Weather is changed. T: {temperature}°C, H: {humidity}%")

class PhoneApp(Observer):
    def update(self, temperature, humidity):
        print(f"Phone App: Temperature changed {temperature}°C")

class EmailNotification(Observer):
    def update(self, temperature, humidity):
        print(f"Email: Weather is changed. T: {temperature}°C, H: {humidity}%")

if __name__ == "__main__":
    weather_data = WeatherData()
    display = WeatherDisplay()
    phone_app = PhoneApp()
    email_notification = EmailNotification()

    weather_data.add_observer(display)
    weather_data.add_observer(phone_app)
    weather_data.add_observer(email_notification)

    weather_data.set_measurements(25, 60)
    weather_data.set_measurements(30, 55)