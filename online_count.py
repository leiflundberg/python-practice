statuses = {
    "Alice": "online",
    "Bob": "offline",
    "Eve": "online",
}

def online_count(statuses):
    counter = 0 
    for key, value in statuses.items():
        if (value == "online"):
            counter+=1
    return counter

print(online_count(statuses))