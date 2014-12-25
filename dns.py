import os
from libcloud.dns.providers import DRIVERS, get_driver as get_dns_driver
from libcloud.dns.types import Provider as DNSProvider


def env_vars():
    env_vars = {}
    for key in os.environ:
        if key.startswith('DNS_'):
            provider = key[4:].split('_')[0].lower()
            if provider not in env_vars:
                if provider in DRIVERS:
                    env_vars[provider] = {}
                elif key[4:].startswith('RACKSPACE_UK'):
                    provider = 'rackspace_uk'
                    env_vars['rackspace_uk'] = {}
                elif key[4:].startswith('RACKSPACE_US'):
                    provider = 'rackspace_us'
                    env_vars['rackspace_us'] = {}
            env_vars[provider] = os.getenv(key)
    return env_vars

if __name__ == '__main__':
    print(True)
