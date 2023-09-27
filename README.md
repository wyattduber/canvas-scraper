# Canvas File Scraper
This application works by openin a chrome tab with the `chromedriver.exe` file, then waiting about 60 seconds for you to sign in, then immediately scraping a course that you specify in `main.py` and it's files.

# Configuration
In `main.py`, specify the base canvas link you want to use (in my case, it was canvas.iastate.edu). Then add the class ID (like a 5 digit number) and it will scrape all of the file ID's in the range that you also set.

# Explanation
I am unaware of how canvas sets their file ID's, but it is somehow related to when the file is uploaded. So you'll want to poke around to any files that you have access to and find their ID's and get a rough explanation. The File ID will be in the link of the file that you are viewing, like `https://canvas.iastate.edu/courses/#####/files/########`

Good luck 
