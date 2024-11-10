import re


def extract_into_set(file_path, patent_ids):
    pattern = r"US \d+[A-Z]* \w\d+"
    file_path = 'id_document_patent.txt'
    with open(file_path, 'r') as file:
        text = file.read()
        matches = re.findall(pattern, text)
        for match in matches:
            patent_ids.add(match)
    return(patent_ids)
    
file_path = 'id_document_patent.txt'
s=set()
print(extract_into_set('id_document_patent.txt', s))

