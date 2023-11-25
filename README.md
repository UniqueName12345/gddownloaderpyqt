Geometry Dash Downloader: Grabbing Banned Beats! 🎶
===================================================

Yo, music rebels! If you're here, you're probably tired of Newgrounds banning songs on Geometry Dash. Well, fret not, 'cause we got a slick Python script to help you out.

How It Works
------------

We cracked the code, literally. The audio link follows this sweet pattern: `https://audio-download.ngfiles.com/(ID - Mod(ID/1000))/(ID)_(Modified name with limit of 26 characters).mp3`. Just remember, it kicks in from ID No. 469775 onwards. Anything before that is a no-go. If you're into the nitty-gritty math stuff, check out "[math.md](http://math.md)" in the repo. But hey, it's only for the hardcore math enthusiasts. This readme is all about vibes, not formalities!

Shoutout to d4n3436 for the OG "GDDownloader." I just rolled it into Python because I heard AutoHotKey was catching some flak as malware.

Usage
-----

1.  Install the goods: `pip install -r requirements.txt`.
2.  Get your hands dirty:
    *   For the command line bosses: `python gddownloadercli.py [song id] [song name in quotes] --save-path [custom path if you're feeling fancy]`.
    *   Or for the chill vibes: `python gddownloadertui.py` (TUI menu for the win).

And yeah, I know the repo screams "PyQT" when it's just a CLI party. My bad. Too lazy to fix. It's not as slick as GD Song File Hub, but it gets the job done occasionally. Newgrounds might catch on, so use it wisely.

Let's Connect
-------------

Got issues? Hit up the Issues tab. Wanna drop some code? Send a Pull Request. Just wanna shoot the breeze? Find me on Scratch as DifferentDance8 or on Geometry Dash as JoshTheProtogen. Don't bother with Discord or Snapchat—those are VIP zones for real-life pals.

Rock on and keep those beats alive! 🤘✨