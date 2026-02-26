from datetime import date

all_calculations_list = ['10.0°F is -12°C', '20.0°F is -7°C',
                         '30.0°F is -1°C', '40.0°F is 4°C',
                         '50.0°F is 10°C', '60.0°F is 16°C']

# Get current date for heading and filename
today = date.today()

# Get day, month and year as individual strings
day = today.strftime("%d")
month = today.strftime("%m")
year = today.strftime("%Y")

file_name = f"temperatures_{day}/{month}/{year}"
write_to = f"{file_name}.txt"

with open(write_to, 'w') as text_file:
