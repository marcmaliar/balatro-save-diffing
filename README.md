# Balatro Save File Diffing

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

## Background of the problem

I had a great Balatro gold stake run. I never beat gold stake before so I was very excited.

However, I made a careless mistake and lost. My save file was deleted because I lost and I was quite frustrated.

I remembered the state of the game at the time. I decided to write a software that generate a Balatro save file.

I looked online for a program that could generate a Balatro save file. I wanted to recreate the state of the game right before I lost it.

## This project

However, there is nothing like that online. The closest thing is the [Balatro Save Loader](https://github.com/WilsontheWolf/balatro-save-loader) tool.

This website decompiles the Balatro save file into a JSON (whose format is a compressed form of a Lua table). I basically copied this into diff.py but in Python. Thank you to the author of this project.

Then, my plan was to

- poll the Balatro save file to see if there are any changes
- if so, save the decompiled JSON into the saves folder
- diff the last JSON with the current JSON and put that into diffs

Why do I care about the diffs? If I want to write something that can generate a save, I need to know how to create a JSON according to how I want the game state to look like. By looking at the diffs, I can figure out how to modify the game state into what I want.

However, apparently diffing JSON objects is not super easy. I wanted to generate an HTML files for the diffs using difflib.HtmlDiff but this was not working.

At some point I gave up and beat gold stake a couple runs later.

## Installation

1. Clone the repository
2. Install the dependencies: `pip install -r requirements.txt`

## Usage

Run main.py

## License

This project is licensed under the [MIT License](LICENSE).

## Contact

- Author: Marc Maliar
- GitHub: [Your GitHub Profile](https://github.com/marcmaliar)
