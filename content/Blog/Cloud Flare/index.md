---
title: "Deploy Smarter, Not Harder: Cloudflare Tunnels for the Win"
Date: 2025-01-20
draft: false
tags:
  - Cloudflare
  - deployment
  - WebDev
  - advice
---
# **Cloudflare Tunnels: Securely Expose Local Applications to the Internet**

## **Introduction**

Over the past few months, I’ve been experimenting with setting up a small home lab, self-hosting various applications on my Raspberry Pi 4, and occasionally deploying my projects. Some of my favorite self-hosted applications include:

- **Nextcloud** – A powerful alternative to cloud storage services.
- **Jellyfin** – A feature-rich home media server.
- **VS Code Server** – A remote-accessible coding environment.

However, accessing these applications remotely presents a few challenges. Traditionally, you would need:

- A **public IP address**
- A **cloud or home server**

Using a public IP can be risky, as it exposes your home network to potential security threats. While renting a VPS from a cloud provider is an option, hosting high-storage and high-RAM applications like Nextcloud and Jellyfin can quickly become expensive. So, what’s the alternative?

Enter **Cloudflare Tunnels** – a secure way to expose local applications to the internet without needing a public IP.

---

## **How Cloudflare Tunnels Work**

Cloudflare Tunnels use a lightweight service called **Cloudflared** to create a secure, reverse tunnel between your local machine and Cloudflare’s global network. This allows you to expose applications on your local network to the public internet via a Cloudflare-managed domain, eliminating the need for port forwarding or a static IP.

![[0_X5p_GBelf4dnPcir.webp]]
### **Key Benefits:**

- No need for a public IP.
- Secure, encrypted connections.
- Easy configuration and management.
- Works with HTTP, SSH, RDP, and SMB traffic.

Here’s a simplified illustration of how Cloudflare Tunnels function:

```
[Local Application] → [Cloudflared] → [Cloudflare Edge] → [Public Internet]
```

Now, let’s set up our first tunnel!

---

## **Prerequisites**

To follow along, you’ll need:

1. A **domain** registered with Cloudflare.
2. Cloudflare **nameservers** configured for your domain.
3. A Cloudflare **Zero Trust account** (requires credit card verification).  

---

## **Installing Cloudflared**

Cloudflared is available on multiple platforms, including:

- **Linux** (AMD64, ARM, ARM64, x86)
- **Docker**
- **Windows**
- **macOS**


### **Installing on Linux**

Run the following command (replace `$ARCH` with your system’s architecture):

```
wget -q https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-linux-{$ARCH}.deb \
    && dpkg -i cloudflared-linux-{$ARCH}.deb
```

### **Authenticating Cloudflared**

Once installed, authenticate your Cloudflare account:

```
cloudflared tunnel login
```

This will open a browser window for you to authorize the domain you want to use for tunnels. After logging in, Cloudflare saves your credentials at:

```
/home/$USER/.cloudflared/cert.pem
```

---

## **Creating a Test Application (NGINX)**

To test our tunnel, let’s set up a simple NGINX server inside a Docker container.

### **Install Docker (if not already installed):**

```
sudo apt update && sudo apt install docker.io
```

### **Run NGINX inside a Docker container:**

```
docker run --name tunnel-nginx -p 5000:80 --detach nginx:latest
```

This command will:

- Pull the latest NGINX image (if not available locally).
- Name the container **tunnel-nginx**.
- Map **port 5000** on the host to **port 80** inside the container.
- Run the container in detached mode.

Verify the running container:

```
docker ps
```

Access NGINX at:

```
http://localhost:5000
```

---

## **Creating and Configuring the Cloudflare Tunnel**

### **Step 1: Create the Tunnel**

```
cloudflared tunnel create nginx-tunnel
```

This generates a credentials file and provides a **Tunnel ID**. Keep this file secure.

### **Step 2: Configure the Tunnel**

Create a config file at `/home/$USER/.cloudflared/nginx-tunnel.yml` with the following content:

```
---
tunnel: <UUID>
credentials-file: /home/$USER/.cloudflared/<UUID>.json
ingress:
  - hostname: tunnel.<your-domain>
    service: http://localhost:5000
  - service: http_status:404
```

Replace `<UUID>` with your Tunnel ID and `<your-domain>` with your actual domain.

### **Step 3: Create a Public DNS Record**

```
cloudflared tunnel route dns nginx-tunnel tunnel.<your-domain>
```

This will create a DNS record in Cloudflare that routes traffic through the tunnel.

---

## **Running the Tunnel**

To start the tunnel, run:

```
cloudflared tunnel --config /home/$USER/.cloudflared/nginx-tunnel.yml run
```

Your NGINX server should now be accessible via **https://tunnel****.** from the public internet!

---

## **Conclusion**

With Cloudflare Tunnels, we securely exposed our local NGINX server to the internet without opening ports or requiring a public IP. This method ensures better security and flexibility, allowing us to host applications remotely with ease.

Beyond basic use cases, Cloudflare Tunnels can also:

- Securely expose **SSH, RDP, or SMB** traffic.
- Protect entire private networks with **Cloudflare WARP**.
- Implement **Cloudflare Access** for granular security controls.

Start using **Cloudflare Zero Trust** today and explore the full potential of Cloudflare Tunnels!

---

### **Further Reading**

- Cloudflare Zero Trust Documentation
- Cloudflare Tunnel Guide




