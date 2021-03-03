from report_vitals import report_normal_vitals,report_abnormal_vitals

bms_attribute_limits = {
     'TEMPERATURE': {'min': 0, 'max': 45},
     'SOC': {'min': 20, 'max': 80},
     'CHARGE_RATE': {'min': 0,'max': 0.8}
        }


def get_battery_vitals(bms_attribute):
    offLimits = []
    for bms_name,bms_value in bms_attribute.items():        
        get_offLimitVitals(bms_name,bms_value,offLimits)       
    return offLimits

def get_offLimitVitals(bms_name,bms_value,offLimits):
    low_breach_val = bms_attribute_limits[bms_name.upper()]['min']
    high_breach_val = bms_attribute_limits[bms_name.upper()]['max']
    if (bms_value < low_breach_val):
        offLimits.append(bms_name.capitalize()+" Low Breach: "+str(low_breach_val))
    elif (bms_value > high_breach_val):
        offLimits.append(bms_name.capitalize()+" High Breach: "+str(high_breach_val))

def battery_is_ok(bms_attribute):
    bms_vitals = get_battery_vitals(bms_attribute)
    if len(bms_vitals) == 0:
        report_normal_vitals()
        return True
    else :
        report_abnormal_vitals(bms_vitals)
        return False
    
if __name__ == '__main__':
  assert(battery_is_ok({'temperature': 25,'Soc': 70, 'Charge_rate': 0.7}) is True)  #all attributes fine
  assert(battery_is_ok({'Temperature': 50,'soc': 85, 'Charge_rate': 0}) is False)  #all attributes off limit
  assert(battery_is_ok({'Temperature': 100,'SOC': 30, 'Charge_rate': 0.5}) is False) #temp off limit
  assert(battery_is_ok({'Temperature': 25,'Soc': 10, 'charge_rate': 0.5}) is False) #SOC off limit
  assert(battery_is_ok({'Temperature': 25,'Soc': 70, 'CHARGE_RATE': 1}) is False) #charge off limit                
