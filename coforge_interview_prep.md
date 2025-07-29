# Interview Questions Preparation

## Set 1

### 1. Techniques of Blackbox Testing
- **Equivalence Partitioning:** Dividing input data into valid and invalid partitions and testing one value from each.
- **Boundary Value Analysis:** Testing at the boundaries between partitions.
- **Decision Table Testing:** Testing all possible combinations of inputs.
- **State Transition Testing:** Testing state changes based on various events.
- **Error Guessing:** Leveraging experience to guess problematic areas.
- **Use Case Testing:** Testing end-to-end business scenarios.

### 2. Example for Boundary Value Analysis
Suppose an input field accepts numbers from 1 to 100:
- **Boundary values:** 0 (just outside), 1 (minimum), 100 (maximum), 101 (just outside).
- Test cases: 0, 1, 100, 101.

### 3. Exception Thrown When XPath Not Locating in findElement
- **NoSuchElementException** is thrown when the element is not found with the provided XPath using `findElement`.

### 4. Difference Between findElement and findElements
| `findElement`                  | `findElements`                   |
| ------------------------------ | -------------------------------- |
| Returns first matching element | Returns a list of all matching   |
| Throws exception if not found  | Returns empty list if none found |

### 5. StaleElementReferenceException
This exception occurs when the element you are referencing is no longer attached to the DOM—for example, after a page reload or dynamic change.

### 6. Method Overloading and Method Overriding Examples in Framework

- **Method Overloading:** Two methods with same name but different parameters in the same class.
  ```java
  public void login(String username) {}
  public void login(String username, String password) {}
  ```
- **Method Overriding:** Subclass redefines a method with same name and parameters.
  ```java
  class BaseTest {
      public void setUp() {}
  }
  class DerivedTest extends BaseTest {
      @Override
      public void setUp() {}
  }
  ```

### 7. Can Constructor Be Overridden?
- **No**, constructors cannot be overridden. Constructor names are tied to the class name and are not inherited.

### 8. Can Value of Static Variable Be Changed? If Yes, How?
- **Yes**, the value of a static variable can be changed using:
  - The class name: `ClassName.variable = value;`
  - By any object reference (but not recommended).

### 9. What is Dry Run in Cucumber?
- A **dry run** in Cucumber verifies that every step defined in feature files has its corresponding step definition mapped, without actually executing the code.

### 10. Difference Between Scenario and Scenario Outline
| Scenario      | Scenario Outline                           |
| ------------- | ------------------------------------------ |
| Runs once     | Runs multiple times (for each set of data) |
| No parameters | Uses `` placeholders and Examples table    |

### 11. BeforeMethod and BeforeTest in TestNG
- **@BeforeMethod:** Runs before every test method.
- **@BeforeTest:** Runs once before any test methods in the `` tag of testng.xml.

### 12. Factory Annotation in TestNG
- **@Factory** is used to create instances of test classes dynamically, allowing different sets of data or configurations per instance.

### 13. git clone vs git fork
| git clone                          | git fork                                     |
| ---------------------------------- | -------------------------------------------- |
| Copies a repository locally        | Creates a copy on your remote GitHub account |
| No link to original repo on GitHub | Linked as forked on GitHub                   |

### 14. git pull vs git fetch
| git pull                   | git fetch                              |
| -------------------------- | -------------------------------------- |
| Fetches and merges changes | Only fetches changes (no merge)        |
| Local branch updated       | Local branch not updated automatically |

### 15. Types of Integration Testing
- **Big Bang Integration**
- **Top Down Integration**
- **Bottom Up Integration**
- **Incremental Integration (Mixed/Hybrid)**

### 16. Postman Code to Fetch Value of Particular Node
Example: Get a `token` node value from response.
```javascript
var jsonData = pm.response.json();
var token = jsonData.token;
console.log(token);
```

### 17. 302 Status Code
- **302 Found** means the requested resource has temporarily moved to a different URI, as indicated in the response's `Location` header. The client should use the new URI for this request.

