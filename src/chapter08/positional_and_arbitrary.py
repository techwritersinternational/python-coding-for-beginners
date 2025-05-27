def mission_log(date, *events):
    print(f"Mission log - Date: {date}")
    for event in events:
        print(f"  Event: {event}")

mission_log("2023-05-20", "Liftoff successful", "Entered orbit", "Deployed satellite")