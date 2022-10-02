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
2. Create roles to access the index:<br/>
a. **admin**: This role has full access to index `amatsa` and kibana<br/>
b. **analyst**: This role has read access to index `amatsa` and kibana<br/>
c. **agent**: This role has write access to index `amatsa`<br/>
```
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
```
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
```
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
```
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

## 💻 Client
