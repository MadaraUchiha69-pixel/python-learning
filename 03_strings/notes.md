🔥 PART 1 — ESCAPE SEQUENCES (ONLY THE USEFUL ONES)

Stop memorizing 50 symbols. Only these 8 matter in real code.

✔️ 1. \n — New line

Used everywhere.

print("Hello\nWorld")

✔️ 2. \t — Tab

Useful for formatting logs, CLI output.

print("Name:\tShivansh")

✔️ 3. \' and \" — Quote inside a quote

Absolutely required for parsing JSON or writing text patterns.

print("He said \"hello\"")

✔️ 4. \\ — Backslash

When dealing with file paths or Windows systems, this is essential.

path = "C:\\Users\\Name"

✔️ 5. \r — Carriage return

Used when writing progress bars in terminals (E-ANID logging).

print("Loading...\rDone")

✔️ 6. \b — Backspace

Rare, but used in ASCII terminal animations.

✔️ 7. \v — Vertical tab

Only relevant in special formatting or legacy systems.

✔️ 8. \a — Bell (sound)

Not essential but you’ll see it in old terminal code.

🔥 PART 2 — STRING METHODS YOU ACTUALLY NEED

I’m not giving you school-level junk.
These functions matter for data cleaning, logs, text parsing, API development, input sanitization, ML preprocessing, etc.

🚀 TOP 10 MUST-KNOW STRING METHODS for practical coding
1. .strip()

Removes extra spaces — CRITICAL in input, logs, API data, scrapers.

name = "  Shivansh  "
name = name.strip()

2. .lower() / .upper()

Standard for case-insensitive checks (login systems, NLP, data cleaning).

email = email.lower()

3. .replace()

Used a LOT in sanitization, preprocessing, cleaning messy strings.

text = text.replace("malware", "safe")

4. .split()

Top 3 most used string function.
Breaks text into parts — super important in parsing logs or CLI input.

words = text.split(" ")

5. .join()

Efficient way to join lists (much faster than looping).

sentence = " ".join(words)

6. .startswith() / .endswith()

Used in filtering file extensions, API checks, URLs, tokens.

if filename.endswith(".txt"):

7. .find() / .index()

Locating substrings — used everywhere in scrapers and scanners.

pos = text.find("password")

8. .count()

Count words, characters, patterns — useful in NLP.

text.count("error")

9. .isdigit() / .isalpha()

Validation — login, OTP, form inputs, security filters.

if otp.isdigit():

10. .format() or f-strings

Critical for logging, output, API payloads.

name = "Shivansh"
print(f"Hello {name}")

🔥 EXTRA: Advanced String Tools You’ll Need Later for E-ANID

If you want to build a cybersecurity/AI project, you will eventually need:

1. .encode() and .decode()

For dealing with bytes, hashing, encryption, APIs.

b = "hello".encode()

2. json.loads() and json.dumps()

For parsing JSON from APIs (100% essential).

3. re (Regular Expressions)

For pattern matching, input sanitization, URL extraction, log parsing.

Example:

import re
emails = re.findall(r"[a-zA-Z0-9_.]+@[a-zA-Z]+\.[a-zA-Z]+", text)
