Issue Summary:

- Duration: The outage occurred from 10:00 AM to 1:00 PM (EAT).
- Impact: The web service was completely inaccessible during the outage, affecting 80% of users who were unable to access the platform.
- Root Cause: A misconfiguration in the load balancer settings caused all incoming traffic to be dropped, leading to the service outage.

Timeline:

- 10:00 AM: Issue detected through monitoring alerts indicating a sudden drop in incoming traffic.
- 10:05 AM: Engineers investigated backend services assuming a database or server issue.
- 10:30 AM: Misleading investigation paths included checking database connections and server logs, which showed no anomalies.
- 11:00 AM: Incident escalated to the infrastructure team for further investigation.
- 12:00 PM: Root cause identified as a misconfiguration in the load balancer settings.
- 1:00 PM: Issue resolved by correcting the load balancer configuration.

Root Cause and Resolution:

The root cause of the outage was traced to a misconfiguration in the load balancer settings. Specifically, the load balancer was configured to drop all incoming traffic instead of distributing it among backend servers. This misconfiguration effectively blocked access to the web service for all users.

To resolve the issue, the load balancer configuration was corrected to properly distribute incoming traffic among backend servers. This involved updating the load balancer settings to ensure proper routing of requests to the web service.

Corrective and Preventative Measures:

Improvements/Fixes:
1. Implement automated configuration checks for load balancers to detect misconfigurations promptly.
2. Enhance monitoring capabilities to provide real-time visibility into load balancer performance and traffic distribution.
3. Conduct regular audits of infrastructure configurations to identify and rectify potential misconfigurations proactively.

Tasks to Address the Issue:
1. Implement automated load balancer configuration checks using infrastructure-as-code tools (e.g., Terraform).
2. Enhance monitoring alerts to include specific metrics related to load balancer performance and traffic distribution.
3. Schedule regular reviews of load balancer configurations to ensure alignment with best practices and security standards.

By implementing these corrective and preventative measures, we aim to minimize the risk of similar incidents in the future and enhance the resilience of our web service infrastructure.
