# OBS Soundboard Script

## Description
This script is designed to create a soundboard in OBS Studio, allowing users to play different sounds using customizable hotkeys. The script uses the OBS Python scripting module (`obspython`) to interact with OBS Studio and manage hotkeys.

## Features
- Supports up to 10 customizable sound buttons.
- Each button can be associated with a specific sound file.
- Custom hotkeys trigger the playback of corresponding sounds.

## Usage
1. Set the sound file for each button by updating the file paths in the `e1` to `e10` instances.
2. Customize the hotkeys associated with each button by modifying the `Hotkey` instances (`h1` to `h10`) in the `script_load` function.
3. Run the script in OBS Studio.

## How to Customize
### Setting Sound Files
- Update the file paths for each sound in the `e1` to `e10` instances.
  ```python
  e1.txt = "bruh.mp3"
  e2.txt = "bugatti.mp3"
  # ... (repeat for e3 to e10)
  ```

### Setting Hotkeys
- Customize hotkeys in the `script_load` function by modifying the `Hotkey` instances (`h1` to `h10`).
  ```python
  h1.htk_copy = Hotkey(cb1, settings, "Button 1: " + e1.txt)
  h2.htk_copy = Hotkey(cb2, settings, "Button 2: " + e2.txt)
  # ... (repeat for h3 to h10)
  ```

## Important Note
Make sure to configure OBS Studio to allow for Python scripting before running this script.

## Sample Soundboard
- Button 1: "bruh.mp3"
- Button 2: "bugatti.mp3"
- Button 3: "chad.mp3"
- Button 4: "huh.mp3"
- Button 5: "saul.mp3"
- Button 6: "sigma.mp3"
- Button 7: "two.mp3"
- Button 8: "vine.mp3"
- Button 9: "why.mp3"
- Button 10: "windows.mp3"

Feel free to modify the script according to your preferences and add more sounds or buttons as needed.
