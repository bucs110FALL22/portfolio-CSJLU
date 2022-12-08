import WeatherAPI
import AnimeAPI
import TempConvert

weather_api = WeatherAPI.WeatherAPI()
kelvin = weather_api.__str__()
temperature = TempConvert.kelvin_to_fahrenheit(kelvin)
anime_api = AnimeAPI.AnimeAPI()
quotation = anime_api.__str__()


def CombinedAPI():
  
  '''
  Checks the weather in Vestal and if its within a certain range, will print     out a random anime quotation. 

  Returns Vestal temperature and quotation (as long as its 10 and 90 degrees Fahrenheit)
  '''
  
  print(f"How does the current temperature  in Vestal feel like? {temperature} degrees Fahrenheit")
  if temperature > 10 and temperature < 90:
    print(f"The temperature isn't too hot or too cold! Here, have an anime quotation: {quotation} Enjoy the rest of your day!")
  elif temperature >= 90:
    print("Too hot for a quotation")
  elif temperature <= 10:
    print("Too cold for a quotation")
  

