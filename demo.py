# Example Python script with fake API keys (DO NOT USE IN PRODUCTION)

API_KEY = "12345-INVALID-API-KEY"
SECRET_KEY = "ABCDE-FAKE-SECRET"
ACCESS_TOKEN = "not-a-real-token-98765"

# Function to simulate API request
def make_api_request():
    headers = {
        "Authorization": f"Bearer {ACCESS_TOKEN}",
        "X-API-KEY": API_KEY
    }
    print("Making API request with headers:", headers)

# Call the function
make_api_request()
