import aiohttp
import asyncio
import argparse
import logging

# Cloudflare API constants
CLOUDFLARE_API_TOKEN = "7fwNRheq1jxKx95YH_cr8fyqo8lz3JG9nWAvucak"
CLOUDFLARE_ZONE_ID = "dc301d73c4e697f6bda8f9cba768f19b"
CLOUDFLARE_API_URL = f"https://api.cloudflare.com/client/v4/zones/{CLOUDFLARE_ZONE_ID}/dns_records"

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[logging.FileHandler("cloudflare_setup.log"), logging.StreamHandler()]
)

logger = logging.getLogger(__name__)

async def create_dns_record(sub_domain, public_ip, ttl, proxied):
    """Create an A record in Cloudflare"""
    data = {
        "type": "A",
        "name": sub_domain,  
        "content": public_ip,  
        "ttl": ttl,
        "proxied": proxied
    }

    headers = {
        "Authorization": f"Bearer {CLOUDFLARE_API_TOKEN}",
        "Content-Type": "application/json"
    }

    async with aiohttp.ClientSession() as session:
        try:
            async with session.post(CLOUDFLARE_API_URL, json=data, headers=headers) as response:
                response_data = await response.json()
                logger.info(f"Cloudflare Response: {response.status} - {response_data}")

                if response.status == 200 and response_data.get("success"):
                    logger.info("DNS Record created successfully!")
                else:
                    logger.error(f"Failed to create DNS record: {response_data}")

        except Exception as e:
            logger.error(f"Error occurred: {e}")

def get_arguments():
    sub_domain = input("Enter the subdomain name: ")
    public_ip = input("Enter the public IP address: ")
    ttl = input("Enter the TTL value (number or 'auto'): ")
    proxied = input("Should it be proxied? (true/false): ").lower()

    # Convert ttl to integer if it's a number, or use 'auto' logic
    ttl = 1 if ttl.lower() == "auto" else int(ttl)
    proxied = proxied == "true"
    return sub_domain, public_ip, ttl, proxied

if __name__ == "__main__":
    sub_domain, public_ip, ttl, proxied = get_arguments()
    asyncio.run(create_dns_record(sub_domain, public_ip, ttl, proxied))

