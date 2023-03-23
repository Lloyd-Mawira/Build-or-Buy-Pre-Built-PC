#2D arrays for PC parts and Pre-built PCs
SSD = [['1', '250 GB', 69.99], ['2', '500 GB', 93.99], ['3', '4 TB', 219.99]]
HDD = [['1', '500 GB', 106.33], ['2', '1 TB', 134.33]]
CPU = [['1', 'Intel Core i7-11700K', 499.99], ['2', 'AMD Ryzen 7 5800X', 312.99]]
MOTHERBOARD = [['1', 'MSI B550-A PRO', 197.46], ['2', 'MSI Z490-A PRO', 262.30]]
RAM = [['1', '16 GB', 82.99], ['2', '32 GB', 174.99]]
GRAPHICS_CARD = [['1', 'MSI GeForce RTX 3060 12GB', 539.99]]
PSU = [['1', 'Corsair RM750', 164.99]]
CASE = [['1', 'Full Tower (black)', 149.99], ['2', 'Full Tower (red)', 149.99]]

PREBUILTS = [['1', 'Legion Tower Gen 7 with RTX 3080 Ti', 3699.99], ['2',
'SkyTech Prism II Gaming PC', 2839.99], ['3', 'ASUS ROG Strix G10CE Gaming PC',
1099.99]]

selectPrice = [] #to hold the prices of the selected pc parts

#Function for picking CPU and Motherboard
def pickCPUandMotherboard():
    print("")
    print("Great! Let's start building your PC!")
    print("")
    print("First, lets pick a CPU.")
    print(f"{CPU[0][0]} : {CPU[0][1]}, ${CPU[0][2]}")
    print(f"{CPU[1][0]} : {CPU[1][1]}, ${CPU[1][2]}")
    cpuSelect = input("Choose the number that corresponds with the part you want: ")

    #Validate the user selects only 1 or 2 as the choice.
    while cpuSelect != CPU[0][0] and cpuSelect != CPU[1][0]:
        cpuSelect = input("Choose the number that corresponds with the part you want: ")
    if (cpuSelect == '1'): #if "Intel Core i7-11700K" CPU is selected
        print("Next, lets pick a compatible motherboard.")
        print(f"{MOTHERBOARD[1][0]} : {MOTHERBOARD[1][1]}, ${MOTHERBOARD[1][2]}")
        motherboardSelect = input("Choose the number that corresponds with the part you want: ")

        #Allow selection of only "MSI Z490-A PRO" motherboard becasue the selected CPU is "Intel Core i7-11700K"
        while motherboardSelect != MOTHERBOARD[1][0]:
            motherboardSelect = input("Choose the number that corresponds with the part you want: ")

        #Add the price of the selected CPU and Motherboard to the "selectPrice" List
        selectPrice.append(CPU[0][2])
        selectPrice.append(MOTHERBOARD[1][2])

    if (cpuSelect == '2'): #if "AMD Ryzen 7 5800X" CPU is selected
        print("Next, lets pick a compatible motherboard.")
        print(f"{MOTHERBOARD[0][0]} : {MOTHERBOARD[0][1]}, ${MOTHERBOARD[0][2]}")
        motherboardSelect = input("Choose the number that corresponds with the part you want: ")
        
        #Allow selection of only "MSI B550-A PRO" motherboard becasue the selected CPU is "AMD Ryzen 7 5800X"
        while motherboardSelect != MOTHERBOARD[0][0]:
            motherboardSelect = input("Choose the number that corresponds with the part you want: ")
        
        #Add the price of the selected CPU and Motherboard to the "selectPrice" List
        selectPrice.append(CPU[1][2])
        selectPrice.append(MOTHERBOARD[0][2])

