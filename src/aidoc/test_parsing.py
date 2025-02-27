import os
import sys
from datetime import datetime

# Global variables
VERSION = "1.0.0"
AUTHOR = "Test User"

def greet(name: str) -> str:
    """Return a greeting message."""
    return f"Hello, {name}!"

class Rectangle:
    """A class representing a rectangle."""

    def __init__(self, length: float, width: float):
        """Initialize the rectangle with length and width."""
        self.length = length
        self.width = width
        self.created_at = datetime.now()

    def area(self) -> float:
        """Calculate the area of the rectangle."""
        return self.length * self.width

    def perimeter(self) -> float:
        """Calculate the perimeter of the rectangle."""
        return 2 * (self.length + self.width)
        
# Standalone function
def current_time() -> str:
    """Return the current timestamp as a string."""
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

if __name__ == "__main__":
    rect = Rectangle(10, 5)
    print(f"Area: {rect.area()}, Perimeter: {rect.perimeter()}")
    print(greet(AUTHOR))
    print(f"Script executed at: {current_time()}")
