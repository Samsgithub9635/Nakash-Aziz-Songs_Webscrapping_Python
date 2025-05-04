import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://en.wikipedia.org/wiki/Nakash_Aziz"

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Find the text "Yoddha: The Warrior" within the HTML
target_text = soup.find(text="Yoddha: The Warrior")

# Find the parent table of the text
if target_text:
    parent_table = target_text.find_parent('table')

    # Read the HTML table using Pandas
    if parent_table:
        # Convert the parent table to a string and then read it using Pandas
        table_string = str(parent_table)
        df_list = pd.read_html(table_string)
        
        # Check if any DataFrame is obtained
        if df_list:
            # Assuming there's only one DataFrame in the list
            df = df_list[0]
            
            # Save the DataFrame to a CSV file without including the index
            df.to_csv("nakash_aziz_table.csv", index=False)  # Specify the file name and index=False
            
            print("DataFrame saved as 'nakash_aziz_bengali_table.csv'")
        else:
            print("No table found in the HTML.")
    else:
        print("Parent table not found.")
else:
    print("Text 'Yoddha: The Warrior' not found on the page.")