### 18. Passing Username and Password in Header Without Exposing in Rest Assured
Use **Base64 encoding** with environment variables or config files to prevent exposure:
```java
String credentials = Base64.getEncoder().encodeToString((username + ":" + password).getBytes());
given().header("Authorization", "Basic " + credentials)...
```

### 19. Program to Find Duplicate Characters in a String With Occurrence (Without HashMap)
```java
public static void findDuplicateChars(String s) {
        s = s.trim().toLowerCase();
        char[] freq  = new char[26];
        for (char c : s.toCharArray()) {
            freq [c-'a']++;
        }

        for (int i =0; i <26; i++) {
            if (freq [i] > 1) {
                System.out.println("char: " + (char) (i+'a') + " occurrence " + freq [i]);
            }
        }
    }
```


## Set 2

### 1. Java Program to Remove Duplicate Characters from a String

**Example Solution:**

```java
public class RemoveDuplicates {
    public static String removeDuplicates(String str) {
        StringBuilder result = new StringBuilder();
        boolean[] seen = new boolean[256]; // For ASCII character set
        for (char c : str.toCharArray()) {
            if (!seen[c]) {
                seen[c] = true;
                result.append(c);
            }
        }
        return result.toString();
    }

    public static void main(String[] args) {
        String input = "geeksforgeeks";
        System.out.println(removeDuplicates(input)); // Output: geksfor
    }
}
```
This method keeps the first occurrence and removes any duplicate characters while preserving the original order[1][2].

### 2. Code to Read Username & Password from a Properties File

**Sample `config.properties` File:**
```
username=admin
password=secret
```

**Java Code:**

```java
import java.util.Properties;
import java.io.FileInputStream;

public class ReadProperties {
    public static void main(String[] args) throws Exception {
        Properties prop = new Properties();
        FileInputStream fis = new FileInputStream("config.properties");
        prop.load(fis);
        String username = prop.getProperty("username");
        String password = prop.getProperty("password");
        System.out.println("Username: " + username);
        System.out.println("Password: " + password);
    }
}
```
This code loads the properties file and fetches the `username` and `password` values using the `getProperty()` method[3][4].

### 3. Use of `GROUP BY` in SQL

- The `GROUP BY` clause groups rows that have the same values in specified columns into summary rows. Aggregate functions like `SUM()`, `COUNT()`, `AVG()`, etc., are often used with `GROUP BY` to get summary data for each group.
- **Example:**

```sql
SELECT department, COUNT(*) AS employee_count
FROM employees
GROUP BY department;
```
This query counts the number of employees in each department[5][6].

### 4. Convincing a Developer If “It’s Not a Bug”

- **Reference requirements/user stories:** Quote specific documentation or acceptance criteria that describe the expected behavior.
- **Visual evidence:** Provide screenshots or recordings to clearly demonstrate the issue.
- **Describe user impact:** Explain how the issue affects the end-user or workflow.
- **Foster collaboration:** Ask open questions for clarification and focus on collective quality, not blame[7][8].

### 5. Handling a JS Alert That Appears Randomly on Button Click in Selenium

**Java Approach:**

- Use `try-catch` block to detect and handle the alert whenever it appears.
- Example code:

```java
try {
    Alert alert = driver.switchTo().alert();
    alert.accept(); // Or alert.dismiss()
} catch (NoAlertPresentException e) {
    // No alert, continue
}
```
- This ensures your script won’t fail if the alert appears only sporadically[9][10].

### 6. What is a StaleElementReferenceException in Selenium?

- **Definition:** This exception is thrown when an element that was previously found in the DOM is no longer attached to it. It often occurs when the page is refreshed or dynamically updated after locating an element.
- **Common Causes:** DOM updates, page navigations, or AJAX calls that remove/rebuild elements.
- **Solution:** Re-locate the element after page changes before interacting with it[11][12].

### 7. Testing GraphQL APIs – Approach

- **Validate queries and mutations:** Test with valid/invalid inputs for schema validation.
- **Check edge cases:** Test limits, required fields, and error responses.
- **Use dedicated tools:** GraphiQL, Postman, or automation frameworks for structured testing.
- **Performance & security checks:** Test under load and check for unauthorized data access.
- **Automate assertions:** Integrate with CI tools or test runners for regression and continuous feedback[13][14].

