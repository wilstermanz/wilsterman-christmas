from hashlib import md5
import random
import streamlit as st


random.seed(0)

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

# Real actual known matches
known_matches = [
    'd6756d8309907c3acde021b8cae3998c'
]

# # test known matches
# known_matches = [
#     '84060eff6a9ad9282ff5651f59c5f384',
#     '4b8c7499eb94277d5f4015bf7c8bfaf6',
#     '7d370a2bd0ccc1119e5d668b54e7e2ff',
#     'c81f715ca643d2ba7f9b55824702354a'
#     ]

givers = family.copy()
recipients = family.copy()

for match_encoded in known_matches:
    giver, recipient = matches_encoded[match_encoded]
    givers.remove(giver)
    recipients.remove(recipient)

for giver in givers:
    recipient = random.choice(recipients)
    recipients.remove(recipient)
    known_matches.append(md5(str((giver, recipient)).encode()).hexdigest())


if __name__ == '__main__':
    st.title("🎁🎄Wilsterman Family Gift Fixer")

    st.write('## Enter secret code here')
    with st.form('code_input'):
        code = st.text_input('code_input', label_visibility='hidden')
        submitted = st.form_submit_button("Get my person!")
        if submitted and len(code) == 6:
            for match in known_matches:
                if code in match:
                    st.success(matches_encoded[match][1])