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
                    env_vars[provider.upper()] = {}
                elif key[4:].startswith('RACKSPACE_UK'):
                    provider = 'RACKSPACE_UK'
                    env_vars['RACKSPACE_UK'] = {}
                elif key[4:].startswith('RACKSPACE_US'):
                    provider = 'RACKSPACE_US'
                    env_vars['RACKSPACE_US'] = {}
            sub_key = key[4:].split(provider.upper())[1][1:]
            env_vars[provider.upper()][sub_key] = os.getenv(key)
    return env_vars


def drivers(config_map):
    return (get_dns_driver(getattr(DNSProvider, provider))
            for provider in config_map)

if __name__ == '__main__':
    print(True)
