from app.utils.file import get_file_extension


def test_should_get_correct_extension() -> None:
    filename = "file.png"
    extension = get_file_extension(filename)
    assert extension == "png"


def test_should_get_extension_in_lower_case() -> None:
    filename = "file.JPEG"
    extension = get_file_extension(filename)
    assert extension == "jpeg"
