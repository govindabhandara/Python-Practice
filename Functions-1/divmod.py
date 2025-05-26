def format_duration(seconds):
    minutes,seconds=divmod(seconds,60)
    hours,minutes=divmod(minutes,60)
    return f"{hours}h {minutes}m {seconds}s"
print(format_duration(3661))
#output 1h 1m 1s
'''real world usage: Displaying video duration (e.g,02:35:10)
                     Tracking time spend on tasks in productivity apps '''
