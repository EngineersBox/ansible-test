import redis, time, subprocess

rd = None
try:
    rd = redis.Redis()
    rd.execute_command("version")
except:
    exit(0)

backup_dir = rd.execute_command("CONFIG get dir")
subprocess.call("docker exec redis systemctl stop redis", shell=True)
time.sleep(2000)
subprocess.call("docker cp dump.rdb redis:{0}".format(backup_dir[1]), shell=True)
subprocess.call("docker exec redis systemctl start redis", shell=True)
