from pydrive2.auth import GoogleAuth
from pydrive2.drive import GoogleDrive
import os
import re
import shutil


# ダウンロード先のディレクトリ名
DOWNLOAD_FOLDER = './gz_downloaded'


# 認証情報を生成
gauth = GoogleAuth()


# Creates local webserver and auto handles authentication.
gauth.LocalWebserverAuth()


# 認証情報をもとにGoogleDriveFileオブジェクトを生成
drive = GoogleDrive(gauth)


# Auto-iterate through all files that matches this query
file_list = drive.ListFile(
    {'q': "'root' in parents and trashed=false"}).GetList()
for file in file_list:
    if re.search('\.png$', file['title']):
        print('title: %s, id: %s' % (file['title'], file['id']))
        id = file['id']

        # 一度Driveインスタンスを作る必要がある
        f = drive.CreateFile({'id': id})

        # 対象のコンテンツのダウンロード
        f.GetContentFile(file['title'])


if not os.path.isdir(DOWNLOAD_FOLDER):
    os.mkdir(DOWNLOAD_FOLDER)
try:
    shutil.move(f['title'], DOWNLOAD_FOLDER)
except:
    os.remove(f['title'])
    print(f'Notice: {f["title"]} is already exist. Remove this file.')


# # Create GoogleDriveFile instance with title 'Hello.txt'.
# f = drive.CreateFile({'title': 'UploadTest.txt'})

# # Set content of the file from given string.
# f.SetContentString('Hello PyDrive!!')
# f.Upload()
# print('title: %s, id: %s' %(f['title'],f['id']))


# # Update Metadata.
# updateId = drive.ListFile({'q': 'title="UPDATED!"'}).GetList()[0]['id']
# u = drive.CreateFile({'id': updateId})
# u.FetchMetadata()
# pprint.pprint(u['mimeType'])
# u['title'] = 'UpdateTest.txt'
# u.Upload()


# # Creating a Folder
# folder = drive.CreateFile({'title':'new_folder','mimeType': 'application/vnd.google-apps.folder'})
# print(folder)
# folder.Upload()


# # フォルダの削除
# # 対象のフォルダ（ファイル）を取得
# folder_id = drive.ListFile({'q':'title = "new_folder"'}).GetList()[0]['id']

# # GoogleDriveオブジェクトを作成して操作を行う
# folder = drive.CreateFile({'id': folder_id})
# pprint.pprint(folder)

# # 対象フォルダの削除
# folder.Delete()


# # ファイルをアップロードする
# # GoogleDriveオブジェクト初期化
# f = drive.CreateFile()
# print(f)

# # アップロードするファイルのパスを指定
# f.SetContentFile('./images/animal_alpaca_huacaya.png')

# # ファイル名を取り出してタイトルとして設定
# f['title'] = os.path.basename('./images/animal_alpaca_huacaya.png')
# f.Upload()
