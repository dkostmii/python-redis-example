import time
import redis
import logging
import sys

RETRY_COUNT = 5
RETRY_TIMEOUT_SECONDS = 3

logging.basicConfig(level=logging.INFO)


def handle():
    """Custom command to wait for the database to be available"""
    logging.info("Waiting for the Redis...")
    retries = 1

    while True:
        try:
            client = redis.StrictRedis(host="redis", port=6379)
            if not client.ping():
                if retries == RETRY_COUNT:
                    logging.error("Unable to connect to the Redis.")
                    sys.exit(1)
                logging.warning("Database unavailable, waiting 3 seconds...")
                time.sleep(RETRY_TIMEOUT_SECONDS)
                retries += 1
            else:
                logging.info("Redis available!")
                sys.exit()
        except redis.ConnectionError:
            if retries == RETRY_COUNT:
                logging.error(f"Unable to connect to the Redis. Tried {retries} times.")
                sys.exit(1)
            logging.warning(f"Database unavailable, waiting {RETRY_TIMEOUT_SECONDS} seconds...")
            time.sleep(RETRY_TIMEOUT_SECONDS)
            retries += 1

handle()