### 8. How Many String Objects Will Be Created?  
### `String s1 = new String("JAVA");`

- **Two Objects:**
    1. A String literal `"JAVA"` in the string pool (if not already present).
    2. A new String object in the heap created by `new String()` referencing the value of `"JAVA"`[15][16].

### 9. Difference between `finally` and `finalize` in Java

|                | `finally`                                      | `finalize`                                     |
|----------------|------------------------------------------------|------------------------------------------------|
| Purpose        | Ensures code runs after try-catch, regardless of outcome | Called by garbage collector before reclamation |
| Usage          | As a block in exception handling               | As a protected method in `Object` class        |
| Invocation     | Explicit—programmer-defined                    | Automatic—invoked by JVM                       |
| Typical use    | Cleanup code (closing resources)               | Resource cleanup before object removal         |

### 10. Use of `protected` Access Modifier

- `protected` members are visible to:
  - The class itself,
  - All subclasses (even outside the package),
  - Other classes in the same package.
- **Purpose:** To allow controlled access to class internals for subclasses while restricting access from unrelated classes.

### 11. Ensuring Thread Safety When Running Tests in Parallel

- **Avoid shared mutable state:** Every test should have its own data, drivers, and setup.
- **Use thread-local storage:** Tools like `ThreadLocal` in Selenium.
- **Stateless test code:** Static/global variables should not store test-specific data.
- **Parallel execution frameworks:** Use frameworks (like TestNG/JUnit) that natively support parallelism and resource isolation.

---

## Set 3

# Selenium WebDriver Questions

### 1. Types of Waits in Selenium

- **Implicit Wait:** Sets a default wait time for the entire life of the WebDriver. Selenium waits for a certain time before throwing a `NoSuchElementException`.
  ```java
  driver.manage().timeouts().implicitlyWait(Duration.ofSeconds(10));
  // Example: Will wait up to 10s for elements before throwing error.
  ```
- **Explicit Wait:** Waits for a certain condition to occur before proceeding (e.g., for a button to be clickable).
  ```java
  WebDriverWait wait = new WebDriverWait(driver, Duration.ofSeconds(15));
  wait.until(ExpectedConditions.elementToBeClickable(By.id("submit")));
  // Real-time: Waits for a "Submit" button to be clickable before clicking.
  ```
- **Fluent Wait:** Similar to Explicit Wait, but can define the polling frequency and ignore specific exceptions.
  ```java
  Wait fluentWait = new FluentWait<>(driver)
      .withTimeout(Duration.ofSeconds(20))
      .pollingEvery(Duration.ofSeconds(2))
      .ignoring(NoSuchElementException.class);
  fluentWait.until(ExpectedConditions.visibilityOfElementLocated(By.id("user")));
  ```

### 2. Page Object Model (POM)

- **Definition:** POM is a design pattern where web page elements and functionalities are separated into different classes called Page Objects. This improves code maintainability and reusability.
- **Implementation Example:**
  - Create a class per page (e.g., `LoginPage`).
  - Define locators and methods for actions (e.g., `enterUsername`, `clickLogin`).
  ```java
  public class LoginPage {
      WebDriver driver;
      @FindBy(id="username") WebElement usernameField;
      @FindBy(id="password") WebElement passwordField;
      @FindBy(id="loginBtn") WebElement loginButton;

      public LoginPage(WebDriver driver) { this.driver = driver; }

      public void enterUsername(String username) { usernameField.sendKeys(username); }
      public void enterPassword(String password) { passwordField.sendKeys(password); }
      public void clickLogin() { loginButton.click(); }
  }
  ```

### 3. Handling Multiple Browser Windows or Tabs

- **Approach:**
  - Use `getWindowHandles()` to get all window handles.
  - Switch context with `switchTo().window(handle)`.
  ```java
  String mainWindow = driver.getWindowHandle();
  // Click opens a new window/tab
  Set allWindows = driver.getWindowHandles();
  for(String window : allWindows) {
      if (!window.equals(mainWindow)) {
          driver.switchTo().window(window);
          // Perform actions in new window
          driver.close();
      }
  }
  driver.switchTo().window(mainWindow); // Switch back
  ```

