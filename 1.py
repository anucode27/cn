def char_stuffing(data, flag='F', escape='E'):
    stuffed_data = ''

    for char in data:
        if char == flag or char == escape:
            stuffed_data += escape + char
        else:
            stuffed_data += char

    return flag + stuffed_data + flag


data = 'HelloF, Eearth!'

stuffed_data = char_stuffing(data)

print("Original Data:", data)
print("Stuffed Data:", stuffed_data)
