import logging
import sys

import flask

import json_logging

app = flask.Flask(__name__)
json_logging.ENABLE_JSON_LOGGING = True
json_logging.init_flask()
json_logging.init_request_instrument(app)

# init the logger as usual
logger = logging.getLogger("test logger")
logger.setLevel(logging.DEBUG)
logger.addHandler(logging.StreamHandler(sys.stdout))


@app.route('/')
def home():
    logger.info("test log statement")
    logger.info("test log statement", extra={'props': {"extra_property": 'extra_value'}})
    return "Hello world"


@app.route('/exception')
def exception():
    try:
        raise RuntimeError
    except BaseException as e:
        logger.error("Error occurred", exc_info=e)
        logger.exception("Error occurred", exc_info=e)
    return "Error occurred, check log for detail"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(5000), use_reloader=False)
