import re

def extract_into_set(file_path, patent_ids):
    pattern = r"US \d+[A-Z]* \w\d+"  # Regex to match patent IDs
    with open(file_path, 'r') as file:
        text = file.read()
        matches = re.findall(pattern, text)  # Find all matches
        for match in matches:
            patent_ids.add(match)  # Add matches to the set
    return patent_ids

file_path = 'id_document_patent.txt'

s = set()
extract_into_set(file_path, s)
def check(s):
    user_name = input("Enter your name: ")
    file_name = f"{user_name}_patentids.txt"
    query = input("What's your query list: ")
    with open(file_name, 'a') as outfile:
        outfile.write(f"{query}:\n")
    while True:
        user_input = input("Enter a string (or type 'STOP' to quit): ")
        if user_input.strip().upper() == "STOP" or user_input.strip() == "":
            print("Exiting the program...")
            break

        if user_input not in s and user_input is not None:
            s.add(user_input)
            with open(file_name, 'a') as outfile:
                outfile.write(f"{user_input}\n")
            print(f"'{user_input}' has been saved to {file_name}")
        else:
            print(f"'{user_input}' is in the set. Try again!")
            
print(len(s))

    

