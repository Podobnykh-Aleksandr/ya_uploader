import requests


class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def get_upload_link(self, disk_file_path):
        upload_url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'OAuth {}'.format(self.token)
        }
        params = {"path": disk_file_path, "overwrite": "true"}
        response = requests.get(upload_url, headers=headers, params=params)
        data = response.json()
        url_to_load = data.get('href')
        return url_to_load

    def upload(self, disk_file_path, local_file_path):
        href = self.get_upload_link(disk_file_path=disk_file_path)
        response = requests.put(href, data=open(local_file_path, 'rb'))
        if response.status_code == 201:
            print("Success")


if __name__ == '__main__':
    local_path_to_file = '001.txt'
    disk_path_to_file = 'net_001'
    TOKEN = input('Введите токен: ')
    uploader = YaUploader(token=TOKEN)
    uploader.upload(disk_path_to_file, local_path_to_file)
