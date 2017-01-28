def get_max_rpm(car):
    car_rpms = {
		'abarth500': 6522,
		'abarth500_s1': 6522,
		'bmw_1m': 7260,
		'bmw_1m_s3': 7060,
		'bmw_m3_e30': 7305,
		'bmw_m3_e30_drift': 8034,
		'bmw_m3_e30_dtm': 9260,
		'bmw_m3_e30_gra': 8260,
		'bmw_m3_e30_s1': 7298,
		'bmw_m3_e92': 8447,
		'bmw_m3_e92_drift': 8463,
		'bmw_m3_e92_s1': 8430,
		'bmw_m3_gt2': 8848,
		'bmw_z4': 7246,
		'bmw_z4_drift': 7060,
		'bmw_z4_gt3': 8773,
		'bmw_z4_s1': 7246,
		'ferrari_312t': 13064,
		'ferrari_458': 9322,
		'ferrari_458_s3': 9312,
		'ferrari_599xxevo': 9152,
		'ferrari_f40': 7822,
		'ferrari_f40_s3': 7829,
		'ktm_xbow_r': 7243,
		'lotus_2_eleven': 8248,
		'lotus_49': 10078,
		'lotus_elise_sc': 8524,
		'lotus_elise_sc_s1': 8526,
		'lotus_elise_sc_s2': 8524,
		'lotus_evora_gtc': 7299,
		'lotus_evora_gte': 7290,
		'lotus_evora_gx': 7298,
		'lotus_evora_s': 7230,
		'lotus_evora_s_s2': 7260,
		'lotus_exige_240': 8540,
		'lotus_exige_240_s3': 8540,
		'lotus_exige_s_roadster': 7267,
		'lotus_exige_scura': 8545,
		'lotus_exos_125': 10255,
		'lotus_exos_125_s1': 18163,
		'mclaren_mp412c': 8586,
		'mclaren_mp412c_gt3': 7620,
		'p4-5_2011': 8282,
		'pagani_huayra': 7105,
		'pagani_zonda_r': 8158,
		'tatuusfa1': 6542
	}

    return car_rpms.get(car)


def change_car_name(car_temp):
    global CAR
    upgrades = ("_s1", "_s2", "_s3", "_drift", "_dtm")
    if car_temp.endswith(upgrades):
        upgrade = car_temp.split("_")[-1].capitalize()
        car_temp = '_'.join(car_temp.split("_")[0:-1])
    else:
        upgrade = "STD"

    if car_temp == "ktm_xbow_r":
        CAR = "X-Bow R"
    elif car_temp == "tatuusfa1":
        CAR = "Formula Abarth"
    elif car_temp == "lotus_49":
        CAR = "Type 49"
    elif car_temp == "ferrari_458":
        CAR = "458 Italia"
    elif car_temp == "bmw_z4":
        CAR = "Z4 E89 35is"
    elif car_temp == "bmw_m3_e30":
        CAR = "M3 E30 Sport Evolution"
    elif car_temp == "p4-5_2011":
        CAR = "P45 Competizione"
    elif car_temp == "abarth500":
        CAR = "500 EsseEsse"
    elif car_temp == "lotus_2_eleven":
        CAR = "2-Eleven"
    elif car_temp == "lotus_elise_sc":
        CAR = "Elise SC"
    elif car_temp in ["lotus_evora_gte", "lotus_evora_gtc"]:
        CAR = (''.join(car_temp.split("_")[1]).title() + " " +
               ''.join(car_temp.split("_")[2]).upper())
    elif car_temp == "mclaren_mp412c":
        CAR = "MP4-12C"
    elif car_temp == "mclaren_mp412c_gt3":
        CAR = "MP4-12C GT3"
    elif car_temp == "ferrari_599xxevo":
        CAR = "599xx EVO"
    elif car_temp == "bmw_m3_e30_gra":
        CAR = "M3 E30 Group A"
    elif car_temp in ["bmw_m3_gt2", "bmw_z4_gt3"]:
        CAR = ' '.join(car_temp.split("_")[1:]).upper()
    else:
        CAR = ' '.join(car_temp.split("_")[1:]).title()
    return upgrade, CAR


def change_track_name(track_temp):
    global TRACK
    if track_temp == "monza66":
        TRACK = "Monza historic 1966"
    elif track_temp == "drift":
        TRACK = "Assetto Dorifto track"
    elif "-" in track_temp:
        TRACK = ' '.join(track_temp.split("-")).title()
    else:
        TRACK = track_temp.capitalize()
    return TRACK
