
# メールアドレスの重複チェック
def MailDuplicationCheck():

    return """
        select email
        from user
        where
            email = %s
        limit 1;
    """