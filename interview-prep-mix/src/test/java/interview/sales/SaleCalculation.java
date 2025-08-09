package interview.sales;

import java.time.LocalDate;
import java.util.Arrays;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class SaleCalculation {

    public Map<String, Double> calucateTotalSalesAmount(List<Book> books, LocalDate from, LocalDate to) {
        Map<String, Double> totalSalesMap = new HashMap<String, Double>();
        try {
            if (books == null || books.isEmpty())
                throw new IllegalStateException("No Books to Caluclate Sales");
            if (from == null || to == null)
                throw new IllegalStateException("Not a valid Date Range");
            boolean ValidDateRange = from.isBefore(to) || from.isEqual(to);
            if (!ValidDateRange)
                throw new IllegalArgumentException("From Date & To Date are not in valid range");

            for (Book book : books) {
            LocalDate sellingDate = book.getSellingDate();
            // if (sellingDate.isAfter(from) && sellingDate.isBefore(to)) {
            if (!sellingDate.isBefore(from) && !sellingDate.isAfter(to)) {
                totalSalesMap.put(book.getAuthor(),
                        totalSalesMap.getOrDefault(book.getAuthor(), 0.0) + book.getSellingAmount());
            }
        }
        } catch (Exception e) {
            e.printStackTrace();
            return totalSalesMap;
        }
        return totalSalesMap;
    }

    public static void main(String[] args) {
        SaleCalculation saleCalculation = new SaleCalculation();
        List<Book> books = Arrays.asList(
            new Book("Book A", "Author X", 250.0, LocalDate.of(2023, 4, 10)),
            new Book("Book B", "Author Y", 300.0, LocalDate.of(2023, 4, 15)));

        LocalDate fromDate = LocalDate.of(2023, 5, 1);
        LocalDate toDate = LocalDate.of(2023, 5, 31);

        Map<String, Double> totalSalesMap = saleCalculation.calucateTotalSalesAmount(books, fromDate, toDate);
        System.out.println(totalSalesMap);

        books = Arrays.asList(
            new Book("Book A", "Author X", 250.0, LocalDate.of(2023, 5, 10)),
             new Book("Book B", "Author Y", 300.0, LocalDate.of(2023, 5, 15)),
             new Book("Book C", "Author X", 150.0, LocalDate.of(2023, 5, 31))
);

        fromDate = LocalDate.of(2023, 6, 1);
        toDate = LocalDate.of(2023, 5, 1);

        totalSalesMap = saleCalculation.calucateTotalSalesAmount(books, fromDate, toDate);
        System.out.println(totalSalesMap);
    }
}

// From < to valid range 
// From > to invalid range
// null

