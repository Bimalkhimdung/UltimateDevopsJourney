import subprocess

def get_user_info():
        try:
                user = subprocess.check_output(["last"], text=True)
                print(user)
        except  subprocess.CalledProcessError as e :
                print(f"failed {e.returncode}")

def still_login():
        try: 
                still_user = subprocess.check_output(["last","grep 'still login'"],text=True)
                print(still_login)
        except subprocess.CalledProcessError as e:
                print(f"no users login {e.returncode}")
def ls():
        try: 
                user = subprocess.run("ls",text=True)
                print(user)
        except subprocess.CalledProcessError as e:
                print(f"no error{e.returncode}")
ls()

#get_user_info()
#still_login()