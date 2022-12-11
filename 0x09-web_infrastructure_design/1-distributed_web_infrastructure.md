## Distributed web infrastructure

The elements that are added are a single load-balancer and an extra server which basically prevents some of the previous SPOF's (on the simple web stack) 
for example: solves the availability problem on high traffic websites by diverting traffic based on different algorithms towards the different servers.

The HAProxy load balancer is equipped with the round-robin algorithm where Requests are distributed across the group of servers sequentially.
It works by using each server behind the load balancer in turns, according to their weights. It's also probably the smoothest and most fair algorithm as the servers' processing time stays equally distributed. As a dynamic algorithm, Round Robin allows server weights to be adjusted on the go.

### Difference between Active-Active & Active-Passive
The infrastructure that you're looking at uses an active-active clustering technology.

An active-active cluster is typically made up of at least two nodes, both actively running the same kind of service simultaneously. 
for example, in a "Round Robin" algorithm, the first client to connect is sent to the first server, the second client goes to the second server, the third client goes back to the first server, the fourth client back to the second server, and so on.

An active-passive cluster is also made up of at least 2 nodes but the second server is just used as a backup if the first server fails.

### Master-Slave DB replication
Master-slave replication enables data from one database server (the master) to be replicated to one or more other database servers (the slaves). The master logs the updates, which then ripple through to the slaves. The slave outputs a message stating that it has received the update successfully, thus allowing the sending of subsequent updates. Master-slave replication can be either synchronous or asynchronous. The difference is simply the timing of propagation of changes. If the changes are made to the master and slave at the same time, it is synchronous. If changes are queued up and written later, it is asynchronous.

### Security concerning load-balancers
if the load-balancer is behind the network perimeter, in a castle-and-moat approach (no one outside but everyone inside the network can access data) then it is potentially a point
of entry. Vulnerabilities in the configurations.

### SPOF
the load-balancer itself can be a SPOF which makes it redundant. The solution is to implement “failover,” which is a handover from one load balancer to another and with both front-ending the same group of web servers.