from common.models import Snippet
from common import sqls
from common.views import ComGetQuery
from snippet.consts import SNIPPET_MSG

import traceback

def DomSnippetCreate(params):
        
    context = {"try_flag": True, "msg": ""}

    try:
        snippet = Snippet()
        snippet.title = params["title"]
        snippet.description = params["description"]
        snippet.code = params["code"]
        snippet.save()

        return context
    
    except:
        context["try_flag"] = "except"
        return context

def DomGetSnippetList():

    context = {"try_flag": True, "msg": ""}

    try:
        query = sqls.GetSnippetList()

        args = []

        qdata = ComGetQuery(query,args)

        if "except_flag" in qdata:
            context["try_flag"] = "except"
            return context
        
        if not qdata:
            context["try_flag"] = False
            context["msg"] = SNIPPET_MSG["snippet_none"]
            return context
                
        context["snippet_list"] = qdata
        return context
    
    except:
        context["try_flag"] = "except"
        print(traceback.print_exc())
        return context

def DomGetSnippetDetail(params):

    context = {"try_flag": True, "msg": ""}

    try:
        query = sqls.GetSnippetDetail()

        args = [
            params["snippet_id"]
        ]

        qdata = ComGetQuery(query,args)
        print(qdata)

        if "except_flag" in qdata:
            context["try_flag"] = "except"
            return context
        
        if not qdata:
            context["try_flag"] = False
            context["msg"] = SNIPPET_MSG["snippet_none"]
            return context
                
        context["snippet"] = qdata[0]
        return context
    
    except:
        context["try_flag"] = "except"
        print(traceback.print_exc())
        return context