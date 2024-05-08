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
from requests.exceptions import HTTPError # we need to import this to let it handle bad requests

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
#   Request headers are sent by the client to the server as part of an HTTP request. 
#   They provide metadata about the request itself, including details such as the user agent, 
#   accepted content types, authentication credentials, cookies, and more. 

#   Response headers are sent by the server to the client in response to an HTTP request. 
#   They provide metadata about the server's response, including details such as the content type, 
#   caching directives, server information, and more.
# --------------------------
print(response.headers) # to check Server's header

"""
If we want to send Headers in the response

import requests

# Define custom headers
headers = {
    'User-Agent': 'MyCustomUserAgent/1.0',  # Example User-Agent header
    'Authorization': 'Bearer YOUR_ACCESS_TOKEN',  # Example Authorization header
    'Accept': 'application/json',  # Example Accept header
}

# Make a GET request with custom headers
response = requests.get('https://api.example.com/data', headers=headers)

# Handle the response
if response.status_code == 200:
    print('Request successful')
    print(response.text)
else:
    print('Error:', response.status_code)

"""

# POST, PUT, and PATCH requests pass their data through the message body rather than through parameters in the query string.
# Using Requests, you’ll pass the payload to the corresponding function’s data parameter.
"""
>>> import requests

>>> requests.post("https://httpbin.org/post", data={"key": "value"})
<Response [200]>

"""

# If, however, we need to send JSON data, then we can use the json parameter. 
# When we pass JSON data via json, Requests will serialize our data and add the correct Content-Type header for us.
"""
>>> response = requests.post("https://httpbin.org/post", json={"key": "value"})
>>> json_response = response.json()
>>> json_response["data"]
'{"key": "value"}'
>>> json_response["headers"]["Content-Type"]
'application/json'
"""


# --------------------------
# Request Inspection
# --------------------------

"""
When you make a request, the Requests library prepares the request before actually sending it 
to the destination server. 
Request preparation includes things like validating headers and serializing JSON content.

You can view the PreparedRequest object by accessing .request on a Response object:

>>> import requests

>>> response = requests.post("https://httpbin.org/post", json={"key":"value"})

>>> response.request.headers["Content-Type"]
'application/json'
>>> response.request.url
'https://httpbin.org/post'
>>> response.request.body
b'{"key": "value"}'
"""

# --------------------------
# Authentication:
# We can even authenticate ourself using requests by passing creds
# --------------------------

# ----------
# Basic Auth
# ----------
import requests
from requests.auth import HTTPBasicAuth

response = requests.get('https://api.example.com/data', auth=HTTPBasicAuth('username', 'password'))

# or we can pass directly as tuple
response = requests.get('https://api.example.com/data', auth=('username', 'password'))


# ----------
# Digest Authentication:
# Unlike Basic Authentication, Digest Authentication sends a hash of the username, password, 
# and other details, providing additional security over HTTP.
# ----------
import requests
from requests.auth import HTTPDigestAuth

response = requests.get('https://api.example.com/data', auth=HTTPDigestAuth('username', 'password'))

# ----------
# OAuth: 
# It involves tokens that users obtain after a login flow.
# ----------
import requests

# Assuming you have obtained an OAuth token
token = 'YOUR_OAUTH_TOKEN'
headers = {'Authorization': f'Bearer {token}'}
response = requests.get('https://api.example.com/data', headers=headers)

# ----------
# OAuth 2.0 Client Credentials:
# For server-to-server communication, 
# OAuth 2.0 client credentials grant can be used. 
# This requires obtaining a token from an OAuth server using client ID and secret.
# ----------
import requests

# Get token from OAuth server
token_url = 'https://api.oauthprovider.com/token'
client_id = 'YOUR_CLIENT_ID'
client_secret = 'YOUR_CLIENT_SECRET'
data = {'grant_type': 'client_credentials'}
response = requests.post(token_url, data=data, auth=(client_id, client_secret))
token = response.json().get('access_token')

# Use token for subsequent requests
headers = {'Authorization': f'Bearer {token}'}
response = requests.get('https://api.example.com/data', headers=headers)


# ----------
# API Keys:
# Some services use API keys for simplified access control. 
# This key is sent as part of the headers or as a query parameter in each request.
# ----------
import requests

api_key = 'YOUR_API_KEY'
headers = {'Authorization': f'ApiKey {api_key}'}
# Alternatively, you could append the API key in query params
# response = requests.get('https://api.example.com/data', params={'api_key': api_key})
response = requests.get('https://api.example.com/data', headers=headers)


# ----------
# SSL Certificate Verification
# By default requests connects to HTTPS, which require SSL certificate,
# but in case if we want to disable SSL certificate, maybe because requests has to land to HTTP
# so we can do this with parameter - verify = False
# ----------
"""
>>> import requests

>>> requests.get("https://api.github.com", verify=False)
InsecureRequestWarning: Unverified HTTPS request is being made to host
⮑ 'api.github.com'. Adding certificate verification is strongly advised.
⮑ See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#tls-warnings
⮑  warnings.warn(
<Response [200]>
"""

# ----------
# Max retries:
# requests uses urllib3 internally, 
# and urllib3 includes a retry mechanism which can be configured through the requests session object.
# ----------
import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

# Define a retry strategy
retry_strategy = Retry(
    total=3,  # Total number of retries
    status_forcelist=[429, 500, 502, 503, 504],  # Status codes to retry
    method_whitelist=["HEAD", "GET", "OPTIONS"],  # HTTP methods to retry
    backoff_factor=1  # Backoff factor to apply between attempts
)

# Apply the retry strategy to all HTTP requests
adapter = HTTPAdapter(max_retries=retry_strategy)
session = requests.Session()
session.mount("https://", adapter)
session.mount("http://", adapter)

# Make a GET request
response = session.get('https://api.example.com/data')
print(response.status_code)


# --------------------------------------------------------------------
# POST:
# --------------------------------------------------------------------

# ----------
# Sending data in key-value pair
# ----------
import requests

url = 'https://api.example.com/submit'
data = {
    'name': 'John Doe',
    'email': 'john.doe@example.com'
}

response = requests.post(url, data=data)
print(response.text)

# ----------
# Posting JSON data:
# if API needs to receive in JSON format, then we can pass this dictionary in json parameter
# ----------
import requests

url = 'https://api.example.com/data'
payload = {
    'key': 'value',
    'key2': 'value2'
}

response = requests.post(url, json=payload)  # The json parameter automatically encodes your data as JSON
print(response.text)

# ----------
# Uploading Files
# request, use the files parameter. 
# ----------
import requests

url = 'https://api.example.com/upload'
files = {'file': open('file.txt', 'rb')}  # Open the file in binary mode

response = requests.post(url, files=files)
print(response.text)

"""
HTTP different status:
    1xx: An informational response which indicates that the request was received and understood.
    2xx: Indicates that the action requested by the client was received, understood and accepted.
    3xx: Indicates that the client must take additional action to complete the request.
    4xx: Intended for situations in which the error seems to have been caused by the client.
    5xx: Occurs when the server fails to fulfill a request.
"""