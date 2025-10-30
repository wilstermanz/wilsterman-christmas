from hashlib import md5
import random

SEED = 777

# Family list
family = [
    'Tom',
    'Vickie',
    'Zach',
    'Katie',
    'Berto',
    'Annie',
    'Nick',
    'Bekah',
    'Lilly'
]

def generate_matches(seed_string):
    random.seed(seed_string)

    possible_matches_local = []
    for giver in family:
        for recipient in family:
            if giver != recipient:
                possible_matches_local.append((giver, recipient))

    matches_encoded_local = {}
    for match in possible_matches_local:
        hash = md5(str(match).encode()).hexdigest()
        matches_encoded_local[hash] = match

    known_matches_local = []

    givers = family.copy()

    recipients_list = givers[:]  # copy the givers list
    while True:
        random.shuffle(recipients_list)  # shuffle for random matches
        if not any(recipients_list[i] == giver for i, giver in enumerate(givers)):
            break  # no self matches
    for i, giver in enumerate(givers):
        recipient = recipients_list[i]
        known_matches_local.append(md5(str((giver, recipient)).encode()).hexdigest())

    return known_matches_local, matches_encoded_local

# Generate matches with the seed
known_matches, matches_encoded = generate_matches(SEED)

# Get codes for each person
codes = {}
for match in known_matches:
    giver = matches_encoded[match][0]
    code = match[::6]
    codes[giver] = code

print("Secret Santa Codes for Distribution:")
print("====================================")
for giver in family:
    print(f"{giver}: {codes[giver]}")
print("\nDistribute these codes to each person via private message.")
