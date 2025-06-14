import re


def regex_demo(text):
    """
    Demonstrates Regular Expression operations in Python.

    Time Complexity: Varies based on pattern (worst case O(n^2) for backtracking-heavy patterns)
    Space Complexity: O(1) or O(n) depending on matches returned

    Args:
        text (str): The input text to analyze.

    Returns:
        dict: Various regex results.
    """
    results = {}

    # 🔍 1. Find all email addresses in the text
    email_pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
    results["emails"] = re.findall(email_pattern, text)

    # 🔍 2. Extract phone numbers (basic format)
    phone_pattern = r"\b\d{3}[-.\s]??\d{3}[-.\s]??\d{4}\b"
    results["phone_numbers"] = re.findall(phone_pattern, text)

    # 🔍 3. Find all words starting with a capital letter
    capital_words_pattern = r"\b[A-Z][a-z]*\b"
    results["capital_words"] = re.findall(capital_words_pattern, text)

    # 🔍 4. Check if the text starts with a specific word
    start_pattern = r"^Hello"
    results["starts_with_hello"] = bool(re.match(start_pattern, text))

    # 🔍 5. Extract hashtags (e.g., #coding, #regex)
    hashtag_pattern = r"#\w+"
    results["hashtags"] = re.findall(hashtag_pattern, text)

    # 🔍 6. Replace URLs with "[LINK]"
    url_pattern = r"https?://\S+"
    results["text_with_links_replaced"] = re.sub(url_pattern, "[LINK]", text)

    return results


# 🚀 Example Usage
text = """
Hello everyone! My email is example123@gmail.com and my backup is hello.world@company.co.
Contact me at 123-456-7890 or visit https://example.com for more info.
Don't forget to follow #coding and #regex!
"""

results = regex_demo(text)

for key, value in results.items():
    print(f"{key}: {value}")
