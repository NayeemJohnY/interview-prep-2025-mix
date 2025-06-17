

An API (Application Programming Interface) is a set of protocols, routines, and tools that allow one piece of software or system to interact with another. It defines the methods and data formats that applications can use to communicate with each other, whether within the same system or over the internet.

Why is API Testing Important ?
Reliability and Performance
Security
Compatibility
Error Handling

HTTP methods (also called HTTP verbs) define the actions that can be performed on a resource in an HTTP request. These methods tell the server what action to perform on the specified resource (usually a URL).

Method	Purpose	Example Usage
GET	Retrieve data from a server	Fetching user details
POST	Submit data to be processed	Creating a new user
PUT	Update an existing resource	Replacing a user's data
PATCH	Partially update a resource	Updating just the name of a user
DELETE	Remove a resource	Deleting a user
HEAD	Retrieve headers (no body)	Checking metadata about a resource
OPTIONS	Retrieve communication options	Checking which methods are allowed for a resource
TRACE	Trace the request path	Debugging or diagnostics
CONNECT	Establish a tunnel to the server	Setting up an encrypted connection


Feature	SOAP	REST
Type	Protocol	Architectural style
Data Format	XML only	JSON, XML, HTML, plain text, etc.
Complexity	More complex and rigid	Simpler and lightweight
Standards	Strong standards (WS-Security, etc.)	No strict standards
State	Can be stateful	Stateless
Security	Built-in security (WS-Security)	Security managed through HTTPS/OAuth
Performance	Slower (due to XML and overhead)	Faster and more efficient
Error Handling	SOAP faults (detailed)	HTTP status codes (basic)
Caching	Not typically used	Supports caching via HTTP headers
Use Cases	Enterprise, financial services, telecom	Web services, mobile apps, public APIs

SOAP is ideal for situations where security, reliability, and complex transactions are critical (e.g., financial services, payment systems).

