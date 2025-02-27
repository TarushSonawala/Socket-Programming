#include <iostream>
#include <chrono>
#include <cstring>
#include <sys/socket.h>
#include <netinet/in.h>
#include <arpa/inet.h>
#include <unistd.h>

int main() {
    // Create UDP socket
    int sock = socket(AF_INET, SOCK_DGRAM, 0);
    if (sock < 0) {
        std::cerr << "Error creating socket" << std::endl;
        return 1;
    }

    // Bind to all interfaces on port 12345
    sockaddr_in serverAddr;
    std::memset(&serverAddr, 0, sizeof(serverAddr));
    serverAddr.sin_family = AF_INET;
    serverAddr.sin_addr.s_addr = INADDR_ANY; //UDP_IP = "0.0.0.0"       # Listen on all network interfaces
    serverAddr.sin_port = htons(12345);//PORT meow

    if (bind(sock, (sockaddr*)&serverAddr, sizeof(serverAddr)) < 0) {
        std::cerr << "Error binding socket" << std::endl;
        close(sock);
        return 1;
    }

    // Set receive timeout to 100ms
    timeval tv;
    tv.tv_sec = 0;
    tv.tv_usec = 100000; // 100 ms
    if (setsockopt(sock, SOL_SOCKET, SO_RCVTIMEO, (const char*)&tv, sizeof(tv)) < 0) {
        std::cerr << "Error setting socket timeout" << std::endl;
        close(sock);
        return 1;
    }

    std::cout << "Listening for UDP messages on port 12345..." << std::endl;

    char buffer[1024];//Buffer Size
    sockaddr_in clientAddr;
    socklen_t clientAddrLen = sizeof(clientAddr);

    // Main loop: measure total data received in one second intervals.
    while (true) {
        auto startTime = std::chrono::steady_clock::now();
        size_t totalBytes = 0;

        // Collect data for 1 second
        while (std::chrono::steady_clock::now() - startTime < std::chrono::seconds(1)) {
            ssize_t bytesReceived = recvfrom(sock, buffer, sizeof(buffer), 0,
                                             (sockaddr*)&clientAddr, &clientAddrLen);
            if (bytesReceived > 0) {
                totalBytes += bytesReceived;
            }
            // If bytesReceived is -1, it may be a timeout; we simply continue.
        }

        // Calculate bits per second and convert to Mbps
        uint64_t bitsPerSecond = totalBytes * 8;
        double mbps = bitsPerSecond / 1000000.0;

        std::cout << "Received: " << bitsPerSecond << " bps, " 
                  << mbps << " Mbps" << std::endl;
    }

    close(sock);
    return 0;
}
