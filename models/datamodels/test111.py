from models.basemodel import Base

data = {
        # "created" : "2014-12-09 T13:50:51.644000z", here was capital 'Z' but I wrote there lowercase 'z' so programme showed error..thank you.
        "created": "2014-12-09T13:50:51.644000Z",
        # "edited":"2014-12-20 T21:17:56.891000z",
        "edited": "2014-12-20T21:17:56.891000Z",
        "url":"https://swapi.dev/api/people/1/"
    }

v = Base(**data)

print(v)