

def identify_day(day):
    class_day = ''
    if day == '1':
        class_day = "today"
    elif day == '2':
        class_day = "yesterday"
    elif day == '3':
        class_day = "last Monday"
    elif day == "4":
        class_day = "last Tuesday"
    elif day == "5":
        class_day = "last wednesday"
    elif day == '6':
        class_day = "last Thusday"
    elif day == '7':
        class_day = "last Friday"
    elif day == "8":
        class_day = "last Saturday"
    elif day == "9":
        class_day = "last Sunday"

    return class_day

def identify_status(status):
    class_status = ''
    
    if status == '1':
        class_status = "pretty well"
    elif status == '2':
        class_status = "smoothly"
    elif status == '3':
        class_status = "quite well"
    elif status == "4":
        class_status = "good as usual"
    elif status == "5":
        class_status = "well"
    return class_status

def identify_material(mat):
    hotdog = ["",
              "Active Reading", 
              "Active Reading 2",
              "Active Reading 3",
              "Unlock 1 LS",
              "Unlock 2 LS",
              "Unlock 3 LS",
              "Unlock 4 LS", 
              "Complete Key", 
              "Compact Key", 
              "Everybody Up 3",
              "Free-talking"]
    
    return hotdog[mat]

def identify_endtheme(theme):
    hotdog = ["",
              "continues to participate actively in class.", 
              "maintains his good reading and listening skills.",
              "maintains her good reading and listening skills.",
              "maintains his good grammar and vocabulary skills.",
              "maintains her good grammar and vocabulary skills.",
              "continues to participate actively and expect more difficult activities.",
              "continues to participate really well and maintains his good english skills.",
              "continues to participate really well and maintains her good english skills.", 
              "to continue participating actively in our upcoming classes.", 
              "expects for more difficult activities and continue to do well in class."]
    
    return hotdog[theme]
    