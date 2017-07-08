import pandas  as pd

def data_exploration(df_data):


if __name__ == '__main__':
    df_data = pd.read_csv(r'../../../Data/Input/dengue_features_train.csv')
    df_data_labels = pd.read_csv(r'../../../Data/Input/dengue_labels_train.csv')
    df_data.set_index(df_data['week_start_date'] + '_' + df_data['city'], inplace=True)
    df_data_labels.set_index(df_data['week_start_date'] + '_' + df_data['city'], inplace=True)