### 4. Difference Between driver.close() and driver.quit()

| Method            | Functionality                                       |
|-------------------|----------------------------------------------------|
| `driver.close()`  | Closes the current browser window                   |
| `driver.quit()`   | Quits the WebDriver session, closing all windows    |

### 5. Handling Dropdowns Using Select Class

- **Usage:**
  ```java
  Select select = new Select(driver.findElement(By.id("country")));
  select.selectByVisibleText("India");
  select.selectByIndex(2);
  select.selectByValue("IN");
  // For multi-select dropdowns: select.deselectAll();
  ```

### 6. Taking Screenshots in Selenium

- **Code Example:**
  ```java
  TakesScreenshot ts = (TakesScreenshot)driver;
  File src = ts.getScreenshotAs(OutputType.FILE);
  FileUtils.copyFile(src, new File("screenshot.png"));
  ```

### 7. Handling iframes in Selenium (with Use Case)

- **Switch by Index, Name, or WebElement:**
  ```java
  driver.switchTo().frame("iframeName");
  // Or: driver.switchTo().frame(0);
  // Or: driver.switchTo().frame(driver.findElement(By.id("frameId")));
  // To return: driver.switchTo().defaultContent();
  ```
- **Use Case:** Filling a form inside an iframe (e.g., payment gateway integration) by switching to the frame, performing actions, then returning to the main page.

# Core Java (OOPs) Questions

### 1. Abstraction in Java

- **Definition:** Hiding the internal implementation and showing only the necessary details.
- **Usage in Framework:** Create abstract `BasePage`/`BaseTest` classes with abstract methods like `login()`, forcing subclasses to implement them.

### 2. Difference Between Abstract Class and Interface

| Feature                     | Abstract Class                 | Interface                         |
|-----------------------------|-------------------------------|-----------------------------------|
| Methods                     | Can have abstract & concrete  | Only abstract (Java 7); default/static from Java 8 |
| Variables                   | Can have instance variables   | Only static and final             |
| Constructors                | Yes                           | No                                |
| Multiple Inheritance        | No                            | Yes (implements multiple)         |

### 3. Polymorphism

- **Definition:** Ability of an object to take many forms.
- **Compile-Time (Method Overloading):**
  ```java
  public void login(String user) {}
  public void login(String user, String pwd) {}
  ```
- **Run-Time (Method Overriding):**
  ```java
  class BasePage { void click() {} }
  class HomePage extends BasePage { void click() {/*overridden*/} }
  BasePage page = new HomePage(); // "click" of HomePage called
  ```

### 4. Encapsulation and Its Importance

- **Definition:** Wrapping data (variables) and code (methods) together, restricting direct access.
- **Importance:** Improves modularity, maintainability, and security in frameworks.
- **Real Project Use:** Page classes where fields are `private`, accessed via `public` getters/setters.

### 5. Difference Between Method Overriding and Method Overloading

| Overriding                               | Overloading                        |
|------------------------------------------|------------------------------------|
| Same method name/signature, subclass     | Same method name, different parameters, same class |
| Run-time polymorphism                    | Compile-time polymorphism          |

### 6. Real-time Example Using Interface and Inheritance

- **Example:**
  ```java
  interface DriverFactory { WebDriver createDriver(); }
  class ChromeFactory implements DriverFactory {
      public WebDriver createDriver() { return new ChromeDriver(); }
  }
  // In test: DriverFactory factory = new ChromeFactory();
  // WebDriver driver = factory.createDriver();
  ```
  - This allows swapping browsers easily and supports extensibility.

# Java Coding Questions

## String: First Non-Repeating Character

```java
public static Character firstNonRepeating(String str) {
    for (int i = 0; i < str.length(); i++) {
        char c = str.charAt(i);
        if (str.indexOf(c) == str.lastIndexOf(c)) {
            return c;
        }
    }
    return null;
}
// Example: firstNonRepeating("swiss") returns 'w'
```

### Array: Find the Missing Number in 1 to N

