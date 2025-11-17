# 🔐 Kali MCP Server

**Model Context Protocol (MCP) server with comprehensive Kali Linux penetration testing tools.**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=flat&logo=docker&logoColor=white)](https://www.docker.com/)
[![Kali Linux](https://img.shields.io/badge/Kali-268BEE?style=flat&logo=kalilinux&logoColor=white)](https://www.kali.org/)

## ⚠️ LEGAL DISCLAIMER

**THIS TOOL IS FOR EDUCATIONAL PURPOSES ONLY!**

✓ Only use on systems you own or have explicit written permission to test  
✓ Comply with all applicable laws and regulations  
✓ Understand that unauthorized access to computer systems is illegal  
✓ Take full responsibility for your actions  

**Unauthorized access to computer systems is a crime.** Use at your own risk!

---

## 🚀 Features

This MCP server provides access to 20+ professional penetration testing tools:

### 🌐 Network Scanning
- **nmap** - Network mapper and port scanner
- **masscan** - Ultra-fast port scanner

### 🕷️ Web Vulnerability Scanners
- **nikto** - Web server vulnerability scanner
- **wpscan** - WordPress security scanner
- **whatweb** - Web technology identifier
- **wafw00f** - Web Application Firewall detector

### 📂 Directory/File Enumeration
- **dirb** - Directory brute forcer
- **gobuster** - Fast directory/DNS/vhost brute forcer

### 💉 Exploitation Tools
- **sqlmap** - SQL injection detection and exploitation
- **searchsploit** - Exploit database search

### 🔍 DNS Enumeration
- **dnsrecon** - DNS enumeration and scanning
- **dnsenum** - DNS enumeration tool

### 🔒 SSL/TLS Testing
- **sslscan** - SSL/TLS configuration tester

### 🔓 Password Cracking
- **hydra** - Network login brute forcer
- **john** - John the Ripper password cracker
- **hashcat** - Advanced password recovery

### 🦠 Windows/SMB Enumeration
- **enum4linux** - Windows and Samba enumeration

### 📡 Additional Tools
- Metasploit Framework
- Burp Suite
- Aircrack-ng suite
- And many more!

---

## 📦 Installation

### Prerequisites

- Docker and Docker Compose installed
- At least 4GB of free disk space
- Linux/macOS or Windows with WSL2

### Quick Start

1. **Clone the repository:**

```bash
git clone https://github.com/JesseEikeland/kali-mcp.git
cd kali-mcp
```

2. **Build the Docker container:**

```bash
docker-compose build
```

⏰ This will take 10-15 minutes as it downloads and installs all tools.

3. **Start the server:**

```bash
docker-compose up -d
```

4. **Access the container:**

```bash
docker-compose exec kali-mcp bash
```

5. **Run the MCP server:**

```bash
python3 server.py
```

---

## 🛠️ Usage

### Available MCP Tools

#### 🌐 Network Scanning

```python
# Basic nmap scan
nmap_scan(target="192.168.1.1", scan_type="basic")

# Full port scan
nmap_scan(target="example.com", scan_type="full")

# Vulnerability scan
nmap_scan(target="192.168.1.1", scan_type="vuln")

# Fast masscan
masscan_scan(target="192.168.1.0/24", ports="1-1000", rate=1000)
```

#### 🕷️ Web Scanning

```python
# Nikto web scan
nikto_scan(target="http://example.com", ssl=False)

# WordPress scan
wpscan_scan(target="http://example.com", enumerate="vp,vt,u")

# Identify web technologies
whatweb_scan(target="http://example.com", aggression=1)

# Detect WAF
wafw00f_detect(target="http://example.com")
```

#### 📂 Directory Brute Force

```python
# Dirb scan
dirb_scan(target="http://example.com")

# Gobuster directory scan
gobuster_scan(target="http://example.com", mode="dir")

# Gobuster DNS enumeration
gobuster_scan(target="example.com", mode="dns")
```

#### 💉 SQL Injection Testing

```python
# Basic SQLMap scan
sqlmap_scan(target="http://example.com/page?id=1")

# With POST data
sqlmap_scan(target="http://example.com/login", data="username=admin&password=test")

# With cookies
sqlmap_scan(target="http://example.com/page", cookie="PHPSESSID=abc123")
```

#### 🔍 Exploit Search

```python
# Search for exploits
searchsploit_search(query="wordpress")

# Exact match search
searchsploit_search(query="Apache 2.4.49", exact=True)
```

#### 🌐 DNS Enumeration

```python
# DNS reconnaissance
dnsrecon_scan(domain="example.com", scan_type="std")

# DNS enumeration
dnsenum_scan(domain="example.com")
```

#### 🔒 SSL/TLS Testing

```python
# Test SSL configuration
sslscan_test(target="example.com:443")
```

#### 🔓 Password Cracking

```python
# Brute force SSH
hydra_bruteforce(
    target="192.168.1.1",
    service="ssh",
    username="admin",
    wordlist="/usr/share/wordlists/rockyou.txt"
)
```

#### 🦠 SMB/Windows Enumeration

```python
# Enumerate Windows/Samba
enum4linux_scan(target="192.168.1.1")
```

#### 🔧 Utility Functions

```python
# List available wordlists
list_wordlists()

# Get legal disclaimer
get_disclaimer()
```

---

## 🏗️ Architecture

```
kali-mcp/
├── Dockerfile              # Kali Linux container with all tools
├── docker-compose.yml      # Container orchestration
├── server.py               # FastMCP server with tool wrappers
├── requirements.txt        # Python dependencies
├── README.md              # This file
├── SETUP.md               # Quick setup guide
├── LICENSE                # MIT License
├── .gitignore             # Git ignore rules
├── scans/                 # Scan results (created on first run)
└── wordlists/             # Custom wordlists (optional)
```

### How It Works

1. **Docker Container**: Runs Kali Linux with all penetration testing tools installed
2. **MCP Server**: Python FastMCP server wraps each tool with safe input sanitization
3. **Non-Root User**: Runs as `pentester` user with minimal required capabilities
4. **Input Sanitization**: All inputs are sanitized to prevent command injection
5. **Timeouts**: Commands have configurable timeouts to prevent hanging

---

## 🔒 Security Features

- ✓ Runs as non-root user (`pentester`)
- ✓ Input sanitization on all parameters
- ✓ Command injection prevention
- ✓ Timeout limits on all operations
- ✓ No new privileges security option
- ✓ Resource limits (CPU/Memory)
- ✓ Minimal required capabilities (NET_RAW, NET_ADMIN)

---

## 🎓 Learning Resources

### Recommended Platforms

- **[HackTheBox](https://www.hackthebox.com/)** - Hands-on pentesting labs
- **[TryHackMe](https://tryhackme.com/)** - Guided learning paths
- **[PentesterLab](https://pentesterlab.com/)** - Web pentesting exercises
- **[VulnHub](https://www.vulnhub.com/)** - Vulnerable VMs for practice

### Books

- "The Web Application Hacker's Handbook" by Dafydd Stuttard
- "Penetration Testing" by Georgia Weidman
- "The Hacker Playbook 3" by Peter Kim

### YouTube Channels

- NetworkChuck
- IppSec
- John Hammond
- The Cyber Mentor

---

## 🐛 Troubleshooting

### Container won't start

```bash
# Check logs
docker-compose logs kali-mcp

# Rebuild container
docker-compose down
docker-compose build --no-cache
docker-compose up -d
```

### Permission errors

```bash
# Fix scan directory permissions
sudo chown -R $USER:$USER ./scans
```

### Tools not found

```bash
# Update package lists
docker-compose exec kali-mcp apt-get update

# Install missing tool
docker-compose exec kali-mcp apt-get install -y <tool-name>
```

---

## 📝 Configuration

### Environment Variables

Edit `docker-compose.yml` to customize:

```yaml
environment:
  - MAX_TIMEOUT=300        # Maximum command timeout (seconds)
  - SCAN_RESULTS_DIR=/home/pentester/scans
```

### Custom Wordlists

Place your wordlists in the `./wordlists` directory:

```bash
mkdir -p wordlists
cp /path/to/custom.txt wordlists/
```

---

## 🤝 Contributing

Contributions are welcome! Please:

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

---

## 📄 License

MIT License - See [LICENSE](LICENSE) file for details

**Important**: This license applies to the code only. You are solely responsible for how you use this software.

---

## ⚖️ Legal Notice

**READ THIS CAREFULLY:**

This tool is provided for **educational and authorized testing purposes only**.

By using this software, you agree that:

1. You will only use it on systems you own or have explicit written authorization to test
2. You understand that unauthorized computer access is illegal
3. You take full responsibility for your actions
4. The authors and contributors are not liable for any misuse or damage

**Always get written permission before testing!**

---

## 🙏 Acknowledgments

- **Kali Linux Team** - For the amazing pentesting distribution
- **FastMCP** - For the MCP server framework
- **Tool Authors** - For creating these incredible security tools
- **NetworkChuck** - For inspiring this project

---

## 📞 Support

- **Issues**: [GitHub Issues](https://github.com/JesseEikeland/kali-mcp/issues)
- **Discussions**: [GitHub Discussions](https://github.com/JesseEikeland/kali-mcp/discussions)

---

## 🗺️ Roadmap

- [ ] Add Metasploit integration
- [ ] Web UI for easier interaction
- [ ] Report generation (PDF/HTML)
- [ ] Automated vulnerability chains
- [ ] Integration with CVE databases
- [ ] Custom scan profiles
- [ ] Scheduled scanning
- [ ] Multi-target support

---

**Remember: With great power comes great responsibility. Use wisely! 🦸**

---

**Made with ❤️ for the security community**