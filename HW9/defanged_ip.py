import re


def ipv4_validation(func):
    def wrapper(ip_address):
        ipv4_pattern = re.compile(r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$')
        if ipv4_pattern.match(ip_address):
            return func(ip_address)
        else:
            return "Invalid IPv4 address"

    return wrapper
@ipv4_validation
def defanged_ip(ip_address):
    modified_ip_address = ip_address.replace(".", "[.]")
    return modified_ip_address


assert defanged_ip("1.1.1.1") == "1[.]1[.]1[.]1"
assert defanged_ip("1.1.1.1111") == "Invalid IPv4 address"