```java
public static int findMissing(int[] nums, int N) {
    int sum = N * (N + 1) / 2;
    int actualSum = 0;
    for (int n : nums) { actualSum += n; }
    return sum - actualSum;
}
// Example: findMissing(new int[]{1,2,4,5,6}, 6) returns 3
```

## Set 4
Certainly! Here are crisp, interview-focused answers and code snippets for each of your queries to help you prepare efficiently.

### Q2: Difference between `replace` and `replaceAll` in Java

- **replace(String target, String replacement)**
  - Replaces all occurrences of the target character or string with the replacement, based on literal matching.
  - **Does not support regular expressions.**
  ```java
  String input = "abc abc";
  input.replace("a", "z"); // "zbc zbc"
  ```
- **replaceAll(String regex, String replacement)**
  - **Uses regular expressions.** Replaces all substrings matching the regex.
  ```java
  String input = "abc abc";
  input.replaceAll("a.", "zz"); // "zz zz"
  ```

### Q3: What are Java Streams? Reverse a Number Using Java Streams.

- **Java Streams:**  
  Added in Java 8, streams allow you to process collections/data (sequences) in a functional style: filter, map, reduce, etc.

### Reverse a Number Using Streams:
```java
int num = 12345;
int reversed = Integer.parseInt(
    new StringBuilder(String.valueOf(num))
        .reverse().toString()
);
// Alternatively, without converting entire number to String (using streams over digits):
int number = 12345;
int rev = String.valueOf(number)
    .chars()
    .map(c -> c - '0')
    .reduce(0, (acc, digit) -> acc = acc * 10 + digit);
```
But using streams alone without converting to string is not straightforward. The most common way is by string manipulation.

### Q4: Reverse First and Last Digit of a Number (e.g., 12345 → 52341), without converting to String

```java
int n = 12345;
int temp = n;
int pow = 1;
while (temp >= 10) {
    temp /= 10;
    pow *= 10;
}
int first = n / pow;
int last = n % 10;
int mid = (n % pow) / 10;

// reconstruct number: last at front, mid as is, first at end
int result = last * pow + mid * 10 + first;
System.out.println(result); // Output: 52341
```

### Q5: How do you handle elements which are a part of shadow root in Selenium?

- **Shadow DOM** elements are not accessible with standard Selenium locators.
- Selenium (as of now) needs JavaScriptExecutor to pierce shadow roots.

**Example:**
```java
// step-by-step shadow root access
JavascriptExecutor js = (JavascriptExecutor)driver;
WebElement shadowHost = driver.findElement(By.cssSelector("shadow-host-css"));
WebElement shadowRoot = (WebElement) js.executeScript("return arguments[0].shadowRoot", shadowHost);
WebElement element = shadowRoot.findElement(By.cssSelector("selector-inside-shadow-root"));
// Alternatively, chain JS to keep drilling deeper as needed
```

### Q6: Challenges Faced While Designing a Selenium Framework

- **Cross-browser compatibility**
- **Dynamic web elements and XPaths**
- **Synchronization/Wait issues**
- **Test data management**
- **Scalability and maintainability**
- **Parallel execution and thread safety**
- **Integration with CI/CD (e.g., Jenkins)**
- **Reporting and logging**

Be ready to discuss solutions—like Page Object Model (POM), custom waits, parameterization, utility classes, thread-local drivers, etc.

### Q7: Automating 100 Manual Test Cases—Which to Pick First?

- **Prioritize critical flows:** Automate smoke tests, regression, high-risk, frequently run cases first.
- **Criteria:** Business value, repeatability, stability, potential for cost savings.
- **Do not pick randomly:** Follow ROI and impact analysis before selection.

### Q8: API Response Validations in Postman

- Use **Tests tab** to write JavaScript validation code.
- Example: Validate status code & response body
```javascript
pm.test("Status code is 200", function() {
    pm.response.to.have.status(200);
});
pm.test("Name is John", function() {
    var jsonData = pm.response.json();
    pm.expect(jsonData.name).to.eql("John");
});
```

### Q9: Knowledge of Playwright Automation Tool

