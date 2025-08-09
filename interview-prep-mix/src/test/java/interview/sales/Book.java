package interview.sales;

import java.time.LocalDate;

public class Book {

    String title;
    String author;
    double sellingAmount;
    LocalDate sellingDate;

    
    public Book(String title, String author, double sellingAmount, LocalDate sellingDate) {
        this.title = title;
        this.author = author;
        this.sellingAmount = sellingAmount;
        this.sellingDate = sellingDate;
    }


    public String getTitle() {
        return title;
    }


    public void setTitle(String title) {
        this.title = title;
    }


    public String getAuthor() {
        return author;
    }


    public void setAuthor(String author) {
        this.author = author;
    }


    public double getSellingAmount() {
        return sellingAmount;
    }


    public void setSellingAmount(double sellingAmount) {
        this.sellingAmount = sellingAmount;
    }


    public LocalDate getSellingDate() {
        return sellingDate;
    }


    public void setSellingDate(LocalDate sellingDate) {
        this.sellingDate = sellingDate;
    }
    
    
}
