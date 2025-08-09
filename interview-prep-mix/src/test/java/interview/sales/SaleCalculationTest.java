package interview.sales;

import java.time.LocalDate;
import java.util.Arrays;
import java.util.Collections;
import java.util.List;
import java.util.Map;

import org.testng.Assert;
import org.testng.annotations.DataProvider;
import org.testng.annotations.Test;

public class SaleCalculationTest {

    @Test(dataProvider = "Sales provider")
    public void verifySaleCalculations(List<Book> books, LocalDate fromDate, LocalDate toDate,
            Map<String, Double> expectedmap) {
        SaleCalculation saleCalculation = new SaleCalculation();
        Map<String, Double> actualSalesMap = saleCalculation.calucateTotalSalesAmount(books, fromDate, toDate);
        Assert.assertEquals(actualSalesMap, expectedmap);
        System.out.println("Expected Map is matched with actualMap " + actualSalesMap);
    }

    @DataProvider(name = "Sales provider")
    public Object[][] dataProvider() {
        return new Object[][] {
                {
                        Arrays.asList(
                                new Book("Book A", "Author X", 250.0, LocalDate.of(2023, 4, 10)),
                                new Book("Book B", "Author Y", 300.0, LocalDate.of(2023, 4, 15))),
                        LocalDate.of(2023, 5, 1),
                        LocalDate.of(2023, 5, 31),
                        Collections.emptyMap()
                },
                {
                        Arrays.asList(
                                new Book("Book A", "Author X", 250.0, LocalDate.of(2023, 5, 10)),
                                new Book("Book B", "Author Y", 300.0, LocalDate.of(2023, 5, 15)),
                                new Book("Book C", "Author X", 150.0, LocalDate.of(2023, 5, 31))),

                        LocalDate.of(2023, 5, 1),
                        LocalDate.of(2023, 5, 31),
                        Map.of("Author X", 400.00, "Author Y", 300.00)
                },
                {
                        null,
                        LocalDate.of(2023, 5, 1),
                        LocalDate.of(2023, 5, 31),
                        Collections.emptyMap()
                },

                {
                        null,
                        null,
                        LocalDate.of(2023, 5, 31),
                        Collections.emptyMap()
                },

                {
                        Collections.emptyList(),
                        LocalDate.of(2023, 5, 31),
                        LocalDate.of(2023, 5, 31),
                        Collections.emptyMap()
                }
        };
    }
}
