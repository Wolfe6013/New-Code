import pygetwindow as gw

# Get a list of all open windows (tabs)
open_windows = gw.getWindowsWithTitle('')
tab_count = len(open_windows)

if tab_count > 0:
    print(f"Number of open tabs: {tab_count}")
    print("List of open tabs:")
    for window in open_windows:
        print(window.title)
else:
    print("No open tabs found.")