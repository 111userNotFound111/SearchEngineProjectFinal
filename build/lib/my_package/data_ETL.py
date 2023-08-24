import pandas as pd 
import os


class DataETL():
    # initialize class and its properties
    def __init__(self):
        self.df_users = None
        self.df_tickets = None
        self.df_organization = None 
        self.df_combined = None
        self.dataframe_list = None
        pd.set_option('display.max_columns', None)

    # load data from file
    def data_extract(self):
        dir_path=os.path.dirname(os.path.realpath(__file__))
        users_path=os.path.join(dir_path, 'users.json')
        tickets_path = os.path.join(dir_path, 'tickets.json')
        organizations_path = os.path.join(dir_path, 'organizations.json')
        
        self.df_users = pd.read_json(users_path)
        self.df_tickets = pd.read_json(tickets_path)
        self.df_organizations = pd.read_json(organizations_path)
        self.dataframe_list = [self.df_users, self.df_tickets, self.df_organizations]

    # add suffix to the column names 
    def df_add_suffix(self):
        self.df_users = self.df_users.add_suffix('_users')
        self.df_tickets = self.df_tickets.add_suffix('_tickets')
        self.df_organizations = self.df_organizations.add_suffix('_orgs')

    # merge all three dataframe on their common keys 
    def combine_dataframe(self):
    # combine user and organization on organization id (use outer merge to )
        df_user_org = pd.merge(self.df_users, self.df_organizations, left_on='organization_id_users', right_on='_id_orgs', how='outer')
    # combine tickets on submitter id 
        self.df_combined = pd.merge(df_user_org, self.df_tickets, left_on='_id_users', right_on='submitter_id_tickets', how='outer')
    # convert floating data type to strings     
        for col in self.df_combined.columns:
            if pd.api.types.is_float_dtype(self.df_combined[col]):
                self.df_combined.loc[self.df_combined[col].notna(), col] = self.df_combined.loc[self.df_combined[col].notna(), col].astype(int).astype(str)
    # flattern lists inside columns 
        self.df_combined['tags_users'] = self.df_combined['tags_users'].apply(lambda x: ', '.join(map(str, x)) if isinstance(x, list) else str(x))
        return self.df_combined 
    # dataETL
    def data_ETL(self):
        self.data_extract()
        self.df_add_suffix()
        self.df_combined = self.combine_dataframe()
        return self.df_combined
    # def data_search(self):
    #     self.search_function(self.df_combined)

    # showing data frame
    def show_data(self):
        print(self.df_combined)


main = DataETL()
main.data_ETL()
#main.show_data()