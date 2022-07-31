check_door = 0
fill_water = 1
add_detergent = 3
cycle = 4
drain_water = 5
spin = 6

current_state = -1
next_state = -1

start = None
door_close = None

if(current_state == check_door):
    if(start == 1 and door_close == 1):
        next_state = fill_water
        motor_on = 0
        fill_value_on = 0
        drain_value_on = 0
        door_lock = 1
        soap_wash = 0
        water_wash = 0
        done = 0
    else:
        next_state = current_state
        motor_on = 0
        fill_value_on = 0
        drain_value_on = 0
        door_lock = 0
        soap_wash = 0
        water_wash = 0
        done = 0
elif(current_state == fill_water):
    if (filled==1):
        if(soap_wash == 0):
            next_state = add_detergent
            motor_on = 0
            fill_value_on = 0
            drain_value_on = 0
            door_lock = 1
            soap_wash = 1
            water_wash = 0
            done = 0
        else:
            next_state = cycle
            motor_on = 0
            fill_value_on = 0
            drain_value_on = 0
            door_lock = 1
            soap_wash = 1
            water_wash = 1
            done = 0
    else:
        next_state = current_state
        motor_on = 0
        fill_value_on = 1
        drain_value_on = 0
        door_lock = 1
        done = 0
elif(current_state == add_detergent):
    if(detergent_added==1):
        next_state = cycle
        motor_on = 0
        fill_value_on = 0
        drain_value_on = 0
        door_lock = 1
        soap_wash = 1
        done = 0
    else:        
        next_state = current_state
        motor_on = 0
        fill_value_on = 0
        drain_value_on = 0
        door_lock = 1
        soap_wash = 1
        water_wash = 0
        done = 0
elif(current_state == cycle):
    if(cycle_timeout == 1):
        next_state = drain_water
        motor_on = 0
        fill_value_on = 0
        drain_value_on = 0
        door_lock = 1
        # soap_wash = 1
        done = 0
    else:
        next_state = current_state
        motor_on = 1
        fill_value_on = 0
        drain_value_on = 0
        door_lock = 1
        # soap_wash = 1
        done = 0
elif(current_state == drain_water):
    if(drained==1):
        if(water_wash==0):
            next_state = fill_water
            motor_on = 0
            fill_value_on = 0
            drain_value_on = 0
            door_lock = 1
            soap_wash = 1
            # water_wash = 1
            done = 0
        else:
            next_state = spin
            motor_on = 0
            fill_value_on = 0
            drain_value_on = 0
            door_lock = 1
            soap_wash = 1
            water_wash = 1
            done = 0
    else:
        next_state = current_state
        motor_on = 0
        fill_value_on = 0
        drain_value_on = 1
        door_lock = 1
        soap_wash = 1
        # water_wash = 1
        done = 0
elif(current_state == spin):
    if(spin_timeout==1):
        next_state = door_close
        motor_on = 0
        fill_value_on = 0
        drain_value_on = 0
        door_lock = 1
        soap_wash = 1
        water_wash = 1
        done = 1
    else:
        next_state = current_state
        motor_on = 0
        fill_value_on = 0
        drain_value_on = 1
        door_lock = 1
        soap_wash = 1
        water_wash = 1
        done = 0
else:
    next_state = check_door

if(reset):
    current_state<=check_door
else:
	current_state<=next_state


