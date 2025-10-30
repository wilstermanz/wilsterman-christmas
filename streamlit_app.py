from hashlib import md5
import random
import streamlit as st

SEED = 777
random.seed(SEED)

# Real actual family
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

# # Test family
# family = ['Alice', 'Brian', 'Catherine', 'David', 'Ella', 'Frank', 'Grace', 'Henry', 'Ivy']

possible_matches = []
for giver in family:
    for recipient in family:
        if giver != recipient:
            possible_matches.append((giver, recipient))

matches_encoded = {}
for match in possible_matches:
    hash = md5(str(match).encode()).hexdigest()
    matches_encoded[hash] = match

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
    recipients = family.copy()

    for match_encoded in known_matches_local:
        giver, recipient = matches_encoded_local[match_encoded]
        givers.remove(giver)
        recipients.remove(recipient)

    recipients_list = givers[:]  # copy the givers list
    while True:
        random.shuffle(recipients_list)  # shuffle for random matches
        if not any(recipients_list[i] == giver for i, giver in enumerate(givers)):
            break  # no self matches
    for i, giver in enumerate(givers):
        recipient = recipients_list[i]
        known_matches_local.append(md5(str((giver, recipient)).encode()).hexdigest())

    return known_matches_local, matches_encoded_local

known_matches, matches_encoded = generate_matches(SEED)

if __name__ == '__main__':
    st.title("🎄 Wilsterman Family Christmas Matcher 🎁❄️")

    st.write("## Secret Santa Assistant 🎅")
    st.write("Enter your 6-character secret code to find out who you're buying for!")

    with st.form('code_input'):
        code = st.text_input('code_input', label_visibility='hidden', max_chars=6, placeholder="Enter code...")
        submitted = st.form_submit_button("Reveal My Match! 🎁")
        if submitted and len(code) == 6:
            matched = False
            code = code.lower()
            for match in known_matches:
                if code == match[::6]:
                    st.success("Your Secret Santa match is **" + matches_encoded[match][1] + "**! 🎉")
                    st.balloons()
                    matched = True
                    break
            if not matched:
                st.error("Invalid code. Please check and try again.")
        elif submitted:
            st.warning("Please enter exactly 6 characters.")
