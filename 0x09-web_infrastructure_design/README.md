# [0. Simple web stack]()
# [1. Distributed web infrastructure](https://github.com/OmarDouiba/alx-system_engineering-devops/blob/master/0x09-web_infrastructure_design/1-distributed_web_infrastructure)
In our Infrastructure Design, we have a load balancer and 3 servers. Each server has a web server of type Nginx, an application server, and a database server. 

### Web Server (Nginx):
We use Nginx to handle HTTP requests coming from users. It serves static web pages and also sends dynamic requests to the application server if needed.

### Application Server:
The application server is used to execute the application logic, process dynamic content, and serve data from the database.

### Database (MySQL):
MySQL is used to store and retrieve data for the application.

Load Balancer:
The load balancer distributes incoming traffic across multiple servers to improve performance and reliability.

When a user sends requests for the HTTP webpage (foobar.com) to the browser, the browser sends the request to the DNS through the ISP. After checking their caches and asking for the IP address of the website, it returns with 8.8.8.8. This IP is then sent to a located server through the internet and hits the load balancer. The load balancer sends this request to the first server, and the response is sent back to the user with static or dynamic content depending on the request.

## For every additional element, why are you adding it?

We added a server to prevent a single point of failure.
The load balancer is added to distribute incoming traffic and prevent a single point of failure.
Database (Primary-Replica) is added to enhance database reliability and provide data redundancy.
What distribution algorithm is your load balancer configured with and how does it work?
My load balancer uses the Round Robin algorithm, working in a cyclic way by distributing traffic evenly between each server. It is simple and especially effective if our servers have the same capacity.

## Is your load-balancer enabling an Active-Active or Active-Passive setup, explain the difference between both?
The load balancer uses an active-active setup, meaning all servers promote high availability, and each server actively handles the traffic. The difference is that in an active-active setup, all servers are actively handling traffic, whereas in an active-passive setup, only one server is active, and the others are on standby until needed.

How does a database Primary-Replica (Master-Slave) cluster work?
In a Primary-Replica cluster, the Primary node receives write operations, and the Replica nodes replicate these operations to maintain a consistent copy. This enhances database reliability and provides data redundancy.

## What is the difference between the Primary node and the Replica node in regard to the application?
The Primary node handles read and write operations, while Replica nodes handle read operations, improving scalability.

## Where are SPOFs?
The current SPOF is in the load balancer, which means if the load balancer goes down, we can't send any more requests to the servers. This can be addressed by adding another load balancer as a slave, providing high availability. If one load balancer is down, we can use the other until we fix it.

## Security issues (no firewall, no HTTPS)?
Without a firewall and HTTPS, we face security issues. If requests are sent using HTTP, our data is not encrypted, exposing important information like passwords. Without a firewall, hackers can easily send payloads with packets, and without HTTPS, there is no encryption in the network to prevent them. Both play important roles in our security.

## No monitoring?
Without monitoring, we can't check our server's health, performance, and security.

# [2. Secured and monitored web infrastructure]()

# [3. Scale up]()




## Authors

- [OMAR DOUIBA](https://github.com/OmarDouiba)
- [OUSSAMA AGNAOU]()
- [HAMZA CHANKOUR]()


## Badges


[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)
[![GPLv3 License](https://img.shields.io/badge/License-GPL%20v3-yellow.svg)](https://opensource.org/licenses/)
[![AGPL License](https://img.shields.io/badge/license-AGPL-blue.svg)](http://www.gnu.org/licenses/agpl-3.0)


## License

[MIT](https://choosealicense.com/licenses/mit/)


