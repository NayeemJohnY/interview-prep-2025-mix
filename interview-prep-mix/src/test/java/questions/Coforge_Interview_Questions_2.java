package questions;

import java.io.File;
import java.time.Duration;
import java.util.Arrays;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

import org.openqa.selenium.By;
import org.openqa.selenium.SearchContext;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.chrome.ChromeOptions;
import org.testng.Assert;
import org.testng.annotations.DataProvider;
import org.testng.annotations.Test;

import io.restassured.RestAssured;

public class Coforge_Interview_Questions_2 {

    // Write a code to click on file name in downloads folder from chrome
    @Test
    public void downloadsChromeHandleShadowRoot() throws InterruptedException {
        ChromeOptions options = new ChromeOptions();
        // String userDataDir =
        // "C:\Users\YourUsername\AppData\Local\Google\Chrome\User Data";
        // String profileDirectory = "Default";
        // options.addArguments("--user-data-dir=" + userDataDir);
        // options.addArguments("--profile-directory=" + profileDirectory);
        String downloadDirectory = String.join(File.separator, System.getProperty("user.dir"), "src", "main",
                "resources");

        HashMap<String, Object> chromePrefs = new HashMap<String, Object>();
        chromePrefs.put("download.default_directory", downloadDirectory);
        options.setExperimentalOption("prefs", chromePrefs);
        options.addArguments("--start-maximized");
        WebDriver driver = new ChromeDriver(options);
        driver.get("https://the-internet.herokuapp.com/download");
        driver.manage().timeouts().implicitlyWait(Duration.ofSeconds(30));
        List<WebElement> links = driver.findElements(By.xpath("//*[@class='example']//a"));
        for (int i = 0; i < 5; i++)
            links.get(i).click();
        Thread.sleep(5000);
        driver.get("chrome://downloads/");
        // Access File
        SearchContext download_manager = driver.findElement(By.cssSelector("downloads-manager"))
                .getShadowRoot();
        List<WebElement> downlaod_items = download_manager.findElements(By.cssSelector("downloads-item"));
        for (WebElement item : downlaod_items) {
            WebElement element = item.getShadowRoot().findElement(By.id("file-link"));
            System.out.println("element Text: " + element.getText());
            if (element.getText().equals("Bug Life Cycle Flowchart.png")) {
                element.click();
                break;
            }
        }
        Thread.sleep(3000);
        driver.quit();
    }

    public Long getResponseTime(String url) {
        return RestAssured.get(url).getTime();
    }

    @Test
    public void getAPIResponseMetrics() {
        List<String> urls = List.of("http://dummyjson.com/posts", "https://dummyjson.com/comments",
                "https://jsonpath.com/", "https://jsonplaceholder.typicode.com/users",
                "https://jsonplaceholder.typicode.com/photos");

        System.out.println(urls.stream().mapToLong(this::getResponseTime).summaryStatistics());
    }

    public int getDenominations(int input, HashMap<Integer, Integer> map) {
        int[] denominations = { 100, 200, 500, 50, 20, 10, 5 };
        Arrays.sort(denominations);
        for (int i = denominations.length - 1; i >= 0; i--) {
            if (input == denominations[i]) {
                map.put(denominations[i], map.getOrDefault(denominations[i], 0) + 1);
                input -= denominations[i];
                break;
            } else if (input > denominations[i]) {
                map.put(denominations[i], map.getOrDefault(denominations[i], 0) + 1);
                input -= denominations[i];
                break;
            }
        }
        return input;
    }

    // Interview way
    @Test
    public void testDenominations() {
        // Denominations = 100,200,500,50,20,10,5-> Input = 380 and Input = 481
        int input = 1520;
        HashMap<Integer, Integer> map = new HashMap<>();
        boolean notMatch = false;
        while (input > 0) {
            int reducedInput = getDenominations(input, map);
            if (input == reducedInput) {
                notMatch = true;
                break;
            }
            input = reducedInput;
        }
        if (notMatch) {
            System.out.println("breaking for No match");
        } else {
            System.out.println("Denominations: " + map);
        }
    }

    // Relook
    public int getDenominations(int[] denominations, int input) {
        for (int i = denominations.length - 1; i >= 0; i--) {
            if (input >= denominations[i]) {
                return denominations[i];
            }
        }
        return -1;
    }

    @Test(dataProvider = "MoneyProvider")
    public void testATMDistribution(int input, Map<Integer, Integer> expectedDenominationsCountMap) {
        // Denominations = 100,200,500,50,20,10,5-> Input = 380 and Input = 481
        int[] denominations = { 100, 200, 500, 50, 20, 10, 5 };
        Arrays.sort(denominations);
        HashMap<Integer, Integer> denominationsCountMap = new HashMap<>();
        while (input > 0) {
            int denomination = getDenominations(denominations, input);
            if (denomination == -1) {
                denominationsCountMap.clear();
                break;
            }

            denominationsCountMap.put(denomination,
                    denominationsCountMap.getOrDefault(denomination, 0) + 1);
            input = input - denomination;
        }
        System.out.println(denominationsCountMap);
        Assert.assertEquals(denominationsCountMap, expectedDenominationsCountMap);
        for (Map.Entry<Integer, Integer> entry : expectedDenominationsCountMap.entrySet()) {
            Assert.assertEquals(entry.getValue(), expectedDenominationsCountMap.get(entry.getKey()));
        }
    }

    @DataProvider(name = "MoneyProvider")
    public Object[][] moneyProvider() {
        return new Object[][] {
                { 1520, Map.of(500, 3, 20, 1) },
                { 481, Map.of() },
                { 380, Map.of(200, 1, 100, 1, 50, 1, 20, 1, 10, 1) }
        };
    }
}
