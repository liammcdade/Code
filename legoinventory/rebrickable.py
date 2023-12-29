import requests
from bs4 import BeautifulSoup

def get_bricklink_part_data(url):
    try:
        response = requests.get(url)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, 'html.parser')

        part_data = []

        # Find all part rows in the table
        rows = soup.find_all('tr', class_='odd') + soup.find_all('tr', class_='even')

        for row in rows:
            cells = row.find_all('td')

            # Extract part number and color from the cells
            part_number = cells[1].get_text(strip=True)
            color = cells[3].get_text(strip=True)

            part_data.append({'part_number': part_number, 'color': color})

        return part_data

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return []

if __name__ == "__main__":
    # Replace 'YOUR_BRICKLINK_URL' with the URL of the BrickLink page you want to scrape
    bricklink_url = 'https://www.bricklink.com/catalogList.asp?v=0&pg=1&sortBy=I&sortAsc=A&catType=P'

    if bricklink_url == 'YOUR_BRICKLINK_URL':
        print("Please replace 'YOUR_BRICKLINK_URL' with the actual BrickLink URL.")
    else:
        part_data = get_bricklink_part_data(bricklink_url)
        print(f"Total parts: {len(part_data)}")
        for part in part_data:
            print(f"Part Number: {part['part_number']}, Color: {part['color']}")
