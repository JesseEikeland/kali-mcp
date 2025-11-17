# 🚀 Using custom.yaml with MCP

This guide shows you how to add the kali-mcp server to your MCP configuration using the included `custom.yaml` file.

## What is custom.yaml?

The `custom.yaml` file is a configuration file that tells the MCP (Model Context Protocol) system about your custom server. It includes:
- Server metadata (name, description, tools)
- Tool definitions
- Docker image information
- Tags and categories

## Setup Instructions

### Step 1: Build Your Docker Image

First, make sure you've built the Docker image:

```bash
cd kali-mcp
docker-compose build
```

This creates the image: `kali-mcp-server:latest`

### Step 2: Locate Your MCP Configuration Directory

The location depends on your system:

**Linux/macOS:**
```bash
~/.config/mcp/
```

**Windows:**
```
%APPDATA%\mcp\
```

### Step 3: Copy custom.yaml

Copy the `custom.yaml` file to your MCP configuration directory:

**Linux/macOS:**
```bash
mkdir -p ~/.config/mcp
cp custom.yaml ~/.config/mcp/custom.yaml
```

**Windows (PowerShell):**
```powershell
New-Item -ItemType Directory -Force -Path "$env:APPDATA\mcp"
Copy-Item custom.yaml "$env:APPDATA\mcp\custom.yaml"
```

### Step 4: Start the Docker Container

Make sure your kali-mcp container is running:

```bash
docker-compose up -d
```

### Step 5: Verify in Claude

The kali-mcp server should now be available in Claude Desktop or other MCP-enabled applications!

You can verify by asking Claude:
```
"What MCP servers are available?"
```

or

```
"Use the kali-mcp server to scan a target"
```

## Available Tools

Once configured, you'll have access to these tools through Claude:

### Network Scanning
- `nmap_scan` - Network mapping and port scanning
- `masscan_scan` - Fast port scanning

### Web Scanning
- `nikto_scan` - Web vulnerability scanning
- `wpscan_scan` - WordPress security scanning
- `whatweb_scan` - Web technology identification
- `wafw00f_detect` - WAF detection

### Directory Enumeration
- `dirb_scan` - Directory bruteforcing
- `gobuster_scan` - Fast directory/DNS enumeration

### Exploitation
- `sqlmap_scan` - SQL injection testing
- `searchsploit_search` - Exploit database search

### DNS Enumeration
- `dnsrecon_scan` - DNS reconnaissance
- `dnsenum_scan` - DNS enumeration

### Security Testing
- `sslscan_test` - SSL/TLS testing
- `hydra_bruteforce` - Password bruteforcing
- `enum4linux_scan` - SMB/Windows enumeration

### Utilities
- `list_wordlists` - List available wordlists
- `get_disclaimer` - Show legal disclaimer

## Example Usage with Claude

Once set up, you can ask Claude things like:

```
"Use nmap_scan to scan scanme.nmap.org with a basic scan"
```

```
"Search for WordPress exploits using searchsploit_search"
```

```
"Run a nikto scan on http://testsite.local"
```

## Troubleshooting

### Server not showing up?

1. **Check Docker is running:**
   ```bash
   docker ps | grep kali-mcp
   ```

2. **Verify custom.yaml location:**
   ```bash
   ls -la ~/.config/mcp/custom.yaml
   ```

3. **Check YAML syntax:**
   ```bash
   # Install yamllint if needed
   yamllint custom.yaml
   ```

4. **Restart Claude Desktop/Application**

### Container issues?

```bash
# Check container logs
docker-compose logs kali-mcp

# Restart container
docker-compose restart
```

## Custom Configuration

You can edit `custom.yaml` to customize:

- **Server name**: Change `kali-mcp` to your preferred name
- **Description**: Update the description text
- **Tools**: Add or remove tools from the list
- **Tags**: Add custom tags for organization
- **Category**: Change from "automation" to "productivity", "monitoring", etc.

## Security Notes

Remember:
- ⚠️ Only use on systems you own or have permission to test
- 🔒 Keep your lab isolated from production networks
- 📋 Always get written authorization before testing
- 🎓 Use for learning and authorized testing only

## Additional Resources

- [MCP Documentation](https://modelcontextprotocol.io/)
- [Claude Desktop](https://claude.ai/desktop)
- [Kali Linux Docs](https://www.kali.org/docs/)
- [NetworkChuck on YouTube](https://www.youtube.com/@NetworkChuck)

---

**Happy (ethical) hacking! 🎯**