application programming interface - a way for a comptuer program to communicate directly with another computer program

restful API - an API that follows a specific set of constraints
- Get
  - Download operation > read only and used to collect information
- Post
  - Creates new content / adds new resource
- Put
  - Modifies existing resources
- Patch
  - Updates part of resources
- Delete
  - Deletes resources

RESTful API Constraints
- Uniform interface - follow a consistent and decoupled interface for API Calls (only one URI for any given resource)
- client-server - there must be a decoupled client and server in the implementation architecture (not same piece of software)/(all communication happens between the API interface)
- stateless - each API call must contain everything required to perform the operation (the sever cannot 'remember' the client from request to request)


REST vs. SOAP
REST - representational state transfer; guidelines for the structure and organization of an API (not a protocol; it's an architecture); can use JSON, XML, YAML, markdown, CSV, plaintext
SOAP - simple object access protocol; a protocol specified at various layers; more overhead, but more comprenhensive; only uses XML