from django import  template

register = template.Library()

@register.filter(name='checknumberofcomments')
def checknumberofcomments(numcomments):
    try:
        numcomments = int(numcomments)
        if numcomments == 0:
            return f'Nenhum comentário'
        elif numcomments == 1:
            return f'{numcomments} comentário'
        else:
            return f'{numcomments} comentários'
    except:
        return f'{numcomments} comentário(s)'
