import socket
import threading
import time
import random

def receiver_thread(port, total_frames):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(("127.0.0.1", port))
    expected_seq = 0
    received_count = 0

    while received_count < total_frames:
        data, addr = sock.recvfrom(1024)
        msg = data.decode()
        
        # Check for corrupted payload signal
        if msg == "CORRUPTED":
            print(f"[Receiver] Received corrupted frame! Dropping frame...")
            continue

        seq_num, frame_data = int(msg[0]), msg[2:]

        # Simulate 20% ACK loss error
        if random.random() < 0.2:
            print(f"[Receiver] Simulated ACK Loss error for Frame {seq_num}")
            continue

        if seq_num == expected_seq:
            print(f"[Receiver] Received Frame {seq_num}: '{frame_data}' -> Sending ACK {seq_num}")
            expected_seq = 1 - expected_seq
            received_count += 1
        else:
            print(f"[Receiver] Duplicate Frame {seq_num} received -> Re-sending ACK {seq_num}")

        sock.sendto(f"ACK_{seq_num}".encode(), addr)
    sock.close()

def sender(port, frames):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.settimeout(2.0)
    server_addr = ("127.0.0.1", port)
    seq_num = 0

    for frame in frames:
        packet = f"{seq_num}:{frame}"
        ack_received = False

        while not ack_received:
            error_chance = random.random()
            
            # Simulate 15% Frame Loss error
            if error_chance < 0.15:
                print(f"[Sender] Simulated Frame Loss error for Frame {seq_num} (Dropping transmission)")
            # Simulate 15% Bit Corruption error
            elif error_chance < 0.30:
                print(f"[Sender] Simulated Bit Corruption error for Frame {seq_num}")
                sock.sendto("CORRUPTED".encode(), server_addr)
            else:
                print(f"[Sender] Sending Frame {seq_num}: '{frame}'")
                sock.sendto(packet.encode(), server_addr)

            try:
                data, _ = sock.recvfrom(1024)
                ack_msg = data.decode()
                if ack_msg == f"ACK_{seq_num}":
                    print(f"[Sender] Received ACK {seq_num}\n")
                    ack_received = True
                    seq_num = 1 - seq_num
            except socket.timeout:
                print(f"[Sender] Timeout! Re-transmitting Frame {seq_num}...\n")

    sock.close()

if __name__ == "__main__":
    PORT = 12345
    
    num_frames = int(input("Enter the number of frames you want to run: "))
    DATA_FRAMES = [f"Frame-{i+1}" for i in range(num_frames)]

    rec_t = threading.Thread(target=receiver_thread, args=(PORT, len(DATA_FRAMES)))
    rec_t.start()

    time.sleep(0.1)
    sender(PORT, DATA_FRAMES)
    rec_t.join()