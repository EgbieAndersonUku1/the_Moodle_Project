
page_identifier = {
    "identifier": {
        "web_page_title": "Add a new course"
    }
}


fields = {
    'full_name': {
        'xpath': '/html/body/div[3]/section/div/div/div/section/div/form/fieldset[1]/div/div[1]/div[2]/input',
    },
    'short_name': {
        'xpath': '/html/body/div[3]/section/div/div/div/section/div/form/fieldset[1]/div/div[2]/div[2]/input',
    },

    'course_category': {
        'xpath': '/html/body/div[3]/section/div/div/div/section/div/form/fieldset[1]/div/div[3]/div[2]/select',
    },

    'course_id': {
        'xpath': '/html/body/div[3]/section/div/div/div/section/div/form/fieldset[1]/div/div[6]/div[2]/input',
    },

    'summary': {
        'xpath': '/html/body/div[3]/section/div/div/div/section/div/form/fieldset[2]/div/div[1]/div[2]/div/div[1]/div/div[2]/div',
    },

    'completion_tracking': {'caret':{
        "xpath": '/html/body/div[3]/section/div/div/div/section/div/form/fieldset[6]/legend/a'
    },
        'dropdown_menu': {
            'xpath': '/html/body/div[3]/section/div/div/div/section/div/form/fieldset[6]/div/div/div[2]/select',
        },
    }
}

btns = {
    'save_and_continue_btn': {
        'xpath': '/html/body/div[3]/section/div/div/div/section/div/form/fieldset[10]/div/div[1]/div/input[1]'
    },
}