- **Yes/No – As per your experience**
- **If yes:**  
  - Playwright offers fast, reliable cross-browser automation.
  - Supports context-level isolation, parallelism, and native support for modern web features (like Shadow DOM).
  - Example languages: JS, Java, Python, C#.  
  - Similar API to Selenium but generally faster and more modern.

# Round 2 (Technical)

### Q1: Tell Me About Yourself (Sample Structure)
- 30-second summary: Name, years of experience, core skills (Selenium, Java, API), domain, frameworks used, and 1-2 key achievements.
- End with current goals or interest in this role.

### Q2: Difference between isDisplayed(), isEnabled(), isSelected()

| Method          | What it checks                    |
|-----------------|----------------------------------|
| isDisplayed()   | Element is visible on page        |
| isEnabled()     | Element is enabled for user action|
| isSelected()    | Element is selected (checkbox/radio)|

### Q3: Presence of Element on Webpage (Selenium)

- Use `findElements()`, check list size:
  ```java
  List elements = driver.findElements(By.id("elementId"));
  if (elements.size() > 0) {
      // element exists
  }
  ```

### Q4: Handling Calendars in Selenium (Sample Code)

**Suppose calendar uses input fields, prev/next month buttons**
```java
// Example: Select a date
driver.findElement(By.id("calendar_icon")).click();
while (!driver.findElement(By.className("month")).getText().equals("May 2024")) {
    driver.findElement(By.id("nextMonth")).click();
}
driver.findElement(By.xpath("//td[text()='20']")).click();
```
Customize by your calendar widget's structure.

### Q5: Find All Broken Links Using Selenium

```java
List links = driver.findElements(By.tagName("a"));
for (WebElement link : links) {
    String url = link.getAttribute("href");
    if (url != null && !url.isEmpty()) {
        HttpURLConnection conn = (HttpURLConnection)new URL(url).openConnection();
        conn.setRequestMethod("HEAD");
        conn.connect();
        int respCode = conn.getResponseCode();
        if (respCode >= 400) {
            System.out.println(url + " is broken");
        }
    }
}
```
---

### Q5 (Duplicate): ElementClickInterceptedException Meaning and Handling

- **Meaning:**  
  Thrown if an element is present but cannot be clicked (e.g., obscured by another element).
- **Handling:**  
  - Wait for visibility/state.
  - Scroll element into view by JavaScript.
  ```java
  ((JavascriptExecutor)driver).executeScript("arguments[0].scrollIntoView(true);", element);
  element.click();
  ```
  - Use explicit waits.

### Q6: Difference Between Exception and Error

| Exception                   | Error                               |
|-----------------------------|-------------------------------------|
| Recoverable by code         | Irrecoverable (e.g., OutOfMemory)  |
| Subclass of Exception class | Subclass of Error class             |

### Q7: Explain Framework Structure / Create One from Scratch

- **Discuss layers:**  
  - Base (config, test setup/teardown)
  - Utilities (helpers)
  - Page Objects (element abstraction)
  - Test cases (business logic)
  - Reporting
  - CI/CD integration
- **Key points:** POM, modularization, reusability, maintainability.

### Q8: What Does `mvn clean` Do?

- Removes the `target` directory—deletes all compiled files and build artifacts for a fresh build.

### Q9: What is String in Java?

- **String is a class representing a sequence of characters.** Immutable objects, created using double quotes (e.g., `"hello"`).

### Q10: Why is String Immutable in Java?

- **Reasons:**  
  - Security (class loading, networking)
  - Thread safety (strings shared easily)
  - String Pooling (storage optimization)
  - Prevents unintended data modification
  
## Set 5
Thank you for sharing the detailed Zeta SDET 2 interview questions for Round 1 and Round 2 (Technical). Here’s a breakdown and detailed review of the questions, as well as guidance on how to approach answering them. This will help you prepare effectively.

## Round 1 (Technical): Breakdown & Approach

1. **Explain about your project, how long is your sprint?**
   - Focus on your latest automation/testing project.
   - Highlight your role, tools/tech stack, scope, and unique challenges.
   - Describe the agile process: “We follow 2-week sprints, plan user stories at the start, and conduct daily standups.”

