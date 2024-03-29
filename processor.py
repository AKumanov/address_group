import re
from collections import defaultdict
from unidecode import unidecode
import Levenshtein as lev
from fuzzywuzzy import fuzz
import usaddress

def normalize_address(address):
    # Convert to lowercase, transliterate non-Latin characters, and remove punctuation
    new_address = re.sub(r'[^\w\s]', '', unidecode(address.lower()))
    # Remove extra spaces
    new_address = re.sub(r'\s+', ' ', new_address)
    # Remove common stop words
    stop_words = ['ul', 'street', 'road', 'strasse', 'chaoyang', 'district', 'prc']
    new_address = ' '.join(word for word in new_address.split() if word not in stop_words)
    return new_address

def parse_address(address):
    # Use usaddress library to parse the address into its components
    try:
        parsed_address = usaddress.tag(address)[0]
    except usaddress.RepeatedLabelError:
        parsed_address = usaddress.tag(address)[0][0]
    # Join the components into a normalized address string
    normalized_address = ' '.join(parsed_address.values())
    return normalized_address


def group_people_by_address(people_dict):
    address_dict = defaultdict(list)
    
    for name, address in people_dict.items():
        # Normalizing address
        normalized_address = normalize_address(address)
        parsed_address = parse_address(address)
        
        # Check if normalized address is already in the dictionary
        found = False
        for key, value in address_dict.items():
            # Calculate Levenshtein distance between normalized addresses
            distance = lev.distance(key, normalized_address)
            
            # Check if addresses are similar based on Levenshtein distance and similarity of components
            if distance <= 20:  # Adjust the threshold as needed
                # Check if any components of the normalized address are similar to components of the existing address
                if any(fuzz.partial_ratio(component, key_component) >= 90 
                       for component in normalized_address.split()
                       for key_component in key.split()):
                    value.append(name)
                    found = True
                    break
        
        # If the normalized address is not found, add it to the dictionary
        if not found:
            address_dict[parsed_address].append(name)
    
    return address_dict

def clean_data(data):
    address_dict = {}
    for name, address in data[1:]:
        address_dict[name] = address
    return address_dict

