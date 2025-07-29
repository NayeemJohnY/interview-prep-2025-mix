## Set 1

### 𝗥𝗼𝘂𝗻𝗱 𝟭: 𝗧𝗲𝗰𝗵𝗻𝗶𝗰𝗮𝗹 𝗦𝗰𝗿𝗲𝗲𝗻𝗶𝗻𝗴

#### 1. Walk me through your automation framework – which tools, design patterns, and reporting mechanisms do you use?
I have designed a **hybrid test automation framework** using **Java, Selenium WebDriver, TestNG, and Maven**. The main design pattern is **Page Object Model (POM)** to keep the code modular and maintainable. For managing dependencies, I use **Maven**. **Extent Reports** is integrated for comprehensive HTML reporting. Build execution and CI/CD is managed via **Jenkins**, and all code is version-controlled with **Git**. The architecture comprises base classes, page classes, utility classes, and test classes, ensuring clear separation of concerns and reusability[4][6].

#### 2. Explain how you use Selenium WebDriver with Java. How do you handle dynamic web elements?
With Selenium WebDriver in Java, I automate browser actions and UI validation. For **dynamic web elements** (where IDs, classes, or XPaths may change), I use strategies such as:
- **Partial attribute matching** with XPath `contains()` or `starts-with()`
- **Stable attributes** for locating via CSS or data attributes
- **Explicit waits** (`WebDriverWait` and `ExpectedConditions`) to handle delayed or dynamically loaded components[1][3][9].

#### 3. What is the role of TestNG in your framework? How do you implement data-driven testing using `@DataProvider`?
**TestNG** is my test runner and assertion library. It supports grouping, parallel execution, detailed reporting, and annotation-based lifecycle management. For **data-driven testing**, I use the `@DataProvider` annotation to feed multiple sets of data into a test method, maintaining test data in Excel, JSON, or arrays, and returning them through dedicated provider methods[6].

#### 4. How do you handle waits in Selenium? What’s the difference between implicit, explicit, and fluent waits?
- **Implicit Wait:** Applies globally, waits for a predefined period until elements appear, but isn’t flexible.
- **Explicit Wait:** Waits for specific conditions for particular elements, e.g., presence, visibility, clickability.
- **Fluent Wait:** Like explicit but customizable polling frequency and exception ignoring, useful for highly dynamic sites[1][3].

#### 5. How do you manage test execution in Jenkins? Have you set up CI pipelines for automated test runs?
All tests are run via **Jenkins pipelines**, which are triggered by code pushes to Git. Jenkins pulls from the repository, executes Maven build and test phases, and publishes reports after each execution. This ensures tests are run consistently on every build and before deployments[4][6].

#### 6. What kind of reports do you generate post automation execution? How do you integrate Extent Reports or Allure?
I use **Extent Reports** for customizable, interactive HTML reports with embedded screenshots and logs. Integration is done by initializing the Extent Report in the test base and logging status in each test method. For Allure, test annotations and listeners are used for report generation and attachment handling[4][6].

#### 7. What is Page Object Model (POM)? How do you maintain reusable components across multiple test cases?
**POM** is a design pattern where we maintain a class for each page containing all element locators and actions relevant to that page. This fosters code reusability. Shared methods are in base or utility classes, and page classes are reused across multiple test cases for consistency[6][8].

#### 8. Have you automated REST API test cases? Which tools or libraries do you use (like Rest Assured or Postman)?
Yes, I have automated REST API tests using **Rest Assured**. It covers validations such as response code, headers, payload, and supports chaining requests. I have also used **Postman** for exploratory API testing and generating test scenarios.

#### 9. How do you capture screenshots on failure and attach them to reports?
On test failure, I use Selenium’s `TakesScreenshot` interface. Captured images are saved to a designated folder, and their paths are logged into **Extent Reports** or **Allure** as attachments, making debugging easier[4][6].

#### 10. What is your approach to version control? How do you structure your code in Git and collaborate with teams?
All code is versioned in **Git** using a feature-branch workflow. The structure follows modular packaging (e.g., `/src/main/java/pages`, `/utils`, `/tests`). We use pull requests and code reviews to ensure quality and visibility in team collaboration[4][6].

### 𝗥𝗼𝘂𝗻𝗱 𝟮: 𝗜𝗻-𝗱𝗲𝗽𝘁𝗵 𝗧𝗲𝗰𝗵𝗻𝗶𝗰𝗮𝗹 𝗘𝘃𝗮𝗹𝘂𝗮𝘁𝗶𝗼𝗻

