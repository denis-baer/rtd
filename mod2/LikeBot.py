"""
Facebook shortcuts:
J and K - Scroll between news feed stories.
enter/return - See more of the selected story.
P - Post a new status.
L - Like or unlike the selected story.
C - Comment on the selected story.
S - Share the selected story.
O - Open an attachment from the selected story.
/ - Search.
Q - Search chat contacts.
? - Open a list of these keyboard shortcuts while in news feed.
"""

from pickle import TRUE
import webbrowser
from pynput import mouse, keyboard
import time

def likebot(url:str):
    """This is a simple facebook likebot.

    :param url: url to the fb-page containing some posts you want to like.
    :type url: str
    """

    webbrowser.get('C:/Program Files/Google/Chrome/Application/chrome.exe %s').open(url)
    mouse.Controller().position = (50, 750)
    mouse.Controller().press(mouse.Button.left)
    mouse.Controller().release(mouse.Button.left)

    start_time = time.time()
    seconds = 15

    while TRUE:
        current_time = time.time()
        elapsed_time = current_time - start_time
        
        if elapsed_time > seconds:
            break

        time.sleep(1)
        keyboard.Controller().press('j')
        keyboard.Controller().release('j')

        time.sleep(1)
        keyboard.Controller().press('l')
        keyboard.Controller().release('l')

        keyboard.Controller().press(keyboard.Key.enter)
        keyboard.Controller().release(keyboard.Key.enter)

if __name__ == '__main__':
    url='https://www.facebook.com/headfound.de'
    likebot(url)