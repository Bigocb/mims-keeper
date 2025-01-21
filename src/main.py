from flask import Flask, request
from sqlalchemy.testing.plugin.plugin_base import logging

from src.data import Data, Interaction

app = Flask(__name__)


@app.route('/keep', methods=['POST'])
def keep() -> str:

    # Get request body
    req_body: dict = request.get_json()

    # Build our initial Interaction object
    keep_req = Interaction(
        prompt=req_body['prompt'],
        response = req_body['response']
    )

    # Create connection and save our Interaction
    database = Data()
    try:
        keep_id = database.save(keep_req)
        return str(keep_id)
    except ConnectionError as e:
        logging.error("There was an error connecting to Atlas: %s", e, exc_info=True)


if __name__ == '__main__':
    app.run(debug=True)