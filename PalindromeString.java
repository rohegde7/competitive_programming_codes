import java.util.Scanner;

/*
Author: Rohit Hegde
github.com/rohegde7
hegde.rohit7@gmail.com


Find if the given string is palindrome or not

*/

public class PalindromeString {

    public static boolean isPalindrome(String word) {
        StringBuilder myWord = new StringBuilder(word);

        int length = myWord.length();

        int pointer1 = 0;
        int pointer2 = length - 1;

        while (pointer1 < pointer2) {
            char char1 = Character.toLowerCase(myWord.charAt(pointer1));
            char char2 = Character.toLowerCase(myWord.charAt(pointer2));

            if (char1 != char2)
                return false;

            pointer1++;
            pointer2--;
        }

        return true;
    }

    public static void main(String[] args) {
        Scanner reader = new Scanner(System.in);
        String word = reader.nextLine();
        System.out.println(isPalindrome(word));
    }
}