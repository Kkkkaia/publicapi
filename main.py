import json
from datetime import datetime
import requests
tender_id = int(input("enter a tender's id:"))
TENDERS_BASE_URL = f"https://tenders.guru/api/es/tenders/{tender_id}"
parameters = {"tender id": tender_id}
main_data = requests.get(TENDERS_BASE_URL, params=parameters).json()

date = main_data['date']
date_format = datetime.strptime(date, '%Y-%m-%d')
new_format_date = date_format.strftime('%B %d, %Y')

print(main_data)
print(f"The tender '{main_data['title']}' was awarded with {main_data['awarded_value']} {main_data['awarded_currency']}"
      f" in {new_format_date}")
