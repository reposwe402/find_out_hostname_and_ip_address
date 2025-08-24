from network_operations import resolve_hostname_to_ip

def main():
    hostname = input("Please enter website address(URL):")
    try:
        print(f'Hostname: {hostname}')
        ip_address = resolve_hostname_to_ip(hostname)
        print(f'IP: {ip_address}')
    except ValueError as error:
        print(error)

if __name__ == "__main__":
    main()

