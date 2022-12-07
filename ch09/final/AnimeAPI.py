import requests

class AnimeAPI:
  def __init__(self):
    self.api_url = f'https://animechan.vercel.app/api/random'

  def get(self):
    r = requests.get(self.api_url)
    response = r.json()
    result = response['quote']
    if response.get('quote'):
      return result
    else:
      None

  #data = r

  def __str__(self):
    return f"{self.get()}"

    


