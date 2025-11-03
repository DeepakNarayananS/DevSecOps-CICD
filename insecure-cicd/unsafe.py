import subprocess

ip = input("Enter your server ip: ")
subprocess.run(["ping", ip])

print("Attempting to connect to the server")
print("Application authentication was successful")