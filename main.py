# -*- coding: utf-8 -*-
# https://github.com/roadwy
from mcp.server.fastmcp import FastMCP
import requests
from typing import Dict, Any, List
import logging


BASE_URL = "https://cve.circl.lu/api/"
mcp = FastMCP("cve-search_mcp")
logger = logging.getLogger(__name__)
logger.info("Starting cve-search_mcp")


def get_requests(uri: str) -> Dict[str, Any]:
    """To get a JSON with all the requests"""
    session = requests.Session()
    url = f"{BASE_URL}{uri}"
    try:
        response = session.get(url, timeout=15)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        logger.error(f"api request failed: {url} - {str(e)}")
        return {"error": str(e)}


@mcp.tool()
def vul_vendors() -> Dict[str, Any]:
    """
    To get a JSON with all the vendors
    """
    return get_requests("browse")


@mcp.tool()
def vul_vendor_products(vendor: str) -> Dict[str, Any]:
    """
    To get a JSON with all the products associated to a vendor
    """
    uri = f"browse/{vendor}"
    return get_requests(uri)


@mcp.tool()
def vul_vendor_product_cve(vendor: str, product: str) -> Dict[str, Any]:
    """
    To get a JSON with all the vulnerabilities per vendor and a specific product
    """
    uri = f"search/{vendor}/{product}"
    return get_requests(uri)


@mcp.tool()
def vul_cve_search(cve_id: str) -> Dict[str, Any]:
    """
    To get a JSON of a specific CVE ID
    """
    uri = f"cve/{cve_id}"
    return get_requests(uri)


@mcp.tool()
def vul_last_cves(number: int = 5) -> List[Dict[str, Any]]:
    """
    To get a JSON of the last <number> (5 by default) CVEs including CAPEC, CWE and CPE expansions
    """
    uri = f"last/{number}"
    return get_requests(uri)


@mcp.tool()
def vul_db_update_status() -> Dict[str, Any]:
    """
    To get more information about the current databases in use and when it was updated
    """
    uri = f"dbInfo"
    return get_requests(uri)


def main():
    # mcp.run(transport='sse')
    mcp.run(transport="stdio")


if __name__ == "__main__":
    main()
