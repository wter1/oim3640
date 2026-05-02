"""Simple CLI app to translate archaic lyrics into modern language."""

import argparse
import json
import re
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path
from typing import Optional

from archaic_dictionary import ARCHAIC_WORDS


def load_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def save_text(path: Path, text: str) -> None:
    path.write_text(text, encoding="utf-8")


def fetch_lyrics_from_api(artist: str, title: str) -> str:
    encoded_artist = urllib.parse.quote(artist.strip())
    encoded_title = urllib.parse.quote(title.strip())
    url = f"https://api.lyrics.ovh/v1/{encoded_artist}/{encoded_title}"
    request = urllib.request.Request(url, headers={"User-Agent": "lyrics-analyzer/1.0"})

    try:
        with urllib.request.urlopen(request, timeout=10) as response:
            if response.status != 200:
                raise ConnectionError(f"Failed to fetch lyrics: HTTP {response.status}")
            payload = json.load(response)
    except urllib.error.HTTPError as exc:
        raise ConnectionError(f"API request failed: {exc.code} {exc.reason}")
    except urllib.error.URLError as exc:
        raise ConnectionError(f"Network error while fetching lyrics: {exc.reason}")

    lyrics = payload.get("lyrics")
    if not lyrics:
        raise ValueError("No lyrics were returned by the API.")
    return lyrics


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
        help="Path to the lyrics text file to analyze.",
    )
    parser.add_argument(
        "--artist",
        help="Artist name for API lyrics lookup.",
    )
    parser.add_argument(
        "--title",
        help="Song title for API lyrics lookup.",
    )
    parser.add_argument(
        "--output",
        "-o",
        help="Output path for the translated lyrics. If not provided, a file named translated_<input> or translated_<artist>_<title>.txt is created.",
    )
    parser.add_argument(
        "--report",
        "-r",
        action="store_true",
        help="Print a short analysis report of archaic words found.",
    )
    return parser.parse_args()


def default_output_path(input_path: Optional[Path] = None, artist: Optional[str] = None, title: Optional[str] = None) -> Path:
    if input_path is not None:
        return input_path.with_name(f"translated_{input_path.name}")

    safe_artist = urllib.parse.quote(artist or "unknown", safe="")
    safe_title = urllib.parse.quote(title or "lyrics", safe="")
    return Path(f"translated_{safe_artist}_{safe_title}.txt")


def main() -> None:
    args = parse_args()

    if args.input and (args.artist or args.title):
        raise ValueError("Use either --input or --artist/--title, not both.")

    if args.input:
        input_path = Path(args.input)
        if not input_path.exists():
            raise FileNotFoundError(f"Input file does not exist: {input_path}")
        lyrics = load_text(input_path)
        output_path = Path(args.output) if args.output else default_output_path(input_path=input_path)
    elif args.artist and args.title:
        print(f"Fetching lyrics for '{args.artist}' - '{args.title}' from the API...")
        lyrics = fetch_lyrics_from_api(args.artist, args.title)
        output_path = Path(args.output) if args.output else default_output_path(artist=args.artist, title=args.title)
    else:
        raise ValueError("Either --input or both --artist and --title must be provided.")

    translated = translate_text(lyrics, ARCHAIC_WORDS)
    save_text(output_path, translated)

    print(f"Translated lyrics saved to: {output_path}")
    if args.report:
        counts = find_archaic_mentions(lyrics, ARCHAIC_WORDS)
        print(build_report(counts, ARCHAIC_WORDS))


if __name__ == "__main__":
    main()
