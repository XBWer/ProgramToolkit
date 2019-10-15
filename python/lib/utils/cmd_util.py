import subprocess


def execute_cmd_with_output(cmd, working_dir=None):
    try:
        # if working_dir is None:
        #     res = subprocess.check_output(cmd, shell=True)
        # else:
        #     res = subprocess.check_output(cmd, shell=True, cwd=working_dir)
        res = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE).communicate()[0].decode('utf-8')
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
