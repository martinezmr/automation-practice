application programming interface - a way for a comptuer program to communicate directly with another computer program

restful API - an API that follows a specific set of constraints

RESTful API Constraints
- Uniform interface - follow a consistent and decoupled interface for API Calls (only one URI for any given resource)
- client-server - there must be a decoupled client and server in the implementation architecture (not same piece of software)/(all communication happens between the API interface)
- stateless - each API call must contain everything required to perform the operation (the sever cannot 'remember' the client from request to request)


REST vs. SOAP
REST - representational state transfer; guidelines for the structure and organization of an API (not a protocol; it's an architecture); can use JSON, XML, YAML, markdown, CSV, plaintext
SOAP - simple object access protocol; a protocol specified at various layers; more overhead, but more comprenhensive; only uses XML

HTTP Request Method - single word 'token' that loosely described the action being performed (first word in request)
- GET - getting information
- HEAD
- POST - adds new information
- PUT - modifies existing information
- DELETE - deletes information
- CONNECT
- OPTIONS
- TRACE

HTTP Response Codes - 3-digit numeric code indicating the type of response (typically text note sent with response)
- 1XX (100-199) - Informational Responses
- 2XX (200-299) - Successful Responses (OK)
- 3XX (300-399) - Redirects
- 4XX (400-499) - Client Errors
  - 401 - Unauthorized
  - 403 - Forbidden
  - 404 - Not Found
- 5XX (500-599) - Server Errors

HTTP Headers - 