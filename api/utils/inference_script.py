import xgboost as xgb
import pandas as pd

# Local paths
xgboost_model_file: str = "xgboost-model"

# Columns used during training
training_columns = [
    "arrival_date",
    "arrival_month",
    "arrival_year",
    "lead_time",
    "market_segment_type_Aviation",
    "market_segment_type_Complementary",
    "market_segment_type_Corporate",
    "market_segment_type_Offline",
    "market_segment_type_Online",
    "no_of_adults",
    "no_of_children",
    "no_of_special_requests",
    "required_car_parking_space",
    "room_type_reserved_Room_Type 1",
    "room_type_reserved_Room_Type 2",
    "room_type_reserved_Room_Type 3",
    "room_type_reserved_Room_Type 4",
    "room_type_reserved_Room_Type 5",
    "room_type_reserved_Room_Type 6",
    "room_type_reserved_Room_Type 7",
    "type_of_meal_plan_Meal Plan 1",
    "type_of_meal_plan_Meal Plan 2",
    "type_of_meal_plan_Meal Plan 3",
    "type_of_meal_plan_Not Selected",
]

# Load the model
model = xgb.Booster()
model.load_model(xgboost_model_file)

def make_inference(input):
    # Create a DataFrame from the input
    df_input = pd.DataFrame(input, columns=[
            "no_of_adults", "no_of_children", "required_car_parking_space", "lead_time",
            "arrival_year", "arrival_month", "arrival_date",
            "type_of_meal_plan", "room_type_reserved", "market_segment_type",
            "no_of_special_requests"
    ])
    # One-hot encode the categorical columns
    df_input = pd.get_dummies(
        data=df_input,
        prefix=[
            "type_of_meal_plan",
            "room_type_reserved",
            "market_segment_type",
        ],
        columns=[
            "type_of_meal_plan",
            "room_type_reserved",
            "market_segment_type",
        ],
    )

    # Add missing columns
    for column in training_columns:
        if column not in df_input.columns:
            df_input[column] = 0

    # Convert boolean columns to integer
    df_input = df_input * 1
    # Sort columns alphabetically
    df_input = df_input.sort_index(axis=1)
    # Preprocess the data
    dtest = xgb.DMatrix(df_input)
    # Predict
    prediction = model.predict(dtest)
    print(df_input.columns)
    return int (prediction[0]+1)







