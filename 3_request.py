"""
If we want to make HTTP request in Python, then we have requests library for it.

Request is a 3rd party library: we need to install it: pip install requests
And we are already familiar with HTTP methods.
"""

import requests

# --------------------------------------------------------------------
# Making GET request
# --------------------------------------------------------------------
# --------------------------
# Basic GET request -
# --------------------------
response = requests.get("https://api.github.com")

# Now we know, that when we make a request to a server, then it returns us
# metadata and the content that we are looking for.

# metadata may include - response code of request

# checking its response status
print(response.status_code)

# if we don't want to heck the response’s status code in an if statement.
# so, there is another way to check using built in method of request library whether it is successful or not.

import requests
from requests.exceptions import HTTPError

URLS = ["https://api.github.com", "https://api.github.com/invalid"]

for url in URLS:
    try:
        response = requests.get(url)
        response.raise_for_status() # If you invoke .raise_for_status(), then Requests will raise an HTTPError for status codes between 400 and 600.
    except HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except Exception as err:
        print(f"Other error occurred: {err}")
    else:
        print("Success!")


# The response of a GET request often has some valuable information, 
# known as a payload, in the message body.
# sometimes, we want response body in Bytes as well, in case of text or image or a file
# to get the response in bytes - we can get it with response.content
print(response.content) # so, this gives raw bytes

# if we want it in text format, then we have
print(response.text) # converting this byte will require encoding schema, request tries to guess the encoding based on the response’s headers if you don’t specify one.

"""
If I had to specify encoding, then I would do like this

response.encoding = "utf-8"  # Optional: Requests infers this.
print(response.text)
"""

# Dealing with JSON object
print(response.json()) # deserialize JSON - converting into Python Dict

# we can also get the URL like this
print(response.url)
print(response.headers) # to see the headers

# --------------------------
# Passing Parameter - 
# if we want to add query parameter, then we have `params` parameter.
# But when do i pass params parameter?
#   Query parameters allow you to filter data based on specific criteria. 
#   Many APIs implement pagination to limit the amount of data returned in each response.
#   We can also Sort the result using query parameter.
#   In some APIs we may also select the response format, if it is JSON or XML
# --------------------------
params = {'key1': 'value1', 'key2': 'value2'}
response = requests.get('https://api.example.com/data', params=params)



# --------------------------
# What are Headers?
# Headers are key-value pairs included in the HTTP request 
# and response messages exchanged between a client and a server. 
# They provide additional information about the request or response .
# Now, Headers can be send by client and User
# 


# --------------------------