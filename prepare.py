import pandas as pd

def update_dtypes(df):
    df['date'] = pd.to_datetime(df.date)
    df['calories_burned'] = df['calories_burned'].str.replace(',', '')
    df['calories_burned'] = df['calories_burned'].astype(int)
    df['steps'] = df['steps'].str.replace(',', '')
    df['steps'] = df['steps'].astype(int)
    df['minutes_sedentary'] = df['minutes_sedentary'].str.replace(',', '')
    df['minutes_sedentary'] = df['minutes_sedentary'].astype(int)
    df['activity_calories'] = df['activity_calories'].str.replace(',', '')
    df['activity_calories'] = df['activity_calories'].astype(int)
    df['distance'] = df['distance'].astype(float)
    df['minutes_lightly_active'] = df['minutes_lightly_active'].astype(int)
    df['minutes_fairly_active'] = df['minutes_fairly_active'].astype(int)
    df['minutes_very_active'] = df['minutes_very_active'].astype(int)
    df[' floors'] = df[' floors'].astype(int)
    df.set_index('date', inplace=True)
    return df

def add_minutes_active_column(df):
    df['minutes_activity'] = df.minutes_lightly_active + df.minutes_fairly_active + df.minutes_very_active
    return df

def merge_yhats():
    forecast_minactive.rename(index=str, columns={'yhat':'minutes_active_pred', 'ds':'date'}, inplace=True)
    forecast_minsedentary.rename(index=str, columns={'yhat':'minutes_sedentary_pred','ds':'date1'}, inplace=True)
    forecast_steps.rename(index=str, columns={'yhat':'steps_pred','ds':'date2'}, inplace=True)
    forecast_calories_burned.rename(index=str, columns={'yhat':'calories_burned_pred','ds':'date3'}, inplace=True)
    frames = [forecast_minactive, forecast_minsedentary, forecast_steps, forecast_calories_burned]
    df_preds = pd.concat(frames, axis=1)
    df_preds = df_preds.drop(['date1','date1','date2','date3'], axis=1)
    df_preds.set_index('date', inplace=True)
    df_preds = df_preds.tail(14)
    df_preds.to_csv('fitbit_preds.csv')
    return df_preds


