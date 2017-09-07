import time
import datetime

def utc_now_ts():
    # time() returns the time in seconds since the epoch as a floating point number
    return int(time.time())

def local_now_str():
    # time() returns the time in seconds since the epoch as a floating point number
    # time.localtime() Like gmtime() but converts to local time. include summer time
    return time.strftime("%Y-%m-%dT%H:%M:%S", time.localtime(time.time()))

def utc_now_str():
    # time() returns the time in seconds since the epoch as a floating point number
    # time.gmtime Convert a time expressed in seconds since the epoch to a struct_time in UTC
    return time.strftime("%Y-%m-%dT%H:%M:%S", time.gmtime(time.time()))

def utc_now_ts_ms():
    return lambda: int(round(time.time() * 1000))

if __name__ == "__main__":
    print(utc_now_ts())
    print(local_now_str())
    print(utc_now_str())
    print(utc_now_ts_ms())
