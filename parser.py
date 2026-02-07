# this file will parse the logs
#BESTPOSA,USB1,0,58.5,FINESTEERING,2209,502061.000,02000020,cdba,16809;SOL_COMPUTED,PPP,51.15043706870,-114.03067882331,1097.3462,-17.0001,WGS84,0.0154,0.0139,0.0288,"TSTR",11.000,0.000,43,39,39,38,00,00,7f,37*52483ac5
# 

ASCII_KEYS = {
    header = 0,
    solution_ststus = 1,
    position_type = 2,
    lat = 3,
    lon = 4,
    height = 5, # Height above sea level
    undulation = 6,
    datum_id = 7,
    lat_std_dev = 8,
    lon_std_dev = 9,
    height_std_dev = 10,
    base_station_id = 11,
    differential_age = 12,
    solution_age = 13,
    num_satellites = 14,
    num_satellites_L1_E1_B1 = 15,
    num_satellites_multi_freq = 16,
    
}