
def GetUserByEmail():

    return """
        select *
        from user
        where
            email = %s and
            active_flag = 1
        limit 1;
    """

def GetUserIdByUserId():

    return """
        select id
        from user
        where
            id = %s and
            active_flag = 1
        limit 1;
    """

def GetSnippetList():

    return """
        select *
        from snippet;
    """

def GetSnippetDetail():

    return """
        select *
        from snippet
        where
            id = %s
        limit 1;
    """