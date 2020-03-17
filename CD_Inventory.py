#------------------------------------------#
# Title: Assignmen08.py
# Desc: Assignnment 08 - Working with classes
# Change Log: (Who, When, What)
# DBiesinger, 2030-Jan-01, created file
# DBiesinger, 2030-Jan-01, added pseudocode to complete assignment 08
# Kenny Lu, 2020-Mar-13, added initial commit class CD
# Kenny Lu, 2020-Mar-14, added docstrings
# Kenny Lu, 2020-Mar-15, added error handling
# Kenny Lu, 2020-Mar-16, updated comments
#------------------------------------------#

# -- DATA -- #
strFileName = 'CDInventory.txt'
lstOfCDObjects = []

class CD:
    """Stores data about a CD:

    properties:
        cd_id: (int) with CD ID
        cd_title: (string) with the title of the CD
        cd_artist: (string) with the artist of the CD
    methods:

    """
    # -- Constructor -- #
    def __init__(self, cd_id: int, cd_title: str, cd_artist: str) -> None:
        self.__cd_id = int(cd_id)
        self.__cd_title = str(cd_title)
        self.__cd_artist = str(cd_artist)

    # -- Properties -- #
    @property
    def cd_id(self):
        return self.__cd_id
    
    @cd_id.setter
    def cd_id(self, value):
        self.__cd_id = value
    
    @property
    def cd_title(self):
        return self.__cd_title
    
    @cd_title.setter
    def cd_title(self, value):
        self.__cd_title = value
        
    @property
    def cd_artist(self):
        return self.__cd_artist
    
    @cd_artist.setter
    def cd_artist(self, value):
        self.__cd_artist = value

    # -- Methods -- #
    def __str__(self):
        # Cd data as formatted string
        return '{}\t{} (by: {})'.format(self.cd_id, self.cd_title, self.cd_artist)
    
    def get_textdata(self):
        # Cd data as text data csv format
        return '{},{},{}\n'.format(self.cd_id, self.cd_title, self.cd_artist)

# -- PROCESSING -- #
class DataProcessor:
    """Handling data processing adding data"""
    
    @staticmethod
    def add_item(CdData, table):
        """function to add CD data to the inventory table.

        Args:
            CdData (tuple): (ID, Title, Artist) to be added to inventory.
            table (list of dict): 2D data structure (list of dicts) that holds the data during runtime.

        Returns:
            None.

        """
        Id, Title, Artist = CdData
        row = CD(Id, Title, Artist)
        table.append(row) 

class FileIO:
    """Processes data to and from file:

    properties:

    methods:
        save_inventory(file_name, lst_Inventory): -> None
        load_inventory(file_name): -> (a list of CD objects)

    """
    @staticmethod
    def load_inventory(file_name: strFileName) -> list:
        """Function to manage data ingestion from file

        Load the data from text file identified by file_name

        Args:
            file_name (string): name of file used to read the data from
            table (list of dict): 2D data structure (list of dicts) that holds the data during runtime

        Returns:
            table (list of dict): 2D data structure (list of dicts) that holds the data during runtime
        """
        lst_Inventory = []
        try:
            lst_Inventory.clear()
            with open(strFileName, 'r') as file:
                for line in file:
                    data = line.strip().split(',')
                    row = CD(data[0], data[1], data[2])
                    lst_Inventory.append(row)
        except FileNotFoundError:
            print("The file {} could not be loaded".format(file_name))

        return lst_Inventory
    
    @staticmethod
    def save_inventory(file_name: strFileName, lst_Inventory: list) -> None:
        """Function to write data in memory to file

        Load the data from memory and write to a text based human readable storage file
        
        Args:
            file_name (string): name of file used to read the data from
            table (list of dict): 2D data structure (list of dicts) that holds the data during runtime

        Returns:
            None.
        """   
        try:
            with open(file_name, 'w') as file:
                for i in lst_Inventory:
                    file.write(i.get_textdata())
        except IOError:
            print("ERROR: The file {} could not be written or saved. Returning to the menu.".format(file_name) + '\n') 

