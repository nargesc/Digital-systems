import pandas as pd
from tabulate import tabulate

# Creating the table data
data = {
    "Trimmer Position": [
        "Turned all the way to the left",
        "Turned all the way to the right"
    ],
    "ADC Value": ["Close to 0", "Close to 65535"],
    "Blinking Speed": ["Very fast or no visible blinking", "Very slow blinking"],
    "Reason": [
        "The wiper is near ground, resulting in a low ADC value and minimal delay.",
        "The wiper is near the highest voltage, resulting in a high ADC value and a long delay."
    ]
}

# Creating a DataFrame
df = pd.DataFrame(data)

# Displaying the table using tabulate
print(tabulate(df, headers='keys', tablefmt='grid'))

