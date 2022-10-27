import os.path

types = ['jpg', 'jpeg', 'zip', 'rar', 'doc', 'txt', 'png', 'pdf', 'xml', 'exe', 'mp4', 'whl']

# Encontrar diretório raiz independente do S.O.
base_path = os.path.expanduser('~')
# Juntando base_path com a Downloads
path = os.path.join(base_path, 'Downloads')
# Navegar até esta pasta e executar as operações a partir de lá
cwd = os.chdir(path)

full_list = os.listdir(cwd)
for type_ in types:
    if type_ not in os.listdir():
        os.mkdir(type_)

for file in full_list:
    for type_ in types:
        if '.' + type_ in file:
            old_path = os.path.join(path, file)
            new_path = os.path.join(path, type_, file)
            os.replace(old_path, new_path)
