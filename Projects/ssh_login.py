import subprocess

# Ask the user for the IP address
ip_address = input("Enter the server IP: ").strip()

# Define the SSH command
ssh_command = f"ssh -i /Users/kelvinleekarchoon/Downloads/kelvin_ec2_MY.pem ubuntu@{ip_address}"

# Run the SSH command
subprocess.run(ssh_command, shell=True)