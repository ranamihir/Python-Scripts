garbled = "!XeXgXaXsXsXeXmX XtXeXrXcXeXsX XeXhXtX XmXaX XI"
message = garbled[::-2]

m = "123456789" # We want "345" and "543"
n = m[2:5:]     #"345"
a = m[4:1:-1]   #"543"  UNDERSTAND THIS STEP PROPERLY

print n
print m
print a