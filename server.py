#!/usr/bin/env python3
"""
Kali MCP Server - Educational Penetration Testing Tools

WARNING: This tool is for EDUCATIONAL PURPOSES ONLY.
Only use on systems you own or have explicit written permission to test.
Unauthorized access to computer systems is illegal.
"""

import subprocess
import re
import json
import os
from typing import Optional, List
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("kali-mcp", dependencies=["subprocess", "re"])

# Configuration
SCAN_RESULTS_DIR = "/home/pentester/scans"
MAX_TIMEOUT = 300  # 5 minutes default timeout

# Ensure scan results directory exists
os.makedirs(SCAN_RESULTS_DIR, exist_ok=True)


def sanitize_input(value: str) -> str:
    """Sanitize input to prevent command injection."""
    # Remove potentially dangerous characters
    return re.sub(r'[;&|`$(){}\\[\\]<>\\n\\r]', '', value)


def run_command(cmd: List[str], timeout: int = MAX_TIMEOUT) -> dict:
    """Execute a command safely and return results."""
    try:
        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            timeout=timeout,
            check=False
        )
        return {
            "success": result.returncode == 0,
            "stdout": result.stdout,
            "stderr": result.stderr,
            "returncode": result.returncode
        }
    except subprocess.TimeoutExpired:
        return {
            "success": False,
            "stdout": "",
            "stderr": f"Command timed out after {timeout} seconds",
            "returncode": -1
        }
    except Exception as e:
        return {
            "success": False,
            "stdout": "",
            "stderr": str(e),
            "returncode": -1
        }


# ============================================================================
# NETWORK SCANNING TOOLS
# ============================================================================

@mcp.tool()
def nmap_scan(target: str, scan_type: str = "basic") -> str:
    """
    Perform nmap network scan.
    
    Args:
        target: IP address or hostname to scan
        scan_type: Type of scan (basic, full, fast, vuln, service)
    
    Returns:
        Scan results as formatted text
    """
    target = sanitize_input(target)
    
    scan_types = {
        "basic": ["-sV", "-sC"],
        "fast": ["-F"],
        "full": ["-p-", "-sV"],
        "vuln": ["--script=vuln"],
        "service": ["-sV", "-sC", "-A"]
    }
    
    flags = scan_types.get(scan_type, ["-sV", "-sC"])
    cmd = ["nmap"] + flags + [target]
    
    result = run_command(cmd, timeout=600)
    
    if result["success"]:
        return f"✓ Nmap Scan Results for {target}:\\n\\n{result['stdout']}"
    else:
        return f"✗ Nmap scan failed:\\n{result['stderr']}"


@mcp.tool()
def masscan_scan(target: str, ports: str = "1-1000", rate: int = 1000) -> str:
    """
    Perform fast masscan port scan.
    
    Args:
        target: IP address or CIDR range
        ports: Port range to scan (e.g., "1-1000" or "80,443,8080")
        rate: Packets per second (default: 1000)
    
    Returns:
        Scan results
    """
    target = sanitize_input(target)
    ports = sanitize_input(ports)
    
    cmd = ["masscan", target, "-p", ports, "--rate", str(rate)]
    result = run_command(cmd, timeout=300)
    
    if result["success"]:
        return f"✓ Masscan Results for {target}:\\n\\n{result['stdout']}"
    else:
        return f"✗ Masscan failed:\\n{result['stderr']}"


# ============================================================================
# WEB VULNERABILITY SCANNERS
# ============================================================================

@mcp.tool()
def nikto_scan(target: str, ssl: bool = False) -> str:
    """
    Run Nikto web server scanner.
    
    Args:
        target: Target URL or IP address
        ssl: Use SSL/TLS (https)
    
    Returns:
        Nikto scan results
    """
    target = sanitize_input(target)
    
    cmd = ["nikto", "-h", target]
    if ssl:
        cmd.append("-ssl")
    
    result = run_command(cmd, timeout=600)
    
    if result["success"] or result["stdout"]:
        return f"✓ Nikto Scan Results for {target}:\\n\\n{result['stdout']}"
    else:
        return f"✗ Nikto scan failed:\\n{result['stderr']}"


@mcp.tool()
def wpscan_scan(target: str, enumerate: str = "vp,vt,u") -> str:
    """
    Scan WordPress site for vulnerabilities.
    
    Args:
        target: WordPress site URL
        enumerate: What to enumerate (vp=vulnerable plugins, vt=vulnerable themes, u=users)
    
    Returns:
        WPScan results
    """
    target = sanitize_input(target)
    enumerate = sanitize_input(enumerate)
    
    cmd = ["wpscan", "--url", target, "--enumerate", enumerate, "--random-user-agent"]
    result = run_command(cmd, timeout=600)
    
    if result["success"] or result["stdout"]:
        return f"✓ WPScan Results for {target}:\\n\\n{result['stdout']}"
    else:
        return f"✗ WPScan failed:\\n{result['stderr']}"


