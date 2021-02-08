import requests

response = requests.get('https://www.google.com')
print(response)
# Alright, now what did the web server respond with?
# Let's take a look at the first 300 characters of the Response.text:
print(response.text[:300])
# Not that HTML can't be messy enough on its own,
# but let's look at the first bytes of the raw message that we received from the server:
response = requests.get('https://www.google.com', stream=True)
print(response.raw.read()[:100])
# What's all that? The response was compressed with gzip,
# so it had to be decompressed before we could even read the text of the HTML.
# One more thing that the Requests library handled for us!
# The requests.Response object also contains the exact request that was created for us.
# We can check out the headers stored in our object to see that the Requests module told the web server
# that it was okay to compress the content:
print(response.request.headers['Accept-Encoding'])
# And then the server told us that the content had actually been compressed.
print(response.headers['Content-Encoding'])
# First, how do we know if a request we made got a successful response?
# You can check out the value of Response.ok, which will be True if the response was good,
# and False if it wasn't.
print(response.ok)
print(response.status_code)
# To write maintainable, stable code,
# you’ll always want to check your responses to make sure they succeeded before trying to process
# them further. For example, you could do something like this:
url = 'https://www.google.com'
response = requests.get(url)
if not response.ok:
    raise Exception("GET failed with status code {}".format(response.status_code))
# Requests has us covered here, too! We can use the Response.raise_for_status() method,
# which will raise an HTTPError exception only if the response wasn’t successful.
response = requests.get(url)
response.raise_for_status()

# HTTP supports several HTTP methods, like GET, POST, PUT, and DELETE.
# We're going to spend time on the two most common HTTP requests: GET and POST.
# The HTTP GET method, of course, retrieves or gets the resource specified in the URL.
# By sending a GET request to the web server, you’re asking for the server to GET the resource for you.
# When you’re browsing the web, most of what you’re doing is using your web browser to issue a whole bunch
# of GET requests for the text, images, videos, and so forth that your browser will display to you.

# A GET request can have parameters. Have you ever seen a URL that looked like this?

"https://example.com/path/to/api/cat_pictures?search=grey+kitten&max_results=15"

#The question mark separates the URL resource from the resource's parameters.
# These parameters are one or more key-value pairs, formatted as a query string.
# In the example above, the search parameter is set to "grey+kitten", and the max_results parameter
# is set to 15.

#But you don't have to write your own code to create an URL like that one.
# With requests.get(), you can provide a dictionary of parameters, and the Requests module will construct
# the correct URL for you!
p = {"search": "grey kitten",
      "max_results": 15}
response = requests.get("https://example.com/path/to/api", params=p)
print(response.request.url)

#An alternative in that case is using the HTTP POST method.
# This method sends, or posts, data to a web service. Whenever you fill a web form and press a button
# to submit, you're using the POST method to send that data back to the web server.
# This method tends to be used when there's a bunch of data to transmit.

#In our scripts, a POST request looks very similar to a GET request.
# Instead of setting the params attribute, which gets turned into a query string and appended to the URL,
# we use the data attribute, which contains the data that will be sent as part of the POST request.
p = {"description": "white kitten",
     "name": "Snowball",
     "age_months": 6}
response = requests.post("https://example.com/path/to/api", data=p)
response.request.url
'https://example.com/path/to/api'

response.request.body
'description=white+kitten&name=Snowball&age_months=6'

#So, if we need to send and receive data from a web service, we can turn our data into dictionaries
# and then pass that as the data attribute of a POST request.

response = requests.post("https://example.com/path/to/api", json=p)
 response.request.url
'https://example.com/path/to/api'
 response.request.body
b'{"description": "white kitten", "name": "Snowball", "age_months": 6}'