import json

from src.model.machine_description_dto import MachineDescriptionDTO
import joblib
import pandas as pd

model = joblib.load("src/service/static/random_forest.pkl")


def predict(machine_description: MachineDescriptionDTO):
    pred = model.predict_proba(_convert_to_dataframe(machine_description))
    return json.dumps(pred.tolist())


def _convert_to_dataframe(machine_description: MachineDescriptionDTO):
    return pd.DataFrame({
        'Type': [_encode_machine_type(machine_description)],
        'Air temperature [°C]': [machine_description.air_temperature],
        'Process temperature [°C]': [machine_description.process_temperature],
        'Rotational speed [rpm]': [machine_description.rotational_speed],
        'Torque [Nm]': [machine_description.torque],
        'Tool wear [min]': [machine_description.tool_wear],
        'Target': [machine_description.target],
        'Temperature difference [°C]': [machine_description.process_temperature - machine_description.air_temperature]
    })


def _encode_machine_type(machine_description: MachineDescriptionDTO):
    match machine_description.type:
        case "M":
            return 1
        case "L":
            return 2
        case "H":
            return 3
        case _:
            return 0
