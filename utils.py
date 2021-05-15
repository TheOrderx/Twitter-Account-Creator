import os


def adb(code):
    os.system("adb " + code)


def get_sms_activate_ru_api():
    import json
    data = open("settings.json", "r+", encoding="utf8")
    jsondata = json.load(data)
    return jsondata["smsActivateRuKey"] #api_key


def go_save(nick, email, passw):
    data = open("users.txt", "a+")
    if email == "":
        data.write("\n" + nick + ":" + passw)
    else:
        data.write("\n" + nick + ":" + passw + ":" + email)
