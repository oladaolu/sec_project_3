import csv
import requests

# Read data from a CSV file and update it via a REST API endpoint
API_URL = "https://reqres.in/api/users"

def read_data_from_csv(csv_file):
    with open(csv_file, mode='r', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        return list(reader)

def add_or_update_user(user_data):
    user_id = user_data.get('id', None)
    if user_id:
        # Use PATCH to update an existing user
        update_url = f"{API_URL}/{user_id}"
        response = requests.patch(update_url, json=user_data)
    else:
        # Use POST to add a new user
        response = requests.post(API_URL, json=user_data)

    if response.status_code == 200 or response.status_code == 201:
        print(f"User with ID {response.json().get('id')} has been successfully {'updated' if user_id else 'added'}.")
    else:
        print(f"Failed to add/update user. Status code: {response.status_code}")

def main():
    csv_file = 'universities_in_canada.csv'
    user_data_list = read_data_from_csv(csv_file)

    for user_data in user_data_list:
        add_or_update_user(user_data)

if __name__ == "__main__":
    main()
