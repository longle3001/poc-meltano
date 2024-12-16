# from prefect.blocks.system import Secret
# import subprocess
# import shlex
# import os

# secret_block = Secret.load("fake-google-private-key-id")

# # Access the stored secret
# a = secret_block.get()
# command = f"meltano config tap-google-monitoring set private_key '{a}'"
# # args = shlex.split(command)
# # result = subprocess.run(args, capture_output=True, text=True)
# os.system(command)

# print(command)


# import yaml

# # Đọc file YAML
# with open('meltano.yml', 'r') as file:
#     config = yaml.safe_load(file)

# # Truy cập `private_key`
# a = """-----BEGIN PRIVATE KEY-----
# MIIEvAIBADANBgkqhkiG9w0BAQEFAASCBKYwggSiAgEAAoIBAQCZfsiMV1IT7k7r
# FjEKDiizJMFswraU8OxM6ESC3OwyyWGkyW9A67AEnQ6D5k7ZkNBC9ToXqvshNsrJ
# CyVBRiA54mYt7nZepr/cM1kWAmVKBL85W1l6n3cg1oLgc7E89EQTm8QcFApWMTAr
# o/CTAcOZufYQNu9LV7i2AGh9LwAG1vHiZqK4VoUvCq5CYR45uUDMFP9pdf76/EOI
# 0nfYrGk40Rgs+q021G8k60JudQXtZ9Gbf0+pPZ4aio3vhhLVj6BXplj7Eecn7ORb
# L6GIw/rX/phRvF90Wkc4b04LIYNL/oQ5Tp4SNO4sPqfWDDfmqPucwhCLqB4SvQ/G
# pe7UcvwFAgMBAAECggEACeDvfkdrvbhOIEd5g339dOjDgWuXUvGd0PtNLCY/a1YA
# 8Jk9jZjoPKZxAIsqKErEzzJiI+jPUx1oIqqSzLx7Js6L00lFbqUJCbPM+CN8/60G
# M5D4qsbS5MGkLaw0dsmlDKVZ6JFfnZl6fKyHN1GF6axetOocL3tR+iCqQ42VUQXw
# haVX7rfmW6ogFVyO01Y2hYlQM+nJYZWHxe96k+LvtkJwhra6zbap2BqBn7cjsEpH
# CKE389jV0JfzRPZc3LB8gXu+f3aT2MY6B7EwJNbVY1pHzOIkmDxl0QnE3iFIr05H
# 4PMYaoL2Zj9W7MT+6YlJGGswesKDwcOQRdMwkWrTdwKBgQDN3hHBSygvdFw+4DW+
# ifZJXgt8NwmemXwe8Rgf/xdXk8dpEaTUqWFWbKSVgitFr1fDqNkbfvupW4gbX2Xb
# d3hODjuENn8tS9g3pBgt5IdooCYSAHM3Z/0Cw20M569SYfzwtGj4j94pNVKFCH+u
# eiqHUwQKOaTHeQBKxje3P9uc3wKBgQC+38qabiHGzKsSXA0JCoxhWN1feXoqqe9V
# iO728u58hrYuX8sjJlTTn3sz+bSzZlDBbXhF7KUsALnN51YIYv8P437sFQ9QODDJ
# xcv85AnGspctdfBM/5vZvU+qhUlqXcNaXwkHkKPRCkeVDdRWcs3n28lmp+/S7UEH
# 9vwTwQQfmwKBgDthyw1OeJD3p4QbeGU1tm0DS5zQ4110OHFUafkQw9LnNaYBCOKu
# 2Pzs6ayWl5TKNy6hDb74qe74EBKVOfRMSc96G4DPl2+haQTjuHXEbaqoR1L5/kIF
# JN4fMN2AFvpUeXmVEJJiLVsFnn/xK6NQaeQO9iNc7UL8jDEFbBzXtqlRAoGAR80N
# fMxC/nKNQ8nGyYjjR9dS5xBeSWBFfMqXAeRenA9cxtMYKi/IJxdOFD4xoG6zoB+a
# 58reU1AulOsZ7Ou4gPSWER7W9Nk+WRiD5KyvlMQnpF1COOTKbr0NE9sxw8Zjr0Ii
# tmrNhNw2Ezbxkld7Z2XBPFGeIJ1JIkLhjljEQVMCgYArIH1fZ1gKfXNVUuk222j/
# qan6OC57Bb1a/pF071aQoXtcPu4JnSis24NuMBhqve2fpn0FBsFehjTSatT4FMMw
# gjeWEtZB2ZFO8Yc1gV6YiwUIWz134yiqVCzq7ROdlKXbta8kF2GjFA5d4C66vhyj
# HAmkF31VTpdTkC1FtFxtTw==
# -----END PRIVATE KEY-----"""
# config['plugins']['extractors'][0]['config']['private_key'] = a




import yaml

