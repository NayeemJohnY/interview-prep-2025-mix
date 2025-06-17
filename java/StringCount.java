import java.util.regex.Pattern;

public class StringCount {

    public static void main(String[] args) {
        String s = "Automat@123ionssss&";
        int letters = 0, numbers = 0, specialchars = 0;
        // Solution 1
        // for (Character ch : s.toCharArray()) {
        // if (Character.isDigit(ch)){
        // numbers++;
        // }
        // else if (Character.isLetter(ch)){
        // letters++;
        // }
        // else {
        // specialchars++;
        // }
    
        // Solution 2
        for (int i = 0; i < s.length(); i++) {
            if ((s.charAt(i) >= 'A' && s.charAt(i) <= 'Z') || (s.charAt(i) >= 'a' && s.charAt(i) <= 'z')) {
                letters++;
            } else if (s.charAt(i) >= '0' && s.charAt(i) <= '9') {
                numbers++;
            } else {
                specialchars++;
            }
        }
        System.out.println("letters Count" + letters);
        System.out.println("numbers Count" + numbers);
        System.out.println("Special Chars Count" + specialchars);
    }
}
