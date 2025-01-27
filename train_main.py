# RAILWAY TICKET RESERVATION SYSTEM

import random

# Taken from the Max_Seats and Max_Name_Length

Max_Seats = [27]
Max_Name_Length = 15            

class Booking:
    def __init__(self):
        self.Train_Name = ""
        self.Train_Number = 0
        self.Name = ""
        self.Age = 0
        self.Gender = ""
        self.Source = ""
        self.Destination = ""
        self.seat_number = 0
        self.Pnr_Number = 0
        self.Ticket_Price = 0
        self.is_booked = False
        
        
 # List of Booking objects
        
train = [Booking() for i in range(Max_Seats[0])]

#initialize the train seats as display Available Seats
def initializeSeats():
    for i in range(Max_Seats[0]):
        train[i].seat_number = i + 1
        train[i].is_booked = False
        

# Display the available seats
        
def displayAvailableSeats():
    
    print("*****-----Available Seats----: -----*****")
    for i in range(Max_Seats[0]):
        if not train[i].is_booked:
            
            print(train[i].seat_number, end = " ")
    print(f"\nTotal Seats: {Max_Seats[0]}")


# Display the booked seats

def bookSeat():
    seat_number = int(input("Enter the seat number: ")) - 1    
    if seat_number < 0 or seat_number >= Max_Seats[0]:
        
        print("*****-----Invalid Seat Number-----*****")
        return
    
    if train[seat_number].is_booked:
        
        print("*****-----Seat Is Already Booked-----*****")
        
    else:
        train[seat_number].Train_Name = random.choice(["Rajdhani Express", 
                                                       "Krishna Express",
                                                       "Amaravaati Express",
                                                       "Chennai Express",
                                                       "Mumbai Express",
                                                       "Kolkata Express",])
        
        train[seat_number].Train_Number = random.randint(17405, 99999)
        
        train[seat_number].Name = input("Enter the Passenger Name: ")
        if len(train[seat_number].Name) > Max_Name_Length:
            print("Name is too long")
            return
        
        train[seat_number].Age = int(input("Enter the Age: "))
        train[seat_number].Gender = input("Enter the Gender: ")
         
        train[seat_number].Source = input("Enter the Source: ")
        train[seat_number].Destination = input("Enter the Destination: ")
        train[seat_number].is_booked = True
        train[seat_number].Pnr_Number = random.randint(8687532, 9999999)
        train[seat_number].Ticket_Price = random.randint(500, 2500)
        
        print(f"*****-----Your Ticket Is Booked Successfully-----*****")
        
        
# cancel the booked ticket

def cancelTicket():
    
    seat_number = int(input("Enter the Seat Number: ")) - 1
    
    if seat_number < 0 or seat_number >= Max_Seats[0]:
        
        print("*****-----Invalid Seat Number-----*****")
        return
    
    if train[seat_number].is_booked:
        train[seat_number].is_booked = False
        
        print(f"*****-----Your Ticket Is Cancelled Successfully-----*****")
        
    else:
        print(f"*****-----Your Ticket Is Invalid-----*****")
        
        

# print the ticket details

def printTicket():
    seat_number = int(input("Enter the seat number: ")) - 1
    
    if seat_number < 0 or seat_number >= Max_Seats[0]:
        
        print("*****-----Invalid Seat Number-----*****")    
        return
    
    if train[seat_number].is_booked:
        print("*****-----Print Ticket Details :-----*****")
        print("Train Name: ", train[seat_number].Train_Name)
        print("Train Number: ", train[seat_number].Train_Number)
        print("Name: ", train[seat_number].Name)
        print("Age: ", train[seat_number].Age)
        print("Gender: ", train[seat_number].Gender)
        print("Source: ", train[seat_number].Source)
        print("Destination: ", train[seat_number].Destination)
        print("Seat Number: ", train[seat_number].seat_number)
        print("PNR: ", train[seat_number].Pnr_Number)
        print("Ticket Price: ", train[seat_number].Ticket_Price)
        
    else:
        print(f"*****-----Your Ticket Is Not Booked-----*****")
        
        
# Main function

def main():
    initializeSeats()
    choice = 0
    while choice != 5:
        print("1. Display available seats")
        print("2. Book a ticket")
        print("3. Cancel ticket")
        print("4. Print ticket")
        print("5. Exit")
        
        choice = int(input("Enter your choice: "))
        
        if choice == 1:
            displayAvailableSeats()
            
        elif choice == 2:
            bookSeat()
            
        elif choice == 3:
            cancelTicket()
            
        elif choice == 4:
            printTicket()
            
        elif choice == 5:
            print("Exiting...")
            
        else:
            print("Invalid choice")
            
            
if __name__ == "__main__":
    main()
    
# Output:
# 1. Display available seats
# 2. Book a ticket
# 3. Cancel ticket
# 4. Print ticket
# 5. Exit
