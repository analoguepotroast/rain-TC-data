These python codes are specifically used to find bearing & distance of flood events associated with their hurricane tracking points. 
Three parts are included:
1.Interpolating hurricane track polylines into hourly hurricane tracking point. (excelsplit.py, track.py)
2.Pairing each flood event with its associated hurricane by time. (DataSelection.py)
3.Calculating bearing and distance information related to the paired flood events and hurricanes. (The base points are hurricane tracking points)

Note that the second part is very time-consuming due to the huge volume of flood events. If the flood events have no relevant hurricanes, they will be out of the selection. 
Using the process illustrated, the following results can be achieved:
1.The hurricane tracks were sucessfully interpolated, providing the possibility of developing even finer spatial resolution of tracking points used to examine the relationship between hurricanes and floods.
2.The location and time of every hurricane tracking point and their relevant flood events were determined. 
3.The bearing distance information of specific flood events based on specific hurricane tracking points was calculated.
