#!/usr/bin/env python3
import socket

def can_connect(host: str, port: int = 80, timeout: float = 5.0) -> bool:
    """Return True if we can open a TCP connection to (host, port)."""
    try:
        # socket.create_connection accepts hostnames or IPs and does DNS safely
        with socket.create_connection((host, port), timeout=timeout):
            return True
    except Exception:
        return False

def main():
    host = input("Enter host or IP (e.g. example.com or 192.0.2.1): ").strip()
    port_input = input("Enter port (press Enter for 80): ").strip()
    port = int(port_input) if port_input else 80

    if can_connect(host, port):
        print(f"Connection to {host}:{port} succeeded.")
        print("Application authentication was successful")
    else:
        print(f"Could not connect to {host}:{port}.")
        print("Application authentication failed")

if __name__ == "__main__":
    main()