from common.models import Snippet

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
