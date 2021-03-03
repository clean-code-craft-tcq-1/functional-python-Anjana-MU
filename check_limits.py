bms_attribute_limits = {
     'temperature': {'min': 0, 'max': 45},
     'soc': {'min': 20, 'max': 80},
     'charge_rate': {'min': 0,'max': 0.8}
        }


def check_attributes_limit(bms_attribute):
    offLimits = []
    for bms_name,bms_value in bms_attribute.items() :
        compare_parameter_values(bms_name,bms_value,offLimits)       
    return offLimits

def compare_parameter_values(bms_name,bms_value,offLimits):
     if (bms_value < bms_attribute_limits[bms_name]['min']) or (bms_value > bms_attribute_limits[bms_name]['max']):
            offLimits.append(bms_name)


def battery_is_ok(bms_attribute):
    bms_attributes_check = check_attributes_limit(bms_attribute)
    if len(bms_attributes_check) == 0:
        print("Battery is ok")
        return True
    else :
        print("Battery is not ok")
        return False
    
if __name__ == '__main__':
  assert(battery_is_ok({'temperature': 25,'soc': 70, 'charge_rate': 0.7}) is True)  #all attributes fine
  assert(battery_is_ok({'temperature': 50,'soc': 85, 'charge_rate': 0}) is False)  #all attributes off limit
  assert(battery_is_ok({'temperature': 100,'soc': 30, 'charge_rate': 0.5}) is False) #temp off limit
  assert(battery_is_ok({'temperature': 25,'soc': 10, 'charge_rate': 0.5}) is False) #SOC off limit
  assert(battery_is_ok({'temperature': 25,'soc': 70, 'charge_rate': 1}) is False) #charge off limit    