#### 1. Describe your framework’s lifecycle. How do you manage parallel execution, cross-browser testing, and reporting?
The framework lifecycle starts with a clean environment setup, followed by test data preparation. **Parallel execution** is enabled via TestNG’s `parallel` attribute and Selenium Grid or cloud providers for cross-browser support. Reporting is continuous, with detailed reports—like Extent Reports—generated after each run, including logs and screenshots[4][6].

#### 2. How do you handle flaky test cases and reduce their occurrence?
I mitigate flaky tests through robust waits, isolation of test data, clean-up routines, retry mechanisms, and by making sure tests are atomic and independent. I also review logs to identify non-deterministic behaviour and refactor or stabilize tests accordingly[4].

#### 3. Explain your experience with API automation in detail – how do you validate headers, payloads, status codes, and chaining requests?
With **Rest Assured**, I validate:
- **Status codes** (e.g., 200, 404)
- **Response headers** for expected values
- **Payload structures** and content with JSON/XML path assertions
- **Chaining requests** by extracting tokens or IDs from one call and passing them to subsequent requests

#### 4. Have you worked with Docker or containers in your automation environment? If yes, explain how you run your tests inside containers.
Yes, I have used **Docker** to build consistent automation environments. Test suites run inside containers defined in Dockerfiles, supporting scalable, reproducible, and isolated test executions—integrated into CI/CD pipelines.

#### 5. How do you manage secrets, config files, and environment-specific data during test execution?
I use **config files** (e.g., `application.properties`, encrypted environment variables) and secret stores. Sensitive data is never hardcoded and is injected at runtime via CI/CD managers or environment variables.

#### 6. What security tools or code quality tools have you integrated into your test pipeline (e.g., SonarQube, OWASP)?
I’ve integrated **SonarQube** for code quality, static analysis, and coverage. For security, I use **OWASP Dependency-Check** to scan dependencies and occasionally perform **DAST or SAST** during CI runs.

#### 7. How do you ensure code coverage and track untested areas of your application?
**Code coverage tools** (like Jacoco for Java) run during the Maven build. I analyze coverage reports and identify missing test areas to improve automation coverage in subsequent sprints.

#### 8. Have you worked on test data management? How do you create and clean test data in pre and post conditions?
Test data is created via scripts or APIs before tests start. Post-test, clean-up scripts or teardown hooks ensure no residual data, maintaining environment integrity for future runs.

#### 9. Explain how you’ve integrated Jenkins with your framework. How do you trigger jobs on Git commits?
**Jenkins** is connected to our Git repository. Any push or merge triggers jobs via **webhooks** or **polling SCM**; Jenkins invokes the Maven build, runs automation, and publishes reports automatically[4][6].

#### 10. What are the benefits of using Maven or Gradle in test automation projects?
They handle **dependency management**, **build lifecycle**, **parallel test execution**, and **integration with reporting** and CI/CD tools. This reduces manual efforts, improves consistency, and streamlines builds[6].


## Set 2
Here are professional, concise answers to each of your automation testing interview questions, aligned with current industry best practices[1][6][7][8]:

**1) You are asked to automate a functionality that is not yet fully developed. How do you handle this?**  
I collaborate closely with developers and business analysts to understand the expected functionality and UI/API contract. I start by creating **automation stubs** or skeleton scripts with placeholder steps and clear documentation. As parts of the feature become available, I iteratively enhance the scripts and add validations. This *shift-left* approach enables early test coverage and continuous feedback without delaying automation[1][5][7].

**2) If a Test fails, what will be your next step?**  
I first analyze logs, error messages, and failure screenshots. I determine if the failure is due to a genuine defect, a test script issue, or an environment problem. If it's a bug, I report it with detailed information; if it's a script/environment issue, I fix it and rerun the test. Documentation of root cause and steps taken is maintained for transparency and future reference[7].

**3) If the application has minor changes, what would be your approach to modifying the Automation scripts?**  
I assess the impact of the change by identifying affected locators or logic. I update **only the relevant components**—thanks to modular design (like POM and utility methods). I use code reviews to ensure accuracy, rerun related tests, and maintain documentation for traceability. Ensuring tests are maintainable and modular significantly eases updates for such changes[6][8].

