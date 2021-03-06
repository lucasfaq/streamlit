from os import getcwd
from git import Repo, GitCommandError

paths = getcwd()
m_repo = Repo(paths)

def git_push():
    try:
        m_repo.git.add(A=True)
        m_repo.git.add(update=True)
        m_repo.index.commit(commit_message)
        origin = m_repo.remote(name='origin')
        origin.push()
    except GitCommandError as error:
        print(f'Aconteceu um Erro {error}')

if m_repo.is_dirty(untracked_files=True):
    print('Foram encontradas alterações')
    commit_message = input('Insira o Commit:')
    git_push()
    print('O repositório foi atualizado com Sucesso!')
else:
    print('Não houve alteração!')