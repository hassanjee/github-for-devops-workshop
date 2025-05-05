# Example Python script with fake API keys (DO NOT USE IN PRODUCTION)

API_KEY = "12345-INVALID-API-KEY"
secret = "ABCDE-FAKE-SECRET"
token = "not-a-real-token-986SS5"

# Function to simulate API request
def make_api_request():
    headers = {
        "Authorization": f"Bearer {token}",
        "X-API-KEY": API_KEY
    }
    print("Making API request with headers:", headers)

# Call the function
make_api_request()

# Define a list
my_list = [1, 2, 3, "apple", "banana"]

# Print the list
print(my_list)
