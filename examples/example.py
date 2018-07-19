from labguru import Labguru, Session, UnAuthorizeException, Project
from labguru.exception import NotFoundException


def get_token():
    lab = Labguru(login='xtutran@gmail.com', password='Password123')
    return lab

def main():
    lab = get_token()
    print(lab.session.token)

    projects = lab.get_all_projects(page_num=1)
    for proj in projects:
        # print(proj)
        if proj.id == 141:
            print(proj)
            print(proj.create_new_folder('New Folder 2'))

if __name__ == '__main__':
    main()