# @property

class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height
    
    @property
    def width(self):
        return self._width
    
    @property
    def height(self):
        return self._height

    @width.setter
    def width(self, new_width):
        if new_width > 0:
            self._width = new_width
        else:
            print("Width must be positive.")

    @height.setter
    def height(self, new_height):
        if new_height > 0:
            self._height = new_height
        else:
            print("Height must be positive.")   
    
    @width.deleter
    def width(self):
        del self._width
        print("Width has been deleted.")

    @height.deleter
    def height(self):
        del self._height
        print("Height has been deleted.")    

rectangle = Rectangle(5, 3)

rectangle.width = 10  # Update width using setter
rectangle.height = 6  # Update height using setter

print(rectangle.width)  # Output: 10
print(rectangle.height)  # Output: 6 

del rectangle.width  # Delete width using deleter
del rectangle.height  # Delete height using deleter