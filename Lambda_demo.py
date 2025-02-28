import boto3
import requests
import pandas as pd
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event,context):
    col = ['name','age','city']
    data = [['Tom', 10, 'NY'], ['Nick', 15, 'LA'], 
            ['Juli', 14, 'NY']]
    df = pd.DataFrame(data, columns=col)
    logger.info(df)

