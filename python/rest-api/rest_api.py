import json
from operator import itemgetter
from collections import OrderedDict


class RestAPI(object):
    def __init__(self, database=None):
        if database is None:
            self.database = {"users": []}
        else:
            self.database = database

    def get(self, url, payload=None):
        if payload:
            payload = json.loads(payload)
            users = payload["users"]
            response = self.build_get_response(users)

            return json.dumps(response)

        else:
            return json.dumps((self.database))

    def post(self, url, payload=None):
        if url == "/add":
            payload = json.loads(payload)
            user_name = payload["user"]
            user_entry = User(user_name)
            self.database["users"].append(user_entry.__dict__)

            return json.dumps(user_entry.__dict__)

        if url == "/iou":
            payload = json.loads(payload)
            lender = payload["lender"]
            borrower = payload["borrower"]
            amount = payload["amount"]

            self.apply_iou_to_database(lender, borrower, amount)
            response = self.build_iou_response(lender, borrower)

            return json.dumps(response)

    def apply_iou_to_database(self, lender, borrower, amount):

        # TODO: Need to apply logic that removes borrower once the owed amount equals 0.

        d = next(t for k, v in self.database.items() for t in v if t["name"] == lender)
        d["owed_by"] = {borrower: amount}
        d["balance"] += int(amount)

        e = next(t for k, v in self.database.items() for t in v if t["name"] == borrower)
        new_entry = {lender: amount}
        e["owes"].update(new_entry)
        e["balance"] -= int(amount)

    def build_get_response(self, users):

        response = {"users": []}

        for value in self.database.get("users"):
            if value["name"] in users:
                response["users"].append(value)

        return response

    def build_iou_response(self, lender, borrower):

        response = {"users": []}

        for value in self.database.get("users"):
            if value["name"] == borrower or value["name"] == lender:
                response["users"].append(value)

        return response


class User(RestAPI):
    def __init__(self, name, owes=None, owed_by=None, balance=0):
        self.name = name
        self.owes = {}
        self.owed_by = {}
        self.balance = 0

