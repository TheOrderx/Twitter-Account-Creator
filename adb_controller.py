import os


def adb(code):
    os.system("adb " + code)


def change_airplane(data):
    if data is True:
        adb("shell settings put global airplane_mode_on 1")
        adb("shell am broadcast -a android.intent.action.AIRPLANE_MODE --ez state true")
    else:
        adb("shell settings put global airplane_mode_on 0")
        adb("shell am broadcast -a android.intent.action.AIRPLANE_MODE --ez state false")


def open_link(link):
    adb("shell am start -a \"android.intent.action.VIEW\" -d \"" + link + "\"")
