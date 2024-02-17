# defang_ip.py

# Function to defang an IP address
def defang_ip_address(ip_address):
    defanged_ip = ip_address.replace('.', '[.]')
    return defanged_ip

# Main function
def main():
    # User input for IP address
    ip_address = input("Enter an IP address: ")

    # Defang the IP address using the defang_ip_address function
    defanged_ip = defang_ip_address(ip_address)

    # Display the original and defanged versions
    print(f"Original IP address: {ip_address}")
    print(f"Defanged IP address: {defanged_ip}")

# Check if the script is run directly
if __name__ == "__main__":
    main()
