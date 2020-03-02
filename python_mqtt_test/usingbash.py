import subprocess

bashCommand = "mosquitto_pub -h 127.0.0.1 -t v1/devices/me/telemetry -u 6V5PDTFsqsHc4Wv2X6Qe -m {\"TEST\":\"vibration\"}"
output = subprocess.check_output(['bash','-c',bashCommand])
