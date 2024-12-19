# import os
# from datetime import datetime

# SENDER_EMAIL = "punit@alluvium.in"
# RECEIVER_EMAIL = "shiv.s@cmr.co.in" # "namdeopatil.1995@gmail.com"      
# # SMTP_LOGIN_EMAIL_PASS = "iewv kclp pjoh wpqk"     # Namdeo Patil
# SMTP_LOGIN_EMAIL_PASS= 'qoyp hdxq zhvc flbb'          # Punit Pandey


# #innovations.it@cmr.co.in
# #"shiv.s@cmr.co.in"



from pydantic import BaseModel
from typing import List


class CameraURL(BaseModel):
    camera_id: int
    url: str

class CameraROIReset(BaseModel):
    camera_id: int
    object_id: int

class SnapDate(BaseModel):
    filename: str
    path: str
    time: str

class SnapMonth(BaseModel):
    filename: str
    path: str
    time: str

class VideoDate(BaseModel):
    filename: str
    path: str
    time: str

class VideoMonth(BaseModel):
    filename: str
    path: str
    time: str

class Object_Count(BaseModel):
    camera_id : int
    object_count: int

class ObjectCountsResponse(BaseModel):
    counts: List[Object_Count]

class People_Count(BaseModel):
    camera_id: int
    people_count: int

class PeopleCountsResponse(BaseModel):
    counts: List[People_Count]

class SnapshotCountResponse(BaseModel):
    count: int
    snapshots: List[SnapDate]  # Replace SnapDate with your snapshot model