**4) How would you automate login functionality for a website?**  
I create a **Page Object Model class** for the login page with locators and methods for entering credentials and submitting the form. The test retrieves credentials (for security, from config/environment variables), executes login, then verifies a successful login (e.g., dashboard visibility or welcome message). Valid and invalid credential scenarios are covered[6].

**5) How would you automate a Test scenario where you need to check if an email is sent after a user registration?**  
After automating user registration, I use scripts or API calls to connect to a test mailbox (via IMAP/POP3 or a tool like Mailosaur). I poll the mailbox for a new message matching criteria (sender, subject, body), parse the email content, and assert its arrival and correctness.

**6) If there is a scenario that takes a long time to execute, would you prefer Manual TestNG or Automation Testing?**  
If the scenario is **repeatable and high-value**, automation is preferable despite execution time, as it saves manual effort and ensures consistency. For rarely changed, low-risk, or one-off scenarios, I might recommend manual testing[4][5]. I also review optimization opportunities in test design or data setup for long scenarios.

**7) How would you automate a scenario where you need to validate the contents of a downloaded file after clicking a button on a webpage?**  
I automate clicking the download button, then use scripts to access the file system (e.g., using Java's `File`/`Scanner`) to open the downloaded file. I parse the file (CSV, PDF, Excel, etc.), validate its contents against expected data, and clean up the downloaded file afterward for repeatability.

**8) How would you automate a scenario where you need to verify a specific color, font, and position of an element on a webpage?**  
I locate the element with WebDriver, then retrieve CSS properties like `color`, `font-family`, and dimensions/coordinates using `getCssValue()` and `getLocation()`. These are compared against expected values to assert correctness, ensuring UI standards compliance.

**9) How would you handle pop-up windows or alert boxes in your Automation script?**  
I use WebDriver’s **Alert** interface to switch context for JavaScript alerts (`driver.switchTo().alert()`), then accept, dismiss, or retrieve alert text as needed. For new browser windows or tabs, I handle window handles (using `getWindowHandles()`, `switchTo().window()`).

**10) How would you automate a scenario where you need to verify if a user is able to scroll down a webpage until the footer section is visible?**  
I automate scrolling using JavaScriptExecutor or WebDriver’s actions API (`scrollIntoView`). Once the footer is scrolled into view, I assert its presence or visibility property, confirming that the scrolling and rendering worked as intended.

**11) You've been asked to automate a legacy application. What is your approach?**  
I begin with a feasibility analysis of automation tool compatibility (Web, desktop, legacy tech stack). I prioritize stable, high-value regression scenarios and develop scripts using **modular, maintainable architecture**. I introduce automation incrementally, refactoring where possible, and ensure robust documentation and version control.

**12) A script you wrote was working fine yesterday but is failing today. How do you troubleshoot?**  
I review recent application changes, code/locator updates, environment differences, and backend data. I rerun the script in isolation, review logs and screenshots, and compare results. Once the root cause is found (app change, test fragility, infra issue), I update the script or report the issue as appropriate[7].

**13) Your Automation scripts are running slowly. How can you improve the speed?**  
To improve speed, I:
- Replace static waits with explicit/fluent waits.
- Run tests in **parallel** or distributed environments (using TestNG, Selenium Grid).
- Limit unnecessary navigation and data setup.
- Optimize locators for faster element access.
- Regularly refactor and remove redundant steps[6][7].

**14) Your Automation script is failing due to a change in the application. How do you handle this?**  
I pinpoint the affected test steps or locators. I update the relevant scripts/components to match the latest application changes, leveraging modular architecture for ease of updates. I rerun tests to confirm stability and document all changes for traceability and collaboration[6][8].

## Set 3
Here are clear, concise, and technically detailed sample answers for your **Core Java, OOPs, Selenium, Framework, and Problem Solving** interview questions.

## Core Java & OOPs

**1. Can we have a catch block without a try block, or a try block without a catch block?**

- **Catch block without a try block:** No, a catch must always be preceded by a try block; otherwise, it will result in a compilation error.
- **Try block without a catch block:** Yes, you can have a try block without a catch block *if* it is followed by a finally block. The finally block will always execute, regardless of whether an exception was thrown[6][7].

**2. Can we handle exceptions without using try and catch?**

Yes, exceptions can be handled without try-catch in several ways:
- *Using the `throws` keyword:* Propagate the exception to the caller method.
- *Using a finally block without catch* (for resource cleanup).
- *Using global exception handlers* (e.g., `Thread.setDefaultUncaughtExceptionHandler()`).
- *Letting the JVM handle uncaught exceptions* (program will terminate and print the stacktrace)[1][2].

