[![MseeP.ai Security Assessment Badge](https://mseep.net/pr/roadwy-cve-search-mcp-badge.png)](https://mseep.ai/app/roadwy-cve-search-mcp)

## CVE-Search MCP Server
----

![CVE-SEARCH_MCP](https://socialify.git.ci/roadwy/cve-search_mcp/image?name=1&theme=Light)

<a href="https://glama.ai/mcp/servers/@roadwy/cve-search_mcp">
  <img width="380" height="200" src="https://glama.ai/mcp/servers/@roadwy/cve-search_mcp/badge" alt="cve-search_mcp MCP server" />
</a>

A Model Context Protocol (MCP) server for querying the [CVE-Search](https://www.cve-search.org/api/) API. This server provides comprehensive access to CVE-Search, browse vendor and product、get CVE per CVE-ID、get the last updated CVEs.

## Requirements
- python 3.10+
- uv
- Cline、Roo Code etc

## Tools
- To get a JSON with all the vendors
- To get a JSON with all the products associated to a vendor
- To get a JSON with all the vulnerabilities per vendor and a specific product
- To get a JSON of a specific CVE ID
- To get a JSON of the last 30 CVEs including CAPEC, CWE and CPE expansions
- To get more information about the current databases in use and when it was updated

## Quick Start
1. Git clone this repository
```
git clone https://github.com/roadwy/cve-search_mcp.git
```
2. Install the dependencies
```
cd cve-search_mcp
uv sync
```
3.Add to your mcp client(vscode with cline/roo code) configuration file, modify the `"YOU_CVE_SEARCH_MCP_DIR_PATH"` as you self dir.
```
    "cve-search_mcp": {
      "command": "uv",
      "args": [
        "--directory",
        "YOU_CVE_SEARCH_MCP_DIR_PATH",
        "run",
        "main.py"
      ],
      "disabled": false,
      "autoApprove": []
    }
```

## Reference
https://github.com/cve-search/cve-search