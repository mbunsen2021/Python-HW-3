




from numbers import Real


class NVector():
    """represent a vector as a list of numeric elements"""

    def __init__(self, *args: Real | list[Real] | tuple[Real, ...]) -> None:
        """ create a vector from one sequence of real numbers storred in a list
            Preconditions:
                argument = 1 then must be an iterable sequence of numbers
                arguments > 1 then each argument must be a number
        
            Postconditions:
                vectors elements are then stored in a new list"""
        if len(args) == 1:
            self.elements = list(args[0])
        else:
            self.elements = list(args)

    def __len__(self) -> int:
        """return the number of elements in the vector"""
        return len(self.elements)

    def __getitem__(self, index: int) -> Real:
        """return the element at the given index
        
        Raises:
            raises IndexError if number is not in the index"""
        return self.elements[index]


    def __setitem__(self, index: int, value: Real) -> None:
        """set the element at the given index to the given value
        
        raises: 
            raises IndexError if number is not in the index """
        self.elements[index] = value

    def __str__(self) -> str:
        """return a readable string representation of the vector"""
        return str(self.elements)

    def __eq__(self, other: object) -> bool:
        """return True if the two vectors have the same elements, False otherwise"""
        if not isinstance(other, NVector):
            return False
        return self.elements == other.elements

    def __ne__(self, other: object) -> bool:
        """return whether other is not an equal NVector"""
        return not self.__eq__(other)

    def __add__(self, other: object) -> NVector:
        """add another vector element by element
        
        preconditions: 
            another vector must be same length
        postconditions:
            not changed

        raises:
            raises ValueError if the two vectors are not the same length    

        """
        if isinstance(other, NVector):
            if len(self) != len(other):
                raise ValueError("Vectors must have same length")
            return NVector([self[i] + other[i] for i in range(len(self))])

        if isinstance(other, (int, float)):
            return NVector([value + other for value in self.elements])

        return NotImplemented

    def __radd__(self, other: object)-> NVector:
        """support number + vector by calling __add__"""
        return self + other

    def __mul__(self, other: object) -> Real:
        """return dot product with a vector or sum 
        
       rasises:
            raises ValueError if vector lengths differ 
        """
        if isinstance(other, NVector):
            if len(self) != len(other):
                raise ValueError("vectors have to have the same length")
            return sum(self[i] * other[i] for i in range(len(self)))

        if isinstance(other, (int, float)):
            return sum(value * other for value in self.elements)

        return NotImplemented

    def __rmul__(self, other: object) -> Real:
        """support * vector using the same rule as vector * number"""
        return self * other

    def zeros(n: int) -> NVector:
        """return a new vector of dimension n containing all zeros
        
        preconditions:
            n >= 0
        """
        if isinstance(n, bool) or not isinstance(n, int):
            raise TypeError("dimension cant be negative")
        if n < 0: 
            raise ValueError("dimension cant be negative")
        return NVector([0] * n)

    
def testif(b: bool, testname: str, msgOK: str = "", msgFailed: str = "") -> bool:
    """Function used for testing.
        param b: boolean, normally a tested condition: true if test passed, false
        otherwise
        param testname: the test name
        param msgOK: string to be printed if param b==True ( test condition true)
        param msgFailed: string to be printed if param b==False
        returns b
        """
    if b:
        print("Success: "+ testname + "; " + msgOK)
    
    else:
        print("Failed: "+ testname + "; " + msgFailed)
        return b

        

def main() -> None:
    """main function to test the NVector class"""
    print("Madison Bunsen | Z23631556")


    v1 = NVector(1, 2, 3)
    v2 = NVector([4, 5, 6])

    testif(len(v1) == 3, "length", "passed", "failed")
    testif(v1[1] == 2 and v1[-1] == 3, "indexing", "passed", "failed")

    v1[0] = 10
    testif(v1[0] == 10, "assignment", "passed", "failed")

    testif(v1 + v2 == NVector(14, 7, 9), "addition", "passed", "failed")
    testif(v2 * 2 == 30 and 2 * v2 == 30, "multiplication", "passed", "failed")
    testif(NVector.zeros(3) == NVector(0, 0, 0), "zeros", "passed", "failed")

    
    
if __name__ == "__main__":
    main()
