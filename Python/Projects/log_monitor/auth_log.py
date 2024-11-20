import subprocess

def read_log():
    try:
        process = subprocess.Popen(
                ["tail","-f","/var/log/auth.log"],
                stdout=subprocess.PIPE,
                text=True            
            )
        ''
        for line in iter(process.stdout.readline,''):
            print(line.strip())
    except KeyboardInterrupt:
        print("stopped due to keyboard interrupt")
    except Exception as e:
        print("Error: {e}")
read_log()