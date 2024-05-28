import datetime
def add(moment):
    # Convert the moment to seconds using timestamp() method
    original_seconds = moment.timestamp()
    # Add 1 gigasecond (10^9 seconds) by adding it to the original seconds
    total_seconds = original_seconds + 1e9
    # Convert the total seconds back to a datetime object using fromtimestamp() method
    final_time = datetime.datetime.fromtimestamp(total_seconds)
    return final_time
