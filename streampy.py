import requests

BASE_URL = 'https://api.streamable.com/'
API_PATH = {
    'upload': 'upload',
    'import': 'import?url='
}
USER = ''
PASS = ''


class Streamable:
    """Wrapper for the Streamable API"""

    def __init__(self):
        """Check if Streamable user account is configured"""
        self.auth = self.check_auth()

    def upload(self, file, title=''):
        """Uploads a video file to Streamable

        :param file: The video file to upload (string)
        :param title: The optional title of the video (string)
        :returns: Response object from server

        """
        url = BASE_URL + API_PATH['upload']
        vid_file = {'file': open(file, 'rb')}
        resp = requests.post(url, files=vid_file, auth=self.auth, data={'title': title})
        return self.result(resp)

    def import_vid(self, url, title=''):
        """Imports a video to Streamable from a URL

        :param url: The URL of the video to import (string)
        :param title: The optional title of the video (string)
        :returns: Response object from server

        """
        url = BASE_URL + API_PATH['import'] + url
        resp = requests.get(url, auth=self.auth, data={'title': title})
        return self.result(resp)

    def result(self, resp):
        """Handle the response object from the server

        :param resp: The response object

        """
        if resp.status_code == 404:
            raise Exception(resp.json())
        code = resp.json()['shortcode']
        url = f'https://streamable.com/{code}'
        print('[+] Upload successful!')
        print(url)

    def check_auth(self):
        """Check if Streamable user account is configured

        Streamable allows both authenticated and unauthenticated (anonymous) uploads

        :returns: tuple if True, which sets auth=(USER, PASS)
        :returns: None if False, which sets auth=None
        ..note:: Data must be formatted this way for the requests module

        """
        if USER and PASS:
            return (USER, PASS)
        else:
            return None


if __name__ == '__main__':

    streamable = Streamable()
    streamable.upload(file='', title='Test upload')
    # streamable.import_vid(url='', title='Test import')
