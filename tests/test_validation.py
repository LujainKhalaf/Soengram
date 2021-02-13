from app.utils.validation import is_email_valid, is_post_image_in_request, is_file_allowed


def test_should_return_true_for_emails() -> None:
    emails = [
        'jason@g.com',
        'j@g.com',
        'j@123.ca',
        'test@hello.co.uk'
    ]

    are_all_emails_valid = all(is_email_valid(email) for email in emails)

    assert are_all_emails_valid is True


def test_should_return_false_for_emails() -> None:
    emails = [
        'j.com',
        'hello@ca'
    ]

    is_any_email_valid = any(is_email_valid(email) for email in emails)

    assert is_any_email_valid is False


class FileMock:

    def __init__(self, filename):
        self.filename = filename


def test_should_return_true_for_files() -> None:
    files = {
        'post_image': FileMock('filename.png')
    }

    result = is_post_image_in_request(files)

    assert result is True


def test_should_return_false_if_constant_not_in_dict() -> None:
    files = {
        'different_key': FileMock('filename.png')
    }

    result = is_post_image_in_request(files)

    assert result is False


def test_should_return_false_if_filename_is_empty() -> None:
    files = {
        'post_image': FileMock('')
    }

    result = is_post_image_in_request(files)

    assert result is False


def test_should_return_false_if_no_extension_in_filename() -> None:
    filename = 'test_file'

    result = is_file_allowed(filename)

    assert result is False


def test_should_return_true_if_file_extension_is_supported() -> None:
    file_names = [
        'file.png',
        'file.jpg',
        'file.jpeg',
        'file.gif'
    ]

    result = all(is_file_allowed(file) for file in file_names)

    assert result is True


def test_should_return_false_if_file_extension_not_supported() -> None:
    file_names = [
        'file.pdf',
        'file.exe',
        'file.txt',
        'file.bin'
    ]

    result = any(is_file_allowed(file) for file in file_names)

    assert result is False
