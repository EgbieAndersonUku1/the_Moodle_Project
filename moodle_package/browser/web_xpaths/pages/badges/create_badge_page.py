page_identifiers = {
    "created_badge_title": {
        "xpath": "/html/body/div[2]/section/div/div/div/section/div[2]/fieldset[1]/table/tbody/tr[1]/td[2]"
    }
}


badge_criteria = {
    "course_completion": "Course completion",
    "activity_completion": "Activity completion"
}

fields = {
    "name": {
        "xpath": "/html/body/div[2]/section/div/div/div/section/div[2]/form/fieldset[1]/div/div[1]/div[2]/input"
    },
    "description": {
        "xpath": "/html/body/div[2]/section/div/div/div/section/div[2]/form/fieldset[1]/div/div[2]/div[2]/textarea"
    },

    "my_badge_pic": {
        "xpath": "/html/body/div[6]/div[2]/div/div[2]/div/div[2]/div[2]/div/a/div[1]/div[3]"
        },

    "dropdown_menu": {
        "xpath": "/html/body/div[2]/section/div/div/div/section/div[2]/table/tbody/tr/td[2]/div/form/div/select"
    },

    "menu":{
        "options": {
            "url_downloader": {
                "xpath": "/html/body/div[6]/div[2]/div/div[2]/div/div[1]/ul/li[4]/a/span",
                "url_field": {
                    "xpath": "/html/body/div[6]/div[2]/div/div[2]/div/div[2]/div[2]/div/div/form/div/div[2]/div/input"
                },
            }
        },

    }
}

btns = {
    "choose_a_file_btn": {
        "xpath": "/html/body/div[2]/section/div/div/div/section/div[2]/form/fieldset[1]/div/div[3]/div[2]/div[2]/div[1]/input"
    },
    "download_btn": {
        "xpath": "/html/body/div[6]/div[2]/div/div[2]/div/div[2]/div[2]/div/div/form/p/button"
    },

    "add_picture_btn": {
         "xpath": "/html/body/div[7]/div[2]/div/div[2]/div/form/div[2]/button[1]"
        },
    "create_badge_btn": {
        "xpath": "/html/body/div[3]/section/div/div/div/section/div[2]/form/fieldset[4]/div/div[1]/div/input[1]"
    },
    "save_btn":{
        "xpath": "/html/body/div[2]/section/div/div/div/section/div[2]/form/fieldset[2]/div/div/div/input[1]"
    }

}

tabs = {
    "overview": {
        "xpath": "/html/body/div[2]/section/div/div/div/section/div[2]/ul/li[1]/a"
    }
}