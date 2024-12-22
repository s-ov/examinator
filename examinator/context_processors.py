def navigation_links(request):
    return {
        'nav_items': [
            {
                "name": "Створити запитання", 
                "url_name": "examinator:create_question",
            },
            {
                "name": "Список запитань", 
                "url_name": "examinator:list_question",
            },
        ]
    }
