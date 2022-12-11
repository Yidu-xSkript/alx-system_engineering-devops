## Simple Web Infrastructure
This generally shows a simple infrastructure of a website. client recieve from DNS Server of A Records the IP of the domain name foobar.com 
and the client sends an HTTP request to the webserver where the webcontent (application files - codebase) is delivered to the client.

Web Server is a computer program that uses HTTP and other protocols to run websites and deliver web content as per the client’s request. 
Each web server has a unique name and IP address. The main role of a web server is to store, process, and transfer the requested web pages to the client. These can be images, files, text, videos, etc. It is a client and server model that supports other protocols like SMTP (Simple Mail Transfer Protocol) and FTP (File Transfer Protocol) as well for storage and transferring files. Web servers are easy to configure and often used in web hosting and applications. Apache HTTP Server, Nginx, Sun Java System Web Server, Resin, etc., are a few web servers.

With application servers, web servers work as a subset. Also, they have the power to carry heavier workloads than a web server. The only idea behind introducing application servers was to reduce the size and complexity of these programs, add more security to the data, and control data flow for better performance and results. It supports a load balancing feature to distribute requests to other servers depending on their availability. Websphere, JBoss, Weblogic, Glassfish, Sybase Enterprise Application Server, etc., are a few Application Servers.

www is in the "A Record" of a DNS Type - found in the authoritative DNS.

The Database relational or non-relational both just return stored data related to the HTTP Request.
The server uses HTTP to communicate with the computer of the user generally uses the port (80).

### Single point of failure
If the server failed, the application would become unstable or crash. This event would prevent users from accessing the application, and it could possibly result in data loss. The use of server clustering technology can mitigate this situation. It would allow a duplicate copy of the application to run on a second physical server. If the first server failed, the second would take over to preserve access to the application and avoid the SPOF.

No scalibility.
server cannot handle high traffic.

server maintenance might affect accessibility.