import numpy as np
q = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71}



# Distributed Multi-Key Generation Protocol
def generate_key_part(node_id):
    # Simulated key generation process (Replace with your actual algorithm)
    key_part = np.random.randint(0, 256, size=32, dtype=np.uint8)
    print(f"Node {node_id} generated key part: {key_part}")
    return key_part


def combine_key_parts(key_parts):
    # Simple XOR combination of key parts (Replace with your actual algorithm)
    combined_key = key_parts[0] ^ key_parts[1]
    print(f"Combined Key: {combined_key}")
    return combined_key


# Complaint Management Strategy Algorithm
class ComplaintManager:
    def __init__(self):
        self.complaints = []

    def log_complaint(self, node_id, severity, description):
        self.complaints.append((node_id, severity, description))
        print(f"Complaint logged - Node {node_id}, Severity: {severity}, Description: {description}")

    def store_parts(self, parts, file_name):
        with open(file_name, "w") as f:
            for part in parts:
                f.write(part + "\n")
                print(f"L'ensemble des parts a été stocké dans le fichier {file_name} !")

    def send_parts(self, parts, url):

        import requests
        data = {"parts": parts}
        response = requests.post(url, data=data)
        if response.status_code == 200:
            print("L'ensemble des parts a été envoyé avec succès !")
        else:
            print("Erreur lors de l'envoi de l'ensemble des parts...")

    def resolve_complaints(self):
        # Simulated complaint resolution (Replace with your actual algorithm)
        for complaint in self.complaints:
            node_id, severity, description = complaint
            if severity == "low":
                print(f"Complaint from Node {node_id} resolved with low priority.")
            elif severity == "medium":
                print(f"Complaint from Node {node_id} resolved with medium priority.")
            else:
                print(f"Complaint from Node {node_id} resolved with high priority.")
        self.complaints = []  # Clear resolved complaints

    def generate_key(self, parts):

        key = ""
        for i in range(len(parts[0])):
            char_set = set(part[i] for part in parts)
            key += random.choice(list(char_set))
        return key

    def publish_key(self, parts, key):

        with open("key.txt", "w") as f:
            f.write(key)
        print(f"La clé ({key}) a été publiée avec succès !")

    def find_max_votes(self, votes):

        max_votes = max(votes.values())
        max_participants = [participant for participant, num_votes in votes.items() if num_votes == max_votes]
        if len(max_participants) == 1:
            return max_participants[0]
        else:
            return max_participants

    def disqualify_participants(self, compplaints, threshold):

        disqualified = [participant for participant, num_complaint in compplaints.items() if num_complaint > threshold]
        return disqualified

    def not_disqualify_participants(self, compplaints, threshold):

        not_disqualified = [num_complaint for participant, num_complaint in compplaints.items() if num_complaint < threshold]
        return not_disqualified

    # Recovery Phase: Each participant Pi in QUAL computes the shares
    def compute_shares(self,QUAL, sf, sf_prime, sg, sg_prime, sh, sh_prime, q):
        sfi = sum(sf[j] % q for j in QUAL) % q
        sf_prime_i = sum(sf_prime[j] % q for j in range(len(QUAL))) % q
        sgi = sum(sg[j] % q for j in range(len(QUAL))) % q
        sg_prime_i = sum(sg_prime[j] % q for j in range(len(QUAL))) % q
        shi = sum(sh[j] % q for j in QUAL) % q
        sh_prime_i = sum(sh_prime[j] % q for j in range(len(QUAL))) % q

        return sfi, sf_prime_i, sgi, sg_prime_i, shi, sh_prime_i

    # Security Requirement C1: Check if any set of (t + 1) shares provided by honest participants defines the same unique secret key sk = (x1, x2, y1, y2, z)
    def check_unique_secret_key(self,shares):
        unique_keys = set(shares)
        return len(unique_keys) == 1

    # Security Requirement C2: Check if there exists an efficient algorithm to recover the unique secret key sk even if at most (t - 1) invalid shares are submitted by dishonest participants.
    def recover_secret_key(self,honest_shares, t):
        # Implement an algorithm to recover the secret key from the honest shares
        # You might need to use polynomial interpolation or other mathematical methods here
        # If t invalid shares are detected, return an error or handle the situation accordingly
        pass

    # Security Requirement C3: Check if all honest participants have the same public key pk
    def check_same_public_key(self,honest_public_keys):
        same_key = len(set(honest_public_keys)) == 1
        return same_key

    # Security Requirement C4: Check if the secret key sk is uniformly distributed in Zq.
    def check_uniform_distribution(self,sk, q):
        # Implement a method to check if the secret key components are within the range of Zq
        # Return True if the distribution is uniform, otherwise False
        pass


import random

class Participant:
    def __init__(self, id):
        self.id = id
        self.keys = {}  # Dictionary to store the participant's generated keys
        self.disqualified = False

def generate_key():
    # Simulate the generation of a key (replace this with actual cryptographic operations)
    return random.randint(1, 100)

def distribute_keys(participants):
    # Simulate the distribution of keys among participants
    for participant in participants:
        for key_type in ['public_key', 'private_key']:
            participant.keys[key_type] = generate_key()

def complaint_management_phase(participants, complaint_threshold):
    # Simulate the complaint management process (same as before)
    pass

def recovery_phase(participants):
    for participant in participants:
        if not participant.disqualified:
            # Compute shares for qualified participants
            sf_i = sum(participant.keys['public_key'] for p in participants if not p.disqualified) % len(q)
            sf_prime_i = sum(participant.keys['private_key'] for p in participants if not p.disqualified) % len(q)


            # Store the computed shares in the participant's keys
            participant.keys['sf_i'] = sf_i
            participant.keys['sf_prime_i'] = sf_prime_i


def mainrecovery():
    num_participants = 5
    complaint_threshold = 2

    participants = [Participant(i) for i in range(num_participants)]

    # Setup Phase: Generate and distribute keys
    distribute_keys(participants)

    # Complaint Management Phase
    for _ in range(num_participants):
        complaint_management_phase(participants, complaint_threshold)

    # Recovery Phase
    qualified_participants = [participant for participant in participants if not participant.disqualified]
    recovery_phase(qualified_participants)

    print("Qualified Participants with Shares:")
    for participant in qualified_participants:
        print(f"Participant {participant.id}: Shares - {participant.keys}")
