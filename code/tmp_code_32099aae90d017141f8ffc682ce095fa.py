import random
import os

# Define the departments and roles within the Shinobi-z company
departments = {
    'Executive': ['CEO', 'CFO', 'CTO'],
    'Engineering': ['Lead Engineer', 'Software Developer', 'Hardware Engineer', 'Test Engineer'],
    'Sales': ['Sales Director', 'Account Manager', 'Sales Representative'],
    'Marketing': ['Marketing Director', 'Content Strategist', 'SEO Specialist'],
    'Customer Support': ['Support Manager', 'Technical Support Specialist']
}

# Function to generate a random name
def generate_name():
    first_names = ['Alex', 'Jamie', 'Jordan', 'Taylor', 'Morgan', 'Casey', 'Riley', 'Quinn']
    last_names = ['Smith', 'Johnson', 'Williams', 'Brown', 'Jones', 'Garcia', 'Miller', 'Davis']
    return f"{random.choice(first_names)} {random.choice(last_names)}"

# Function to generate an email address
def generate_email(name, department):
    domain = 'shinobi-z.com'
    name_parts = name.lower().split()
    return f"{name_parts[0][0]}{name_parts[1]}@{domain}"

# Create the directory for the organizational structure
os.makedirs('Shinobi-z/Organizational_Structure', exist_ok=True)

# Generate the organizational structure and save to a text file
with open('Shinobi-z/Organizational_Structure/structure.txt', 'w') as file:
    for department, roles in departments.items():
        file.write(f"{department} Department:\n")
        for role in roles:
            name = generate_name()
            email = generate_email(name, department)
            file.write(f"  {role}: {name}, Email: {email}\n")
        file.write("\n")

print("The organizational structure for Shinobi-z has been created and saved to 'Shinobi-z/Organizational_Structure/structure.txt'")