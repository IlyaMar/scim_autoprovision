from flask_restful import Resource
import logging
import os
from flask import request


log = logging.getLogger(__name__)


class Groups(Resource):
    @staticmethod
    def get():
        filter = request.args.get('filter')
        log.info("get groups by filter %s" % filter)
        return {}, 404

    @staticmethod
    def post():
        if not request.json:
            abort(400)
        log.info("post group %s" % request.json)
        return {}, 201
