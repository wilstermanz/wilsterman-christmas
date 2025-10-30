from hashlib import md5
import random
import streamlit as st


random.seed(646887542)

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
    # 'd6756d8309907c3acde021b8cae3998c'      # Vickie's match
    # , '6e0e6f62753a0e4b27ed83f485c08c86'    # Annie's match
    # , '7df2b10c01c83f295cc461e3f141f084'    # Katie's match
    # , 'a0e524e4f3e0909edd3a62ed2d116fd4'    # Berto's match
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
    while giver == recipient:
        recipient = random.choice(recipients)
    recipients.remove(recipient)
    known_matches.append(md5(str((giver, recipient)).encode()).hexdigest())

if __name__ == '__main__':
    # Add intense Christmas visuals with CSS and snow animation
    st.markdown("""
    <style>
    [data-testid="stAppViewContainer"] {
        background: linear-gradient(135deg, #b22222, #228b22);
        color: #fff !important;
        font-family: 'Arial', sans-serif;
    }
    [data-testid="stHeader"] {
        background: transparent;
    }
    .stText input {
        background-color: rgba(255, 255, 255, 0.9);
        color: #333;
        border: 2px solid #ffd700;
    }
    .stButton button {
        background-color: #ff0000;
        color: #fff;
        border: 2px solid #ffd700;
        font-size: 18px;
        padding: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

    # Snow animation background
    st.markdown("""
    <div style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; pointer-events: none; overflow: hidden; z-index: -1;">
        <div class="snowflake">❄️</div>
        <div class="snowflake">❄️</div>
        <div class="snowflake">❄️</div>
        <div class="snowflake">❄️</div>
        <div class="snowflake">❄️</div>
        <div class="snowflake">❄️</div>
        <div class="snowflake">❄️</div>
        <div class="snowflake">❄️</div>
        <div class="snowflake">❄️</div>
        <div class="snowflake">❄️</div>
    </div>
    <style>
    .snowflake {
        position: absolute;
        font-size: 20px;
        animation: snowfall 10s linear infinite;
        opacity: 0.8;
    }
    .snowflake:nth-child(1) { left: 10%; animation-delay: 0s; }
    .snowflake:nth-child(2) { left: 20%; animation-delay: 1s; }
    .snowflake:nth-child(3) { left: 30%; animation-delay: 2s; }
    .snowflake:nth-child(4) { left: 40%; animation-delay: 3s; }
    .snowflake:nth-child(5) { left: 50%; animation-delay: 4s; }
    .snowflake:nth-child(6) { left: 60%; animation-delay: 5s; }
    .snowflake:nth-child(7) { left: 70%; animation-delay: 6s; }
    .snowflake:nth-child(8) { left: 80%; animation-delay: 7s; }
    .snowflake:nth-child(9) { left: 90%; animation-delay: 8s; }
    .snowflake:nth-child(10) { left: 100%; animation-delay: 9s; }
    @keyframes snowfall {
        0% { transform: translateY(-100vh); }
        100% { transform: translateY(100vh); }
    }
    </style>
    """, unsafe_allow_html=True)

    st.title("🎅🎁🎄 Ho Ho Ho! Wilsterman Family Christmas Matcher ❄️🥳")

    st.write("## 🛷 Santa's Little Secret Helper 🎅")
    st.write("### Enter your magical 6-character secret code to unwrap your special gift assignment! 🎁✨")

    with st.form('code_input'):
        code = st.text_input('code_input', label_visibility='hidden', max_chars=6, placeholder="Code here...")
        submitted = st.form_submit_button("🎀 Unwrap Your Match! 🚀")
        if submitted and len(code) == 6:
            matched = False
            for match in known_matches:
                if code == match[::6]:
                    st.success("🎉🎊 Eureka! Your Secret Santa snow angel is **" + matches_encoded[match][1] + "**! Ho ho ho! 🎄🥁")
                    st.balloons()
                    matched = True
                    break
            if not matched:
                st.error("❌ Oh no! That code didn't jingle our bells. Check with Santa! 🎅")
        elif submitted:
            st.warning("❗ Please enter exactly 6 characters, like Santa's magic! ✨")
