
import java.util.Arrays;

public class Morgan_Stanley_Interview_Question {

    // Helper method to reverse a subarray in place
    public static void reverse(int[] arr, int left, int right) {
        while (left < right) {
            int temp = arr[left];
            arr[left++] = arr[right];
            arr[right--] = temp;
        }
    }

    public static void main(String[] args) {
        int[] arr = {7, 6, 4, 9, 1, 5, 8, 12, 11, 10, 2};
        int k = 3;
        // output = {4,6,7,5,1,9,11,12,8,2,10}
        int i = 0;
        while (i + k < arr.length) {
            reverse(arr, i, i + k - 1);
            i += k;
        }
        reverse(arr, i, arr.length - 1);
        System.out.println(Arrays.toString(arr));
    }

    // 3) Rest API testing status codes
    // 4) Explain about framework
    // 5) Explain what new things implemented in framework
    // 6) Do you have knowledge in SQL and NoSQL queries

    /*
     * R2 Tech Inteview
     * 
     * It looks like you've got a series of questions that span topics in software
     * testing, APIs, automation, and system performance. Let's break them down one
     * by one:
     * 
     * ---
     * 
     * ### 2) **Agile Ceremonies**
     * 
     * Agile ceremonies are a set of meetings that help teams stay aligned, make
     * decisions, and maintain focus during sprints. They include:
     * 
     * **Sprint Planning**: Defining the work to be completed in the upcoming
     * sprint.
     * **Daily Stand-up**: A daily, short meeting for team members to discuss
     * progress and roadblocks.
     * **Sprint Review**: A meeting at the end of the sprint to demo the work
     * completed.
     * **Sprint Retrospective**: Reflecting on what went well and what can be
     * improved in the next sprint.
     * 
     * ---
     * 
     * ### 3) **Test Strategy**
     * 
     * A **Test Strategy** is a high-level document that defines the test
     * objectives, approach, scope, and resources needed for the project. It sets
     * the direction for how testing will be performed. Key components include:
     * 
     * **Test objectives**
     * **Scope of testing**
     * **Testing approach**
     * **Test deliverables**
     * **Roles and responsibilities**
     * **Tools and resources**
     * 
     * ---
     * 
     * ### 4) **Test Planning**
     ** 
     * Test Planning** is a more detailed document that outlines the specifics of
     * how testing will be executed. This includes:
     * 
     * **Test goals**: What you're testing and why.
     * **Test deliverables**: What results are expected (e.g., reports, defect
     * logs).
     * **Test schedule**: Timeline for when each test activity will happen.
     * **Test environment**: Hardware, software, and network configurations needed.
     * **Risk management**: Identifying potential risks and how to mitigate them.
     * 
     * ---
     * 
     * ### 5) **Rest Assured Components**
     * 
     * In **Rest Assured**, components refer to the parts of the framework you
     * interact with to perform API testing. Some key components include:
     * 
     * **Request Specification**: Defines HTTP request settings (headers,
     * parameters, etc.).
     * **Response Specification**: Defines the expected HTTP response settings
     * (status code, body content, etc.).
     * **Assertions**: Validate the response (e.g., status code, JSON data, response
     * time).
     * **Request Methods**: Used for making HTTP requests like `GET`, `POST`, `PUT`,
     * `DELETE`.
     * 
     * ---
     * 
     * ### 6) **SQL Constraints**
     ** 
     * SQL Constraints** are rules applied to columns in a database table to ensure
     * the integrity and correctness of the data. Key constraints include:
     * 
     * **NOT NULL**: Ensures a column cannot have a NULL value.
     * **UNIQUE**: Ensures all values in a column are unique.
     * **PRIMARY KEY**: Uniquely identifies each row in a table.
     * **FOREIGN KEY**: Ensures the relationship between two tables is valid.
     * **CHECK**: Ensures the values in a column meet a specific condition.
     * **DEFAULT**: Provides a default value if no value is specified.
     * 
     * ---
     * 
     * ### 7) **Components in UI Framework**
     * 
     * 1. Page Object Model (POM)
     * 2. Locators
     * 3. Test Data Management
     * 4. Assertions
     * 5. Test Runner
     * 6. Reports
     * 7. Browser/Driver Management
     * 8. Synchronization
     * 9. Cross-Browser Testing
     * 10. Logging
     * 11. CI/CD Integration
     * 12. Utility Methods
     * 13. Mocking and Stubbing
     * 
     * 
     * They are often reusable elements that interact with one another to provide a
     * functional UI.
     * 
     * ---
     * 
     * ### 8) **How to Assert Response Field in Rest Assured**
     * 
     * To assert a response field in Rest Assured, you use methods like `.then()` to
     * validate specific values in the response. For example:
     * 
     * ```java
     * given().
     * when().
     * get("https://api.example.com").
     * then().
     * assertThat().
     * body("fieldName", equalTo("expectedValue"));
     * ```
     * 
     * This checks that the value of `"fieldName"` in the response body equals
     * `"expectedValue"`.
     * 
     * ---
     * 
     * ### 9) **Any Investment Stock Experience**
     * 
     * I don’t have personal experiences, but if you’re looking for insights or
     * resources on investment in stocks, I can provide data-driven strategies or
     * answer questions about stock analysis, risk management, etc. Let me know what
     * you'd like to explore!
     * 
     * ---
     * 
     * ### 10) **How to Disable SSL in Selenium**
     * 
     * To disable SSL verification in Selenium, you need to configure the browser’s
     * settings. For example, in Chrome:
     * 
     * ```java
     * ChromeOptions options = new ChromeOptions();
     * options.addArguments("--ignore-certificate-errors");
     * WebDriver driver = new ChromeDriver(options);
     * ```
     * 
     * For Firefox, you can use:
     * 
     * ```java
     * FirefoxOptions options = new FirefoxOptions();
     * options.setAcceptInsecureCerts(true);
     * WebDriver driver = new FirefoxDriver(options);
     * ```
     * 
     * ---
     * 
     * ### 11) **How to Handle Cookies in Rest Assured**
     * 
     * To handle cookies in Rest Assured, you can capture, assert, or modify cookies
     * during your requests. Example:
     * 
     * **Capture cookies:**
     * 
     * ```java
     * Response response = given().get("https://api.example.com");
     * Cookies cookies = response.detailedCookies();
     * ```
     * 
     * **Use cookies in requests:**
     * 
     * ```java
     * given().
     * cookies("cookieName", "cookieValue").
     * when().
     * get("https://api.example.com").
     * then().
     * statusCode(200);
     * ```
     * 
     * ---
     * 
     * ### 12) **How to Handle Ajax Components in Selenium**
     * 
     * Handling **AJAX** components in Selenium requires waiting for the page to
     * finish loading or for specific elements to be rendered. You can use:
     * 
     * **Explicit Waits**: Wait for a specific element to appear.
     * 
     * ```java
     * WebDriverWait wait = new WebDriverWait(driver, 10);
     * WebElement element =
     * wait.until(ExpectedConditions.visibilityOfElementLocated(By.id("ajaxElement")
     * ));
     * ```
     * 
     * **Implicit Waits**: Wait for elements in general without specifying which
     * one.
     * 
     * ```java
     * driver.manage().timeouts().implicitlyWait(10, TimeUnit.SECONDS);
     * ```
     * 
     * ---
     * 
     * ### 14) **Logic to Find First Non-Repeating Character in a String**
     * 
     * To find the first non-repeating character in a string, you can use a
     * frequency map. Here's a basic approach:
     * 
     * 1. Loop through the string and count the occurrences of each character.
     * 2. Loop through the string again to find the first character that occurs only
     * once.
     * 
     * Example code (Java):
     * 
     * ```java
     * public char firstUniqChar(String s) {
     * Map<Character, Integer> count = new HashMap<>();
     * 
     * for (char c : s.toCharArray()) {
     * count.put(c, count.getOrDefault(c, 0) + 1);
     * }
     * 
     * for (char c : s.toCharArray()) {
     * if (count.get(c) == 1) {
     * return c;
     * }
     * }
     * 
     * return '\0'; // If no non-repeating character is found
     * }
     * ```
     * 
     * ---
     * 
     * ### 15) **What is API Mocking? How to Do That**
     ** 
     * API mocking** involves simulating API responses without needing the actual
     * API to be up and running. This is useful for testing when the actual API is
     * unavailable.
     * 
     * **Mocking frameworks** like **WireMock** or **Mockito** can be used.
     * In **WireMock**, you can set up mock responses:
     * 
     * ```java
     * stubFor(get(urlEqualTo("/api/resource"))
     * .willReturn(aResponse().withStatus(200).
     * withBody("{ \"message\": \"Success\" }")));
     * ```
     * 
     * This creates a mock API that returns a predefined response.
     * 
     * ---
     * 
     * ### 16) **How to Reduce Test Execution Time**
     * 
     * To reduce test execution time:
     * 
     * **Parallel Execution**: Run tests in parallel using tools like **TestNG** or
     * **JUnit**.
     * **Optimize Test Suite**: Remove redundant tests, prioritize tests, and only
     * run critical ones.
     * **Test Data Optimization**: Use smaller datasets or mock data.
     * **Parallelize Test Environments**: Run tests on multiple environments or
     * devices simultaneously.
     * 
     * ---
     * 
     * ### 17) **CPU/Memory Metrics When Tests Are Executed in Parallel**
     * 
     * When tests are run in parallel, system resources such as CPU and memory usage
     * typically increase. Key metrics to monitor include:
     * 
     * **CPU Usage**: May increase linearly with the number of tests running in
     * parallel.
     * **Memory Usage**: Each parallel test consumes memory. Monitoring tools like
     * **JVM Profiler** or **VisualVM** can be helpful.
     * **Garbage Collection**: Running multiple tests in parallel can lead to more
     * frequent GC pauses.
     * 
     * ---
     * 
     * ### 18) **Testing Techniques**
     * 
     * Some common **testing techniques** include:
     * 
     * **Boundary Value Analysis (BVA)**: Testing at the boundaries of input values.
     * **Equivalence Partitioning**: Dividing input data into equivalent partitions
     * to reduce test cases.
     * **State Transition Testing**: Verifying system behavior across different
     * states.
     * **Pairwise Testing**: Testing all combinations of input values in pairs.
     * **Exploratory Testing**: Simultaneously learning about the application while
     * testing it.
     * 
     * ---
     * 
     */
}
