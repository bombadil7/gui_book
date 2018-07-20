import os
import sys

fpath = "/data/data/com.android.gles3jni/files"

"""
  Default parameters for number of files to copy, 
  starting position and name are 1, 0, fpga_in respectively.
  User can enter these arguments in order, or use switches
  to specify a particular argument.  
  Examples:
  default:
  python mv_file.py

  order with 5 files starting with '2':
  python mv_file.py 5 2 thick_filter
  
  using switches starting with file 2, 5 files, thick_filter
  python mv_file.py s=2 n=5 name=thick_filter

"""
def parse_input():
    num = 1
    start = 0
    name = 'fpga_in'
#    name = 'thick_filter'
    if len(sys.argv) == 1:
        return (num, start, name)
    elif len(sys.argv) > 4:
        print("Usage: num=# start=# name=<>")
        exit()
    elif sys.argv[1].isdigit():
        num = int(sys.argv[1])
        if len(sys.argv) > 2 and sys.argv[2].isdigit():
            start = int(sys.argv[2])
        if len(sys.argv) > 3 and sys.argv[3].isalpha():
            name = sys.argv[3]
    else:
        for arg in sys.argv[1:]:
            a = [x.strip() for x in arg.split("=")]
            if a[0] == 'num' or a[0] == 'n':
                num = int(a[1])
            elif a[0] == 'start' or a[0] == 's':
                start = int(a[1])
            elif a[0] == 'name':
                name = a[1]
            else:
                print("Unknown argument %s" % a[0])
                print("Usage: num=# start=# name=<>")
                exit()
    return (num, start, name)

        
def copy_files():
    num, start, name = parse_input()
    for f in range(num):
        fin = fpath + '/%s_' % name + str(f+start) + '.csv"'
        fout = 'output/%s_' % name + str(f+start) + '.csv'
        command = 'adb shell "run-as com.android.gles3jni cat ' \
                    + fin + ' > ' + fout
        print(command)
        os.system(command)

if __name__ == '__main__':
    os.system("adb devices")
    os.system("adb root")
#    os.system("adb shell" + " ls -l " + fpath)
    copy_files()


