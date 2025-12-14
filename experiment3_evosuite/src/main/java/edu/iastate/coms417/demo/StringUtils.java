package edu.iastate.coms417.demo;

/**
 * String utility class - demonstrates EvoSuite test generation
 */
public class StringUtils {
    
    public String reverse(String str) {
        if (str == null) {
            return null;
        }
        return new StringBuilder(str).reverse().toString();
    }
    
    public boolean isPalindrome(String str) {
        if (str == null || str.isEmpty()) {
            return false;
        }
        String cleaned = str.toLowerCase().replaceAll("[^a-z0-9]", "");
        return cleaned.equals(reverse(cleaned));
    }
    
    public int countWords(String str) {
        if (str == null || str.trim().isEmpty()) {
            return 0;
        }
        return str.trim().split("\\s+").length;
    }
}

