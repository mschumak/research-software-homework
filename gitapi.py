# Michael Schumaker
# Building Research Software

# Simple API usage example code

import requests
import json
import argparse
from pprint import pprint

the_parser = argparse.ArgumentParser(description="Code to read from the Github API. Enter token on command line if not using Google Colab.")
the_parser.add_argument(
    'token',
    default="",
    type=str,
    help="Enter the Github access token if Google Colab isn't being used.",
)

try:
    from google.colab import userdata
    token = userdata.get('ghtoken')
except ImportError:
    # The code is not being run from within Google Colab
    # Get the token from the command line instead
    the_args = the_parser.parse_args()
    token = the_args.token

user_response = requests.get(url='https://api.github.com/user', 
        headers={'Authorization': 'Bearer ' + token})

# Print the current user information
if (int(user_response.status_code) == 200):
    user_response_json = json.loads(user_response.text)
    print('Current username: ' + user_response_json['login'])
    print('Current name: ' + user_response_json['name'])

print("=====================================================")

# Do another request to get the users with large numbers of repositories
query = 'repos:>30000'
repos_response = requests.get(url='https://api.github.com/search/users', 
        params={'q': query},
        headers={'Authorization': 'Bearer ' + token})

if (int(repos_response.status_code) == 200):
    repos_response_json = json.loads(repos_response.text)
    print("Users with more than 30000 repositories:")
    for user in repos_response_json['items']:
        print(user['login'])