2. **Have you created a framework from scratch? What are challenges you have faced while working with framework?**
   - Share specific details: “Yes, using Selenium, Maven, TestNG, and Page Object Model. Main challenges: code reusability, parallel execution, handling dynamic elements, and maintaining test data.”
   - Mention how you resolved issues.

3. **Difference between StringBuffer and StringBuilder**
   - Both are mutable, but `StringBuffer` is thread-safe (synchronized), `StringBuilder` is not (thus, faster).

4. **Program to remove duplicate elements from an ArrayList.**
   ```java
   List list = Arrays.asList(1, 2, 2, 3, 4, 3);
   Set set = new LinkedHashSet<>(list);
   List result = new ArrayList<>(set);
   ```

5. **Where have you used Inheritance in your framework?**
   - Example: “I’ve created a BaseTest class with common setup/teardown. Test classes extend BaseTest to reuse code.”

6. **How would you handle authentication popup using Selenium?**
   - If it’s a basic auth dialog: Use
     ```
     driver.get("http://username:password@yoursite.com");
     ```
   - For other popups: Use AutoIT or Robot (for Windows), or handle via API calls if possible.

7. **How many test cases have you automated in a single sprint?**
   - Give a specific number and context (“~20–25 e2e, depending on complexity and story points”).

8. **Difference between RequestSpecification, ResponseSpecification in REST Assured—write code & explain.**
   - `RequestSpecification`: Defines request setup (headers, params, body).
   - `ResponseSpecification`: Defines expected response (status, content-type).
   ```java
   RequestSpecification reqSpec = new RequestSpecBuilder().setBaseUri("api.com").build();
   ResponseSpecification resSpec = new ResponseSpecBuilder().expectStatusCode(200).build();
   given().spec(reqSpec).when().get("/users").then().spec(resSpec);
   ```

9. **Difference between 500 vs 503 API Status Code**
   - `500 Internal Server Error`: Server-side error, unexpected condition.
   - `503 Service Unavailable`: Server is temporarily unable to handle request (overload/maintenance).

## Round 2 (Technical): Breakdown & Approach

1. **Remove all duplicate elements from a string.**
   ```java
   String str = "banana";
   StringBuilder sb = new StringBuilder();
   for(char c : str.toCharArray()) {
     if(sb.indexOf(String.valueOf(c)) == -1) sb.append(c);
   }
   // Output: "ban"
   ```

2. **Fetch username and password from a properties file (code).**
   ```java
   Properties prop = new Properties();
   FileInputStream fis = new FileInputStream("config.properties");
   prop.load(fis);
   String user = prop.getProperty("username");
   String pass = prop.getProperty("password");
   ```

3. **Use of GroupBy in SQL.**
   - Used to aggregate rows sharing a value in columns (e.g., `SELECT dept, COUNT(*) FROM emp GROUP BY dept;`).

4. **Logged a bug, developer says it’s not a bug—how do you convince them?**
   - Use data: attach logs/screenshots, refer to requirements/user stories, reproduce issue step-by-step, open discussion.

5. **Handling random JS alert in Selenium.**
   - Use `WebDriverWait` with `ExpectedConditions.alertIsPresent()` in a try-catch, polling after any UI interaction.

6. **Stale Element Exception.**
   - Happens if element’s DOM reference is lost; resolve by re-finding the element just before use.

7. **Have you tested GraphQL API? How?**
   - Use tools like Postman or code with RestAssured, specifying GraphQL endpoint and passing queries as payload.

8. **How many string objects created: `String s1 = new String("JAVA");`**
   - Two: one in string pool ("JAVA"), one in heap (the new object).

9. **Difference between finally and finalize in Java**
   - `finally`: Block after try-catch, always executes code.
   - `finalize`: Method called by GC before object is destroyed (discouraged in new code).

10. **Use of protected access modifier?**
    - Accessible within package and by subclasses in any package.

11. **How do you achieve thread safety in your framework with parallel tests?**
    - Use ThreadLocal storage for WebDriver/objects, avoid static/shared mutable state, use synchronized blocks if needed.
