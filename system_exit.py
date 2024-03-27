import sys
def success():
    print("successful execution")
    sys.exit(0)

# Abnormal termination
def failure():
    print("abnormal termination")
    sys.exit(1)

success()
