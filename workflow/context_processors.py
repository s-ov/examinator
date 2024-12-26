def navigation_links(request):
    return {
        'nav_items': [
            {
                "name": "Створити тест", 
                "url_name": "workflow:knowledge_test_create",
            },
            {
                "name": "Створити білет", 
                "url_name": "workflow:testpaper_create",
            },
            {
                "name": "Створити запитання", 
                "url_name": "workflow:create_question",
            },
            {
                "name": "Список запитань", 
                "url_name": "workflow:list_question",
            },
            {
                "name": "Список білетів", 
                "url_name": "workflow:testpaper_list",
            },
            {
                "name": "Список тестів", 
                "url_name": "workflow:knowledge_test_list",
            },
        ]
    }
