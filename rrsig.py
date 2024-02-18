import time
from datetime import datetime, timezone
import base64
import os

def create_dummy_signature():
    # Generate a dummy digital signature
    dummy_signature = os.urandom(96)  # Match the signature size for ECDSAP384SHA384
    return base64.b64encode(dummy_signature).decode('utf-8')

def create_dummy_rrsig(signer_name, type_covered, algorithm, labels, original_ttl,
                       expiration, inception, key_tag):
    dummy_signature = create_dummy_signature()  # Generate a dummy digital signature

    # Format the signature start and end times
    inception_date = datetime.fromtimestamp(inception, timezone.utc).strftime('%Y%m%d%H%M%S')
    expiration_date = datetime.fromtimestamp(expiration, timezone.utc).strftime('%Y%m%d%H%M%S')

    # Create the RRSIG record
    rrsig_record = f"{type_covered} {algorithm} {labels} {original_ttl} {expiration_date} " \
                   f"{inception_date} {key_tag} {signer_name} {dummy_signature}"

    return rrsig_record

# Parameters for creating a dummy RRSIG record
signer_name = "a.test."  # Signer's zone
type_covered = "A"  # Record type being covered
algorithm = 14  # ECDSAP384SHA384 algorithm
labels = 3  # Number of labels in the signed domain name
original_ttl = 86400  # Original TTL of the signed record
current_time = int(time.time())
expiration = current_time + 7 * 24 * 3600  # Expiration time (one week from now)
inception = current_time - 24 * 3600  # Start time (one day ago)
key_tag = 6350  # Key tag

# Generate the dummy RRSIG records
for i in range(10):
    dummy_rrsig = create_dummy_rrsig(signer_name, type_covered, algorithm, labels,
                                     original_ttl, expiration, inception, key_tag)
    print(f"\t\t\t86400\tRRSIG\t{dummy_rrsig}")

