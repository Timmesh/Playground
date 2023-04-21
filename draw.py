from diagrams import Cluster, Diagram
from diagrams.aws.compute import EC2
from diagrams.aws.database import RDS
from diagrams.aws.integration import SQS
from diagrams.aws.network import ELB
from diagrams.onprem.client import User, Users
from diagrams.onprem.container import Docker
from diagrams.onprem.database import PostgreSQL
from diagrams.onprem.inmemory import Redis
from diagrams.onprem.monitoring import Grafana, Prometheus
from diagrams.onprem.network import Nginx
from diagrams.onprem.queue import Kafka

with Diagram("Food Delivery System", show=False):
    # Users
    customer = User("Customer")
    delivery = User("Delivery Partner")
    admin = User("Admin")

    # Load balancer
    lb = ELB("Load Balancer")

    # Web servers
    with Cluster("Web Servers"):
        web = [EC2("Web 1"),
               EC2("Web 2"),
               EC2("Web 3")]

    # Cache servers
    with Cluster("Cache Servers"):
        cache = [Redis("Cache 1"),
                 Redis("Cache 2")]

    # Database servers
    with Cluster("Database Servers"):
        db_master = RDS("DB Master")
        db_master - [RDS("DB Slave 1"),
                     RDS("DB Slave 2")]

    # Message brokers
    with Cluster("Message Brokers"):
        queue = SQS("Queue")
        topic = Kafka("Topic")

    # Microservices
    with Cluster("Microservices"):
        order = Docker("Order Service")
        payment = Docker("Payment Service")
        notification = Docker("Notification Service")
        recommendation = Docker("Recommendation Service")
        driver = Docker("Driver Service")

    # Data warehouse
    with Cluster("Data Warehouse"):
        dw = PostgreSQL("DW")

    # Data processing
    with Cluster("Data Processing"):
        spark = Docker("Spark")

    # Monitoring
    with Cluster("Monitoring"):
        prometheus = Prometheus("Prometheus")
        grafana = Grafana("Grafana")

    # Data flow
    customer >> lb >> web[0] >> cache[0] >> db_master
    customer >> lb >> web[1] >> cache[1] >> db_master
    customer >> lb >> web[2] >> cache[0] >> db_master
    customer >> lb >> web[2] >> cache[1] >> db_master
    customer >> lb >> [*web] >> order >> queue >> payment >> topic >> notification
    customer >> lb >> [*web] >> recommendation >> dw
    delivery >> lb >> [*web] >> driver >> queue >> notification
    delivery >> lb >> [*web] >> driver >> topic >> notification
    admin >> lb >> web[0] >> cache[0] >> db_master
    admin >> lb >> web[1] >> cache[1] >> db_master
    admin >> lb >> web[2] >> cache[0] >> db_master
    admin >> lb >> web[2] >> cache[1] >> db_master
    admin >> lb >> [*web] >> order >> queue >> payment >> topic >> notification
    db_master - dw << spark << topic

    # Monitoring flow
    web[0] - prometheus - grafana
    web[1] - prometheus
    web[2] - prometheus
