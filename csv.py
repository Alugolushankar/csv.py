import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL of the HDFC Bank credit card page
url = "http://www.hdfcbank.com/personal/pay/cards/creditcards"

# Make an HTTP request to the URL
response = requests.get(url)

# Parse the HTML content of the response using BeautifulSoup
soup = BeautifulSoup(response.content, "html.parser")

# Find all the credit card product elements on the page
card_products = soup.find_all("div", class_="prod-detail")

# Initialize a list to store the credit card details
cards_list = []

# Loop through each credit card product and extract its details
for card in card_products:
    # Extract the card name
    card_name = card.find("div", class_="prod-title").text.strip()

    # Extract the card fee
    card_fee = card.find("div", class_="prod-fee").text.strip()

    # Extract the reward points/percentage per 100 spent
    reward_points = card.find("div", class_="prod-rewards").text.strip()

    # Extract the lounge access
    lounge_access = card.find("div", class_="prod-lounge").text.strip()

    # Extract the milestone benefit
    milestone_benefit = card.find("div", class_="prod-benefit").text.strip()

    # Extract the card fee reversal condition
    fee_reversal = card.find("div", class_="prod-reversal").text.strip()

    # Create a dictionary of the card details
    card_dict = {"Card Name": card_name,
                 "Card fee": card_fee,
                 "Reward points/percentage per 100 spent": reward_points,
                 "Lounge access": lounge_access,
                 "Milestone benefit": milestone_benefit,
                 "Card fee reversal condition if any": fee_reversal}

    # Add the card details to the list
    cards_list.append(card_dict)

# Create a pandas DataFrame from the list of card details
cards_df = pd.DataFrame(cards_list)

# Save the DataFrame to a CSV file
cards_df.to_csv("HDFC_Credit_Cards_Details.csv", index=False)