def report_normal_vitals():
    print("Battery is Ok")
    
def report_abnormal_vitals(bms_vitals):
    print("Abnormal Vitals")
    for vitals in bms_vitals:
        print(vitals)  
