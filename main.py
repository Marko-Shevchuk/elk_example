import logging
import logstash

logger = logging.getLogger('ELK-test-app')
logger.setLevel(logging.INFO)

handler = logstash.TCPLogstashHandler(host="localhost", port=5044)
logger.addHandler(handler)


def main():
    for idx in range(3):
        logger.info(f"Test test test round {idx}")
        logger.info("Get that real important data", extra={"data": {"key": f"data-{idx}"}})

        try:
            a = 69 / 0
            print(a)
        except ZeroDivisionError as e:
            logger.exception(f"UH-OH! EXCEPTION occurred: {e}")


if __name__ == "__main__":
    main()