package edu.iastate.coms417.demo;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.BeforeEach;
import static org.junit.jupiter.api.Assertions.*;

/**
 * Test class for StringUtils - demonstrates RTS with multiple test classes
 */
public class StringUtilsTest {
    
    private StringUtils stringUtils;
    
    @BeforeEach
    void setUp() {
        stringUtils = new StringUtils();
    }
    
    @Test
    void testReverse() {
        assertEquals("olleh", stringUtils.reverse("hello"));
        assertEquals("", stringUtils.reverse(""));
        assertNull(stringUtils.reverse(null));
    }
    
    @Test
    void testIsPalindrome() {
        assertTrue(stringUtils.isPalindrome("racecar"));
        assertTrue(stringUtils.isPalindrome("A man a plan a canal Panama"));
        assertFalse(stringUtils.isPalindrome("hello"));
        assertFalse(stringUtils.isPalindrome(null));
    }
    
    @Test
    void testCountWords() {
        assertEquals(3, stringUtils.countWords("hello world test"));
        assertEquals(1, stringUtils.countWords("single"));
        assertEquals(0, stringUtils.countWords(""));
        assertEquals(0, stringUtils.countWords(null));
    }
}

