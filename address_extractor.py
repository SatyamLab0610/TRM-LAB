import re

BTC_REGEX = r'\\b(bc1|[13])[a-zA-HJ-NP-Z0-9]{25,39}\\b'
ETH_REGEX = r'\\b0x[a-fA-F0-9]{40}\\b'
TRON_REGEX = r'\\bT[a-zA-HJ-NP-Z0-9]{33}\\b'

def extract_addresses(text):
    addresses = set()
    for regex in [BTC_REGEX, ETH_REGEX, TRON_REGEX]:
        matches = re.findall(regex, text)
        for m in matches:
            addresses.add(m if isinstance(m, str) else m[0])
    return list(addresses)
