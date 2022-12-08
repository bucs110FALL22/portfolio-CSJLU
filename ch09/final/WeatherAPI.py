import requests

class WeatherAPI:

  def __init__(self):
    
    '''
    Initializes the API url for getting weather at specific locations
    '''
    
    self.api_url = f"https://api.openweathermap.org/data/2.5/weather?lat=42.05678&lon=-76.02539&appid=415a293136d42c2c83285355a72009e6"

  def get(self):
    
    '''
    Converts API data into json and checks to see if 'feels_like' data from the API url can be obtained. 
    If so, returns what is contained in 'feels_like'.
  
    Returns data currently in 'feels_like'
    '''
    
    r = requests.get(self.api_url)
    response = r.json()
    result = response['main']['feels_like']
    if response.get('main'):
      return result
    else:
      return None 

  def __str__(self):
    
    '''
    Returns a string that represents the data in 'feels_like'
    '''
    
    return f"{self.get()}"





