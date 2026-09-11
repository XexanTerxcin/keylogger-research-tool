# Keylogger Research Lab

> ⚠️ **Educational & Authorized Security Research Project**

A Python-based keylogging research tool developed from scratch to study how keyboard event monitoring, local telemetry collection, asynchronous processing, and HTTP-based communication can be implemented in a controlled security laboratory.

The project was created as part of my hands-on exploration of **offensive security, red-team techniques, Python security tooling, and endpoint telemetry**.

---

## ⚠️ Disclaimer

This project is intended **strictly for educational purposes, authorized penetration testing, security research, and controlled laboratory environments**.

Do not deploy or use this software on computers, accounts, or networks without explicit authorization from the owner.

The author is not responsible for misuse of this project.

---

## 🎯 Project Goals

The main objective of this project was to understand the technical building blocks behind keylogging and telemetry collection rather than relying on existing tools.

The project explores:

* Keyboard event monitoring
* Background processing
* Thread-safe queues
* Local telemetry storage
* System identification
* HTTP communication
* Remote telemetry collection
* Timestamped event logging
* Basic endpoint data collection

---

## 🧠 Architecture

```text
                 ┌─────────────────────┐
                 │   Keyboard Events   │
                 └──────────┬──────────┘
                            │
                            ▼
                 ┌─────────────────────┐
                 │   Event Listener    │
                 └──────────┬──────────┘
                            │
                            ▼
                 ┌─────────────────────┐
                 │   Input Buffer      │
                 └──────────┬──────────┘
                            │
                     Queue / Thread
                            │
                ┌───────────┴───────────┐
                ▼                       ▼
       ┌─────────────────┐     ┌─────────────────┐
       │  Local Logging  │     │ HTTP Telemetry  │
       │   TXT File      │     │    Endpoint     │
       └─────────────────┘     └─────────────────┘
```

---

## 🛠️ Technologies

* **Python 3**
* `pynput` — keyboard event monitoring
* `requests` — HTTP communication
* `threading` — background processing
* `queue` — thread-safe task handling
* `socket` — hostname/IP information
* `uuid` — machine identification
* `tempfile` — temporary directory handling

---

## ✨ Features

### Keyboard Event Monitoring

Captures keyboard events and handles printable and selected special keys.

### Asynchronous Processing

Keyboard events are placed into a thread-safe queue and processed by a background worker.

This prevents network operations from directly blocking the keyboard listener.

### System Identification

The tool can associate collected telemetry with basic system information such as:

* Machine identifier
* Hostname
* Username
* Local IP address
* Timestamp

### Local Telemetry

Collected data can be written to a timestamped local log file for laboratory analysis.

### HTTP Telemetry

The research version demonstrates how collected telemetry can be transmitted to a configured HTTP endpoint.

---

## 📂 Project Structure

```text
keylogger-research-lab/
├── keylogger.py
├── README.md
└── requirements.txt
```

---

## 🚀 Installation

Clone the repository:

```bash
git clone https://github.com/XexanTerxcin/keylogger-research-tool.git
cd keylogger-research-tool
```

Install the dependencies:

```bash
pip install -r requirements.txt
```

Example `requirements.txt`:

```text
pynput
requests
```

---

## 🧪 Laboratory Usage

Run the program only inside an environment you own or have explicit authorization to test.

A suitable environment could be:

```text
Host Machine
     │
     ├── Windows Test VM
     │
     └── Linux Test VM
```

For safe experimentation, use **synthetic test input and dummy data** rather than real passwords, credentials, private messages, or other sensitive information.

---

## 🔐 Security Considerations

Keylogging is a highly sensitive capability because keyboard input can contain:

* Passwords
* Authentication codes
* Private messages
* API keys
* Personal information

For this reason, this project should never be used to monitor another person's device without explicit authorization.

When publishing or modifying this project:

* Never commit credentials.
* Never commit captured keyboard logs.
* Never publish private API endpoints.
* Never include real authentication tokens.
* Use an isolated laboratory environment.
* Use synthetic data whenever possible.

---

## 📚 What I Learned

This project helped me understand several practical concepts:

* Event-driven programming
* Python concurrency
* Producer/consumer architecture
* Thread synchronization
* HTTP POST requests
* System information gathering
* Local telemetry collection
* Remote telemetry architecture
* Error handling
* Security implications of endpoint monitoring

More importantly, it helped me understand how seemingly small components can be combined into a complete security tool.

---

## 👨‍💻 Author

**Sk Md Yahya**

Computer Science & Engineering student and technology enthusiast exploring:

* Cybersecurity
* Red Teaming
* Linux
* Python
* Electronics
* Networking
* Gaming Technology

---

## ⚖️ Responsible Use

Security knowledge is powerful.

Use it to **learn, test, secure, and improve systems — not to compromise people.**
