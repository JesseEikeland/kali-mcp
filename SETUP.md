# 🚀 Quick Setup Guide

## Step 1: Prerequisites

Install Docker and Docker Compose:

### Ubuntu/Debian
```bash
sudo apt-get update
sudo apt-get install docker.io docker-compose
sudo usermod -aG docker $USER
# Log out and back in
```

### macOS
```bash
# Install Docker Desktop from docker.com
brew install docker docker-compose
```

### Windows
- Install Docker Desktop for Windows
- Enable WSL2
- Install Ubuntu from Microsoft Store

## Step 2: Clone and Build

```bash
git clone https://github.com/JesseEikeland/kali-mcp.git
cd kali-mcp
docker-compose build
```

⏰ This will take 10-15 minutes depending on your internet speed.

## Step 3: Start the Server

```bash
docker-compose up -d
```

## Step 4: Access the Container

```bash
docker-compose exec kali-mcp bash
```

## Step 5: Test a Tool

Inside the container:

```bash
# Test nmap
nmap -sV scanme.nmap.org

# Test search exploit
searchsploit wordpress

# List wordlists
ls /usr/share/wordlists/
```

## Step 6: Run the MCP Server

```bash
python3 server.py
```

## Testing with Claude

Once the server is running, you can interact with it through Claude using MCP tools!

Example commands:
```
"Use nmap_scan to scan 192.168.1.1"
"Search exploits for Apache 2.4.49"
"Run nikto scan on http://testsite.local"
```

## Troubleshooting

### Can't build container
```bash
# Clear Docker cache
docker system prune -a
docker-compose build --no-cache
```

### Permission denied
```bash
sudo chown -R $USER:$USER .
```

### Tools not working
```bash
# Update packages
docker-compose exec kali-mcp apt-get update
docker-compose exec kali-mcp searchsploit -u
```

## Safety Tips

✅ **DO:**
- Use on your own lab network
- Test on HackTheBox/TryHackMe
- Get written permission before testing

❌ **DON'T:**
- Scan without permission
- Test production systems
- Attack public infrastructure

## Next Steps

1. Set up a lab environment (VirtualBox VMs)
2. Try HackTheBox: https://www.hackthebox.com
3. Watch NetworkChuck tutorials
4. Practice on intentionally vulnerable VMs

Happy (ethical) hacking! 🎯