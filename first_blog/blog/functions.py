def user_directory_path_for_image_avatar_author_files(instance, filename) -> str:
    """ Функция для формирования пути для загрузки файлов с аватарами для определенного автора

    :param instance: объект, который хранит данные о пользователе
    :param filename: имя файла
    :return: Путь до сохраняемого файла
    """
    return f"image/author/avatar/user_{instance.id}_{filename}"


def user_directory_path_for_background_image_author_files(instance, filename) -> str:
    """ Функция для формирования пути для загрузки файлов с задним фоном для определенного автора

    :param instance: объект, который хранит данные о пользователе
    :param filename: имя файла
    :return: Путь до сохраняемого файла
    """
    return f"image/author/background/user_{instance.id}_{filename}"


def user_directory_path_for_image_preview_post_files(instance, filename) -> str:
    """ Функция для формирования пути для загрузки файлов с картинками для превью определенного поста

    :param instance: объект, который хранит данные о пользователе
    :param filename: имя файла
    :return: Путь до сохраняемого файла
    """
    return f"image/post/preview/post_{instance.id}_{filename}"
