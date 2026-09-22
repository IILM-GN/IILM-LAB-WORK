# Parity Check - Even Parity

data = input("Enter original binary data: ")

# Calculate parity bit
ones = data.count('1')

if ones % 2 == 0:
    parity_bit = '0'
else:
    parity_bit = '1'

# Data sent by sender
sent_data = data + parity_bit

print("\nData sent by sender:", sent_data)

# Receiver enters the received data
received_data = input("Enter received data: ")

# Check number of 1s in received data
received_ones = received_data.count('1')

if received_ones % 2 == 0:
    print("No error detected.")
else:
    print("Error detected!")

print("Final received data:", received_data)