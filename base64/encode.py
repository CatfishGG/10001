import base64

kitnebaarlunddu = 10

def encode_lund_times(text, iterations=kitnebaarlunddu):
    encoded_lund = text.encode('utf-8') 
    for _ in range(iterations):
        encoded_lund = base64.b64encode(encoded_lund)
    return encoded_lund.decode('utf-8')


lund = "kya lund encode krega lawde"

# Encode 50 times
encoded_lund = encode_lund_times(lund)

# Save the result to a file
with open("lunded.txt", "w") as file:
    file.write(encoded_lund)

print("lunded text saved to 'lunded.txt'")
