def combine_shifts(shifts):
    combined_shifts = {}

    for shift in shifts:
        shift_id = list(shift.keys())[0]
        shift_name = shift[shift_id]

        if shift_id not in combined_shifts:
            combined_shifts[shift_id] = {"name": shift_name, "dates": []}

        combined_shifts[shift_id]["dates"].append(
            {"start": shift["start"], "end": shift["end"]}
        )

    # Reformat to match your desired output
    result = {}
    for k, v in combined_shifts.items():
        result[k] = {"name": v["name"], "dates": v["dates"]}

    return result


# Example usage
shifts = [
    {1: "Day", "start": "2024-08-18 12:00", "end": "2024-08-18 20:00"},
    {2: "Afternoon", "start": "2024-08-18 20:00", "end": "2024-08-19 05:00"},
    {3: "Night", "start": "2024-08-18 09:00", "end": "2024-08-18 12:00"},
    {3: "_time_left", "start": "2024-08-19 05:00", "end": "2024-08-19 09:00"},
]

combined = combine_shifts(shifts)
print(combined)
