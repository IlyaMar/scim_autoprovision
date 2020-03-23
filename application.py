from flask import Flask
from flask_restful import Api
import logging

from resources import users, groups

log = logging.getLogger(__name__)


app = Flask(__name__)
api = Api(app)

api.add_resource(users.Users, '/Users')
api.add_resource(groups.Groups, '/Groups')


def init_logging():
    logging.basicConfig(level=logging.DEBUG,
                        format='%(asctime)s %(levelname)s\t[%(name)s]\t%(process)s %(thread)s\t%(message)s')


if __name__ == '__main__':
    init_logging()
    log.info('SCIM Service Provider started')
    app.run()
    # app.run(debug=False, processes=1, host="0.0.0.0")
