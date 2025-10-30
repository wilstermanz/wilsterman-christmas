from hashlib import md5
import random
import streamlit as st


random.seed(1234567)

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

known_matches = []

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
        background: linear-gradient(to bottom, #1e3a5f, #0d4f3c);
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
    <div class="snow-container">
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
    .snow-container {
        position: fixed;
        top: 0;
        left: 0;
        width: 100vw;
        height: 100vh;
        pointer-events: none;
        overflow: hidden;
        z-index: 9999;
        background: transparent;
    }
    .snowflake {
        position: absolute;
        font-size: 30px;
        color: #fff;
        text-shadow: 0 0 5px #ffd700;
        animation: snowfall linear infinite;
        opacity: 0;
    }
    .snowflake:nth-child(1) {
        left: 5%;
        font-size: 25px;
        animation-duration: 8s;
        animation-delay: -2s;
    }
    .snowflake:nth-child(2) {
        left: 10%;
        font-size: 35px;
        animation-duration: 9s;
        animation-delay: -4s;
    }
    .snowflake:nth-child(3) {
        left: 15%;
        font-size: 28px;
        animation-duration: 10s;
        animation-delay: -1.5s;
    }
    .snowflake:nth-child(4) {
        left: 20%;
        font-size: 32px;
        animation-duration: 9.5s;
        animation-delay: -3.2s;
    }
    .snowflake:nth-child(5) {
        left: 25%;
        font-size: 30px;
        animation-duration: 8.5s;
        animation-delay: -5s;
    }
    .snowflake:nth-child(6) {
        left: 30%;
        font-size: 26px;
        animation-duration: 10.5s;
        animation-delay: -2.8s;
    }
    .snowflake:nth-child(7) {
        left: 35%;
        font-size: 33px;
        animation-duration: 11s;
        animation-delay: -3.5s;
    }
    .snowflake:nth-child(8) {
        left: 40%;
        font-size: 29px;
        animation-duration: 9.2s;
        animation-delay: -1.2s;
    }
    .snowflake:nth-child(9) {
        left: 45%;
        font-size: 31px;
        animation-duration: 10.2s;
        animation-delay: -4.8s;
    }
    .snowflake:nth-child(10) {
        left: 50%;
        font-size: 27px;
        animation-duration: 8.8s;
        animation-delay: -2.5s;
    }
    .snowflake:nth-child(11) {
        left: 55%;
        font-size: 34px;
        animation-duration: 12s;
        animation-delay: -3.8s;
    }
    .snowflake:nth-child(12) {
        left: 60%;
        font-size: 28px;
        animation-duration: 9.8s;
        animation-delay: -5.5s;
    }
    .snowflake:nth-child(13) {
        left: 65%;
        font-size: 30px;
        animation-duration: 11.5s;
        animation-delay: -1.8s;
    }
    .snowflake:nth-child(14) {
        left: 70%;
        font-size: 32px;
        animation-duration: 8.2s;
        animation-delay: -4.2s;
    }
    .snowflake:nth-child(15) {
        left: 75%;
        font-size: 26px;
        animation-duration: 10.8s;
        animation-delay: -2.2s;
    }
    .snowflake:nth-child(16) {
        left: 80%;
        font-size: 35px;
        animation-duration: 13s;
        animation-delay: -3.9s;
    }
    .snowflake:nth-child(17) {
        left: 85%;
        font-size: 29px;
        animation-duration: 9.4s;
        animation-delay: -1.4s;
    }
    .snowflake:nth-child(18) {
        left: 90%;
        font-size: 31px;
        animation-duration: 10.6s;
        animation-delay: -4.5s;
    }
    .snowflake:nth-child(19) {
        left: 95%;
        font-size: 27px;
        animation-duration: 8.6s;
        animation-delay: -0.8s;
    }
    .snowflake:nth-child(20) {
        left: 100%;
        font-size: 33px;
        animation-duration: 11.8s;
        animation-delay: -3.1s;
    }
    .snowflake:nth-child(21) {
        left: 105%;
        font-size: 29px;
        animation-duration: 9.5s;
        animation-delay: -4.7s;
    }
    .snowflake:nth-child(22) {
        left: 115%;
        font-size: 31px;
        animation-duration: 10.3s;
        animation-delay: -2.3s;
    }
    .snowflake:nth-child(23) {
        left: 125%;
        font-size: 27px;
        animation-duration: 8.9s;
        animation-delay: -5.2s;
    }
    .snowflake:nth-child(24) {
        left: 135%;
        font-size: 35px;
        animation-duration: 12.5s;
        animation-delay: -1.9s;
    }
    .snowflake:nth-child(25) {
        left: 145%;
        font-size: 28px;
        animation-duration: 9.7s;
        animation-delay: -3.6s;
    }
    .snowflake:nth-child(26) {
        left: 155%;
        font-size: 32px;
        animation-duration: 11.2s;
        animation-delay: -2.1s;
    }
    .snowflake:nth-child(27) {
        left: 165%;
        font-size: 26px;
        animation-duration: 9.1s;
        animation-delay: -4.3s;
    }
    .snowflake:nth-child(28) {
        left: 175%;
        font-size: 33px;
        animation-duration: 10.9s;
        animation-delay: -1.6s;
    }
    .snowflake:nth-child(29) {
        left: 185%;
        font-size: 30px;
        animation-duration: 12.1s;
        animation-delay: -3.4s;
    }
    .snowflake:nth-child(30) {
        left: 195%;
        font-size: 29px;
        animation-duration: 9.3s;
        animation-delay: -2.7s;
    }

    @keyframes snowfall {
        0% {
            transform: translateY(-100vh);
            opacity: 0;
        }
        10% {
            opacity: 0.8;
        }
        90% {
            opacity: 0.8;
        }
        100% {
            transform: translateY(100vh);
            opacity: 0;
        }
    }


    </style>
    """, unsafe_allow_html=True)

    # Disable snow on mobile
    st.markdown("""
    <style>
    @media (max-width: 767px) {
        .snow-container {
            display: none;
        }
    }
    </style>
    """, unsafe_allow_html=True)

    st.title("🎄 Wilsterman Family Christmas Matcher 🎁❄️")

    st.write("## Secret Santa Assistant 🎅")
    st.write("Enter your 6-character secret code to find out who you're buying for!")

    with st.form('code_input'):
        code = st.text_input('code_input', label_visibility='hidden', max_chars=6, placeholder="Enter code...")
        submitted = st.form_submit_button("Reveal My Match! 🎁")
        if submitted and len(code) == 6:
            matched = False
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
