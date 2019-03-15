database = {
    "users": [
        {
            "name": "Adam",
            "owes": {"Bob": 3.0, "Josh": 4.0},
            "owed_by": {},
            "balance": -3.0,
        },
        {"name": "Bob", "owes": {}, "owed_by": {"Adam": 3.0}, "balance": 3.0},
    ]
}

lender = "Adam"
borrower = "Bob"

for value in database.get("users"):
    if value["name"] == borrower:
        if lender in value["owed_by"].keys():
            print(value["owed_by"][lender])
