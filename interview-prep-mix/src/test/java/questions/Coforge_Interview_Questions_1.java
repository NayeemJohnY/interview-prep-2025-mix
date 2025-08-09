package questions;

import java.io.FileInputStream;
import java.io.IOException;
import java.time.Duration;
import java.util.List;
import java.util.Properties;
import java.util.stream.Collectors;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.chrome.ChromeOptions;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.WebDriverWait;

import io.restassured.RestAssured;

// Write a Pseudo code for interface to achieve multiple inheritance.

interface BrowserManager {

    String CHROME = "chrome";
    String FIREFOX = "firefox";

    public String getBrowser();

    public static void click() {
    }

}

class Reporting {

    public void setUpReport() {
        System.out.println("Set up report");
    }

    public void printreport() {
    }

}

class Test1 extends Reporting implements BrowserManager {

    private String browser = CHROME;

    @Override
    public String getBrowser() {
        return browser;
    }

}

class ReadPorperties {

    Properties prop;

    ReadPorperties() {
        try {
            FileInputStream fs = new FileInputStream("src/main/resources/config.properties");
            prop = new Properties();
            prop.load(fs);
        } catch (IOException e) {
            e.printStackTrace();
        }

    }

    public String getProperty(String key) {
        return prop.getProperty(key).trim();
    }
}

public class Coforge_Interview_Questions_1 {

    public static void main(String[] args) {
        // Use java 8 stream to filter and collect
        List<String> list = List.of("John", "James", "David", "Robin");
        System.out.println(list.stream().filter(s -> s.charAt(0) == 'J').toList());
        System.out.println(list.stream().filter(s -> s.charAt(0) == 'J').collect(Collectors.toList()));
        ReadPorperties properties = new ReadPorperties();
        String username = properties.getProperty("username");
        String password = properties.getProperty("password");
        System.out.println(username + " " + password);

        // Get price for IndiGo flights & headless mode
        ChromeOptions options = new ChromeOptions();
        options.addArguments("--headless");
        WebDriver driver = new ChromeDriver(options);
        driver.get("https://www.makemytrip.com/");
        driver.findElement(By.xpath("//*[text()='Search']")).click();
        By indigoPriceLocator = By.xpath("""
                    //*[contains(@class, "listingCard ")]
                    [descendant::*[@data-test="component-airlineHeading" and text()="IndiGo"]]
                    /descendant::*[@data-test="component-fare"]/span
                """);
        List<WebElement> priceElements = new WebDriverWait(driver, Duration.ofSeconds(30)).until(
                ExpectedConditions.visibilityOfAllElementsLocatedBy(indigoPriceLocator));
        priceElements.forEach(ele -> {
            System.out.println(ele.getText());
        });

        // Validate JSOn schema
        RestAssured.get().then();

        // Difference between Rest and WebService
        // 500 , 503, 529
    }
}