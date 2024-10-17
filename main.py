import requests
from datetime import datetime

# Note for new users: use this link to access the habit tracker graph:
# https://pixe.la/v1/users/avirami2/graphs/ueudjs23123322.html

# User-specific details for authentication and API interaction
USERNAME = "avirami2"
TOKEN = "420439483948hdgasdqsd"
ID = "ueudjs23123322"

# Step 1: Create a User (POST request)
# Endpoint to create a new user on Pixela.
# This step is required only once. Once the user is created, comment out this block.
pixela_endpoint = "https://pixe.la/v1/users"
user_params = {
    "token": TOKEN,                # User's API token (authentication)
    "username": USERNAME,          # Desired username
    "agreeTermsOfService": "yes",  # Agreement to terms of service
    "notMinor": "yes"              # Confirmation that user is not a minor
}

# Uncomment the lines below to create a user.
# r = requests.post(url=pixela_endpoint, json=user_params)
# print(r.text)  # Prints the response from the server

# Step 2: Create a Graph (POST request)
# Endpoint to create a new graph for tracking a habit or activity.
# Like user creation, this step is needed only once per graph.
graph_endpoint = f"https://pixe.la/v1/users/{USERNAME}/graphs"
graph_params = {
    "id": ID,                 # Unique ID for the graph
    "name": "Cycling Graph",  # Name of the graph
    "unit": "Km",             # Unit of measurement for the activity
    "type": "float",          # Data type of the measurement (e.g., float, int)
    "color": "shibafu"        # Color of the graph line (e.g., shibafu = green)
}

headers = {
    "X-USER-TOKEN": TOKEN  # Header for authentication
}

# Uncomment the lines below to create a graph.
# r = requests.post(url=graph_endpoint, json=graph_params, headers=headers)
# print(r.text)  # Prints the response from the server

# Step 3: Retrieve the Graph
# You can view the graph in a web browser by visiting the following URL format:
# https://pixe.la/v1/users/{USERNAME}/graphs/{ID}.html
# Example: https://pixe.la/v1/users/avirami2/graphs/ueudjs23123322.html
# The .html extension renders the graph as a proper webpage.

# Step 4: Post a Pixel to the Graph (POST request)
# Endpoint to log a new entry (pixel) on the graph.
pixel_endpoint = f"https://pixe.la/v1/users/{USERNAME}/graphs/{ID}"

# Get today's date in the required format (YYYYMMDD)
now = datetime.now()
today_date = now.strftime("%Y%m%d")

# Prompt user for the quantity of activity to log
post_params = {
    "date": today_date,              # Date for the pixel
    "quantity": input("How many Km did you run today? ")  # Quantity of activity
}

# Post the pixel to the graph
r = requests.post(url=pixel_endpoint, json=post_params, headers=headers)
print(r.text)  # Prints the response from the server

# Step 5: Update a Pixel (PUT request)
# Endpoint to update a previously logged pixel.
put_pixel_endpoint = f"https://pixe.la/v1/users/{USERNAME}/graphs/{ID}/{today_date}"

put_params = {
    "quantity": "10"  # Update the quantity to a new value (e.g., 10 Km)
}

# Uncomment the lines below to update a pixel.
# r = requests.put(url=put_pixel_endpoint, json=put_params, headers=headers)
# print(r.text)  # Prints the response from the server

# Step 6: Delete a Pixel (DELETE request)
# Endpoint to delete a previously logged pixel.
# Uncomment the lines below to delete a pixel.
# r = requests.delete(url=put_pixel_endpoint, headers=headers)
# print(r.text)  # Prints the response from the server