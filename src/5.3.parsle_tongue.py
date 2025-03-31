import re

def parsle_tongue(file_path):

    """
    the function try to extract hidden sentence from binary file

    params: path to file
    return: hidden sentence
    """



    pattern = re.compile(rb'[a-z]{5,}!')
    chunk_size = 4096

    messages = set()

    with open(file_path, 'rb') as file:
        data = b''
        while chunk := file.read(chunk_size):
            data += chunk
            matches = pattern.findall(data)
            for match in matches:
                messages.add(match.decode())

            data = data[-(len(pattern.pattern) * 2):]

    return messages

if __name__ == "__main__":
    file_path = 'logo.jpg'
    secret_messages = parsle_tongue(file_path)
    for message in secret_messages:
        print(message)


