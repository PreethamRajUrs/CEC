import java.util.Scanner;

public class Main {
    static String[] ones = {"", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine",
                            "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
                            "sixteen", "seventeen", "eighteen", "nineteen"};
    static String[] tens = {"", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"};

    static String twoDigit(int n) {
        return n < 20 ? ones[n] : tens[n / 10] + (n % 10 > 0 ? " " + ones[n % 10] : "");
    }

    static String convert(int n) {
        if (n == 0) return "zero";
        return (n / 100000 > 0 ? twoDigit(n / 100000) + " lakh " : "") +
               (n / 1000 % 100 > 0 ? twoDigit(n / 1000 % 100) + " thousand " : "") +
               (n / 100 % 10 > 0 ? ones[n / 100 % 10] + " hundred " : "") +
               (n % 100 > 0 ? twoDigit(n % 100) : "");
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        String words = convert(n).trim();
        System.out.println(Character.toUpperCase(words.charAt(0)) + words.substring(1));
    }
}

   