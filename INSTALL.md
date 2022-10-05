# 🧰 Installation

## 🚀 Server
### Setup Elasticsearch + Kibana
Elasticsearch and Kibana is easy to setup on any OS platorm - Linux, Darwin or Windows. Our project uses v8.4 for both Elasticsearch and Kibana.
We setup both Elasticsearch and Kibana on a Ubuntu 22.04 LTS VM with the following specifications:
* CPU: 2vCPU
* RAM: 2GB
* Disk: 60GB

1. Refer instructions to [install](https://www.elastic.co/guide/en/elasticsearch/reference/8.4/install-elasticsearch.html) Elasticsearch.
2. Refer instructions to [install](https://www.elastic.co/guide/en/kibana/current/install.html) Kibana.

If you want to skip the official documentation and quickly get hands-on, simply follow [this](https://std.rocks/gnulinux_siem_01_install_v8.html) for a quick setup!

### Create Index, Roles and Users
1. Access Kibana from your browser at https://<ip-address:port-number> and login with the built-in account `elastic`. Navigate to Management and then Dev Tools.

2. Create index *amatsa*
`PUT /amatsa`

3. Create roles to access the index:<br/>
a. **admin**: This role has full access to index `amatsa` and kibana<br/>
b. **analyst**: This role has read access to index `amatsa` and kibana<br/>
c. **agent**: This role has write access to index `amatsa`<br/>
```Text
POST _security/role/admin
{
  "indices": [
    {
      "names": [
        "amatsa"
      ],
      "privileges": [
        "*",
      ],
      "allow_restricted_indices": false
    }
  ],
  "applications": [
    {
      "application": "kibana-.kibana",
      "privileges": [
        "*"
      ],
      "resources": [
        "*"
      ]
    }
  ]
}
```
```Text
POST _security/role/analyst
{
  "indices": [
    {
      "names": [
        "amatsa"
      ],
      "privileges": [
        "read",
        "monitor"
      ],
      "allow_restricted_indices": false
    }
  ],
  "applications": [
    {
      "application": "kibana-.kibana",
      "privileges": [
        "read"
      ],
      "resources": [
        "*"
      ]
    }
  ]
}
```
```Text
POST _security/role/agent
{
  "indices": [
    {
      "names": [
        "amatsa"
      ],
      "privileges": [
        "write"
      ]
    }
  ]
}
```
4. Create one user account for each of the roles created
```Text
POST _security/user/<username>
{
  "roles": [
    <one-of-the-created-roles>
  ],
  "full_name": "Account Name",
  "email": "mail@example.com",
  "password": "password"
}
```
5. Setup [runtime fields](data/index/runtime_fields.md) for your index after installing one client.

## 💻 Client
Setting up the client is very easy! 😉 Yes, we took care of that!!! The client is a python script that sends updates about system metrics to your Elasticsearch every X mins. We don't tamper your client's Python installations. We setup our own virtual environments and execute inside that. We use the task scheduler (or cronjob) to schedule the client scripts to run.
### Prerequisites
*   Python 3.10+ (symlinked to python)
### Steps
1.  Download or clone this repository and cd to the cloned directory.
2.  Clients use the YAML file in `src/config/amatsa-client.yml` to read configuration. **You should change these parameters depending on how you are setting up the Elasticsearch server**. Configuration includes:
*   version: For client version tracking. You can leave this as it is!
*   endpoint: Elasticsearch endpoint used by client used to push collected data. Give the HTTPS endpoint where your Elasticsearch is running. Elasticsearch v8.4 uses TLS by default and it is **recommended** to not downgrade to HTTP.
*   tls-fingerprint: To verify authenticity of Elasticsearch server. The tls-fingerprint can be retrieved from the Elasticsearch server using this command:
```Text
openssl x509 -fingerprint -sha256 -in /etc/elasticsearch/certs/http_ca.crt
```
*   username, password: Authentication to write to Elasticsearch. This is the client username and password you configured for role `agent`.
*   index: Document will be written to this index in Elasticsearch. **Tip**: To skip this step altogether, you can edit this config file before deploying the repository to clients!
3.  Take ownership of script deploy.sh using `chmod +x deploy.sh`
4.  If you want the metric collection to happen every 30 mins, you should run `./deploy.sh 30`. Pass a value of X to the deploy.sh script depending on the client workload and how frequently you want to update.
5.  Your client should be up and running by now!

To uninstall, simply delete the scheduled task and remove the repository.