**3. What is Polymorphism and its types? Explain with respect to your project.**

Polymorphism is the ability of an object to take many forms. **Two types:**
- **Compile-time (Static) Polymorphism:** Method overloading (same method name, different parameters).  
- **Run-time (Dynamic) Polymorphism:** Method overriding (subclass provides a specific implementation).

*Project example:*  
In automation, method overloading can be used to create multiple `clickElement` methods (by locator, by WebElement). Method overriding is seen in base page classes where child pages override a `navigateToPage()` method with page-specific logic.

**4. Where have you implemented Encapsulation and Abstraction in your project?**

- **Encapsulation:** All page elements and actions are private/protected within Page Object classes, accessible via public getters/setters/methods.
- **Abstraction:** Interfaces or abstract classes define contracts for common utilities like browser drivers or reporting, hiding implementation details.

**5. Difference between protected and private in Java?**

- **private:** Accessible only within the same class.
- **protected:** Accessible within the same package and by subclasses in other packages.

**6. Can we create an object of an Interface or Abstract class? Why or why not?**

No, you cannot directly instantiate an **interface** or **abstract class** because they may contain unimplemented (abstract) methods. Instantiation requires concrete implementation.

**7. Example of method overloading and method overriding in Selenium?**

- **Overloading:**  
  ```java
  public void clickElement(By locator) { ... }
  public void clickElement(WebElement element) { ... }
  ```
- **Overriding:**  
  ```java
  // In BasePage.java
  public void openPage() { ... }
  // In LoginPage.java
  @Override
  public void openPage() { ... }
  ```

## Selenium / Automation

**1. What are the major exceptions you get in Selenium?**

- `NoSuchElementException`
- `ElementNotVisibleException` / `ElementNotInteractableException`
- `TimeoutException`
- `StaleElementReferenceException`
- `WebDriverException`

**2. How will you send the up and down arrow keys as input in a textbox?**

Using Selenium's `sendKeys()` method with `Keys` enum, e.g.:
```java
element.sendKeys(Keys.ARROW_UP);
element.sendKeys(Keys.ARROW_DOWN);
```

**3. Difference between findElements and findElement**

| findElement          | findElements            |
|----------------------|------------------------|
| Returns first match  | Returns a list         |
| Throws exception if not found | Returns empty list if not found |

**4. Fluent wait syntax**
```java
Wait wait = new FluentWait<>(driver)
    .withTimeout(Duration.ofSeconds(30))
    .pollingEvery(Duration.ofSeconds(5))
    .ignoring(NoSuchElementException.class);
```

**5. Explicit and implicit wait**

- **Implicit Wait:** Applied globally, tells WebDriver to poll DOM for certain time when locating elements.
- **Explicit Wait:** Waits for a specific condition for a specific element.
- **Fluent Wait:** Like explicit wait, but with custom polling and exceptions to ignore.

**6. Difference between Selenium 3.0 and 4.0 version**

- Selenium 4 supports W3C WebDriver protocol natively.
- Improved relative locators.
- Enhanced browser and window/pane management APIs.
- Built-in support for CDP (Chrome DevTools Protocol).

**7. Dropdowns & Links: Find common options between two dropdowns in separate tabs**

- Store dropdown options from the first tab in a List.
- Switch to new tab using window handles.
- Get options from second dropdown.
- Compare both option lists using Java Set/List retainAll for commonality.

*Step-wise:*
1. Find and store options from first dropdown.
2. Click link, switch to new tab.
3. Find and store options from second dropdown.
4. Compare both sets and print/display common values.

## Framework & TestNG

**1. Explain the Depends On attribute in TestNG.**

`@Test(dependsOnMethods={"methodName"})`  
Ensures that a test runs only after the specified dependent test methods have executed and passed. Useful for sequence control.

**2. Regression/smoke suite triggers**

- Use TestNG groups: Tag tests (e.g., `@Test(groups={"regression"})`, `@Test(groups={"smoke"})`)
- Configure CI tool (like Jenkins) to run suites by group:  
  ```
  mvn test -Dgroups=regression
  mvn test -Dgroups=smoke
  ```

## Problem Solving

**1. Print number of characters in string "ttessst@innn123ggg!"**
```java
public class CharCount {
    public static void main(String[] args) {
        String str = "ttessst@innn123ggg!";
        System.out.println(str.length()); // Output: 18
    }
}
```

