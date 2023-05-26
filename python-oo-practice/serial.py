"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """
    def __init__(self, start=100):
        """Define strt attribute to iniate the sequence and 
        a counter to keep a count
        """
        self.start = start
        self.count = 0
    
    def generate(self):
        """"Pass current instance to generate method 
        to increase start attribute and counter by 1
        """
        self.start += 1
        self.count += 1
        return self.start

    def reset(self):
        """"Pass current instance to reset method 
        and decrease number by subtracting counter attribute from itself
        to get the initial number where the squence started
        """
        self.start -= self.count
        return self.start
    
    def __str__(self) -> str:
        """"Define str method to print the instance of class"""
        return '<SerialGenerator start= {} next = {}>'.format(self.start, self.start + 1)

serial = SerialGenerator(100)
print(serial)
print(serial.generate())
print(serial)
print(serial.generate())
print(serial.reset())
print(serial.generate())
