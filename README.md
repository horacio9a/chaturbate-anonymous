chaturbate-anonymous
====================
chaturbate-anonymous lets you follow and archive your selected models' shows on chaturbate.com.
So it does not favorites than selected models, which makes it easy to record specific models at a given time, not all the favorites that can be accumulated and too much for our disk free space;)
We know that chaturbate is 'fast on the trigger' to ban somebody, and I have been convinced by this myself several times.
Often, we are banned from some models. For all these problems is the solution is this chaturbate-anonymous script.

Requirements
============
[Python 2.7.13](https://www.python.org/ftp/python/2.7.13/python-2.7.13.msi)
[RTMPDump(ksv)](https://github.com/K-S-V/Scripts/releases) used to capture the streams must be somewere in the path or in directory with this script.
[ffmpeg](https://ffmpeg.zeranoe.com/builds/) must be somewere in the path or in directory with this script.

Setup
=====
1. Install requirements `pip install -r Requirements.txt`
2. Download and unpack the [code](https://codeload.github.com/horacio9a/chaturbate-anonymous/zip/master).
3. Open console and go into the directory where you unpacked the files (default is C:/-cba-py/)
4. cba.bat can be anywhere (default is C:/Windows/)
5. Edit `config.cfg` to your wish or accept default data.

Running & Output
================
These scripts I made in April this year and I see they work without problems today.
Now I've added `config.cfg` and `cba.bat` so it's now easier to use.
It's best to use 'Command Promt' first to install `Requirements.txt` and to try the basic `cb.py` script. 
All four scripts are very similar and are based on the basic `cb.py` which is most secure to use. 
If you use `cba.bat` it would be good to make a link and put it in the task bar for easier startup. 
While using scripts `cb.py`, `cbff.py` and `cbm.py`(options numbers 0, 1 and 2) using `cba.bat` you can easily start the different models that are in `CB_Model.txt`. 
However, if you want to record a certain model permanently, then you need to use `cba.bat` to start `cbr.py` (option number 3). 
If you want to record another model then you need to start another copy of `cba.bat`. 
Otherwise, I have deliberately predicted that each recording has its own rtmpdump or ffmpeg frame so you can easily stop recording at any time if needed. 
Scripts `cbff.py` and `cbm.py` have a 'play' option so you can track what's happening in the room and you can quickly intervene if you want to turn on the recording. 
For this reason, I have put the model number at `CB_Model.txt` in the ffplay window at the end (after asterix `*`).
