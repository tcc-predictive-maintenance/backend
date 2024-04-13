from pydantic import BaseModel


class MachineDescriptionDTO(BaseModel):
    type: str
    air_temperature: float
    process_temperature: float
    rotational_speed: int
    torque: float
    tool_wear: int
    target: int

