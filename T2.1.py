# Given values
V_ref = 3.3  # Reference voltage in volts
ADC_max = 2**12 - 1  # Maximum ADC value for 12-bit (4095)

# Given ADC values
adc_values = [2734, 3999, 137, 512]

import pandas as pd
from tabulate import tabulate

# Given values
V_ref = 3.3  # Reference voltage in volts
ADC_max = 2**12 - 1  # Maximum ADC value for 12-bit (4095)

# Given ADC values
adc_values = [2734, 3999, 137, 512]

# Calculate the corresponding input voltages
input_voltages = [(adc / ADC_max) * V_ref for adc in adc_values]

# Create a DataFrame for better visualization
df = pd.DataFrame({"ADC Value": adc_values, "Input Voltage (V)": input_voltages})

# Print the table using tabulate
print(tabulate(df, headers='keys', tablefmt='pretty'))

