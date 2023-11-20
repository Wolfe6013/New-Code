import pygetwindow as gw

open_windows = gw.getWindowsWithTitle('')
file_count = len(open_windows)

if file_count > 0:
    print(f"Number of open files: {file_count}")
    print("List of open files:")
    for window in open_windows:
        print(window.title)
else:
    print("No open files found.")