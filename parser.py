# this file will parse the logs
#BESTPOSA,USB1,0,58.5,FINESTEERING,2209,502061.000,02000020,cdba,16809;SOL_COMPUTED,PPP,51.15043706870,-114.03067882331,1097.3462,-17.0001,WGS84,0.0154,0.0139,0.0288,"TSTR",11.000,0.000,43,39,39,38,00,00,7f,37*52483ac5
# 
def get_log_data(param, data):
    KEYS = {
        "solution_ststus": 0,
        "position_type": 1,
        "lat": 2,
        "lon": 3,
        "height": 4,  # Height above sea level
        "undulation": 5,
        "datum_id": 6,
        "lat_std_dev": 7,
        "lon_std_dev": 8,
        "height_std_dev": 9,
        "base_station_id": 10,
        "differential_age": 11,
        "solution_age": 12,
        "num_satellites": 13,
        "num_satellites_L1_E1_B1": 14,
        "num_satellites_multi_freq": 15,
    }

    data = "#BESTPOSA,USB1,0,58.5,FINESTEERING,2209,502061.000,02000020,cdba,16809;SOL_COMPUTED,PPP,51.15043706870,-114.03067882331,1097.3462,-17.0001,WGS84,0.0154,0.0139,0.0288,\"TSTR\",11.000,0.000,43,39,39,38,00,00,7f,37*52483ac5"
    if ";" in data:
        no_header = data[data.index(";"):] 
    split_string = no_header[1:].split(",")
    print(split_string[KEYS["lat"]])

get_log_data(1, 1)