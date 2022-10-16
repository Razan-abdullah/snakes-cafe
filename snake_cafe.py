

def Create_order():
    Menu = {
        "Wings": 0,
        "Cookies": 0,
        "Spring Rolls": 0,
        "Salmon": 0,
        "Steak": 0,
        "Meat Tornado": 0,
        "A literal Garden": 0,
        "Ice Cream": 0,
        "Cake": 0,
        "Pie": 0,
        "Coffee": 0,
        "Tea": 0,
        "Unicorn Tears": 0
    }
    
    
    print ("What woulde you like to order ?")
    order=[]
    check=True
    while True:
        O=input("Enter you order Here: ")
        if O=="quit":
            if len(order)==0:
                print("Thanks to visit us ,Have a nice day")
                break
            else:
                print(f"your order is {order}")
                print("Thank you to choose us :)")
                break
        for (key, value) in Menu.items():
            if O==key:
                check=False
                Menu[key]=Menu[key]+1
                print(f" {Menu[key]} order of {key} has been added to youe meal")
                order.append(O)
        if check:
            print ("OOPs ! this isn't in our Menu :)")    
        
    



if __name__ == "__main__":
   
    Welcom = '''
        *************************************
        ***  Welcome to the Snake Cafe    ***
        *** Please see our menu below     ***          
        *** to quit at any time type quit ***
        
        ------
        Menu
        
        Appetizers
        ----------
        wings 
        cookies 
        spring rolls  
        
        -----
        entrees
        -------
        Salmon 
        Steak
        Meat Tornado
        A literal Garden
        
        ----
        
        Desserts  
        ---------
        Ice cream
        Cake
        Pie     
        -----
        
        Drinks 
        --------
        coffee
        Tea
        Unicorn Tears
        
        *******************************************
        
        ***   What Would you like to order ?    ***
        
        '''
    print(Welcom)
    Create_order()
    
    
