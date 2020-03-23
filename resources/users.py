from flask_restful import Resource
import logging
import copy
from aps import g_aps as aps
from flask import request


log = logging.getLogger(__name__)


class Users(Resource):
    scim_user_template = {
        'schemas': ['urn:ietf:params:scim:schemas:core:2.0:User', 'urn:ietf:params:scim:schemas:extension:enterprise:2.0:User'],
        'externalId': 'Mikhail.Terekhov',
        'userName': 'Mikhail.Terekhov@ingrammicro.com',
        'active': True,
        'displayName': 'Terekhov, Mikhail',
        'emails': [{'primary': True, 'type': 'work', 'value': 'Mikhail.Terekhov@ingrammicro.com'}],
        'meta': {'resourceType': 'User'}
    }

    @staticmethod
    def get():
        filter = request.args.get('filter')
        log.info("get user by filter %s" % filter)
        fr = Users.__scim_filter_to_rql(filter)
        url = "aps/2/collections/pa-admin-users?%s" % fr
        u = aps.get(url)
        if not u:
            return {}, 404
        else:




    @staticmethod
    def __aps_to_scim(u):
        r = copy.deepcopy(Users.scim_user_template)
        r["externalId"] = u["fullName"]
        r["userName"] = u["login"]
        r["active"] = not u["disabled"]
        r["displayName"] = u["displayName"]
        r["emails"] = [{'primary': True, 'type': 'work', 'value': u["email"]}]
        



    @staticmethod
    def __scim_filter_to_rql(f):
        userNameEq = "userName eq "
        if f.startswith(userNameEq):
            userName = f[len(userNameEq):].replace("\"", "")
            return "login=eq=%s" % userName
        else:
            raise Exception("unexpected users filter %s" % f)

    @staticmethod
    def __scim_to_aps(u):
        pass