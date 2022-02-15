def create_time_series_structure(events, columns):
    import pandas as pd

    min_date = min(events.Date)
    max_date = max(events.Date)
    return pd.DataFrame(index=pd.period_range(start=pd.Period(min_date, 'D'), end=pd.Period(max_date, 'D')), columns=columns)


user_name = 'kaninaba94'