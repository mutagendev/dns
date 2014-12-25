import os
from libcloud.dns.providers import DRIVERS, get_driver as get_dns_driver
from libcloud.dns.types import Provider as DNSProvider


_KEYS = {k, v for key, os.environ[key] in os.environ if provider_related(os.environ[key])}


def provider_related(environ_key):
    for provider in DRIVERS:
        if environ_key.startswith(provider.upper()):
            return True
    return False


if __name__ == '__main__':
