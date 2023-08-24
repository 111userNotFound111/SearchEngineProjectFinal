#!/usr/bin/env python3

class UserInterface:
    
    def __init__(self, df_combined, column_mapping):
        self.df_combined = df_combined
        self.column_mapping = column_mapping
    
    # user interface commands 
    def run(self):
        print("Welcome to Zendesk Search")
        print("Type 'quit' to exit at any time, Press 'Enter' to continue")
        # infinite loop, unless signal break
        while True:
            quit_status=False
            print("\nSelect search options:")
            print("* Press 1 to search Zendesk")
            print("* Press 2 to view a list of searchable fields")
            print("* Type 'quit' to exit")
            # check for first option input
            choice = input()
            # if use want to quit, set quit_status to true
            if choice == 'quit':
                quit_status=True
                file_name=-1
                column_name=-1
                value=-1
                print("Goodbye!")
                return file_name, column_name, value, quit_status
            # if user want to check list of searchable fields 
            elif choice == '2':
                for keys in self.column_mapping.keys():
                    print(f'dataframe name - {keys} :')
                    for search_items in self.column_mapping[keys]:
                        content=search_items.replace(f'_{keys}','')
                        print(content)
                
            # if user want to search
            elif choice == '1':
                print("\nSelect 1) Users or 2) Tickets or 3) Organizations")
                file_input = input()
                
                # Mapping user input to actual dataset names
                file_name_mapping = {
                    '1': 'users',
                    '2': 'tickets',
                    '3': 'organizations'
                }
                
                file_name = file_name_mapping.get(file_input)
                if not file_name:
                    print("Invalid selection. Please choose 1, 2, or 3.")
                    continue
                # Check if the input file name is valid
                if file_name not in self.column_mapping:
                    file_name = input("Invalid file name. Please enter 'users', 'tickets', or 'organizations'.") 

                # ask user for column input
                print("\nEnter column name")
                # modify input and check in column_mapping
                column_name = input()
                if file_input=='1':
                    column_name=column_name+'_users'
                elif file_input=='2':
                    column_name=column_name+'_tickets'
                elif file_input=='3':
                    column_name=column_name+'_orgs'
        
                # if not in column, ask user re-enter a column name
                try:
                    while column_name not in self.column_mapping[file_name]:
                        print("Invalid column name. Please make sure the column name exists in the selected file.")
                        column_name = input("Enter column name: ")
                        if file_input=='1':
                            column_name=column_name+'_users'
                        elif file_input=='2':
                            column_name=column_name+'_tickets'
                        elif file_input=='3':
                            column_name=column_name+'_orgs'
                except KeyError:
                    print(f"Error: {file_name} not found in column mapping.")
                    continue

                print("\nEnter search value")
                value = input()
                
                # Check if the value exists in the input  
                if value not in self.df_combined[column_name].values:
                    print("No results found")
                    value=''
                else:
                    print('11111 value exists 111111')
                    return file_name, column_name, value, quit_status


if __name__ == "__main__":
    UserInterface.run()