@mcp.tool()
def whatweb_scan(target: str, aggression: int = 1) -> str:
    """
    Identify web technologies.
    
    Args:
        target: Target URL
        aggression: Aggression level (1-4, default: 1)
    
    Returns:
        WhatWeb results
    """
    target = sanitize_input(target)
    
    cmd = ["whatweb", "-a", str(aggression), target]
    result = run_command(cmd)
    
    if result["success"]:
        return f"✓ WhatWeb Results for {target}:\\n\\n{result['stdout']}"
    else:
        return f"✗ WhatWeb failed:\\n{result['stderr']}"


@mcp.tool()
def wafw00f_detect(target: str) -> str:
    """
    Detect Web Application Firewall.
    
    Args:
        target: Target URL
    
    Returns:
        WAFW00F results
    """
    target = sanitize_input(target)
    
    cmd = ["wafw00f", target]
    result = run_command(cmd)
    
    if result["success"]:
        return f"✓ WAFW00F Results for {target}:\\n\\n{result['stdout']}"
    else:
        return f"✗ WAFW00F failed:\\n{result['stderr']}"


# ============================================================================
# DIRECTORY/FILE BRUTEFORCING
# ============================================================================

@mcp.tool()
def dirb_scan(target: str, wordlist: str = "/usr/share/dirb/wordlists/common.txt") -> str:
    """
    Brute force directories and files.
    
    Args:
        target: Target URL
        wordlist: Path to wordlist file
    
    Returns:
        Dirb results
    """
    target = sanitize_input(target)
    
    cmd = ["dirb", target, wordlist, "-r", "-S"]
    result = run_command(cmd, timeout=600)
    
    if result["success"] or result["stdout"]:
        return f"✓ Dirb Results for {target}:\\n\\n{result['stdout']}"
    else:
        return f"✗ Dirb failed:\\n{result['stderr']}"


@mcp.tool()
def gobuster_scan(target: str, wordlist: str = "/usr/share/wordlists/dirb/common.txt", mode: str = "dir") -> str:
    """
    Fast directory/DNS/vhost bruteforce.
    
    Args:
        target: Target URL (for dir mode) or domain (for dns mode)
        wordlist: Path to wordlist
        mode: Scan mode (dir, dns, vhost)
    
    Returns:
        Gobuster results
    """
    target = sanitize_input(target)
    mode = sanitize_input(mode)
    
    cmd = ["gobuster", mode, "-u", target, "-w", wordlist]
    result = run_command(cmd, timeout=600)
    
    if result["success"] or result["stdout"]:
        return f"✓ Gobuster Results for {target}:\\n\\n{result['stdout']}"
    else:
        return f"✗ Gobuster failed:\\n{result['stderr']}"


# ============================================================================
# SQL INJECTION
# ============================================================================

@mcp.tool()
def sqlmap_scan(target: str, data: Optional[str] = None, cookie: Optional[str] = None) -> str:
    """
    Test for SQL injection vulnerabilities.
    
    Args:
        target: Target URL
        data: POST data (optional)
        cookie: Cookie string (optional)
    
    Returns:
        SQLMap results
    """
    target = sanitize_input(target)
    
    cmd = ["sqlmap", "-u", target, "--batch", "--random-agent"]
    
    if data:
        data = sanitize_input(data)
        cmd.extend(["--data", data])
    
    if cookie:
        cookie = sanitize_input(cookie)
        cmd.extend(["--cookie", cookie])
    
    result = run_command(cmd, timeout=600)
    
    if result["success"] or result["stdout"]:
        return f"✓ SQLMap Results for {target}:\\n\\n{result['stdout']}"
    else:
        return f"✗ SQLMap failed:\\n{result['stderr']}"


# ============================================================================
# EXPLOIT DATABASE
# ============================================================================

@mcp.tool()
def searchsploit_search(query: str, exact: bool = False) -> str:
    """
    Search exploit database.
    
    Args:
        query: Search term (software name, CVE, etc.)
        exact: Use exact matching
    
    Returns:
        Search results
    """
    query = sanitize_input(query)
    
    cmd = ["searchsploit", query]
    if exact:
        cmd.append("--exact")
    
    result = run_command(cmd)
    
    if result["success"]:
        return f"✓ SearchSploit Results for '{query}':\\n\\n{result['stdout']}"
    else:
        return f"✗ SearchSploit failed:\\n{result['stderr']}"


# ============================================================================
# DNS ENUMERATION
# ============================================================================

@mcp.tool()
def dnsrecon_scan(domain: str, scan_type: str = "std") -> str:
    """
    DNS enumeration and scanning.
    
    Args:
        domain: Target domain
        scan_type: Type of scan (std, axfr, bing, yand, snoop)
    
    Returns:
        DNSRecon results
    """
    domain = sanitize_input(domain)
    scan_type = sanitize_input(scan_type)
    
    cmd = ["dnsrecon", "-d", domain, "-t", scan_type]
    result = run_command(cmd)
    
    if result["success"]:
        return f"✓ DNSRecon Results for {domain}:\\n\\n{result['stdout']}"
    else:
        return f"✗ DNSRecon failed:\\n{result['stderr']}"


