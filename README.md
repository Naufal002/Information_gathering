![img](https://github.com/user-attachments/assets/74b5f95b-3816-4dc7-a404-a55e0fe1a285)
```py
request_url = f"http://ip-api.com/json/{ip_address}" #backup.py
```
```py
requset_url = f"https://geolocation-db.com/jsonp/{ip_address}" #main.py
```
<h1>INFORMATION GATHERING</h1>
<p>Geolocation API Limitations: Free APIs like ip-api.com can have limited accuracy, especially for large entities like Facebook that may use distributed server locations globally. These APIs sometimes generalize the location of a large ISP, such as Facebook or Akamai, leading to inaccuracies.

Proxy or CDN Influence: Large websites like Facebook and government websites often use Content Delivery Networks (CDNs) like Akamai, which can mask the true location of their servers. Instead of providing the actual physical server location, the API might be returning the location of the CDN node closest to you.

IP Blocks: For large organizations, a single IP address can map to multiple locations due to how their infrastructure is set up (load balancers, multiple data centers, etc.). This can cause geolocation services to give a generalized location.<p>
