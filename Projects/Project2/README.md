# Project 2: Song Lyrics Analyzer

This project is a simple lyrics analyzer that reads an input text file, identifies archaic words, and translates them into modern equivalents.

## Features

- Load song lyrics from a text file
- Detect archaic words such as `thou`, `thee`, `hath`, and `wherefore`
- Translate archaic words to modern English
- Save the translated lyrics to a new text file
- Optionally print a short report of archaic words found

## Usage

From the project root, run:

```bash
python code/lyrics_analyzer.py --input code/sample_song.txt --report
```

To customize the output file name:

```bash
python code/lyrics_analyzer.py --input code/sample_song.txt --output code/translated_song.txt --report
```

## Notes

- The dictionary is defined in `code/archaic_dictionary.py`.
- This app works with plain text lyrics files and preserves capitalization when replacing words.