**2. Programs on String Manipulation, HashMap**

- String reversal:
  ```java
  String reversed = new StringBuilder(str).reverse().toString();
  ```
- Count character frequency:
  ```java
  HashMap map = new HashMap<>();
  for (char c : str.toCharArray())
      map.put(c, map.getOrDefault(c, 0) + 1);
  ```

**3. Difference between list, set, map and usage in framework**

| Type  | Duplicates | Ordered | Access Type     | Usage in framework              |
|-------|------------|---------|-----------------|---------------------------------|
| List  | Yes        | Yes     | By index        | Store sequence of test steps    |
| Set   | No         | No      | Unique elements | Store unique tags/browsers      |
| Map   | Keys unique| No      | Key-value pair  | Store config, data mappings     |


## Set 4
## Java & Selenium, SQL, Testing, and Framework Interview Q&A

### 2. Java Code: Reverse a String While Preserving Whitespace

```java
public static String reversePreservingSpaces(String str) {
    char[] input = str.toCharArray();
    char[] result = new char[input.length];

    // Copy spaces to their positions
    for (int i = 0; i           | Returns an empty list                 |
[12][13]

### 9. Implicit Wait vs Explicit Wait

| Wait Type     | Scope              | Usage                   | Custom Conditions      |
|---------------|--------------------|-------------------------|-----------------------|
| Implicit      | All element locates| Once per WebDriver      | No (global only)      |
| Explicit      | Specific elements  | Per element/condition   | Yes                   |

- **Implicit**: Set at WebDriver start, applies to all searches.
- **Explicit**: Waits for specific condition (like clickable, visible), more flexible for dynamic elements.[14][15]

### 10. Selenium Code to Automate a Calendar Element

```java
// Open calendar
driver.findElement(By.id("calendar_icon")).click();
// Example: Select May 20, 2025
while (!driver.findElement(By.className("month")).getText().equals("May 2025")) {
    driver.findElement(By.id("nextMonth")).click();
}
driver.findElement(By.xpath("//td[text()='20']")).click();
```
Customize selectors as per calendar widget.

### 11. Fetch Text from a Text Box in Selenium

```java
String text = driver.findElement(By.id("myTextbox")).getAttribute("value");
```
Use `.getAttribute("value")` for input fields.

### 12. Enter Text in an Alert Using Selenium

```java
Alert alert = driver.switchTo().alert();
alert.sendKeys("yourTextHere");
alert.accept(); // press OK
```
Works with prompt dialogs (not with simple alerts/confirm, which may not be editable).

### 13. Checked vs Unchecked Exceptions

| Checked Exception                             | Unchecked Exception                      |
|-----------------------------------------------|------------------------------------------|
| Checked at compile time                       | Checked at runtime                       |
| Must be declared/handled                      | No requirement to handle                 |
| Example: IOException, SQLException            | Example: NullPointerException, ArithException |

### 14. XPath Selects Two Elements: Does findElement Throw Exception?

- **No**: `findElement(By.xpath(...))` returns the **first matching element**. Only throws if no elements are found.

### 15. Smoke Testing vs Sanity Testing

|              | Smoke Testing                                | Sanity Testing                              |
|--------------|----------------------------------------------|---------------------------------------------|
| Scope        | Broad, basic functionality (build acceptance)| Focused, after changes/fixes                |
| Depth        | Shallow                                      | Deeper, limited area                        |
| Purpose      | "Is the build testable?"                     | "Is the bug fixed, features working?"        |

### 16. Relative Locators in Selenium

- Introduced in Selenium 4.
- Allow locating elements **relative to other known elements** (above, below, near, leftOf, rightOf).
- Example:
  ```java
  WebElement label = driver.findElement(By.id("usernameLabel"));
  WebElement input = driver.findElement(with(By.tagName("input")).below(label));
  ```

### 17. Challenges Faced in Projects

- Dynamic locators/unstable elements.
- Synchronization across environments/browsers.
- Reliable reporting/integration with CI.
- Managing test data for automation.
- Handling flaky or intermittent test failures.
- Test maintenance with frequent UI changes.

### 18. How to Pick Test Cases for Regression Testing

- Select core functionalities/business-critical workflows.
- Areas with recent code changes/bug fixes.
- High-risk/use frequency modules.
- Tests prone to integration issues.
- Previously failed test cases.

## Techno-Managerial: Framework & Practices

### 1. Explain Your Framework in Detail

- Modular, layered structure (Base, Utilities, Page Objects, Test cases).
- Uses Page Object Model, Singleton for driver, Factory for browser.
- Reporting integrated with Extent/Allure.
- Configurations managed via property files/environment variables.
- Data-driven via TestNG DataProviders/external Excel/CSV.
- Integrated with CI (Jenkins, Azure).

### 2. 100 Pages: Do You Create 100 Page Objects?

- Typically, YES: One per logical page for maintainability.
- However, reuse "component" objects for common widgets across pages.
- DRY principle: Group similar pages/components where practical.

### 3. "Element Click Intercepted" Exception & Fix

- Occurs when another element (e.g., overlay, modal) overlaps the clickable one.
- **Fixes**:
  - Add waits for element visibility/clickability.
  - Scroll element into view:  
    `((JavascriptExecutor)driver).executeScript("arguments.scrollIntoView(true);", element);`
  - Dismiss overlays/popups or use JS click as last resort.

### 4. Take Screenshots for Failed Test Cases Only in TestNG

- Use `ITestListener` interface's `onTestFailure()` method to capture screenshots and attach to reports.

### 5. Connect Test Cases with Azure

- Integrate test frameworks with Azure DevOps using plugins (e.g., Azure Test Plans, REST APIs).
- Map automation results to work items/test cases for traceability.

### 6. What is the Get Fetch Command?

- `git fetch`: Downloads latest changes from remote, updates local tracking branches.  
  Does not change your working files.

### 7. Delete Variable in Postman After Test

```javascript
pm.environment.unset("variableName");
```
Use `pm.environment.unset()` or `pm.globals.unset()` in the Tests tab.

### 8. Why Prefer Cucumber BDD?

- Bridges gap between technical and non-technical stakeholders.
- Uses Gherkin syntax for readable scenarios.
- Enables living documentation and early validation.
- Drives collaboration with business/requirements teams.

### 9. Dynamic Binding vs Static Binding

| Type           | Binding Time         | Example                                    |
|----------------|---------------------|---------------------------------------------|
| Static Binding | Compile-time        | Method overloading, private/static/final    |
| Dynamic Binding| Runtime             | Method overriding, polymorphism             |

### 10. Method Overloading vs Method Overriding

| Aspect               | Overloading                          | Overriding                              |
|----------------------|--------------------------------------|-----------------------------------------|
| Definition           | Same method name; diff params         | Subclass redefines parent method        |
| Compile/Run          | Compile time                         | Run time                               |

### 11. Comparable vs Comparator

|             | Comparable           | Comparator                             |
|-------------|---------------------|----------------------------------------|
| Interface   | compareTo(Object o) | compare(Object a, Object b)            |
| Use         | Default sort order  | Custom sort orders                     |

### 12. User-Friendly Login Page Criteria

- Clear error/help messages.
- Accessible field/tab navigation.
- Fast, consistent response.
- Secure (masked passwords, no info leak).
- Mobile/responsive design.

### 13. 5 Points for a Good Test Case

- Clear objective/expected outcome.
- Stepwise, concise instructions.
- Input data & preconditions specified.
- Traceable to requirement/user story.
- Independent, repeatable, and unambiguous.

### 14. Developer Not Fixing a Bug: What To Do

- Provide clear evidence and impact analysis.
- Reference requirement documentation.
- Facilitate a team discussion to align expectations.

### 15. What Are Threads in JMeter?

- Each thread simulates a virtual user.
- Multiple threads enable load/concurrency simulation.

### 16. Can You Automate CAPTCHAs?

- Generally, NO: Automation tools cannot solve CAPTCHAs as intended for human validation.
- Solutions: Use test/bypass hooks in non-production or consult devs for test environments.

### 17. Use Cases for Fluent Waits in Selenium

- When polling for element's presence/condition that may need repeated attempts.
- For dynamic content that appears/disappears unpredictably.

### 18. Open New Tab in Selenium

```java
driver.switchTo().newWindow(WindowType.TAB);
```
Or use JavaScript:  
`((JavascriptExecutor) driver).executeScript("window.open()");`

### 19. Purpose of CRON Expression in Jenkins

- Schedules jobs (builds/tests) automatically at specified times.
- Example: `H 2 * * 1-5` runs job at 2 AM on weekdays.

---
