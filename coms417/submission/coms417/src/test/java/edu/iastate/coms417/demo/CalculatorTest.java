package edu.iastate.coms417.demo;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.BeforeEach;
import static org.junit.jupiter.api.Assertions.*;

/**
 * Test class for Calculator - demonstrates RTS with Ekstazi
 */
public class CalculatorTest {
    
    private Calculator calculator;
    
    @BeforeEach
    void setUp() {
        calculator = new Calculator();
    }
    
    @Test
    void testAdd() {
        assertEquals(5, calculator.add(2, 3));
        assertEquals(0, calculator.add(-1, 1));
        assertEquals(100, calculator.add(50, 50));
    }
    
    @Test
    void testSubtract() {
        assertEquals(1, calculator.subtract(3, 2));
        assertEquals(-2, calculator.subtract(1, 3));
        assertEquals(0, calculator.subtract(5, 5));
    }
    
    @Test
    void testMultiply() {
        assertEquals(6, calculator.multiply(2, 3));
        assertEquals(0, calculator.multiply(0, 5));
        assertEquals(-6, calculator.multiply(-2, 3));
    }
    
    @Test
    void testDivide() {
        assertEquals(2.0, calculator.divide(6, 3), 0.001);
        assertEquals(2.5, calculator.divide(5, 2), 0.001);
        assertEquals(-2.0, calculator.divide(-6, 3), 0.001);
    }
    
    @Test
    void testDivideByZero() {
        assertThrows(IllegalArgumentException.class, () -> {
            calculator.divide(10, 0);
        });
    }
    
    @Test
    void testPower() {
        assertEquals(8, calculator.power(2, 3));
        assertEquals(1, calculator.power(5, 0));
        assertEquals(25, calculator.power(5, 2));
    }
    
    @Test
    void testPowerNegativeExponent() {
        assertThrows(IllegalArgumentException.class, () -> {
            calculator.power(2, -1);
        });
    }
}

