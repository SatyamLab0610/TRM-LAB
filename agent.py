import asyncio, json
from crawler import crawl_site
from classifier import classify_site
from address_extractor import extract_addresses

URLS = [
    "https://22betcanada.com",
    "https://bitocitex.com",
    "https://timeecoin.com/wap"
]

async def analyze(url):
    print("Analyzing:", url)
    page = await crawl_site(url)

    if not page:
        return {"url": url, "classification": "NOT_SCAM", "confidence": 0.2}

    addresses = extract_addresses(page["text"])
    verdict, confidence = classify_site(page["text"], addresses)

    return {
        "url": url,
        "classification": verdict,
        "crypto_addresses": addresses,
        "confidence": confidence
    }

async def main():
    results = []
    for url in URLS:
        results.append(await analyze(url))

    with open("output.json", "w") as f:
        json.dump(results, f, indent=2)

    print("Done! Results saved to output.json")

asyncio.run(main())
