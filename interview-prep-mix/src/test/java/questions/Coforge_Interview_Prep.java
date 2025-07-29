package questions;

import java.util.stream.IntStream;

public class Coforge_Interview_Prep {
    public void login(String username) {
    }

    public void login(String username, String password) {
    }

    public boolean login(int password) {
        return true;
    }

    // 19. Program to Find Duplicate Characters in a String With Occurrence (Without
    // HashMap)
    public static void findDuplicateChars(String s) {
        s = s.trim().toLowerCase();
        char[] freq = new char[26];
        for (char c : s.toCharArray()) {
            freq[c - 'a']++;
        }

        for (int i = 0; i < 26; i++) {
            if (freq[i] > 1) {
                System.out.println("char: " + (char) (i + 'a') + " occurrence " + freq[i]);
            }
        }
    }

    public static void reverseFistAndLast(int number) {
        int digits = 1;
        int temp = number;
        while (temp >= 10) {
            digits *= 10;
            temp = temp / 10;
        }
        int first = temp;
        int last = number % 10;
        int mid = (number % digits) / 10;
        System.out.println(last * digits + mid * 10 + first);

    }

    public static void main(String[] args) {
        findDuplicateChars("programming");
        String s = "Hello Its programming";
        System.out.println(s.replace("o", "*"));
        System.out.println(s.replaceAll("o", "*"));

        // Reverse Number
        int number = 12345;
        int rev = IntStream.iterate(number, i -> i > 0, i -> i / 10).reduce(0, (acc, i) -> acc * 10 + i % 10);
        System.out.println(rev);
        String snum = String.valueOf(number);
        rev = IntStream.iterate(snum.length() - 1, i -> i >= 0, i -> i - 1).reduce(0,
                (acc, i) -> acc * 10 + snum.charAt(i) - '0');
        System.out.println(rev);

        // Reverse First and Last
        reverseFistAndLast(12345);
    }

}

class Test extends Coforge_Interview_Prep {

    @Override
    public void login(String password) {
    }
}