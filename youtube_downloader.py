import pytubefix, pathlib, sys

print('FLORESTDEV\nДовнлоадер для видосов.\nНе рекомендуется качать большие файлы.\nПриложение запишет логи в специальный файл `log.txt`, в папке где то запущено.')
url = input(f'Введите ссылку на видео для скачивания: ')
filename = input(f'Введите название файла (например: video.mp4): ')
path = input(f'Введите путь к папке, куда Вы хотите сохранить свое видео (введите none, если хотите скачать в эту папку): ')
type_ = input(f'Использовать аутентификацию через Google аккаунт? yes/no ')

def download_callback(stream, chunk, bytes_remaining):
    size = stream.filesize
    bytes_downloaded = size - bytes_remaining
    print(f'Статус скачивания: {round(bytes_downloaded, 2)} байтов')


def downloader(url: str, filename: str, path: str, type_: str):
    try:
        if type_ == 'no':
            yt = pytubefix.YouTube(url, 'WEB', on_progress_callback=download_callback)
            video = yt.streams.get_highest_resolution()
            if path != 'none':
                video.download(path, filename)
            else:
                video.download(pathlib.Path(sys.argv[0]).parent.resolve(), filename=filename)
            print(f'Проверьте папку, которую Вы указали ранее.')
            with open(pathlib.Path(sys.argv[0]).parent.resolve() / 'log.txt', 'w') as f:
                f.write(f'Успешно скачен файл с именем {filename}')
                f.close()
        if type_ == 'yes':
            yt = pytubefix.YouTube(url, 'WEB', on_progress_callback=download_callback, use_oauth=True)
            video1 = yt.streams.get_highest_resolution()
            if path != 'none':
                video1.download(path, filename)
            else:
                video1.download(pathlib.Path(sys.argv[0]).parent.resolve(), filename)
            print(f'Проверьте папку, которую Вы указали ранее.')
            with open('log.txt', 'w') as f:
                f.write(f'Успешно скачен файл с именем {filename}')
                f.close()
    except Exception as e:
        print(f'Произошла ошибка: {e}.\nПожалуйста, сообщите о ней разработчику.\nTelegram: @florestone4185\nПочта: florestone4185@internet.ru')
        with open(pathlib.Path(sys.argv[0]).parent.resolve() / 'log.txt', 'w') as f:
            f.write(f'Произошла ошибка: {e}.\nПожалуйста, сообщите о ней разработчику.\nTelegram: @florestone4185\nПочта: florestone4185@internet.ru')
            f.close()

if __name__ == '__main__':
    downloader(url, filename, path, type_)