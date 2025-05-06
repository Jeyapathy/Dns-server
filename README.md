# Dns-server #
**Build Your Own DNS Server** 

This project is a minimal custom implementation of a DNS server using Python and UDP sockets. It demonstrates how DNS queries work at a low level — from parsing requests to responding with DNS records.
DNS is a protocol used to resolve domain names to IP addresses. We'll build a DNS server that's capable of responding to basic DNS queries.
## What It Does

- Listens for DNS queries over UDP
- Parses incoming DNS packets
- Resolves A-record queries (IPv4 addresses)
- Sends back correctly formatted DNS responses

## Technologies Used

- Python (socket, struct)
- UDP networking
- DNS protocol basics

## Getting Started

1. Clone the repo:
   ```bash
   git clone https://github.com/your-username/build-your-own-dns.git
   cd build-your-own-dns 
