# 🖥 AMATSA
Asset Monitoring and Analytics Tool for System Administrators

## 👩🏼‍💻 🚀 Developer Environment Setup

### Prerequisites
1. Python 3.10+
2. VS Code (to make collaboration easier. We don't want to argue over tabs vs spaces!)

### Setup
1. Spawn terminal and change working directory to repo directory.
2. Create virtual environment using venv: `path/to/python -m venv .venv`
3. Activate virtual environment:<br/>
Linux/MacOS:  `source .venv/bin/activate`<br/>
Windows:  `source .venv/Scripts/activate`<br/>
4. Install Python dependencies
`pip install -r requirements.txt`

## 💻 Python Client

See [client installation](INSTALL.md#-client) instructions.

1. Clients use the YAML file in `src/config/amatsa-client.yml` to read configuration. Configuration includes:
* version - client version
* endpoint - elastic endpoint client uses to push collected data
* tls-fingerprint - verify authenticity of Elasticsearch server
* username, password - authentication to write to Elasticsearch
* index - index where document will be written in Elasticsearch