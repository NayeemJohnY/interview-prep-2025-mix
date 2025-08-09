Coding Challenge: Book Sales Aggregator

Objective

Design a system to manage book sales and calculate total sales per author within a given date range.

Problem Statement

You are required to implement two classes:

1. Book Class
This class should represent a book sale record with the following attributes:

title (String): The title of the book.
author (String): The author of the book.
sellingAmount (double): The amount for which the book was sold.
sellingDate (LocalDate): The date the book was sold.


2. SaleCalculation Class
This class should contain a method:


Functionality:

The method should return a Map where:
Key: Author name
Value: Total sales amount for that author

Only include books sold within the date range [fromDate, toDate] (inclusive).
If no books are sold in the range, return an empty map.

Requirements
Follow clean code principles: meaningful naming, modular design, and proper formatting.
Ensure null safety and input validation where appropriate.


Write JUnit test cases to validate:

Normal scenarios
Edge cases 

Sample Input 1


List<Book> books = Arrays.asList(
    new Book("Book A", "Author X", 250.0, LocalDate.of(2023, 5, 10)),
    new Book("Book B", "Author Y", 300.0, LocalDate.of(2023, 5, 15)),
    new Book("Book C", "Author X", 150.0, LocalDate.of(2023, 6, 5))
);

LocalDate fromDate = LocalDate.of(2023, 5, 1);
LocalDate toDate = LocalDate.of(2023, 5, 31);


Expected Output 1


{
    "Author X": 250.0,
    "Author Y": 300.0
}



Sample Input 2


List<Book> books = Arrays.asList(
    new Book("Book A", "Author X", 250.0, LocalDate.of(2023, 4, 10)),
    new Book("Book B", "Author Y", 300.0, LocalDate.of(2023, 4, 15))
);

LocalDate fromDate = LocalDate.of(2023, 5, 1);
LocalDate toDate = LocalDate.of(2023, 5, 31);


Expected Output 2


{}


Deliverables
Book.java – Class definition with required fields and constructors.
SaleCalculation.java – Class with the calculateAuthorWiseSales method.
SaleCalculationTest.java – JUnit test class with at least 4 test cases.
Code should be clean, readable, and follow Java best practices.