def validate_phone(phone):
    for ch in ['(', ')', '-', ' ']:
        phone = phone.replace(ch, '')
    return phone
