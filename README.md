# 🖥 AMATSA
[![Build](https://github.com/VSangarya/AMATSA/actions/workflows/build.yml/badge.svg)](https://github.com/VSangarya/AMATSA/actions/workflows/build.yml)
[![GitHub release (latest by date)](https://img.shields.io/github/v/release/VSangarya/AMATSA?display_name=tag)](https://github.com/VSangarya/AMATSA/releases)
[![Codacy Badge](https://app.codacy.com/project/badge/Coverage/4d32b2c8032341409d0f8a73a1b2a3d1)](https://www.codacy.com/gh/VSangarya/AMATSA/dashboard?utm_source=github.com&utm_medium=referral&utm_content=VSangarya/AMATSA&utm_campaign=Badge_Coverage)
[![Codacy Badge](https://app.codacy.com/project/badge/Grade/4d32b2c8032341409d0f8a73a1b2a3d1)](https://www.codacy.com/gh/VSangarya/AMATSA/dashboard?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=VSangarya/AMATSA&amp;utm_campaign=Badge_Grade)
[![Commit Acitivity](https://img.shields.io/github/commit-activity/w/VSangarya/AMATSA)](https://github.com/VSangarya/AMATSA/pulse)
[![Issues](https://img.shields.io/github/issues/VSangarya/AMATSA?color=red)](https://github.com/VSangarya/AMATSA/issues)
[![Contributors](https://img.shields.io/github/contributors/VSangarya/AMATSA)](https://github.com/VSangarya/AMATSA/graphs/contributors)
[![License](https://img.shields.io/github/license/VSangarya/AMATSA)](LICENSE)
![Languages](https://img.shields.io/github/languages/count/VSangarya/AMATSA)
[![Code Size](https://img.shields.io/github/languages/code-size/VSangarya/AMATSA)](src)
[![Contributor Covenant](https://img.shields.io/badge/Contributor%20Covenant-2.1-4baaaa.svg)](CODE-OF-CONDUCT.md)
[![Repo Size](https://img.shields.io/github/repo-size/VSangarya/AMATSA)](https://github.com/VSangarya/AMATSA/)

Have you ever reported to your organization's IT team that your machine is slow or running out of disk space? Well, I guess most of us have done this at some point. What if your IT team can be proactive and give you a new disk (or a new asset to meet your workload!) before you even go to them?

Asset Monitoring and Analytics Tool for sysadmins (we call it AMATSA) is a client-based solution for system administrators to monitor assets in their organization. amatsa-client is cross-platform (Linux, Windows, macOS), can be installed on a server/user PC and takes less than 50MB of disk space at runtime. Once you install the amatsa-client on a host, it will periodically send system metrics (asset info, cpu/memory utilization, network etc.) to the backend server. The backend server runs on Elasticsearch and can be hosted on-premise or in the cloud. Sysadmins can then import our [pre-built](data/kibana/dashboard.ndjson) Kibana dashboard or build custom visualization on top of raw data sent by the clients.

## 📖 Usecases
*  Gather asset information - how many assets are there in the organization, specification of each asset etc.
*  Monitor assets that haven't rebooted in a while to apply security patches.
*  Monitor assets that have high CPU/memory utilization over time.
*  Monitor assets running out of disk space.
*  Monitor network speed of assets across the organization.

## Workflow and 'How to Do Stuff'
* The architecure of the system is shown below:
![System Architecture](assets/system_architecture.jpg)
    * The script installed at the client side collects client metrics and at fixed intervals and pushes these metrics as a JSON to the elastic server.
    * Kibana is connected to the Elastic Server from where it fetches the data and renders this data in the dashboards accessible by system administrators.
    * This update happens in realtime.

* To use the system: 

    * Follow the steps in [Installation](README.md#🛠-installation).

    * Adding new metrics:
        * You can make changes to the classes in the 'src' directory to track additional metrics or   remove metrics that are currently tracked.
        * Leverage Kibana's convenient UI to create new dashboards as per your requirements.

    * View dashboards:
        * Access your AWS server using your browser.
        * Enter your Kibana credentials to view the dashboards.

## 🛠 Installation
*  See [server installation](INSTALL.md#-server) instructions to setup Elasticsearch and Kibana.
*  See [client installation](INSTALL.md#-client) instructions to deploy amatsa-client on assets.
*  Once the server and the clients are setup, you can import and explore our pre-built Kibana dashboards.

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