#Function for picking RAM
def pickRAM ():
    print("Next, let's pick your RAM.")
    print(f"{RAM[0][0]} : {RAM[0][1]}, ${RAM[0][2]}")
    print(f"{RAM[1][0]} : {RAM[1][1]}, ${RAM[1][2]}")
    ramSelect = input("Choose the number that corresponds with the part you want: ")

    #Validate the user selects only 1 or 2 as the choice.
    while ramSelect != RAM[0][0] and ramSelect != RAM[1][0]:
        ramSelect = input("Choose the number that corresponds with the part you want: ")
    if (ramSelect == RAM[0][0]):
        selectPrice.append(RAM[0][2])
    if (ramSelect == RAM[1][0]):
        selectPrice.append(RAM[1][2])

#Function for picking PSU
def pickPSU ():
    print("Next, let's pick your PSU.")
    print(f"{PSU[0][0]} : {PSU[0][1]}, ${PSU[0][2]}")

    #Validate the user selects only 1 as the choice.
    psuSelect = input("Choose the number that corresponds with the part you want: ")
    while psuSelect != PSU[0][0]:
        psuSelect = input("Choose the number that corresponds with the part you want: ")
    selectPrice.append(PSU[0][2])

#Function for picking Case
def pickCase ():
    print("Next, let's pick your case.")
    print(f"{CASE[0][0]} : {CASE[0][1]}, ${CASE[0][2]}")
    print(f"{CASE[1][0]} : {CASE[1][1]}, ${CASE[1][2]}")
    caseSelect = input("Choose the number that corresponds with the part you want: ")

    #Validate the user selects only 1 or 2 as the choice.
    while caseSelect != CASE[0][0] and caseSelect != CASE[1][0]:
        caseSelect = input("Choose the number that corresponds with the part you want: ")
    if (caseSelect == CASE[0][0]):
        selectPrice.append(CASE[0][2])
    if (caseSelect == CASE[1][0]):
        selectPrice.append(CASE[1][2])

#Get the first elements of the 2D arrays
def extract(list):
    first_element = []
    for i in list:
        first_element.append(i[0])
    return first_element

#Function for picking SSD and/or HDD
def pickSSDorHDD():
    print("Next, let's pick an SSD (optional, but you must have at least one SSD or HDD)")
    print(f"{SSD[0][0]} : {SSD[0][1]}, ${SSD[0][2]}")
    print(f"{SSD[1][0]} : {SSD[1][1]}, ${SSD[1][2]}")
    print(f"{SSD[2][0]} : {SSD[2][1]}, ${SSD[2][2]}")
    SSD_pick = input("Choose the number that corresponds with the part you want (or X to not get an SSD): ")

    #Validate the user selects only 1, 2 or 3 as the choice.
    while (SSD_pick not in extract(SSD) and SSD_pick != 'x' and SSD_pick != 'X'):
        SSD_pick = input('Choose the number that corresponds with the part you want (or X to not get an SSD): ')
    print("Next, let's pick an HDD (optional, but you must have at least one SSD or HDD)")
    print(f"{HDD[0][0]} : {HDD[0][1]}, ${HDD[0][2]}")
    print(f"{HDD[1][0]} : {HDD[1][1]}, ${HDD[1][2]}")
    if (SSD_pick == 'x' or SSD_pick == 'X'):

        #The user must pick an HDD becasue no SSD picked
        HDD_pick = input("Choose the number that corresponds with the part you want (since you did not get an SSD, you must get an HDD): ")
        while (HDD_pick not in extract(HDD)):
            HDD_pick = input("Choose the number that corresponds with the part you want (since you did not get an SSD, you must get an HDD): ")
        if (HDD_pick == HDD[0][0]):
            selectPrice.append(HDD[0][2])
        if (HDD_pick == HDD[1][0]):
            selectPrice.append(HDD[1][2])
    else:

        #Get the price of SSD picked and add it to the "selectPrice" list 
        if (SSD_pick == SSD[0][0]):
            selectPrice.append(SSD[0][2])
        if (SSD_pick == SSD[1][0]):
            selectPrice.append(SSD[1][2])
        if (SSD_pick == SSD[2][0]):
            selectPrice.append(SSD[2][2])

        #The user can also pick an HDD even after picking SSD
        HDD_pick = input("Choose the number that corresponds with the part you want (or X to not get an HDD): ")
        while (HDD_pick not in extract(HDD) and HDD_pick != 'x' and HDD_pick != 'X'):
            HDD_pick = input("Choose the number that corresponds with the part you want (or X to not get an HDD): ")
        if (HDD_pick == HDD[0][0]):
            selectPrice.append(HDD[0][2])
        if (HDD_pick == HDD[1][0]):
            selectPrice.append(HDD[1][2])

