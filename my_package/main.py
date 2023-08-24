#!/usr/bin/env python3
from my_package.data_ETL import DataETL
from my_package.data_processing import DataProcessing
from my_package.user_interface import UserInterface

class Main():
    def __init__(self):
        self.etl = DataETL()
        self.df_combined = self.etl.data_ETL()
        self.column_mapping = {
                "users": [col for col in self.df_combined.columns if '_users' in col]+ ['name_orgs', 'subject_tickets'],
                "tickets": [col for col in self.df_combined.columns if '_tickets' in col]+['name_orgs','_id_users'],
                "organizations": [col for col in self.df_combined.columns if '_org' in col]+['_id_users','subject_tickets']
            }
        self.ui = UserInterface(self.df_combined, self.column_mapping)
    def run(self):
        self.etl.data_ETL()
        while True:  # Start of the search loop
            
            dataset, term, value, quit_status = self.ui.run()  
            
            if quit_status==True:
                print("Goodbye!")
                break  # Exit the search loop
            else:
                if value:
                    print('value exists')
                    dp = DataProcessing(self.etl.df_combined,self.column_mapping)
                    dp.search(dataset, term, value)

                    print("\nDo you want to continue or quit? (Type 'continue' to search again or 'quit' to exit)")
                    user_decision = input()
                else:
                    print('value does not exists')
                    print("\nDo you want to continue or quit? (Type 'continue' to search again or 'quit' to exit)")
                    user_decision = input()

                if user_decision.lower() == 'quit':
                    print("Goodbye!")
                    break  # Exit the search loop
def main_entry_point():
    main_app = Main()
    main_app.run()
