"""Simple CLI app to translate archaic lyrics into modern language."""

import argparse
import re
from pathlib import Path

from archaic_dictionary import ARCHAIC_WORDS


def load_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def save_text(path: Path, text: str) -> None:
    path.write_text(text, encoding="utf-8")


def normalize_word(word: str) -> str:
    return word.lower()


def preserve_case(original: str, replacement: str) -> str:
    if original.isupper():
        return replacement.upper()
    if original[0].isupper():
        return replacement.capitalize()
    return replacement


def make_archaic_regex(dictionary: dict) -> re.Pattern:
    pattern = r"\b(" + "|".join(re.escape(word) for word in dictionary) + r")\b"
    return re.compile(pattern, flags=re.IGNORECASE)


def translate_text(text: str, dictionary: dict) -> str:
    regex = make_archaic_regex(dictionary)

    def replacement(match: re.Match) -> str:
        original_word = match.group(0)
        modern_word = dictionary[normalize_word(original_word)][0]
        return preserve_case(original_word, modern_word)

    return regex.sub(replacement, text)


def find_archaic_mentions(text: str, dictionary: dict) -> dict:
    counts: dict[str, int] = {}
    regex = make_archaic_regex(dictionary)
    for match in regex.finditer(text):
        word = normalize_word(match.group(0))
        counts[word] = counts.get(word, 0) + 1
    return counts


def build_report(counts: dict, dictionary: dict) -> str:
    if not counts:
        return "No archaic words found in the lyrics."

    lines = ["Archaic words found:"]
    for word, count in sorted(counts.items()):
        modern, meaning = dictionary[word]
        lines.append(f"- {word}: {count} time(s) -> {modern} ({meaning})")
    return "\n".join(lines)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Translate archaic song lyrics into modern words and save the result."
    )
    parser.add_argument(
        "--input",
        "-i",
        required=True,
        help="Path to the lyrics text file to analyze.",
    )
    parser.add_argument(
        "--output",
        "-o",
        help="Output path for the translated lyrics. If not provided, a file named translated_<input> is created.",
    )
    parser.add_argument(
        "--report",
        "-r",
        action="store_true",
        help="Print a short analysis report of archaic words found.",
    )
    return parser.parse_args()


def default_output_path(input_path: Path) -> Path:
    return input_path.with_name(f"translated_{input_path.name}")


def main() -> None:
    args = parse_args()
    input_path = Path(args.input)
    if not input_path.exists():
        raise FileNotFoundError(f"Input file does not exist: {input_path}")

    lyrics = load_text(input_path)
    translated = translate_text(lyrics, ARCHAIC_WORDS)
    output_path = Path(args.output) if args.output else default_output_path(input_path)
    save_text(output_path, translated)

    print(f"Translated lyrics saved to: {output_path}")
    if args.report:
        counts = find_archaic_mentions(lyrics, ARCHAIC_WORDS)
        print(build_report(counts, ARCHAIC_WORDS))


if __name__ == "__main__":
    main()
