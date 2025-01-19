"""
- What is HTTP?
  Hypertext Transfer Protocol (HTTP) is designed to enable communications between clients and servers.
  HTTP works as a request-response protocol between a client and server.


  Example: A client (browser) sends an HTTP request to the server; 
           then the server returns a response to the client. 
           The response contains status information about the request 
           and may also contain the requested content.

  - So, what happens when we(browser) make HTTP request?
      1. You tell your browser to go to http://someserver.com/link.
      2. Your device and the server set up a TCP connection. (While HTTP doesn’t require TCP, it does require a reliable lower-level protocol.)
      3. Your browser sends an HTTP request to the server.
      4. The server receives the HTTP request and parses it.
      5. The server responds with an HTTP response.
      6. Your computer receives, parses, and displays the response.

           

- Different types of HTTP Methods
    GET
    POST
    PUT
    HEAD
    DELETE
    PATCH
    OPTIONS
    CONNECT
    TRACE

- from above the most common are - GET and POST
  - GET is used to request data from a specified resource.
    If we just want to fetch the data then we use get request 
    we can't request to modify anything with this request.
    we request for the specific data to fetch using the query string (name/value pairs) which sent in the URL of a GET request.
    We don't use get request for sensitive data.

  - POST is used to send data to a server to create/update a resource.
    So, the data we are sending to get it created or updated, we send it 
    in request body.

  - PUT is used to send data to a server to create/update a resource.

  - So, what's difference between PUT and POST?
    - PUT: This method is used to update an existing resource or create a new resource 
           if it does not exist at the specified URL.
           It is idempotent, meaning that making multiple identical PUT requests 
           will always result in the same state of the server. 


    - POST: This method is primarily used to create a new resource. 
            Unlike PUT, POST is not idempotent, which means if you send the same POST request multiple times, 
            it may result in multiple new resources being created. 

  - HEAD is almost identical to GET, but without the response body. So, in head we don't get any content.
    So, if we want to know the size of the content then we can prefer HEAD method.

  - PATCH: The PATCH method is used to apply partial modifications to a resource.

  - TRACE: If we want to test the path for the target resource, it is useful for debugging.

  - DELETE: The DELETE method deletes the specified resource.

  

- So, now what is HTTPS?
  HTTPS is a bit more secure protocol, in this communication happens in a secure way with encyption between client and server.
  This encrypted connection is provided by TLS or SSL.
  TLS and SSL are cryptographic protocols that encrypt the information before it's sent over a network.
  So, if user mentioning about sensitive information in some website, then just make sure that either it is a trusted host
  or it is HTTPS protocol. 
"""
