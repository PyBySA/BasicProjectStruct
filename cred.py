import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

ashley_product_url = 'https://apigw3.ashleyfurniture.com/productinformation/'
api_endpoint = 'https://apigw3.ashleyfurniture.com/productinformation/Products?ShipTo=01&Customer=3846300'
username = os.getenv('ash_username')
password = os.getenv('ash_password')
clientId = os.getenv('clientId')

db_user = os.getenv('db_user')
db_password = os.getenv('db_password')
db_host = os.getenv('db_host')
database = os.getenv('database')
db_schema = os.getenv('db_schema')
db_port = 5000
db_conn_pool = 1
db_conn_pool_max = 2

echo = False
vendor_name = "Ashley"
chunk_size = 100
variable = 50
compair_variable = 40
current_user = 'Testing@User'
max_workers = 3
