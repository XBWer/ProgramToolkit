import subprocess


def execute_cmd(cmd, working_dir):
    try:
        res = subprocess.check_output(cmd, shell=True, cwd=working_dir).decode("utf-8").strip()
    except Exception as e:
        print("Execute {} failed! cwd={}".format(cmd, working_dir))
        print(e)
        return None
    return res
