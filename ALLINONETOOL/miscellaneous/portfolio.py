# portfolio_manager.py
import os
import json

def load_portfolio(filename='portfolio.json'):
    """Load portfolio data from a JSON file."""
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            return json.load(file)
    else:
        return {'cash': 10000, 'assets': {}}

def save_portfolio(portfolio, filename='portfolio.json'):
    """Save portfolio data to a JSON file."""
    with open(filename, 'w') as file:
        json.dump(portfolio, file, indent=4)
