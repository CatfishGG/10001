import base64

kitnibaarlunddediya = 10
def decode_lundediya_times(text, iterations=kitnibaarlunddediya):
    decoded_lund = text.encode('utf-8')  # Convert to bytes
    for _ in range(iterations):
        decoded_lund = base64.b64decode(decoded_lund)
    return decoded_lund.decode('utf-8')  # Return as a string

# Read the encoded text from the file
with open("lunded.txt", "r") as file:
    encoded_text = file.read()

# Decode 50 times (assuming matching the encoding process)
decoded_lund = decode_lundediya_times(encoded_text)

print("decoded-lunded text:", decoded_lund)
