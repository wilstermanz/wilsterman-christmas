from hashlib import md5
import streamlit as st

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

matches = []
for giver in family:
    for recipient in family:
        if giver != recipient:
            matches.append((giver, recipient))

matches_encoded = {}
for match in matches:
    hash = md5(str(match).encode()).hexdigest()
    matches_encoded[hash] = match


st.title("🎁🎄Wilsterman Family Gift Fixer")
giver = st.selectbox(label='Giver', options=family)
recipient = st.selectbox(label='Recipient', options=family)
if giver == recipient:
    st.error('Giver cannot be recipient')
else:
    st.write(f'```\n{md5(str((giver, recipient)).encode()).hexdigest()}')
