[SIO](http://www.sio.no/) changed their website and structure in November.
The changes broke the API, and I'll probably not fix that.

**Don't use this. The menu will not be up to date**

# IFI dinner

Check this weeks dinner with the command line

`$ ./dagens_ifi.py`

![Screenshot](https://raw.githubusercontent.com/jarlefosen/dagens_ifi/master/img/screenshot.png)

## Setup

Clone the repository

`$ git clone https://github.com/jarlefosen/dagens_ifi.git`

Make the file executable

`$ chmod +x dagens_ifi.py`

That's it.

## API

I'm using Kimono Labs as the JSON provider. It's crawling SIO's café page and serves the upcomming dishes for this week as JSON.

https://www.kimonolabs.com/api/1zpgdth4?kimmodify=1