@mcp.tool()
def dnsenum_scan(domain: str) -> str:
    """
    DNS enumeration tool.
    
    Args:
        domain: Target domain
    
    Returns:
        DNSenum results
    """
    domain = sanitize_input(domain)
    
    cmd = ["dnsenum", domain]
    result = run_command(cmd, timeout=300)
    
    if result["success"] or result["stdout"]:
        return f"✓ DNSenum Results for {domain}:\\n\\n{result['stdout']}"
    else:
        return f"✗ DNSenum failed:\\n{result['stderr']}"


# ============================================================================
# SSL/TLS TESTING
# ============================================================================

@mcp.tool()
def sslscan_test(target: str) -> str:
    """
    Test SSL/TLS configuration.
    
    Args:
        target: Target host:port
    
    Returns:
        SSLScan results
    """
    target = sanitize_input(target)
    
    cmd = ["sslscan", target]
    result = run_command(cmd)
    
    if result["success"]:
        return f"✓ SSLScan Results for {target}:\\n\\n{result['stdout']}"
    else:
        return f"✗ SSLScan failed:\\n{result['stderr']}"


# ============================================================================
# PASSWORD CRACKING
# ============================================================================

@mcp.tool()
def hydra_bruteforce(target: str, service: str, username: str, wordlist: str) -> str:
    """
    Brute force login credentials.
    
    Args:
        target: Target IP or hostname
        service: Service to attack (ssh, ftp, http-post-form, etc.)
        username: Username to test
        wordlist: Path to password wordlist
    
    Returns:
        Hydra results
    """
    target = sanitize_input(target)
    service = sanitize_input(service)
    username = sanitize_input(username)
    
    cmd = ["hydra", "-l", username, "-P", wordlist, target, service]
    result = run_command(cmd, timeout=600)
    
    if result["success"] or result["stdout"]:
        return f"✓ Hydra Results for {target}:{service}:\\n\\n{result['stdout']}"
    else:
        return f"✗ Hydra failed:\\n{result['stderr']}"


# ============================================================================
# SMB/WINDOWS ENUMERATION
# ============================================================================

@mcp.tool()
def enum4linux_scan(target: str) -> str:
    """
    Enumerate Windows/Samba systems.
    
    Args:
        target: Target IP address
    
    Returns:
        Enum4linux results
    """
    target = sanitize_input(target)
    
    cmd = ["enum4linux", "-a", target]
    result = run_command(cmd, timeout=300)
    
    if result["success"] or result["stdout"]:
        return f"✓ Enum4linux Results for {target}:\\n\\n{result['stdout']}"
    else:
        return f"✗ Enum4linux failed:\\n{result['stderr']}"


# ============================================================================
# UTILITY FUNCTIONS
# ============================================================================

@mcp.tool()
def list_wordlists() -> str:
    """
    List available wordlists on the system.
    
    Returns:
        List of wordlist paths
    """
    wordlist_dirs = [
        "/usr/share/wordlists",
        "/usr/share/dirb/wordlists",
        "/usr/share/dirbuster/wordlists"
    ]
    
    output = "Available Wordlists:\\n\\n"
    
    for directory in wordlist_dirs:
        if os.path.exists(directory):
            cmd = ["find", directory, "-type", "f", "-name", "*.txt"]
            result = run_command(cmd)
            if result["success"]:
                output += f"\\n{directory}:\\n{result['stdout']}\\n"
    
    return output


@mcp.tool()
def get_disclaimer() -> str:
    """
    Get legal disclaimer and usage guidelines.
    
    Returns:
        Disclaimer text
    """
    return """
    ⚠️  LEGAL DISCLAIMER ⚠️
    
    This tool is provided for EDUCATIONAL PURPOSES ONLY.
    
    You must:
    ✓ Only use on systems you own or have explicit written permission to test
    ✓ Comply with all applicable local, state, and federal laws
    ✓ Understand that unauthorized access to computer systems is illegal
    ✓ Take full responsibility for your actions
    
    Unauthorized access to computer systems is a crime under:
    - Computer Fraud and Abuse Act (CFAA) in the United States
    - Computer Misuse Act in the United Kingdom
    - Similar laws in other jurisdictions
    
    The authors and contributors of this tool are not responsible for any
    misuse or damage caused by this software.
    
    USE AT YOUR OWN RISK!
    """


if __name__ == "__main__":
    # Print disclaimer on startup
    print(get_disclaimer())
    print("\\n" + "="*60)
    print("Kali MCP Server Starting...")
    print("="*60 + "\\n")
    
    # Run the MCP server
    mcp.run(transport="stdio")