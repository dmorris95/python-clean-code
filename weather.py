#Task 1

class Weather:
    def __init__(self):
        self.city_weather = {
            "New York": {"temperature": 70, "condition": "Sunny", "humidity": 50},
            "London": {"temperature": 60, "condition": "Cloudy", "humidity": 65},
            "Tokyo": {"temperature": 75, "condition": "Rainy", "humidity": 70}
                            }
    
    def get_weather(self, city_name):
        if city_name in self.city_weather.keys():
            return self.city_weather.get(city_name, "Weather data is unavailable")
        else:
            return False

    def detailed_weather_display(self, city):
        detailed_forecast = self.get_weather(city)
        return (f"Weather in {city} is {detailed_forecast['condition']} with a temperature of {detailed_forecast['temperature']} degrees. The humidity is {detailed_forecast['humidity']}%.")

    def basic_weather_display(self, city):
        simple_forecast = self.get_weather(city)
        return (f"Weather in {city} is {simple_forecast['temperature']} degrees")


def main():
    weather_app = Weather()
    while True:
        try:
            city = input("Enter the city to get the weather forecast or 'exit' to quit: ")
            if city.lower() == 'exit':
                break
            if weather_app.get_weather(city) == False:
                print("Weather for", city, "is unavailable at the moment.")
            else:
                if input("Do you want a detailed forecast? (yes/no): ").lower() == "yes":
                    forecast = weather_app.detailed_weather_display(city)
                else:
                    forecast = weather_app.basic_weather_display(city)
                print(forecast)
        except Exception as e:
            print("An error occurred:", e)

if __name__ == "__main__":
    main()

