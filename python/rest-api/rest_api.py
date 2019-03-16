import json


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

            # self.apply_iou_to_database(lender, borrower, amount)
            self.apply_iou(lender, borrower, amount)
            response = self.build_iou_response(lender, borrower)

            return json.dumps(response)

    def apply_iou(self, lender, borrower, amount):

        for value in self.database.get("users"):
            if value["name"] == lender:
                if borrower in value["owes"].keys():
                    value["owes"][borrower] -= amount
                    value["balance"] += amount
                    if value["owes"][borrower] == 0:
                        del value["owes"][borrower]
                    elif value["owes"][borrower] < 0:
                        owed_balance = abs(value["owes"][borrower])
                        value["owed_by"] = {borrower: owed_balance}
                        del value["owes"][borrower]
                else:
                    value["owed_by"] = {borrower: amount}
                    value["balance"] += int(amount)

        for value in self.database.get("users"):
            if value["name"] == borrower:
                if lender in value["owed_by"]:
                    value["owed_by"][lender] -= amount
                    value["balance"] -= amount
                    if value["owed_by"][lender] == 0:
                        del value["owed_by"][lender]
                    elif value["owed_by"][lender] < 0:
                        new_amount = abs(value["owed_by"][lender])
                        new_entry = {lender: new_amount}
                        value["owes"].update(new_entry)
                        del value["owed_by"][lender]
                else:
                    new_entry = {lender: amount}
                    value["owes"].update(new_entry)
                    value["balance"] -= amount

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