REST is preferred for modern web applications that require fast, simple, and scalable communication (e.g., social media platforms, mobile apps, and public APIs



Status Code	Meaning	When to Use
200 OK	Request succeeded, data returned	Successful GET, PUT, or PATCH requests
201 Created	Request succeeded, resource created	Successful POST request (creating a new resource)
400 Bad Request	Invalid syntax or malformed request	Invalid parameters or data format in the request
401 Unauthorized	No valid authentication credentials	Missing or incorrect authentication (e.g., API token)
403 Forbidden	Server refuses to authorize the request	Lack of permission to access the resource
500 Internal Server Error	Server encountered an unexpected error	Generic error when the server fails to process the request

What is Rest Assured, and why is it used for API testing?
Rest Assured is a popular Java-based library used for API testing, particularly for testing RESTful web services. It provides a simple and effective way to automate the process of sending HTTP requests and validating the responses, making it a useful tool for developers and testers working with APIs.

Ease of Use
Supports Various HTTP Methods
Flexible Assertion
Supports Authentication and Authorization
public class APITest {

    public static void main(String[] args) {
        
        // Sending a GET request to a mock API
        Response response = RestAssured.get("https://jsonplaceholder.typicode.com/posts/1");

        // Verifying the response status code
        response.then().statusCode(200);
        
        // Verifying the response body contains expected values
        response.then().body("id", equalTo(1))
                     .body("title", containsString("sunt aut facere"))
                     .body("userId", equalTo(1));
    }
}


public void testQueryParam() {
        RestAssured.baseURI = "https://jsonplaceholder.typicode.com";  // Example API

        // Send GET request with query parameter (e.g., userId=1)
        given()
            .param("userId", 1)  // Add query parameter (userId=1)
        .when()
            .get("/posts")  // Send GET request to /posts endpoint
        .then()
            .statusCode(200)  // Validate the status code is 200
            .body("userId[0]", equalTo(1));  // Assert the first post's userId is 1
    }

    public void testPathParam() {
        RestAssured.baseURI = "https://jsonplaceholder.typicode.com";  // Example API

        // Send GET request with path parameter (e.g., /posts/1)
        given()
            .pathParam("postId", 1)  // Add path parameter (postId=1)
        .when()
            .get("/posts/{postId}")  // Use path parameter in the URL
        .then()
            .statusCode(200)  // Validate the status code is 200
            .body("id", equalTo(1));  // Assert the post id in the response is 1
    }

     public void testBasicAuth() {
        RestAssured.baseURI = "https://example.com";  // Example API with Basic Auth

        given()
            .auth().basic("username", "password")  // Provide username and password for Basic Authentication
        .when()
            .get("/secure-endpoint")  // Send GET request to secure endpoint
        .then()
            .statusCode(200);  // Validate the response status code
    }


    Steps to follow:
Obtain an access token from the OAuth server.
Use the access token in the Authorization header to make API requests.

public void testOAuth() {
        // Step 1: Obtain access token
        String accessToken = given()
            .formParam("grant_type", "client_credentials")  // OAuth flow parameter
            .formParam("client_id", "your-client-id")
            .formParam("client_secret", "your-client-secret")
        .when()
            .post("https://oauth-server.com/token")  // OAuth token endpoint
        .then()
            .statusCode(200)  // Validate successful token retrieval
            .extract().path("access_token");  // Extract access token from response

        // Step 2: Use the access token in subsequent API request
        given()
            .auth().oauth2(accessToken)  // Use the access token for OAuth authentication
        .when()
            .get("https://api.example.com/secure-endpoint")  // Secure API endpoint
        .then()
            .statusCode(200);  // Validate the response status code

Authentication Type	Description	REST Assured Handling
Basic Authentication	Username and password sent in the Authorization header.	.auth().basic(username, password)
OAuth 2.0	Token-based authentication using access tokens.	.auth().oauth2(accessToken)
Bearer Token	Using a Bearer token (often obtained from OAuth).	.auth().oauth2(accessToken)
Digest Authentication	Secure method using hashed credentials.	.auth().digest(username, password)
API Key	Authentication using an API key in headers or query parameters.	.header("Authorization", "API-Key your-api-key") or .param("api_key", "your-api-key")
JWT (JSON Web Token)	Uses JWT tokens for secure communication.	.auth().oauth2("your-jwt-token")
Custom Header Authentication	Uses custom headers for authentication.	.header("X-Auth-Token", "your-auth-token")
Session Authentication	Uses session cookies after logging in.	.cookie("session_id", sessionId)
HMAC (Hash-based MAC)	Authentication using a cryptographic hash function.	Custom code to generate HMAC hash and pass it in headers.


What is JSON Schema Validation?
JSON Schema Validation is a method of validating the structure, format, and constraints of a JSON response against a predefined schema. A JSON schema defines the expected structure of the data, including the types of values (e.g., string, number, boolean), required fields, optional fields, and specific constraints (e.g., minimum, maximum, regex patterns). The goal of JSON Schema validation is to ensure that the API response is in the correct format and meets all the expected requirements.


 public void testJsonSchemaValidation() {
        RestAssured.baseURI = "https://jsonplaceholder.typicode.com"; // Example API

        // Define the expected schema file
        String schemaFile = "src/test/resources/response-schema.json";  // Path to your JSON schema file

        given()
            .when()
                .get("/users/1")  // Make a GET request to the endpoint
            .then()
                .assertThat()
                .body(matchesJsonSchemaInClasspath(schemaFile))  // Validate response body against the schema
                .body("id", equalTo(1))  // Additional assertion: validate `id` field value
                .body("name", notNullValue())  // Ensure `name` is not null
                .statusCode(200);  // Validate the response status code
    }


    In Rest Assured, you can handle dynamic response validation using several strategies, including:

Validating static values like status codes or non-changing fields.
Using regular expressions or pattern matching for dynamic fields that follow a certain format, such as timestamps or GUIDs.
Extracting dynamic values from the response and performing further assertions based on the extracted data.
Partial response validation to ignore certain dynamic fields that aren’t relevant for validation.


@Test
    public void testDeserialization() {
        RestAssured.baseURI = "https://jsonplaceholder.typicode.com";

        // Send GET request to retrieve a user and deserialize the response into a User object
        User user = given()
                        .when()
                            .get("/users/1")
                        .then()
                            .statusCode(200)
                            .extract()
                            .as(User.class);  // Deserialization: converting JSON to User object

        // Validate the deserialized data
        assert user.getName().equals("Leanne Graham");
        assert user.getEmail().equals("Sincere@april.biz");
    }