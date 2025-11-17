FROM kalilinux/kali-rolling:latest

# Set environment variables
ENV DEBIAN_FRONTEND=noninteractive
ENV PYTHONUNBUFFERED=1

# Update and install essential tools
RUN apt-get update && apt-get upgrade -y && \
    apt-get install -y \
    # Core Kali tools
    kali-linux-core \
    # Network scanning
    nmap \
    masscan \
    # Web vulnerability scanners
    nikto \
    wpscan \
    # Directory/file brute forcing
    dirb \
    dirbuster \
    gobuster \
    # Exploitation tools
    sqlmap \
    metasploit-framework \
    # Exploit database
    exploitdb \
    # Web proxies
    burpsuite \
    # Password cracking
    hydra \
    john \
    hashcat \
    # Wireless tools
    aircrack-ng \
    reaver \
    # Enumeration
    enum4linux \
    smbclient \
    nbtscan \
    # DNS tools
    dnsrecon \
    dnsenum \
    fierce \
    # SSL/TLS testing
    sslscan \
    sslyze \
    # Vulnerability scanners
    openvas \
    # Web application tools
    whatweb \
    wafw00f \
    # Social engineering
    set \
    # Forensics
    binwalk \
    foremost \
    # Reverse engineering
    radare2 \
    # Network tools
    netcat-traditional \
    socat \
    tcpdump \
    wireshark \
    # Python and pip
    python3 \
    python3-pip \
    python3-dev \
    python3-venv \
    # Build tools
    git \
    wget \
    curl \
    vim \
    nano \
    # Additional utilities
    net-tools \
    iputils-ping \
    dnsutils \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Create non-root user with necessary capabilities
RUN useradd -m -s /bin/bash pentester && \
    mkdir -p /home/pentester/scans && \
    chown -R pentester:pentester /home/pentester

# Switch to pentester user for Python package installation
USER pentester
WORKDIR /home/pentester

# Create a virtual environment and install Python packages
RUN python3 -m venv /home/pentester/venv && \
    /home/pentester/venv/bin/pip install --upgrade pip && \
    /home/pentester/venv/bin/pip install --no-cache-dir \
    fastmcp \
    pydantic \
    python-nmap \
    requests \
    beautifulsoup4

# Copy MCP server code
COPY --chown=pentester:pentester server.py /home/pentester/server.py
COPY --chown=pentester:pentester requirements.txt /home/pentester/requirements.txt

# Update exploitdb (needs to be done as root, so we'll do it in entrypoint)
# Create an entrypoint script
USER root
RUN echo '#!/bin/bash\nsearchsploit -u 2>/dev/null || true\nsu - pentester -c "cd /home/pentester && /home/pentester/venv/bin/python server.py"' > /entrypoint.sh && \
    chmod +x /entrypoint.sh

# Switch back to pentester user
USER pentester

# Expose MCP server port
EXPOSE 8000

# Run the MCP server using the virtual environment
ENTRYPOINT ["/entrypoint.sh"]