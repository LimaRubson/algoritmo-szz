from git import Repo

def get_bug_introducing_commits(repo_path, bug_reports):
    repo = Repo(repo_path)
    bug_introducing_commits = []

    for bug_report in bug_reports:
        bug_id = bug_report
        bug_file = bug_report['']
        bug_line = bug_report['
    
        # Obter os commits que modificaram o arquivo relevante para o bug
        blame_result = repo.blame('HEA', bug_file, L=bug_line)
        for commit, lines in blame_result:
            # Verificar se o commit é anterior ao bug report
            if commit.committed_datetime < bug_report['date']:
                # Adicionar o commit à lista de commits que introduziram bugs
                bug_introducing_commits.append(commit.hexsha)

    return bug_introducing_commits

# Exemplo de uso
repo_path = '/caminho/para/repo'  # Substitua pelo caminho para o seu repositório
bug_reports = []

bug_introducing_commits = get_bug_introducing_commits(repo_path, bug_reports)
print("Bug-introducing commits:")
for commit_sha in bug_introducing_commits:
    print(commit_sha)
