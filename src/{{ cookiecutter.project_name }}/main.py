
import logging

from {{ cookiecutter.project_name }}.log_factory import get_logger


logger = get_logger(logging.INFO)


def main():
    logger.info("Hello from {{ cookiecutter.project_name }}!")


if __name__ == "__main__":
    main()
