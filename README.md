# Discord-VC-Exploit
Discord VC Exploit to lag VCS, after all this time, this is STILL working.

# How to use?

• Open the py file,
• then open devtools on discord, go to network and join a vc, dont start watching a screenshare but you should see a request called `?v=5`

![image](https://user-images.githubusercontent.com/84104542/133483447-215e02a6-8636-45fa-a6bd-1c1c0602525b.png)

• (reason you shouldnt watch a screenshare is it makes 2 and it can confuse)
• click on it and copy the `websocket (request) url`

![image](https://user-images.githubusercontent.com/84104542/133483793-094b20cf-892a-4873-9ac7-e87a0e7bb321.png)

• then paste it into the console and **VERY IMPORTANT TO CHANGE** v=6 to v=5!!, DONT CLOSE DEVTOOLS, then enter then paste in the server id
• then YOUR user id
• then get a randdom id of someone in the vc and pop it in
• if you listened and didnt close devtools, go to messages at the top

![image](https://user-images.githubusercontent.com/84104542/133484232-f1373260-e654-4b1f-bc4b-5518be640899.png)

• Then scroll up and select one with opcode 0
• expand it like this and copy the session id and token

![image](https://user-images.githubusercontent.com/84104542/133484408-6d693c44-bb2d-4797-bc14-808d002c2a1b.png)

Pop both in and click enter, 

![image](https://user-images.githubusercontent.com/66729830/144730605-2b1dbc53-8aaa-4b79-b699-42c01f946fc2.png)

it should look like the image above

if you are disconnecting and reconnecting that means its working, the vc should be lagging OR people wont be able to hear eachother and should be reconnecting/rtc connecting.

also works in stage discovery and that shit and works better in big vcs

please dont call me a skid for putting -1 everywhere even though it literally makes no difference at all. i was just like testing

also alot of unneccesary code

this is kinda like ilinkeds exploit if you look at how it works.

# known issues or something

```py
"module 'websocket' has no attribute 'create_connection'"?

do py -m pip install websocket-client

or python -m pip install websocket-client

or python3 -m pip install websocket-client

or pip install websocket-client

whatever one works
```






