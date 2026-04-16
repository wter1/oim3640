# #TODO: Resquests and stuff
# import requests

# # GET: read all messages
# data = requests.get('https://oim.108122.xyz/messages').json()
# for msg in data:
#     print(msg)

# # POST: send a message (1-140 characters)
# requests.post('https://oim.108122.xyz/message',
#               json={'message': 'Hello from Wah!'},
#               headers={'X-Token': 'wahwah'})

# # Delete?
# requests.delete('https://oim.108122.xyz/message',
#               json={'message': 'Hello from Wah!'},
#               headers={'X-Token': 'wahwah'})

#TODO: API's
import requests
import os
from dotenv import load_dotenv
from pprint import pprint

load_dotenv()
API_KEY = os.getenv('OPENWEATHER_API_KEY')

location = input("Please enter a location: ")
url = (f'https://api.openweathermap.org/data/2.5/weather?q={location}&appid={API_KEY}&units=imperial')

print(url)
data = requests.get(url).json()

print(f"Wellesley: {data['main']['temp']}°F")

# Can you modify the code to get weather information for any city?

# print(len(data))
# pprint(data)


# #TODO: OpenAI
# import requests
# import os
# from dotenv import load_dotenv
# from pprint import pprint
# from openai import OpenAI


# load_dotenv()

# client = OpenAI()  # reads OPENAI_API_KEY from .env
# # response = client.chat.completions.create(
# #     model='gpt-5-nano',
# #     messages=[{'role': 'user', 'content': 'Hello!'}]
# # )
# # print(response.choices[0].message.content)

# response = client.responses.create(
#     response_id = 0
#     model = "gpt-5-nano",
#     input = "\033[1;35mWrite a one-sentence bedtime story about a Gnome called Rob who's so    hungry, he could eat a horse.\033[m"
#     previous_response_id = response_id + 1
# )


# print(f"\033[1;33m{response.output_text}\033[m")