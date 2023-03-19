import os
import time
import feedparser
#import pyfiglet
#ascii text display currently under development

# Fetch the RSS feed
rss_feed_url = 'https://www.cybertalk.org/feed/'
feed = feedparser.parse(rss_feed_url)

# Extract the content and save it as a string
rss_content = ""
for entry in feed.entries:
    rss_content += entry.title + "\n" + entry.summary + "\n\n"

# Print the RSS content
#print(rss_content)

def scroll_text(text, delay=0.09):
    # Clear the screen
    os.system('cls' if os.name == 'nt' else 'clear')

    # Calculate the total width of the screen
    screen_width = os.get_terminal_size().columns

    # Pad the text with spaces so that it's longer than the screen width
    text = ' ' + text + ' ' * (screen_width - len(text))

    # Loop through the text and print it one character at a time
    for i in range(len(text) - screen_width):
        os.system('cls' if os.name == 'nt' else 'clear')
        print(text[i:i+screen_width])
        time.sleep(delay)

#ascii_art = pyfiglet.figlet_format(rss_content, font="big")

scroll_text(rss_content)
