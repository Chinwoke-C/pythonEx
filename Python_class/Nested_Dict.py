first_dict = {
    "key_1": "jude hates python",
    "key_2": {
        "name": "paragon",
        "age": "4 month",
        "loan amount": " 4 million",
        "size": 38,
        "weight": 3.9,
    },
    "key_3": 500,
    "key_4": [50, 10, 5.9, "hate python"],
    "key_5": "fantastic"
}
if __name__ == '__main__':
    # print(first_dict["key_2"]["size"])
    # print(first_dict["key_4"][3])
    for key in first_dict["key_2"]:
        print(key)


