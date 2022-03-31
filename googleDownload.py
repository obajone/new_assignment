from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import os

gauth = GoogleAuth()
drive = GoogleDrive(gauth)

folder = '1jssIFkeWWQmToMZkTvmRkUbrw07ErDBd'

file_list = drive.ListFile({'q' : f"'{folder}' in parents and trashed = false"}).GetList()
# for file in file_list:
#     print(file['title'])
for index, file in enumerate(file_list):
    print(index+1, 'file downloaded : ', file['title'])
    file.GetContentFile(file['title'])