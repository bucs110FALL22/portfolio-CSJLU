import requests

class AnimeAPI:
  def __init__(self):
    
    '''
    Initializes the API url for getting random anime quotations
    '''
    
    self.api_url = f'https://animechan.vercel.app/api/random'

  def get(self):

    '''
    Converts API data into json and checks to see if 'quote' data from the API url can be obtained. 
    If so, returns what is contained in 'quote'.
  
    Returns data currently in 'quote'
    '''
    
    r = requests.get(self.api_url)
    response = r.json()
    result = response['quote']
    if response.get('quote'):
      return result
    else:
      None


  def __str__(self):
    
    '''
    Returns a string that represents the data in 'quote'
    '''
    
    return f"{self.get()}"

    


