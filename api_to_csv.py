import requests
import csv

# Fetch data from the API and populate it into a CSV file
def fetch_data_from_api(api_url):
    response = requests.get(api_url)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Failed to fetch data from API. Status code: {response.status_code}")

def write_data_to_csv(data, output_file):
    with open(output_file, mode='w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Name', 'Country', 'Domain'])
        for item in data:
            writer.writerow([item['name'], item['country'], item['domains'][0]])

def main():
    api_url = 'http://universities.hipolabs.com/search?country=Canada'
    output_file = 'universities_in_canada.csv'

    try:
        data = fetch_data_from_api(api_url)
        write_data_to_csv(data, output_file)
        print(f"Data has been successfully written to {output_file}.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()
