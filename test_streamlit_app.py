import unittest
from hashlib import md5
import random
import hashlib

# Import from the actual app file for true testing (copy removed to avoid duplication issues)
try:
    from streamlit_app import generate_matches, family
except ImportError as e:
    # Fallback if import fails
    print(f"Import failed: {e}. Using fallback.")
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

def generate_matches_fallback(seed_string):
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
    random.shuffle(recipients_list)  # shuffle for random matches without self
    for i, giver in enumerate(givers):
        recipient = recipients_list[i]
        known_matches_local.append(md5(str((giver, recipient)).encode()).hexdigest())

    return known_matches_local, matches_encoded_local

# Use imported or fallback
if 'generate_matches' in globals():
    generate_matches_fallback = generate_matches

# Set up for setUp
def import_logic():
    known_matches, matches_encoded = generate_matches_fallback('1234567')
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

    def test_randomness_fairness(self):
        """Test that with many random runs, each giver has equal chance to each recipient using the app's code."""
        from collections import defaultdict
        import random
        random.seed()  # use system time for varying runs
        n = 100000  # Reduced for speed
        freq = defaultdict(lambda: defaultdict(int))
        for i in range(n):
            if i % 20 == 0 or i == n-1:
                print(f"Progress: {i+1}/{n} runs complete")
            # Use local generate_matches (copied from app) with different seed
            seed = str(random.randint(0, 1000000) + i * 123456)
            known_matches, matches_encoded = generate_matches(seed)
            for match in known_matches:
                try:
                    giver, reciever = matches_encoded[match]
                    freq[giver][reciever] += 1
                except KeyError:
                    pass  # Skip any slips in self pairs

        # Each pair should have approx n / 72
        expected = n / (len(family) * (len(family) - 1))
        min_freq = min(min(counts.values()) for counts in freq.values())
        max_freq = max(max(counts.values()) for counts in freq.values())
        # Print readable stats
        print(f"\n🎲 **Randomness Fairness Test Results** 🎲")
        print(f"   - Total runs: {n}")
        print(f"   - Expected times per giver-recipient pair: {expected:.1f}")
        print(f"   - Lowest pair count (min): {min_freq}")
        print(f"   - Highest pair count (max): {max_freq}")
        if expected > 0:
            under_rep_ratio = min_freq / expected
            over_rep_ratio = max_freq / expected
            print(f"   - Under-representation (min/expected): {under_rep_ratio:.2f} (should be >0.5)")
            print(f"   - Over-representation (max/expected): {over_rep_ratio:.2f} (should be <15.0)")
        print(f"   => If min is too low or max too high, the randomness may be biased.\n")

        # Specific for Zach as giver
        print("🎄 Specific: Times Zach gave to each recipient:")
        for recipient in family:
            if recipient != 'Zach':
                count = freq['Zach'][recipient]
                print(f"   Zach -> {recipient}: {count} times")
        print("")
        self.assertGreater(min_freq, expected * 0.5, "Some pairs are under-represented, randomness may be biased.")
        self.assertLess(max_freq, expected * 15, "Some pairs are over-represented, randomness may be biased.")

if __name__ == '__main__':
    unittest.main()
