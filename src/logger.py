# src/logger.py

import logging

def setup_logger():
    logging.basicConfig(
        filename='anomaly_log.txt',
        level=logging.INFO,
        format='%(asctime)s - Anomaly Detected - Value: %(message)s'
    )

def log_anomaly(value):
    logging.info(value)

