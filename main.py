

from shamirsharesecret import SSS

import os 
import sys 
import Algo
def recovery_phase(participants):
    for participant in participants:
        if not participant.disqualified:
            # Compute shares for qualified participants
            sf_i = sum(participant.keys['public_key'] for p in participants if not p.disqualified) % q
            sf_prime_i = sum(participant.keys['private_key'] for p in participants if not p.disqualified) % q


            # Store the computed shares in the participant's keys
            participant.keys['sf_i'] = sf_i
            participant.keys['sf_prime_i'] = sf_prime_i
def mainrecovery2():
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

class Runner :

    def __init__(self, a, b,_c):
        self.a= a  
        self.b= b 
        self.c = _c
    

    def getData(self):
        return self.a, self.b , self.c 
    



if  __name__ =='__main__':
    ruuner  =Runner(17,19,23)
    S,N,K = ruuner.getData()
    sss = SSS(13, 17, 5, 3)
print("x = " + str(sss.choose_x()))
print("y = " + str(sss.generate_shares()))
# manual test
print("The key is " + str(sss.reconstruct_key([1, 3, 5], [8, 10, 11])))  # must return 13
# Calculate the share for different x
print("The share for x=1 is " + str(sss.calculate_y(1, [0,3,5], [sss.k, 10, 11])))
print("The share for x=3 is " + str(sss.calculate_y(3, [0,1,5], [sss.k, 8, 11])))
print("The share for x=5 is " + str(sss.calculate_y(5, [0,1,3], [sss.k, 8, 10])))

sss = SSS(1234, 1613, 6, 3)
print("x = " + str(sss.choose_x()))
print("y = " + str(sss.generate_shares()))
# manual test
print("The key is " + str(sss.reconstruct_key([1, 2, 3], [1494, 329, 965])))  # must return 1234
# Calculate the share for different x
print("The share for x=1 is " + str(sss.calculate_y(1, [0,2,3], [sss.k, 329, 965])))
print("The share for x=2 is " + str(sss.calculate_y(2, [0,1,3], [sss.k, 1494, 965])))
print("The share for x=3 is " + str(sss.calculate_y(3, [0,1,2], [sss.k, 1494, 329])))

sss = SSS(31318, 31847, 10, 5)
print("x = " + str(sss.choose_x()))
print("y = " + str(sss.generate_shares()))
# manual test
print(sss.reconstruct_key([413, 432, 451, 470, 489], [25439, 14847, 24780, 5910, 12734]))
print(sss.reconstruct_key([584, 432, 451, 470, 489], [21462, 14847, 24780, 5910, 12734]))
print(sss.reconstruct_key([584, 413, 565, 546, 489], [21462, 25439, 20806, 28578, 12734]))
print(sss.reconstruct_key([489, 565, 451, 470, 527], [12734, 20806, 24780, 5910, 12555]))
print(sss.reconstruct_key([508, 432, 584, 470, 489], [12492, 14847, 21462, 5910, 12734]))
# Calculate the share for different x
print("The share for x=413 is " + str(sss.calculate_y(413, [0, 432, 451, 470, 489], [sss.k, 14847, 24780, 5910, 12734])))
print("The share for x=584 is " + str(sss.calculate_y(584, [413, 432, 451, 470, 489], [25439, 14847, 24780, 5910, 12734])))
print("The share for x=508 is " + str(sss.calculate_y(508, [489, 565, 451, 470, 527], [12734, 20806, 24780, 5910, 12555])))
print("The share for x=0 is " + str(sss.calculate_y(0, [413, 432, 451, 470, 489], [25439, 14847, 24780, 5910, 12734])))

'''
    Share verification
'''

sss = SSS(1234, 94875355691, 9, 5)
x = [11, 22, 33, 44, 55, 66, 77, 88, 99]
y = [537048626, 89894377870, 65321160237, 18374404957, 24564576435, 87371334299, 60461341922, 10096524973, 81367619987]
print(sss.reconstruct_key([11, 22, 33, 44, 55],[537048626, 89894377870, 65321160237, 18374404957, 24564576435]))
print(sss.reconstruct_key([22, 33, 44, 55, 66],[89894377870, 65321160237, 18374404957, 24564576435, 87371334299]))
print(sss.reconstruct_key([33, 44, 55, 66, 77],[65321160237, 18374404957, 24564576435, 87371334299, 60461341922]))
print(sss.reconstruct_key([44, 55, 66, 77, 88],[18374404957, 24564576435, 87371334299, 60461341922, 10096524973]))
print(sss.reconstruct_key([55, 66, 77, 88, 99],[24564576435, 87371334299, 60461341922, 10096524973, 81367619987]))
print(sss.reconstruct_key([11, 22, 33, 44, 55, 66, 77, 88, 99], [537048626, 89894377870, 65321160237, 18374404957, 24564576435, 87371334299, 60461341922, 10096524973, 81367619987]))
print(sss.reconstruct_key([22, 33, 44, 55, 66, 77, 88, 99], [89894377870, 65321160237, 18374404957, 24564576435, 87371334299, 60461341922, 10096524973, 81367619987]))
print(sss.reconstruct_key([11, 22, 33, 44, 55, 66, 77, 88], [537048626, 89894377870, 65321160237, 18374404957, 24564576435, 87371334299, 60461341922, 10096524973]))

