# DesktopCleanup


Clean you're mac desktop from pictures / movies ("jpg","png",mov"). 
It creates a new folder called cleanup on desktop. It orders all pictures into a year/month/day order and move you're
 pictures into it. 
It gives a short notification how many files are moved.
 
### Dependencies:
- Python 3
- pync


Add script to the crontab and let it run every hour.
``` 0 * * * * /Users/USER/gitPrivat/desktopCleanup/cleanup.py```
