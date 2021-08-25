def dashboardplan():
    urls = {
        "card": {
            "user-onboarded": "dashboard/onboarded/",
        },
        "company": {
            "list": "dashboard/company/",
            "detail": "dashboard/company/<str:id>/",
            "Create": "dashboard/company/create/",
            "Delete": "dashboard/company/delete/<str:id>/",
        },
    }

    return urls
