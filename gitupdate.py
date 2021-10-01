import os
import git
from git import Repo

local_path = r'C:\Users\Administrador\AppData\Local\Programs\Python\Python39\Projetos\Streamlit'
m_repo = Repo(local_path)
commit_message = 'Comentário Automático'

for remote in m_repo.remotes:
    print(f'- {remote.name} {remote.url}')

def git_push():
    try:
        m_repo.git.add(A=True)
        m_repo.git.add(update=True)
        m_repo.index.commit(commit_message)
        origin = m_repo.remote(name='origin')
        origin.push()
    except git.exc.GitCommandError as error:
        print(f'Aconteceu um Erro {error}')

if m_repo.is_dirty(untracked_files=True):
    print('Foram encontradas alterações')
    git_push()