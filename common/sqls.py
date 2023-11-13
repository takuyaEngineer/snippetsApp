
# メールアドレスの重複チェック
def MailDuplicationCheck():

    return """
        select email
        from user
        where
            email = %s
        limit 1;
    """

def GetUserByEmail():

    return """
        select *
        from user
        where
            email = %s and
            active_flag = 1
        limit 1;
    """

def GetUserByUserId():

    return """
        select id
        from user
        where
            id = %s
            active_flag = 1
        limit 1;
    """
