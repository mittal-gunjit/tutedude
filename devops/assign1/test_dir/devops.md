# DevOps

## Major Topics
- [DevOps](#devops)
  - [Major Topics](#major-topics)
    - [CI/CD](#cicd)
    - [Containerization](#containerization)
    - [Linux](#linux)
    - [Databases](#databases)
    - [Cloud](#cloud)
      - [Providers](#providers)
      - [Common Services](#common-services)
    - [Networking](#networking)
    - [Programming Languages](#programming-languages)
  - [Questions:](#questions)

### CI/CD

CircleCI, Jenkins, Github Actions, GitLab CI, ArgoCD, etc.

### Containerization

Docker, k8s, microservices architecture and deployment.

### Linux

Bash Scripting, CLI familiarity, several different cli tools

### Databases

MySql, Postgres, MongoDB, ElasticSearch, Redis etc.

### Cloud

#### Providers

AWS, Azure, GCP, Terraform

#### Common Services

Virtual Machines, cloud hosted databases, storage solutions, DNS, VPC, Container Runtimes, Kubernetes, ETL.

### Networking

DNS, Ingress, Nginx, reverse proxy, SSL, SSH, VM, Message Queues, Async Tasking, IPV4.

### Programming Languages

Python, JavaScript, C/C++, Java, Golang, Scala.

## Questions:

* * *
Name a few CI/CD tools.

CircleCI, Jenkins, Github Actions, GitLab CI, ArgoCD, Chef, Puppet.
* * *
What are multi stage dockerfiles and how will you share data between different stages.

multi stage dockerfiles are those which have more than one base image, i.e, they are built on top of atleast two base images, and the way that data is shared is such that, each stage is given an alias, and in the other stage u can reference a previous stage by the alias, i.e, ```--from=alias```
* * *
How will you check if a webiste is up or not using CLI tools or a Bash Script

Use any http tool like curl, wget, ping, etc. if the content returned is correct, then the webiste is up, else the command would return a 404 not found error
* * *
How will you make a bash script executable and how will you schedule the script run at a given time everyday.

```chmod +x script.sh```, this will make the script executable, and scheduling can be done by any tools, like hickory, crontab, etc.
* * *
Preferred DB - SQL or NoSQL.

SQL databases: Mysql, Postgres, MariaDB and more

NOSQL databases: MongoDB Redis Cassandra Elasticsearch Firebase
* * *
How will you connect to a Postgres DB using the CLI

using a CLI tool called PSQL which takes in different parameters such as host ip, username, password, port, database name.
* * *
What are Docker Tags?

Tags are used to implement a versioning system to docker images, usually they will look like, ```nginx:1.19.1``` , here 1.19.1 is the tag, tags come after a semicolon
* * *
How will you log onto a VM hosted on the cloud

using a ssh client tool, linux has the default ssh tool, windows has putty, both require a private key file, named either .pem or .ppk
* * *
Can two VMs that are in different regions talk to each other.

Not by default, but you can establish a connection using a VPN gateway.
* * *
How will you run docker images on any cloud provider.

AWS - ECS, apprunner, EKS, EC2
Azure - Container instances, AKS, Azure VMs
GCP - Cloud Run, GKE, GCP Compute instances
* * *
Name some popular data transformation and big data frameworks

Hadoop, pyspark, AWS Glue, or just basic pandas
* * *
Why is kubernetes even required?

To orchestrate the running, managing and configuring of docker containers using a single control plane.
* * *
Difference between A records and CNAME records

A records point to ipv4 addresses
CNAME records point to another DNS entry.
* * *
What is a reverse proxy

When one common IP address or host name redirects to different endpoints for different hostname headers, it is called a reverse proxy.
* * *
How will you implement a Task Queue, in any programming language

3rd party tools - Kafka, spark, rabbit mq, redis, AWS SQS
or any language specific library like celery for python
* * *
Difference between IPV4 and IPV6

IPV4 is the original standard with 4 dot pattern like 192.187.54.1
IPV6 is the new paradigm which has a 6 semicolon pattern, like 2404:6800:4007:828::200e

IPv4 will only have numbers upto 255 per dot
IPv6 can have numbers and letters in any format
* * *
How will insert a CSV file into a postgres table using python

Import CSV using pandas, connect to a postgres instance using pyscopg2 and use pandas.sql.io library or custom format data to match sql standards
* * *
what are list comprehensions

these are one-liners that can transform a list to a another state, taking a lambda function, or regular function or basic arithmetic function as input, these can also have conditional foramtting.
* * *
Any other programming question if required.