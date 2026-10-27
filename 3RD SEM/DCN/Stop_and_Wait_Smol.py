import random

total_frames = int(input("Enter the number of frames to send: "))

frame = 1
sequence_number = 0

while frame <= total_frames:
    print("\nSender: Sending Frame", frame,
          "with Sequence Number", sequence_number)

    # Simulate whether the ACK is received
    ack_received = random.choice([True, False])

    if ack_received:
        print("Receiver: Frame", frame, "received successfully.")
        print("Receiver: Sending ACK", sequence_number)
        print("Sender: ACK", sequence_number, "received.")

        frame += 1
        sequence_number = 1 - sequence_number

    else:
        print("Receiver: Frame", frame, "received.")
        print("Network: ACK lost!")
        print("Sender: Timeout occurred.")
        print("Sender: Retransmitting Frame", frame)

print("\nAll frames transmitted successfully.")