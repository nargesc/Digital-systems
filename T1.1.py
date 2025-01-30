import numpy as np
import matplotlib.pyplot as plt

# Define time points (every 0.1s)
t = np.arange(0, 1.1, 0.1)

# Define the original signal based on visual estimation from the given diagram
original_signal = np.array([0.05, 0.2, 0.1, 0.05, 0.03, 0.2, 0.6, 1.1, 1.4, 1.2, 0.6])

# Define quantization levels (3-bit ADC, 8 levels)
max_voltage = 1.4  # Maximum voltage
num_levels = 2**3  # 3-bit quantization (8 levels)
quantization_step = max_voltage / (num_levels - 1)

# Perform quantization (round to the nearest level)
quantized_signal = np.round(original_signal / quantization_step) * quantization_step

# Convert to 3-bit binary values
binary_values = [format(int(q / quantization_step), '03b') for q in quantized_signal]

# Plot the original signal
plt.figure(figsize=(10, 5))
plt.plot(t, original_signal, linestyle='dashed', color='blue', marker='o', label="Original Signal")

# Plot sampled values
plt.scatter(t, original_signal, color='blue', label="Sampled Values")

# Plot quantized values in red
plt.scatter(t, quantized_signal, color='red', label="Quantized Values")

# Add binary values next to quantized points
for i in range(len(t)):
    plt.text(t[i], quantized_signal[i] + 0.05, binary_values[i], fontsize=12, color='red', ha='center')

# Configure plot labels and title
plt.xlabel("Time (seconds)")
plt.ylabel("Voltage (V)")
plt.title("A/D Conversion with Correct Linear Quantization")
plt.legend()
plt.grid(True)

# Show plot
plt.show()
