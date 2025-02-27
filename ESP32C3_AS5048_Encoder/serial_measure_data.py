import serial
import time

ser = serial.Serial('/dev/ttyACM0', 115200, timeout=1)

bits_per_cycle = 10  

print("Receiving data and calculating frequency every second:")

while True:
    start_time = time.time()
    byte_count = 0
    interval = 1  
    

    while time.time() - start_time < interval:
        if ser.in_waiting:
            data = ser.read(ser.in_waiting)
            byte_count += len(data)
 #           print(data.decode('utf-8', errors='replace'), end='', flush=True)
    
    elapsed_time = time.time() - start_time
    data_rate_bps = (byte_count * 8) / elapsed_time  # bits per second
    frequency = data_rate_bps / bits_per_cycle
    mbps = data_rate_bps/1000000
    print("\nData rate: {:.2f} bps,Mbps: {:.2f}, Frequency: {:.2f} Hz".format(data_rate_bps,mbps, frequency))
