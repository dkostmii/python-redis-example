import redis
import logging

logging.basicConfig(level=logging.INFO)


def main():
    client = redis.StrictRedis(host="redis", port=6379)
    key = "message"
    value = "Hello, World!"
    client.set(key, value)
    logging.info("Set '%s' key in Redis to %s", key, value)


if __name__ == "__main__":
    main()
