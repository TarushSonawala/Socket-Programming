import socket
import time

# UDP configuration
UDP_IP = "0.0.0.0"       # Listen on all network interfaces
UDP_PORT = 12345         # Must match the remotePort used by your transmitter

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))
# Set a short timeout so the loop doesn't block indefinitely
sock.settimeout(0.1)

print(f"Listening for UDP messages on port {UDP_PORT}...")

while True:
    start_time = time.time()
    total_bytes = 0
    
    # Collect data for 1 second
    while time.time() - start_time < 1.0:
        try:
            data, addr = sock.recvfrom(1024)  # Buffer size of 1024 bytes
            total_bytes += len(data)
        except socket.timeout:
            # No data received in this interval; continue polling
            pass
    
    # Calculate bits per second
    bits_per_second = total_bytes * 8
    # Convert to megabits per second (Mbps)
    mbps = bits_per_second / 1_000_000
    
    print(f"Received: {bits_per_second} bps, {mbps:.2f} Mbps")
