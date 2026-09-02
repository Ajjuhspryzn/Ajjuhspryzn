from datetime import date
from pathlib import Path
import re

# Your 10 quotes
quotes = [
    (
        "Do not be sorry. Be better.",
        "Kratos | God of War"
    ),
    (
        "Death can have me when it earns me.",
        "Kratos | God of War"
    ),
    (
        "Arise.",
        "Sung Jinwoo | Solo Leveling"
    ),
    (
        "Surpass your limits.",
        "Yami Sukehiro | Black Clover"
    ),
    (
        "Set your heart ablaze!",
        "Kyojuro Rengoku | Demon Slayer"
    ),
    (
        "Throughout heaven and earth, I alone am the honored one.",
        "Satoru Gojo | Jujutsu Kaisen"
    ),
    (
        "If you don’t fight, you can’t win!",
        "Eren Yeager | Attack on Titan"
    ),
    (
        "Sometimes feelings are easier to hide in another language.",
        "Alisa Kujou (Alya) | Alya Sometimes Hides Her Feelings in Russian"
    ),
    (
        "Dying to win and risking death to win are completely different.",
        "Satoru Gojo | Jujutsu Kaisen"
    ),
    (
        "Do not seek strength. Build it.",
        "Kratos | God of War"
    )
]

# Fixed starting date
START_DATE = date(2026, 9, 2)

# Calculate how many days have passed
today = date.today()
days_passed = (today - START_DATE).days

# Rotate through the quotes cyclically
quote_index = days_passed % len(quotes)

quote, author = quotes[quote_index]

# Read README
readme_path = Path("README.md")
readme = readme_path.read_text(encoding="utf-8")

# Replace the content between the quote markers
new_quote_section = f"""<!-- DAILY_QUOTE_START -->
> “{quote}”  
> — **{author}**
<!-- DAILY_QUOTE_END -->"""

pattern = r"<!-- DAILY_QUOTE_START -->.*?<!-- DAILY_QUOTE_END -->"

if re.search(pattern, readme, flags=re.DOTALL):
    readme = re.sub(
        pattern,
        new_quote_section,
        readme,
        flags=re.DOTALL
    )
else:
    print("Daily quote markers were not found in README.md")
    raise SystemExit(1)

# Save README
readme_path.write_text(readme, encoding="utf-8")

print(f"Today's quote: {quote}")
print(f"Author: {author}")
print(f"Quote number: {quote_index + 1}")
