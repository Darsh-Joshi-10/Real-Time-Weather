import tkinter as tk
import requests

class WeatherApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Weather App")
        
        self.city_label = tk.Label(self.master, text="Enter City:")
        self.city_label.pack(pady=10)
        
        self.city_entry = tk.Entry(self.master, font=("Arial", 12))
        self.city_entry.pack(pady=5)
        
        self.search_button = tk.Button(self.master, text="Search", command=self.get_weather)
        self.search_button.pack(pady=5)
        
        self.result_label = tk.Label(self.master, text="", font=("Arial", 12))
        self.result_label.pack(pady=10)
    
    def get_weather(self):
        city = self.city_entry.get().strip()
        
        if not city:
            self.result_label.config(text="Please enter a city")
            return
        
        # Add your OpenWeatherMap API key here
        api_key = "YOUR_API_KEY"
        
        try:
            url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=imperial"
            response = requests.get(url)
            data = response.json()
            
            if data["cod"] != 200:
                self.result_label.config(text="City not found")
            else:
                temperature = data["main"]["temp"]
                description = data["weather"][0]["description"]
                weather_info = f"Temperature: {temperature}°F\nDescription: {description}"
                self.result_label.config(text=weather_info)
        
        except requests.exceptions.RequestException:
            self.result_label.config(text="Error fetching weather data")
        
        self.city_entry.delete(0, tk.END)

root = tk.Tk()
app = WeatherApp(root)
root.mainloop()
