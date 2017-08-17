
page_identifiers = {
    "identifier": "Enrolled users"
}

fields = {
        "search_bar": {
            "xpath": "/html/body/div[3]/div/div[3]/div[1]/input[1]"
        },
        "filter_bar": {
            "xpath": "/html/body/div[2]/section/div/div/div/section/div[2]/form/fieldset/div/div[1]/div[2]/input"
        },
}


enrolled_students = {
    "student": {
        "xpath": "/html/body/div[2]/section/div/div/div/section/div[2]/table/tbody/tr[1]/td[1]/div[2]"
    }
}

btns = {
    "enrolment_page": {
        "enrol_user_btn": {
            "xpath": "/html/body/div[2]/section/div/div/div/section/div[2]/div[4]/div[1]/form/div/input[1]",
        },

        "enrol_btn": {
            "xpath": "/html/body/div[3]/div/div[2]/div[2]/div/div[2]/div/div[4]/input"
        },
        "finish_enrolment_btn": {
            "xpath": "/html/body/div[3]/div/div[3]/div[2]/input"
        },
    },

    "unenrolment": {
        "unenrol_user_btn": {
            "xpath": "/html/body/div[2]/section/div/div/div/section/div[2]/div/div/div[1]/form/div/input[1]"

        }
    },

    "search": {
        "search_btn": {
            "xpath": "/html/body/div[3]/div/div[3]/div[1]/input[2]"
        },
    },
    "filter": {
        "filter_btn": {
            "xpath": "/html/body/div[2]/section/div/div/div/section/div[2]/form/fieldset/div/div[5]/div/input[1]"
        },
    },

    "search_in_enrol_bar": {
        "search_btn": {
            "xpath": "/html/body/div[3]/div/div[3]/div[1]/input[2]"
        }
    },
    "enrol_frame": {
        "close_btn": {
            "xpath": "/html/body/div[3]/div/div[1]/div"
        }
    }

}

icons = {
   "unenrol": {
       "delete_icon": {
           "xpath": "/html/body/div[2]/section/div/div/div/section/div[2]/table/tbody/tr/td[5]/div/a[1]/i"
       }
   }
}
