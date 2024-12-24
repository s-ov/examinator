def navigation_links(request):
    return {
        'nav_items': [
            {
                "name": "Створити тест", 
                "url_name": "examinator:knowledge_test_create",
            },
            {
                "name": "Створити білет", 
                "url_name": "examinator:testpaper_create",
            },
            {
                "name": "Створити запитання", 
                "url_name": "examinator:create_question",
            },
            {
                "name": "Список запитань", 
                "url_name": "examinator:list_question",
            },
            {
                "name": "Список білетів", 
                "url_name": "examinator:testpaper_list",
            },
        ]
    }
