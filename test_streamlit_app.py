import unittest
from hashlib import md5
import random

# Import the logic from streamlit_app.py
def import_logic():
    # Repeat the code from streamlit_app.py for matching
    random.seed(1234567)

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

    possible_matches = []
    for giver in family:
        for recipient in family:
            if giver != recipient:
                possible_matches.append((giver, recipient))

    matches_encoded = {}
    for match in possible_matches:
        hash = md5(str(match).encode()).hexdigest()
        matches_encoded[hash] = match

    # Uncommented real known matches
    # known_matches = [
    #     'd6756d8309907c3acde021b8cae3998c' ,      # Vickie's match
    #     '6e0e6f62753a0e4b27ed83f485c08c86',    # Annie's match
    #     '7df2b10c01c83f295cc461e3f141f084',    # Katie's match
    #     'a0e524e4f3e0909edd3a62ed2d116fd4',    # Berto's match
    # ]
    known_matches = []

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

    return family, known_matches, matches_encoded

class TestSecretSanta(unittest.TestCase):

    def setUp(self):
        self.family, self.known_matches, self.matches_encoded = import_logic()

    def test_all_family_members_have_matches(self):
        """Test that all family members are assigned to give."""
        givers = [self.matches_encoded[match][0] for match in self.known_matches]
        self.assertEqual(sorted(givers), sorted(self.family), "Not all family members are givers.")

    def test_all_family_members_receive_matches(self):
        """Test that all family members are assigned to receive."""
        recipients = [self.matches_encoded[match][1] for match in self.known_matches]
        self.assertEqual(sorted(recipients), sorted(self.family), "Not all family members are recipients.")

    def test_no_self_loops(self):
        """Test that no one is matched to themselves."""
        for match in self.known_matches:
            giver, recipient = self.matches_encoded[match]
            self.assertNotEqual(giver, recipient, f"{giver} is matched to themselves.")

    def test_unique_recipients(self):
        """Test that each recipient is unique (no one gets multiple gifts)."""
        recipients = [self.matches_encoded[match][1] for match in self.known_matches]
        self.assertEqual(len(recipients), len(set(recipients)), "Some recipients are duplicated.")

    def test_unique_givers(self):
        """Test that each giver is unique (no one gives multiple gifts)."""
        givers = [self.matches_encoded[match][0] for match in self.known_matches]
        self.assertEqual(len(givers), len(set(givers)), "Some givers are duplicated.")

    def test_codes_are_unique(self):
        """Test that all codes are unique."""
        codes = [match[:6] for match in self.known_matches]
        self.assertEqual(len(codes), len(set(codes)), "Some codes are not unique.")

    def test_code_validation(self):
        """Test that the truncated code correctly identifies the match."""
        for original_match in self.known_matches:
            truncated_code = original_match[:6]
            # Find if any known match starts with truncated_code
            possible_matches = [m for m in self.known_matches if m[:6] == truncated_code]
            self.assertEqual(len(possible_matches), 1, f"Truncated code {truncated_code} matches multiple or no full codes.")
            self.assertEqual(possible_matches[0], original_match, f"Truncated code {truncated_code} does not match original.")

if __name__ == '__main__':
    unittest.main()