def add_private_key_to_yaml(file_path, key_name, key_value):
    # Đọc nội dung file YAML
    with open(file_path, 'r') as file:
        data = yaml.safe_load(file)

    # Duyệt qua cấu trúc YAML để tìm và thêm private_key
    if 'plugins' in data and 'extractors' in data['plugins']:
        for extractor in data['plugins']['extractors']:
            if 'config' in extractor:
                # Thêm `private_key` nếu chưa tồn tại
                if key_name not in extractor['config']:
                    extractor['config'][key_name] = key_value

    # Ghi nội dung YAML đã cập nhật trở lại file
    with open(file_path, 'w') as file:
        yaml.safe_dump(data, file)

# Đường dẫn đến file YAML
file_path = 'meltano.yml'

# Gọi hàm để thêm private_key
a = """-----BEGIN PRIVATE KEY-----
MIIEvAIBADANBgkqhkiG9w0BAQEFAASCBKYwggSiAgEAAoIBAQCZfsiMV1IT7k7r
FjEKDiizJMFswraU8OxM6ESC3OwyyWGkyW9A67AEnQ6D5k7ZkNBC9ToXqvshNsrJ
CyVBRiA54mYt7nZepr/cM1kWAmVKBL85W1l6n3cg1oLgc7E89EQTm8QcFApWMTAr
o/CTAcOZufYQNu9LV7i2AGh9LwAG1vHiZqK4VoUvCq5CYR45uUDMFP9pdf76/EOI
0nfYrGk40Rgs+q021G8k60JudQXtZ9Gbf0+pPZ4aio3vhhLVj6BXplj7Eecn7ORb
L6GIw/rX/phRvF90Wkc4b04LIYNL/oQ5Tp4SNO4sPqfWDDfmqPucwhCLqB4SvQ/G
pe7UcvwFAgMBAAECggEACeDvfkdrvbhOIEd5g339dOjDgWuXUvGd0PtNLCY/a1YA
8Jk9jZjoPKZxAIsqKErEzzJiI+jPUx1oIqqSzLx7Js6L00lFbqUJCbPM+CN8/60G
M5D4qsbS5MGkLaw0dsmlDKVZ6JFfnZl6fKyHN1GF6axetOocL3tR+iCqQ42VUQXw
haVX7rfmW6ogFVyO01Y2hYlQM+nJYZWHxe96k+LvtkJwhra6zbap2BqBn7cjsEpH
CKE389jV0JfzRPZc3LB8gXu+f3aT2MY6B7EwJNbVY1pHzOIkmDxl0QnE3iFIr05H
4PMYaoL2Zj9W7MT+6YlJGGswesKDwcOQRdMwkWrTdwKBgQDN3hHBSygvdFw+4DW+
ifZJXgt8NwmemXwe8Rgf/xdXk8dpEaTUqWFWbKSVgitFr1fDqNkbfvupW4gbX2Xb
d3hODjuENn8tS9g3pBgt5IdooCYSAHM3Z/0Cw20M569SYfzwtGj4j94pNVKFCH+u
eiqHUwQKOaTHeQBKxje3P9uc3wKBgQC+38qabiHGzKsSXA0JCoxhWN1feXoqqe9V
iO728u58hrYuX8sjJlTTn3sz+bSzZlDBbXhF7KUsALnN51YIYv8P437sFQ9QODDJ
xcv85AnGspctdfBM/5vZvU+qhUlqXcNaXwkHkKPRCkeVDdRWcs3n28lmp+/S7UEH
9vwTwQQfmwKBgDthyw1OeJD3p4QbeGU1tm0DS5zQ4110OHFUafkQw9LnNaYBCOKu
2Pzs6ayWl5TKNy6hDb74qe74EBKVOfRMSc96G4DPl2+haQTjuHXEbaqoR1L5/kIF
JN4fMN2AFvpUeXmVEJJiLVsFnn/xK6NQaeQO9iNc7UL8jDEFbBzXtqlRAoGAR80N
fMxC/nKNQ8nGyYjjR9dS5xBeSWBFfMqXAeRenA9cxtMYKi/IJxdOFD4xoG6zoB+a
58reU1AulOsZ7Ou4gPSWER7W9Nk+WRiD5KyvlMQnpF1COOTKbr0NE9sxw8Zjr0Ii
tmrNhNw2Ezbxkld7Z2XBPFGeIJ1JIkLhjljEQVMCgYArIH1fZ1gKfXNVUuk222j/
qan6OC57Bb1a/pF071aQoXtcPu4JnSis24NuMBhqve2fpn0FBsFehjTSatT4FMMw
gjeWEtZB2ZFO8Yc1gV6YiwUIWz134yiqVCzq7ROdlKXbta8kF2GjFA5d4C66vhyj
HAmkF31VTpdTkC1FtFxtTw==
-----END PRIVATE KEY-----"""
add_private_key_to_yaml(file_path, 'private_key', a)
