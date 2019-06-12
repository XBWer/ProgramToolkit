import subprocess
from src.utils.diff_util import diff_parser_from_str


def git_clone(project_url, folder_path):
    args = ['clone', project_url, folder_path]
    try:
        subprocess.check_call(['git'] + list(args))
    except Exception as e:
        print("git clone failed! url=%s" % project_url)
        print(e)
        return False
    return True


def git_log(work_dir):
    import os
    cmd = "git log --pretty=short > git.log"
    try:
        subprocess.call(cmd, shell=True, cwd=work_dir)
    except Exception as e:
        print("git log failed! cwd=%s" % work_dir)
        print(e)
        return False
    log_fpath = os.path.join(work_dir, 'git.log')
    return log_fpath


def get_commit_msg(commit, work_dir):
    """
    Untested
    :param commit:
    :param work_dir:
    :return:
    """
    cmd = "git log --format=%B -n 1 %s" % commit
    try:
        commit_msg = subprocess.check_output(cmd, shell=True, cwd=work_dir)
    except Exception as e:
        print("get_commit_msg failed! cwd=%s" % work_dir)
        print(e)
        return False
    return commit_msg


def git_checkout(folder_path, commit_sha):
    args = ['--git-dir', folder_path + '/.git', '--work-tree', folder_path, 'checkout', commit_sha]
    return subprocess.check_call(['git'] + list(args))


def git_diff(folder_path, parent_com, cur_com):
    '''
    :param folder_path:
    :param parent_com:
    :param cur_com:
    :return:
    '''
    args = ['--git-dir', folder_path + '/.git', '--work-tree', folder_path, 'diff', '--unified=0', parent_com, cur_com]
    return subprocess.check_output(['git'] + list(args))


def get_modified_file_list(diff_str):
    diffs = diff_parser_from_str(diff_str)
    modified_sol_list = []
    for d in diffs:
        source_file = str(d.source_file)
        target_file = str(d.target_file)
        modified_sol_list.append(source_file)
    return modified_sol_list


if __name__ == '__main__':
    # git_clone('https://github.com/XBWer/WordSimilarity.git', '/home/bowenxu/Downloads/test')
    # git_checkout('/home/bowenxu/Downloads/test/', '2664b848dcadb6f29d802c06006d78269347434a')
    # write_str = git_diff(
    #     '/home/bowenxu/Desktop/Research/ProgramRepair/SmartContract/SmartContractProject/data/manualDataset/3-GoodCases-FaultLocalization/checked_succeed_ambrosus#Ambrosus/cases/4-goodcase-less5/0be01e2c68499f6b76e849d20c2c5c98cf1b7179_diff_cd491e113285d9b7ef6bddea562932744863e823/new',
    #     'cd491e113285d9b7ef6bddea562932744863e823', '0be01e2c68499f6b76e849d20c2c5c98cf1b7179')
    # write_str= git_diff('/home/bowenxu/Downloads/test','179586fef4a816b16b3541ac490b79777909b3c4','71cfe15ea81d4c6e677dc1d0d161237d7b910fb4')
    # print(write_str)
    git_log("/data/bowen/SmartContract-FixPattern/Repos/7070#fabric/github_repo")
