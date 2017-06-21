import os, sys, argparse
from fuzzywuzzy import fuzz, process
from subprocess import call

# Parse command line arguments
parser = argparse.ArgumentParser()
parser.add_argument('-s', '--search', dest='search', action='store')
parser.add_argument('-e', '--edit', dest='edit', action='store')
parser.add_argument('-d', '--delete', dest='delete', action='store')
parser.add_argument('-n', '--note', dest='note', action='store')
parser.add_argument('-l', '--list', dest='list', action='store_true')
args = parser.parse_args()

ROOT_PATH = os.path.join(os.path.expanduser('~'), ".pynotes")

def _fuzzyfinder(note, limit):
    notes = [n for n in os.listdir(ROOT_PATH) if os.path.isfile(os.path.join(ROOT_PATH, n))]
    found = process.extract(note, notes, limit=limit)
    return found

def _delete(note):
    print("Looking for file: {}".format(note))
    print("Found: <note>")
    print("Deleting <note>")

def _search(note):
    results = _fuzzyfinder(note, limit=3)
    print("------------------")
    print("match %   |   note")
    print("------------------")
    for result in results:
        print("{0:3}: {1}".format(result[1], result[0]))

def _list():
    notes = [n for n in os.listdir(ROOT_PATH) if os.path.isfile(os.path.join(ROOT_PATH, n))]
    print(notes)
    for note in notes:
        note = note.strip('.')[0]
        print(note)

def _edit(note):
    print("Looking for file: {}".format(note))
    print("Opening <note> for editting")

def _create(note):
    note_path = os.path.join(ROOT_PATH, note + '.md')
    print("Creating: {}".format(note_path))
    
    call(['vim', note_path])
    with open(note_path, 'r') as fp:
        edited_message = fp.read()

    print(edited_message)

def main():
    if not os.path.exists(ROOT_PATH):
        os.makedirs(ROOT_PATH)

    if args.list:
        _list()
    elif args.search:
        _search(args.search)
    elif args.edit:
        _edit(args.edit)
    elif args.delete:
        _delete(args.delete)
    elif args.note:
        _create(args.note)

if __name__ == "__main__":
  main()
