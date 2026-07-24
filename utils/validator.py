import ipaddress
import os
import re


def is_valid_ip(ip):
    """
    Validate an IPv4 or IPv6 address.
    """
    try:
        ipaddress.ip_address(ip)
        return True
    except ValueError:
        return False


def file_exists(path):
    """
    Check if a file exists.
    """
    return os.path.isfile(path)


def directory_exists(path):
    """
    Check if a directory exists.
    """
    return os.path.isdir(path)


def is_valid_port(port):
    """
    Validate a TCP/UDP port number.
    """
    try:
        port = int(port)
        return 1 <= port <= 65535
    except (TypeError, ValueError):
        return False


def is_valid_domain(domain):
    """
    Validate a domain name.
    """
    pattern = (
        r"^(?!-)(?:[A-Za-z0-9-]{1,63}\.)+"
        r"[A-Za-z]{2,63}$"
    )
    return re.fullmatch(pattern, domain) is not None
