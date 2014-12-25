import os
from libcloud.dns.providers import DRIVERS, get_driver as get_dns_driver
from libcloud.dns.types import Provider as DNSProvider


def env_vars():
    env_vars = {}
    for key in os.environ:
        if key.startswith('DNS_'):
            env_vars[key[4:]] = os.getenv(key)
    return env_vars

if __name__ == '__main__':
    print(True)
