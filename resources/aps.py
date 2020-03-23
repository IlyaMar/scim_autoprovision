
import urllib
import urllib2
import json
import logging
import ssl


log = logging.getLogger(__name__)

g_aps = Aps()


class Aps:
    APS2_RESOURCES = 'aps/2/resources'
    __ssl_ctx = ssl.create_default_context()
    __ssl_ctx.check_hostname = False
    __ssl_ctx.verify_mode = ssl.CERT_NONE

    def __init__(self):
        self.brand = 'https://hkhzi.brndd013794a-0c4de9.aqa.int.zone/'
        self.id_token = 'eyJhbGciOiJSUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICJtYWZVQUFscm9JOWdhSVdtZGZlbzQ5QVV5NmhEZ0JXSXNqZFY0WjBiVndVIn0.eyJqdGkiOiJkOTIzZGVmMC0wMTZkLTQzY2ItYjVlNy1kMWE0NDM5YTc2ZjciLCJleHAiOjE1ODUwMTcxNjQsIm5iZiI6MCwiaWF0IjoxNTg0OTgxMTY0LCJpc3MiOiJodHRwczovL2hraHppLmJybmRkMDEzNzk0YS0wYzRkZTkuYXFhLmludC56b25lL2F1dGgvcmVhbG1zL3NyMSIsImF1ZCI6ImNsaSIsInN1YiI6ImY6YThlNDc2Y2ItMDE3OC00ZTU3LTk5NjktNGE0Yzc0MGNlYzdjOjEiLCJ0eXAiOiJJRCIsImF6cCI6ImNsaSIsImF1dGhfdGltZSI6MCwic2Vzc2lvbl9zdGF0ZSI6IjVkN2YwMDkyLTFmZDMtNDQyYy1hMjc5LTUxZDlmNTNlNzEzZSIsImFjciI6IjEiLCJhY2NvdW50X2lkIjoxLCJ1c2VyX2lkIjoxLCJhY2NvdW50X3VpZCI6IjIxMzU0MDEwLWJhMTAtNDY5NC1hNDg2LTU0M2NjYjIyYzI5ZCIsImFjY291bnRfaCI6IjEifQ.Ujco3YumUi80CZ4lR-FZ3M2FISUO2SAHHxtbQ3a_sQJpB_Tdgf-couVjvkXgjdNII9COp5EIeWwOH5O12JO2RU7crfATBSXxtFXJwv9389U5g_2WGcqUOEIKU99aUnnxNK0apOodTOiswxUEQ0__UTrXcmg7qaakceXgU64A7e6bK7CgAbqRc4yr7CIQ-qJrG5IYIaf-9QxgNtnQCw1PiVf7FkSw4QOnt-U9PQpnrQLhkqoW4xKTAMBmTHfzMpew3kyyY_Q0BtkvEAG8yA_1XX2iGsnzgGWhHdoFrt0EyeLDag_De7ec_7o2tG3j0nglg2HMrFDBhg-SGNM7BNY2pg'


    def __query(self, rql, method, data):
        full_url = "%s/%s" % (self.brand, rql)
        req = urllib2.Request(full_url, data)
        req.get_method = lambda: method
        return self.__open_url(req)

    def __open_url(self, request):
        log.debug("APS %s %s" % (request.get_method(), request.get_full_url())
        resp = urllib2.urlopen(request, context=Aps.__ssl_ctx)
        log.debug("response %d" % resp.getcode())
        return resp


    def get(self. rql):
        resp = self.query(rql, 'GET')
        assert resp.getcode() == 200
        return json.loads(resp.read())