# -- PRESENTATION (Input/Output) -- #
class IO:
    """Handling Input / Output"""
     
    @staticmethod
    def print_menu():
        """Displays a menu of choices to the user

        Args:
            None.

        Returns:
            None.
        """
        print('Menu\n\n[l] load Inventory from file\n[a] Add CD\n[i] Display Current Inventory')
        print('[s] Save Inventory to file\n[x] exit\n')

    @staticmethod
    def menu_choice():
        """Gets user input for menu selection

        Args:
            None.

        Returns:
            choice (string): a lower case string of the users input out of the choices l, a, i, d, s or x

        """
        choice = ' '
        while choice not in ['l', 'a', 'i', 'd', 's', 'x']:
            choice = input('Which operation would you like to perform? [l, a, i, s or x]: ').lower().strip()
        print()  # Add extra space for layout
        return choice
    
    @staticmethod
    def add_data():
        """Get data from user to be added to data structure.

        Returns:
            Id (integer): ID of the new CD
            Title (string): Title of the new CD
            Artist (string): Artist of the new CD

        """
        while True:
            str_Id = input('Enter ID (Integer only): ').strip()
            if str_Id.lower() == 'exit':
                break
            # Try-except to ensure input is integer
            try:
                Id = int(str_Id) 
            except ValueError as e:
                print("Oops! Please enter integer only. Try again or type \'exit\' to return to the menu.")  
                continue
            Title = input('What is the CD\'s title? ').strip()
            Artist = input('What is the Artist\'s name? ').strip()
            return Id, Title, Artist
    
    @staticmethod
    def show_inventory(table):
        """Displays current inventory table

        Args:
            table (list of dict): 2D data structure (list of dicts) that holds the data during runtime.

        Returns:
            None.

        """
        print('======= The Current Inventory: =======')
        print('ID\tCD Title (by: Artist)\n')
        for row in table:
            print(row)
        print('======================================')
   
# -- Main Body of Script -- #

# 1. When program starts, read in the currently saved Inventory
lstOfCDObjects = FileIO.load_inventory(strFileName)
IO.show_inventory(lstOfCDObjects)

# 2. start main loop
while True:
    # 2.1 Display Menu to user and get choice
    IO.print_menu()
    strChoice = IO.menu_choice()
    
    # 3. Process menu selection
    # 3.1 process exit first
    if strChoice == 'x':
        break
    # 3.2 process load inventory
    if strChoice == 'l':
        print('WARNING: If you continue, all unsaved data will be lost and the Inventory re-loaded from file.')
        strYesNo = input('type \'yes\' to continue and reload from file. otherwise reload will be canceled')
        if strYesNo.lower() == 'yes':
            print('reloading...')
            lstOfCDObjects = FileIO.load_inventory(strFileName)
            IO.show_inventory(lstOfCDObjects)
        else:
            input('canceling... Inventory data NOT reloaded. Press [ENTER] to continue to the menu.')
            IO.show_inventory(lstOfCDObjects)
        continue  # start loop back at top.
    # 3.3 process add a CD
    elif strChoice == 'a':
        # 3.3.1 Ask user for new ID, CD Title and Artist
        # 3.3.2 Add item to the table
        # Try-except in case user wants to exit out of the loop
        CdInfo = IO.add_data()
        # try:
        DataProcessor.add_item(CdInfo, lstOfCDObjects)
        # except Exception:
        #     print("Returning to the menu...")    
        IO.show_inventory(lstOfCDObjects)
    # 3.4 process display current inventory
    elif strChoice == 'i':
        IO.show_inventory(lstOfCDObjects)
        continue # start loop back at top.
    # 3.5 process save inventory to file
    elif strChoice == 's':
        # 3.5.1 Display current inventory and ask user for confirmation to save
        IO.show_inventory(lstOfCDObjects)
        strYesNo = input('Save this inventory to file? [y/n] ').strip().lower()
        # 3.5.2 Process choice
        if strYesNo == 'y':
            # 3.5.2.1 save data
            FileIO.save_inventory(strFileName, lstOfCDObjects)
        else:
            input('The inventory was NOT saved to file. Press [ENTER] to return to the menu.')
        continue  # start loop back at top.
    # 3.6 catch-all should not be possible, as user choice gets vetted in IO, but to be save:
    else: 
        print('General Error')
     