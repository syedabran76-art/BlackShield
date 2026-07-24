import socket

from utils.helpers import separator


def dns_lookup():
    separator()
    print("BlackShield - DNS Lookup")
    print("=" * 60)

    domain = input("Enter a domain (e.g. example.com): ").strip()

    if not domain:
        print("\nNo domain entered.")
        separator()
        input("\nPress Enter to continue...")
        return

    try:
        hostname, aliases, addresses = socket.gethostbyname_ex(domain)

        print("\nResults")
        print("-" * 60)
        print(f"Hostname : {hostname}")

        if aliases:
            print(f"Aliases  : {', '.join(aliases)}")
        else:
            print("Aliases  : None")

        print("\nIP Addresses")
        for ip in addresses:
            print(f" - {ip}")

    except socket.gaierror:
        print("\nUnable to resolve the domain.")

    separator()
    input("\nPress Enter to continue...")
