from django import template

register = template.Library()

@register.inclusion_tag('blog/templatetags/paginator.html')
def paginator(page_obj):


        # article = Article.objects.all()
        # paginator = Paginator(article,3)
        # page_obj = paginator.page(page)
        page_range = page_obj.paginator.page_range
        data = {
            'page_obj': page_obj,
            'page_range': page_range,
        }
        if page_obj.has_next():
            next_number = page_obj.next_page_number()
            data['next_number'] = next_number
        if page_obj.has_previous():
            previous_number = page_obj.previous_page_number()
            data['previous_number'] = previous_number
        return data