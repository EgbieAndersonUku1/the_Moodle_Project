page_identifiers = {
   "identifier": {
       "title": {
             "text": "Enrolment methods"
             },
       "table": {
           "text":"Self enrolment (Student)"
       },
       "menu_option": {
           "choice": "Self enrolment"
       }
   }
}

fields = {
    "table": {
        "tag": "td"
    },

    "dropdown_menu":{
        "xpath": "/html/body/div[2]/section/div/div/div/section/div[2]/div/div/form/div/select"
    },

}

icon = {
   "remove": {
       "self_enrolment_icon":{
           "xpath": "/html/body/div[2]/section/div/div/div/section/div[2]/div/table/tbody/tr[3]/td[4]/a[1]/i"
       }
   }
}

btns = {
   "toggle_on_or_off_self_enrolment":{
       "add_btn": {
           "xpath": "/html/body/div[2]/section/div/div/div/section/div[2]/form/fieldset[2]/div/div/div/input[1]"
       }
   },
   "turn_off_self_enrolment":{
       "continue_btn": {
           "xpath": "/html/body/div[2]/section/div/div/div/section/div[2]/div/div/div[1]/form/div/input[1]"
       }
   }
}
