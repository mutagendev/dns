import os
from libcloud.dns.providers import DRIVERS, get_driver as get_dns_driver
from libcloud.dns.types import Provider as DNSProvider


def provider_related(environ_key):
    for provider in DRIVERS:
        if environ_key.startswith(provider.upper()):
            return True
    return False


_KEYS = {key: os.environ[key] for key in os.environ if provider_related(os.environ[key])}

if __name__ == '__main__':
    print(True)
