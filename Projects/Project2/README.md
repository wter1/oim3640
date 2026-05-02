# Project 2: Song Lyrics Analyzer

This project is a simple lyrics analyzer that reads an input text file, identifies archaic words, and translates them into modern equivalents.

## Features

- Load song lyrics from a text file
- Detect archaic words such as `jive`, `cat`, `pad`, and `gams`
- Translate archaic words to modern English
- Save the translated lyrics to a new text file
- Optionally print a short report of archaic words found

## Usage

From the project root, run:

```bash
python Projects/Project2/code/lyrics_analyzer.py --input Projects/Project2/code/sample_song.txt --report #idk if the root will be different for who ever runs the code, but just make sure its where you're loading in your .txt files

#If you did it this way the output will still give a translated version but the naming is defaulted to what ever the computer wants to do.
```

To customize the output file name:

```bash
python Projects/Project2/code/lyrics_analyzer.py --input Projects/Project2/code/sample_song.txt --output Projects/Project2/code/translated_song.txt --report
```

To fetch lyrics from the web using artist and song title:

```bash
python Projects/Project2/code/lyrics_analyzer.py --artist "Nat King Cole" --title "Unforgettable" --report
```

The app uses an online lyrics API to retrieve song text when `--artist` and `--title` are provided.

## Notes

- The dictionary is defined in `code/archaic_dictionary.py`.
- This app works with plain text lyrics files and preserves capitalization when replacing words.
