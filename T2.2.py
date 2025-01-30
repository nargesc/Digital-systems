import pandas as pd

# Given values
reference_voltage = 5.0  # V
resolution = 14  # bits
max_adc_value = (2 ** resolution) - 1  # Maximum ADC output value for a 14-bit ADC

# Input voltages for the four cases
input_voltages = [3.3, 0.65, 5.0, 2.1]

# Calculate ADC output values for each input voltage
adc_outputs = [(input_voltage / reference_voltage) * max_adc_value for input_voltage in input_voltages]

# Create a DataFrame to display the results
adc_results = pd.DataFrame({
    'Input Voltage (V)': input_voltages,
    'ADC Output Value': adc_outputs
})

# Display the table
print(adc_results)
