import visen

def check_pattern_in_text(pattern, text):
    """Check if pattern is in text"""

    pattern = visen.clean_tone(pattern)
    text = visen.clean_tone(text)
    return pattern in text


def standardize_tone(text):
    """Standardize Vietnamese tone"""

    return visen.clean_tone(text)