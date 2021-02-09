from app.utils.validation import is_email_valid


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
