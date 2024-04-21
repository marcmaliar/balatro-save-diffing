
import difflib
import json
import datetime
import time
from convert import process_file
import webbrowser
import os
import shutil
from diff import generate_html_diff

# Initialize the current_save variable
try:
    with open(f"/Users/mmaliar/src/python/balatro/saves/raw.jkr", 'rb') as file:
        old_raw = file.read()
        old_save = process_file(old_raw)
except Exception as e:
    # raise Exception(e)
    print(e)
    old_raw = None
    old_save = {}

delete = True
if delete:
    # Delete the diffs directory if it exists
    diffs_dir = '/Users/mmaliar/src/python/balatro/diffs'
    if os.path.exists(diffs_dir):
        shutil.rmtree(diffs_dir)

    # Delete the saves directory if it exists
    saves_dir = '/Users/mmaliar/src/python/balatro/saves'
    if os.path.exists(saves_dir):
        shutil.rmtree(saves_dir)

    # Create the diffs directory
    os.mkdir(diffs_dir)

    # Create the saves directory
    os.mkdir(saves_dir)

# Infinite loop
while True:
    # Open the file and load it as JSON
    try:
        with open('/Users/mmaliar/Library/Application Support/Balatro/1/save.jkr', 'rb') as file:
            raw = file.read()
            save = process_file(raw)

            # Check if the save is identical to the current_save
            if raw == old_raw:
                pass  # print("Save is identical to current_save")
            else:
                # Set the current_save to this save
                # old_formatted = json.dumps(old_save, indent=4)
                # new_formatted = json.dumps(save, indent=4)

                # Save it again to the saves folder with a timestamp
                timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
                save_file = \
                    f"/Users/mmaliar/src/python/balatro/saves/save_{timestamp}.json"

                with open(save_file, 'w') as file:
                    json.dump(save, file, indent=4)
                with open(f"/Users/mmaliar/src/python/balatro/saves/raw.jkr", 'wb') as file:
                    file.write(raw)
                print(f'Save is different. New save file created: {save_file}')

                # Create a difflib.HtmlDiff() object
                # d = difflib.HtmlDiff()

                # Generate the HTML diff
                diff = generate_html_diff(old_save, save)

                # Write the diff to an HTML file
                def stringify(diff):
                    if isinstance(diff, list):
                        return [stringify(d) for d in diff]
                    elif isinstance(diff, dict):
                        return {str(k): stringify(v) for k, v in diff.items()}
                    elif isinstance(diff, set):
                        return {stringify(d) for d in diff}
                    else:
                        return diff
                with open(f'/Users/mmaliar/src/python/balatro/diffs/diff_{timestamp}.txt', 'w') as file:
                    diff = stringify(diff)
                    json.dump(diff, file, indent=4)
                # webbrowser.open(
                #    f'/Users/mmaliar/src/python/balatro/diffs/diff_{timestamp}.html')

                old_raw = raw
                old_save = save
    except Exception as e:
        print(e)
        pass
    # Wait for a certain amount of time before checking again
    time.sleep(0.5)  # Adjust the delay as needed
