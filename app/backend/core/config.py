import os

## Use this configuration to test database localy - DO NOT PUSH!
os.environ["POSTGRES_USER"] = "postgres"
os.environ["POSTGRES_PASSWORD"] = "Yamaha-2012"
os.environ["POSTGRES_HOST"] = "localhost"
os.environ["POSTGRES_PORT"] = "5432"
os.environ["POSTGRES_DB"] = "NBP_Curr"
os.environ['POSTGRES_CONNECTION_STRING']=f"postgresql://{os.environ['POSTGRES_USER']}:{os.environ['POSTGRES_PASSWORD']}@{os.environ['POSTGRES_HOST']}:{os.environ['POSTGRES_PORT']}/{os.environ['POSTGRES_DB']}"

## Connection string
CONNECTION_STRING = os.environ["POSTGRES_CONNECTION_STRING"]

CURRENCIES = "currencies"
