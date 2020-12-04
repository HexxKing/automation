#I worked on some of this lab with my midterm project group
import re


def get_document(path):
    with open(path, 'r') as file:
        text = file.read()
    return text


def parse_phone_numbers(text):
    pattern = r"((\(\d{3}\)|\d{3})?[\s-]?(\d{3})[\s-]?(\d{4})(x\d+)?)"
    numbers = re.findall(pattern,text)
    formatted_numbers = []
    for number in numbers:
        preamble = ""
        if not len(number[1]):
            preamble += "206"
        elif len(number[1]) == 5:
            preamble += number[1][1:4]
        else:
            preamble += number[1]

        current_number = f"{preamble}-{number[2]}-{number[3]}{number[4]}"
        if not current_number in formatted_numbers:
            formatted_numbers.append(current_number)
    formatted_numbers.sort()
    return formatted_numbers

def write_phone_numbers(soupy_mess_doc, existing_contacts):
    formatted_numbers = parse_phone_numbers(get_document(soupy_mess_doc))
    existing_contacts = parse_phone_numbers(get_document(existing_contacts))

    for contact in existing_contacts:
        if contact in formatted_numbers:
            formatted_numbers.remove(contact)

    target = "phone_numbers.txt"
    with open(target, 'w') as file:
        file.write("\n".join(formatted_numbers))


def parse_emails(text):
    pattern = r"(\w+(\.\w+)*@\w+\.\w+)"
    emails = re.findall(pattern, text)

    new_emails = []
    for email in emails:
        if not email[0] in new_emails:
            new_emails.append(email[0])

    new_emails.sort()
    return new_emails


def write_emails(soupy_mess_doc, existing_contacts):
    new_emails = parse_emails(get_document(soupy_mess_doc))
    existing_emails = parse_emails(get_document(existing_contacts))

    for email in existing_emails:
        if email in new_emails:
            new_emails.remove(email)

    target = "emails.txt"
    with open(target, 'w') as file:
        file.write("\n".join(new_emails))


if __name__ == "__main__":
    write_phone_numbers('assets/potential-contacts.txt', 'assets/existing-contacts.txt')
    write_emails('assets/potential-contacts.txt', 'assets/existing-contacts.txt')