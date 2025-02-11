import json

def get_json():
    with open("data.json", "r") as file:
        data = json.load(file)
    return data

def json_to_md(data):
    gptOutput = data["gptOutput"]
    return gptOutput

def update_json(update, data):
    print(type(update) == str)
    if update[0] != " ":
        update = " " + update
    updated_md = data["gptOutput"] + update
    data.update({"gptOutput": updated_md})
    with open("data.json", "w") as file:
        json.dump(data, file)

if __name__ == "__main__":
    #json_to_md()
    #update_json("test", get_json())
    pass

