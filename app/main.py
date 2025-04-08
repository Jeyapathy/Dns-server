import socket

def create_dns_response(query):
    """
    Create a minimal valid DNS response.
    This assumes the query is a standard DNS query.
    """
    # DNS header is 12 bytes: transaction ID (2), flags (2), counts (4 x 2)
    transaction_id = query[:2]
    flags = b'\x81\x80'  # standard response: QR=1, RD=1, RA=1, no error
    qdcount = query[4:6]  # questions count
    ancount = b'\x00\x01'  # 1 answer
    nscount = b'\x00\x00'
    arcount = b'\x00\x00'
    header = transaction_id + flags + qdcount + ancount + nscount + arcount

    # Extract question section (start after 12-byte header)
    question = query[12:]
    
    # Build fake answer
    # Name is a pointer to offset 12 (0xc00c), type A, class IN
    answer_name = b'\xc0\x0c'
    answer_type = b'\x00\x01'
    answer_class = b'\x00\x01'
    ttl = b'\x00\x00\x00\x3c'  # 60 seconds
    rdlength = b'\x00\x04'
    rdata = b'\x7f\x00\x00\x01'  # 127.0.0.1

    answer = answer_name + answer_type + answer_class + ttl + rdlength + rdata

    return header + question + answer

def main():
    HOST = "127.0.0.1"
    PORT = 2053

    print(f"DNS-like UDP server starting on {HOST}:{PORT}...")

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((HOST, PORT))

    try:
        while True:
            data, addr = sock.recvfrom(512)
            print(f"Received {len(data)} bytes from {addr}")

            response = create_dns_response(data)

            sock.sendto(response, addr)
            print(f"Sent response to {addr}")
    except Exception as e:
        print(f"Server error: {e}")
    finally:
        sock.close()
        print("Server stopped.")

if __name__ == "__main__":
    main()
