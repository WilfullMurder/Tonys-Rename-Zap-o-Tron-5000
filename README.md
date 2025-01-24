# Tony's Rename Zap-o-Tron 5000

Tony's Rename Zap-o-Tron 5000 is a handy utility for batch-renaming files in directories. The application automatically removes the first 5 characters from filenames that match the pattern `xx - {filename}.mp3` (where `xx` are numbers between 01 and 40). It provides an intuitive GUI for selecting directories and zapping files effortlessly.

## Features

- **Batch Renaming**: Quickly rename multiple files in a directory by removing the prefix `xx - `.
- **Intuitive GUI**: Add directories and process files with ease using a user-friendly interface.
- **Error Prevention**: Processes only files matching the specific format to ensure safety.

---

## How to Use

1. **Download the Application**:
   - Clone or download this repository.
   - Locate the `Tony's Rename Zap-o-Tron 5000` executable in the `dist` folder.

2. **Run the Application**:
   - Execute the program from the `dist` folder:
     ```bash
     python <path_to_executable>
     ```
     (or double-click the executable if you're on Windows).

3. **Select Directories**:
   - Click the **"Add a Directory"** button in the GUI to select folders containing files you want to rename.
   - The selected directories will be displayed in the list box.

4. **Zap Files**:
   - Once directories are added, click the **"Zap Files"** button to process all matching files in the selected directories.
   - Files matching the pattern `xx - {filename}.mp3` will be renamed by removing the prefix `xx - `.

---

## Example

### Before:
01 - Cheerful Violins.mp3
### After:
Cheerful Violins.mp3


## Disclaimer
This is literally a repo for a guy at work (Tony) that wants to batch rename (Zap) loads of his music files.
It was a very specific task to solve and probably won't help anyone else at all.
