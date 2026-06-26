import pandas as pd

def preprocess(
    ssc,
    hsc,
    degree,
    etest,
    mba,
    gender,
    ssc_board,
    hsc_board,
    hsc_stream,
    degree_type,
    workex,
    specialisation
):

    data = {
        "ssc_p": ssc,
        "hsc_p": hsc,
        "degree_p": degree,
        "etest_p": etest,
        "mba_p": mba,

        "gender_M": 1 if gender == "Male" else 0,

        "ssc_b_Others": 1 if ssc_board == "Others" else 0,

        "hsc_b_Others": 1 if hsc_board == "Others" else 0,

        "hsc_s_Commerce": 1 if hsc_stream == "Commerce" else 0,
        "hsc_s_Science": 1 if hsc_stream == "Science" else 0,

        "degree_t_Others": 1 if degree_type == "Others" else 0,
        "degree_t_Sci&Tech": 1 if degree_type == "Sci&Tech" else 0,

        "workex_Yes": 1 if workex == "Yes" else 0,

        "specialisation_Mkt&HR": 1 if specialisation == "Mkt&HR" else 0
    }

    return pd.DataFrame([data])