#Function for picking Graphics card
def pickgraphicsCard ():
    print("Finally, let's pick your graphics card (or X to not get a graphics card).")
    print(f"{GRAPHICS_CARD[0][0]} : {GRAPHICS_CARD[0][1]}, ${GRAPHICS_CARD[0][2]}")
    cardSelect = input("Choose the number that corresponds with the part you want: ")
    while cardSelect != GRAPHICS_CARD[0][0] and cardSelect != 'x' and cardSelect != 'X':
        cardSelect = input("Choose the number that corresponds with the part you want: ")
    if (cardSelect == GRAPHICS_CARD[0][0]):
            selectPrice.append(GRAPHICS_CARD[0][2])

#Function for picking Prebuilt PC
def pickPrebuiltPC():
    print("Great! Let's pick a pre-built PC!")
    print("")
    print("Which prebuilt would you like to order?")
    print(f"{PREBUILTS[0][0]} : {PREBUILTS[0][1]}, ${PREBUILTS[0][2]}")
    print(f"{PREBUILTS[1][0]} : {PREBUILTS[1][1]}, ${PREBUILTS[1][2]}")
    print(f"{PREBUILTS[2][0]} : {PREBUILTS[2][1]}, ${PREBUILTS[2][2]}")
    PREBUILTS_pick = input("Choose the number that corresponds with the part you want: ")

    #Validate the user selects only 1, 2, or 3 as the choice.
    while (PREBUILTS_pick not in extract(PREBUILTS)):
        PREBUILTS_pick = input('Choose the number that corresponds with the part you want: ')

    if (PREBUILTS_pick == PREBUILTS[0][0]):
        price = PREBUILTS[0][2]
    if (PREBUILTS_pick == PREBUILTS[1][0]):
        price = PREBUILTS[1][2]
    if (PREBUILTS_pick == PREBUILTS[2][0]):
        price = PREBUILTS[2][2]

    return price #return price for the selected pre-built PC
    
#pickItems function, which acts as the heart of the programme
def  pickItems():
    prices = [] #list of prices for all PC ordered (both custom and pre-built). 
    choice = input("Would you like to build a custom PC (1), purchase a pre-built PC (2), or would you like to checkout (3)? ")
    while choice != '1' and choice != '2' and choice != '3':
        choice = input("Would you like to build a custom PC (1), purchase a pre-built PC (2), or would you like to checkout (3)? ")
    
    #Always prompt the user to choose whether to build a custom PC or purchase a pre-built PC and exists the loop when the user types 3, which is to checkout.
    while choice != '3':
        if choice == '1':
            pickCPUandMotherboard()
            pickRAM ()
            pickPSU ()
            pickCase ()
            pickSSDorHDD()
            pickgraphicsCard ()
            total_price = 0
            for i in selectPrice:
                total_price = total_price + i
            prices.append(total_price)
            print(f"You have selected all of the required parts! Your total for this PC is ${total_price}")
        elif choice == '2':
            price = pickPrebuiltPC()
            print(f"Your total price for this prebuilt is ${price}")
            prices.append(price)
        choice = input("Would you like to build a custom PC (1), purchase a pre-built PC (2), or would you like to checkout (3)? ")
        
        #Validate the user selects only 1, 2 or 3 as the choice.
        while choice != '1' and choice != '2' and choice != '3':
            choice = input("Would you like to build a custom PC (1), purchase a pre-built PC (2), or would you like to checkout (3)? ")
    
    return prices
    

print("Welcome to my PC shop!")
print("")
if __name__ == '__main__':
    print(pickItems())
