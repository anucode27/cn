def crc_encode():
    # Input Polynomial and Frame from user
    polynomial = input("ENTER POLYNOMIAL: ")
    frame = input("ENTER THE FRAME: ")

    m = len(polynomial)
    n = len(frame)

    # Eliminate leading zeros in the polynomial
    for i in range(m):
        if polynomial[i] == '1':
            polynomial = polynomial[i:]
            m = len(polynomial)
            break

    # Adjust the polynomial to remove leading zeros
    polynomial = list(polynomial)

    # Create a list for the full frame with appended zeros for CRC calculation
    cl = m + n - 1
    c = list(frame) + ['0'] * (cl - n)  # Add n-1 zeros at the end of frame

    # CRC Remainder Calculation
    for i in range(n):
        if c[i] == '1':
            for j in range(m):
                c[i + j] = '0' if polynomial[j] == c[i + j] else '1'

    # Copy original frame data into the beginning of c[] for the final message
    c[:n] = frame

    # Convert c to a string for final message
    message = ''.join(c)
    print(f"\nTHE MESSAGE IS: {message}")

# Run the CRC encoder
crc_encode()
