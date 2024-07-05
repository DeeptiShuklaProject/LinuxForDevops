import requests
import psycopg2
import os

# PostgreSQL database connection details
db_params = {
    'dbname': 'clinic',
    'user': 'postgres',
    'password': '@Vyaan123',
    'host': 'localhost',
    'port': '5432'
}

# Headers to mimic your specific browser
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
    'Accept-Language': 'en-US,en;q=0.9',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1'
}

# Connect to PostgreSQL database
conn = psycopg2.connect(**db_params)
cursor = conn.cursor()

# Query to get the PDF metadata
cursor.execute('SELECT name, url FROM pdfs')
rows = cursor.fetchall()

# Directory to save the PDFs
os.makedirs('downloaded_pdfs', exist_ok=True)

# Download each PDF from the stored URLs
for row in rows:
    file_name, url = row
    pdf_response = requests.get(url, headers=headers)
    pdf_response.raise_for_status()
    
    file_path = os.path.join('downloaded_pdfs', file_name)
    
    with open(file_path, 'wb') as file:
        file.write(pdf_response.content)
    
    print(f'Downloaded: {file_path}')

# Close the database connection
conn.close()

print('All PDFs have been downloaded from the database.')
