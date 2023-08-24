import pandas as pd

class DataProcessing:
    def __init__(self, df, column_mapping):
        self.df_combined = df
        self.column_mapping = column_mapping

    # part1: check user inputs
    # part2: search_results : process inputs and print results
    def search(self, file_name, column_name, value):
        
        # modified 
        def col_name_modify(file_name, column_name):
            if file_name == 'users':
                column_name = str(column_name).replace('_users','')
            elif file_name == 'tickets':
                column_name = str(column_name).replace('_tickets','')
            elif file_name == 'organizations':
                column_name = str(column_name).replace('_orgs','')
            return column_name

        # Check column name
        input_column = column_name
        column_name = col_name_modify(file_name, column_name)

        # 
        def search_results(file_name, column_name ):
            # Search the combined dataframe and output corresponding values
            search_result = self.df_combined[self.df_combined[input_column] == value]

            # Select only the columns relevant to the selected file name and relevant information from the other two files
            df_result = search_result[self.column_mapping[file_name] ]

            # remove deliminators from the column name 
            if file_name == 'users':
                df_result = df_result.rename(columns={'name_orgs': 'organization_name'})
                df_result = df_result.rename(columns={'subject_tickets': 'ticket'})
            elif file_name == 'tickets':
                df_result = df_result.rename(columns={'name_orgs': 'organization_name'})
                df_result = df_result.rename(columns={'_id_user': 'user_id'})
            elif file_name == 'organizations':
                df_result = df_result.rename(columns={'_id_user': 'user_id'})
                df_result = df_result.rename(columns={'subject_tickets': 'ticket'})

            # for different file_name input, assign different values to parameters
            for column in df_result.columns:
                if file_name == 'users':
                    new_column = column.replace('_users','')
                    df_result.rename(columns={column: new_column}, inplace=True)
                    addition_column1 = 'organization_name'
                    addition_column2 = 'ticket'
                elif file_name == 'tickets':
                    new_column = column.replace('_tickets','')
                    df_result.rename(columns={column: new_column}, inplace=True)
                    addition_column1 = 'organization_name'
                    addition_column2 = 'user_id'
                elif file_name == 'organizations':
                    new_column = column.replace('_orgs','')
                    df_result.rename(columns={column: new_column}, inplace=True)
                    addition_column1 = 'user_id'
                    addition_column2 = 'ticket'

            # Print user-related columns without duplicates in lists
            for column in df_result[:-2]:
                values = set(df_result[column].values)
                result_values = ' | '.join(map(str, values))
                print(f"{column}: {result_values}")

            #print(df_result)
            #print("1111111111",input_column)
            #print("2222222222",column_name)
            # print organizations 
            df_result_grouped = df_result.groupby(column_name).agg({addition_column1: lambda x: list(x)}).reset_index()
            # print organization 
            result_name = None
            for index, row in df_result_grouped.iterrows():
                # print(f"\n_id_users: {row['_id']}")
                for i, variable1 in enumerate(row[addition_column1]):
                    if variable1 != result_name:
                        print(f"{addition_column1}_{i}: {variable1}")
                        result_name = variable1
                    else : 
                        break

            # change this line based on user input:
            df_result_grouped = df_result.groupby(column_name).agg({addition_column2: lambda x: list(x)}).reset_index()
            # print tickets 
            for index, row in df_result_grouped.iterrows():
                # print(f"\n_id_users: {row['_id']}")
                for i, variable2 in enumerate(row[addition_column2]):
                    print(f"{addition_column2}_{i}: {variable2}")

        # Execute the function here, changes based on the input file_name, 
        search_results(file_name, column_name,)