if sss.validate_shares(x, y):
    print("Shares are valid")
else:
    print("Shares are not valid")
    print("The defective share is " + str(sss.find_defective_share([11, 22, 33, 44, 55, 66, 77, 88, 99], [537048626, 89894377870, 65321160237, 18374404957, 24564576435, 87371334299, 60461341922, 10096524973, 81367619987])))

# Complaint Management Strategy Algorithm
    complaint_manager =Algo.ComplaintManager()
    complaint_manager.log_complaint(1, "low", "Node 1 is running slow")
    complaint_manager.log_complaint(2, "high", "Node 2 crashed")
    parts = ["abcde", "fghij", "klmno", "pqrst"]  # Exemple de parts
    random_key = complaint_manager.generate_key(parts)  # Générer une clé aléatoire à partir des parts
    print("Clé choisie au hasard   :", random_key)

    complaint_manager.publish_key(parts, random_key)
    votes = {"Participant 1": 10, "Participant 2": 15, "Participant 3": 7, "Participant 4": 15,
             "Participant 5": 8}

    max_votes = complaint_manager.find_max_votes(votes)  # Trouver les participants avec le maximum de votes
    print("Participant(s) avec le maximum de votes :", max_votes)
    malicious_participants = complaint_manager.disqualify_participants(votes,
                                                                       12)  # Disqualifier les participants qui ont plus de 12 votes
    if len(malicious_participants) > 0:
        print("Les participants malhonnêtes sont :", malicious_participants)
    else:
        print("Aucun participant malhonnête n'a été identifié.")
    parts2 = ["abcde", "fghij", "klmno", "pqrst"]  # Exemple de parts
    url = "https://example.com/api/parts"  # Exemple d'URL de serveur distant
    complaint_manager.store_parts(parts, "parts.txt")
    complaint_manager.send_parts(parts2, url)
    complaint_manager.resolve_complaints()


    #recovery phase

    not_qualifiesd = complaint_manager.not_disqualify_participants(votes,12)

    print ( f" \n not_qualifiesd  particiapants {not_qualifiesd}  \n")
    QUAL = [i  % 3 for i in  not_qualifiesd]  # Set of non-disqualified participants
    sf = [12, 15, 10, 8, 14]  # Placeholder values for sf[j] for all j
    sf_prime = [9, 13, 18, 6, 11]  # Placeholder values for sf_prime[j] for all j
    sg = [7, 17, 21, 19, 16]  # Placeholder values for sg[j] for all j
    sg_prime = [20, 25, 22, 24, 23]  # Placeholder values for sg_prime[j] for all j
    sh = [30, 27, 29, 26, 28]  # Placeholder values for sh[j] for all j
    sh_prime = [33, 31, 36, 32, 34]  # Placeholder values for sh_prime[j] for all j
    q = 37  # Placeholder value for q (modulus)

    sfi, sf_prime_i, sgi, sg_prime_i, shi, sh_prime_i = complaint_manager. compute_shares(QUAL, sf, sf_prime, sg, sg_prime, sh, sh_prime,q)
    print(
        f"Computed shares for Pi: sfi = {sfi}, sf_prime_i = {sf_prime_i}, sgi = {sgi}, sg_prime_i = {sg_prime_i}, shi = {shi}, sh_prime_i = {sh_prime_i}")

    # security
    honest_shares = [12, 15, 10, 8, 14]  # Placeholder values for honest shares
    t = 2  # Placeholder value for t (maximum number of dishonest participants)
    if complaint_manager.check_unique_secret_key(honest_shares):
        secret_key = complaint_manager.recover_secret_key(honest_shares, t)
        print(f"Recovered secret key: {secret_key}")
    else:
        print("Error: The shares provided do not define the same unique secret key.")

    honest_public_keys = [(12, 34, 56), (12, 34, 56), (12, 34, 56)]  # Placeholder values for honest public keys
    if complaint_manager.check_same_public_key(honest_public_keys):
        print("All honest participants have the same public key.")
    else:
        print("Error: Not all honest participants have the same public key.")

    secret_key = (12, 34, 56, 78, 90)  # Placeholder value for the secret key
    q = 100  # Placeholder value for q (modulus)
    if complaint_manager.check_uniform_distribution(secret_key, q):
        print("The secret key is uniformly distributed in Zq.")
    else:
        print("Error: The secret key is not uniformly distributed in Zq.")

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
        # Randomly select a participant to make a complaint
        complainant = random.choice(participants)
        accused = random.choice(participants)

        # Simulate the complaint management process
        if accused == complainant:
            # Disqualify the accused participant if the complainant accuses themselves
            accused.disqualified = True
        else:
            # Count the number of complaints against the accused participant
            complaint_count = sum(1 for participant in participants if participant == accused)
            if complaint_count >= complaint_threshold:
                accused.disqualified = True


    def main():
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
        print("Qualified Participants:")
        for participant in qualified_participants:
            print(f"Participant {participant.id}: Keys - {participant.keys}")


    main()
    Algo.mainrecovery()
    mainrecovery2()
    from  participant import  Participantrecoery,mainrec
    mainrec()
