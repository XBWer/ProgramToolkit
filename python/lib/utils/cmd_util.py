import subprocess


def execute_cmd_with_output(cmd, working_dir=None):
    try:
        res = subprocess.check_output(cmd, shell=True, stderr=subprocess.STDOUT, cwd=working_dir)
    except Exception as e:
        print("Execute {} failed! cwd={}".format(cmd, working_dir))
        print(e)
        return None
    return res


def execute_cmd_without_output(cmd, working_dir):
    try:
        subprocess.call(cmd, shell=True, cwd=working_dir)
    except Exception as e:
        print("Execute {} failed! cwd={}".format(cmd, working_dir))
        print(e)
        return False
    return True
