import logging
import structlog

def get_logger(loglevel: logging._Level):
    # Set the stdlib level (this controls what gets through)
    logging.basicConfig(level=loglevel)

    structlog.configure(
        processors=[
            structlog.stdlib.filter_by_level,          # drops below-threshold logs
            structlog.processors.TimeStamper(fmt="iso"),
            structlog.dev.ConsoleRenderer(),  # pretty for dev; use JSONRenderer for prod
        ],
        wrapper_class=structlog.stdlib.BoundLogger,    # gives you .info/.warning/.error etc.
        context_class=dict,
        logger_factory=structlog.stdlib.LoggerFactory(),
    )

    logger = structlog.get_logger()
    return logger
