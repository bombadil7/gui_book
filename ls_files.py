import os

sh = "adb shell"
fpath = "/data/data/com.android.gles3jni/files"

os.system("adb devices")
os.system("adb root")
os.system(sh + " ls -l " + fpath)

