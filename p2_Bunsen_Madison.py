# Madison Bunsen
# Z23631556
# Question 1 

class ParkingPermit:
    """Parking Permit for faculty or student to park on campus
    
    Attributes: 
        ownername (str): name of the person who is buying the permit
        month (int): number of months the permit is valid for
        feeschedule: dict[str, float]: dictionary containing the fees for the permit 
    """

    def __init__(self, ownername: str, month: int, feeschedule: dict[str, float]) -> None:
        """Create a permit 
        
        Args:
            ownername (str): name of the person who is buying the permit
            month (int): number of months the permit is valid for
            feeschedule: dict[str, float]: dictionary containing the fees for the permit

        Preconditions: 
            month >= 0 and feeschedule has the key monthly

        Postconditions:
           the three values are stores as attributes 
        
        """
        self.ownername = ownername
        self.month = month
        self.feeschedule = feeschedule

    def cost(self) -> float:
       """Calculate the cost of the permit
       
       Preconditions:
         feeschedule contains the key monthly 

       Postconditions:
          returns the cost of the permit based on the number of months and the monthly fee           
       """
       return self.month * self.feeschedule["monthly"]

    def __str__(self) -> str:
        """Return a string of the owner, months and cost of permit"""
        return f"Owner: {self.ownername}, Months: {self.month}, cost: ${self.cost():.2f}"
    
    def __repr__(self) -> str:
        """Return a string that looks like the constructor for the class"""
        return f"ParkingPermit(ownername={self.ownername!r}, month={self.month!r}, feeschedule={self.feeschedule!r})"




class StudentPermit(ParkingPermit):
    """Student Parking Permit for students to park on campus
    
    Args:
        ownername (str): name of the person who is buying the permit
        month (int): number of months the permit is valid for
        feeschedule: dict[str, float]: dictionary containing the fees
        vehiclesregistered (int): number of vehicles registered


    Preconditions:
       month >= 0 and vehiclesregistered >= 1

    Postconditions:
       inherited attributes from ParkingPermit and stores vehiclesregistered as an attribute
    """
    def __init__(self, ownername: str, month: int, feeschedule: dict[str, float], vehiclesregistered: int) -> None:
        super().__init__(ownername, month, feeschedule)
        self.vehiclesregistered = vehiclesregistered 

    def cost(self) -> float:
        """Calculate the cost of the permit for a student
        
        Preconditions: 
            feeschedule contains the keys monthly and extravehicle
            
        Postconditions:
            returns the cost of the permit based on the number of months, the monthly fee and the number of vehicles registered
            
  """
        if self.vehiclesregistered > 1:
            extravehicles = self.vehiclesregistered - 1
        else:
            extravehicles = 0
        return (self.month * self.feeschedule["monthly"] + extravehicles * self.feeschedule["extravehicle"])

    def __str__(self) -> str:
        """Return a string of the owner, months, cost of permit and number of vehicles registered"""
        return f"Student - {super().__str__()}, Vehicles: {self.vehiclesregistered}"

    def __repr__(self) -> str:
        """Return a string that looks like the constructor for the class"""
        return f"StudentPermit({self.ownername!r}, {self.month!r}, {self.feeschedule!r}, {self.vehiclesregistered!r})"


class FacultyPermit(ParkingPermit):
    """Faculty parking permit with or without garage access
    
    Attributes: 
        garageaccess (bool): True if the faculty has access to the garage, False otherwise
    """

    def __init__(self, ownername: str, month: int, feeschedule: dict[str,float], garageaccess: bool) -> None:
        """Create a faculty permit with or without garage access
     
        Args:
         ownername (str): name of the person getting the permit 
         month (int): number of months the permit is valid for 
         feeschedule dic[str, float]: dictionary containing fees
         garageaccess(bool): has access to the garage or not

        Preconditions:
         month >= 0 and feeschedule has the keys monthly and garageaccess

        Postconditions:
         Inherited attributes are set by parent constructor and garageaccess is stored
     
        """
    
        super().__init__(ownername, month, feeschedule)
        self.garageaccess = garageaccess

    def cost(self) -> float:
        """Calculate the cost of the permit for a faculty member
        
        Preconditions: 
            feeschedule contains the keys monthly and garageaccess

        Postconditions:
            returns the cost of the permit based on the number of months, the monthly fee and whether or not the faculty has garage access
        """
        if self.garageaccess == True:
            return(self.month * self.feeschedule["monthly"] + self.month *self.feeschedule["garageaccess"])
        else:
            return(self.month * self.feeschedule["monthly"])

    def __str__(self) -> str:
        """Return a string of the owner, months, cost of permit and whether or not the faculty has garage access"""
        return f"Faculty- {super().__str__()}, Garage Access: {self.garageaccess}"

    def __repr__(self) -> str:
        """Return a string that looks like the constructor for the class"""
        return f"FacultyPermit({self.ownername!r}, {self.month!r}, {self.feeschedule!r}, {self.garageaccess!r})"



def summarize_list(permits: list[ParkingPermit]) -> float:
    """Calculate the total cost of all permits in the list and print the owner and cost of each permit
    
    Args:
        permits (list[ParkingPermit]): list of ParkingPermit objects

    Preconditions:
        permits is a list of ParkingPermit objects
    
    Postconditions:
        prints the owner and cost of each permit
        returns the total cost of all permits
    """
    total = 0.0
    for p in permits:
        amount = p.cost()
        print(f"{p.ownername}: ${amount:.2f}")
        total += amount
    return total

def main() -> None:
    """Test values for permits and print the total cost of all permits and total revenue"""
    
    StudentFees = {"monthly": 25, "extravehicle": 10}
    FacultyFees = {"monthly": 40, "garageaccess": 15}

    permits = [
        StudentPermit("Sophia", 6, StudentFees, 3),
        FacultyPermit("Dr.Jinkens", 24, FacultyFees, True) ]

    for p in permits:
      print(p)
      print(repr(p))

    print("Summary of all permits: ")
    total = summarize_list(permits)
    print(f"Total: ${total:.2f}")

main()



        


