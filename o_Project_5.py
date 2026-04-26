import pandas as pd
class Flight:
    def __init__(self, flight_num, delay_time):
        self.flight_num = flight_num
        self.delay_time = delay_time
    def check_severity(self):
        if self.delay_time > 60:
            print("Severe Warning:", self.flight_num, "is heavily delayed (", self.delay_time, "mins )")
        elif self.delay_time >= 30:
            print("Warning:", self.flight_num, "is delayed (", self.delay_time, "mins )")
        else:
            print("Flight", self.flight_num, "is on time")
data = pd.read_csv("n_arrivals.csv")
data["Minutes_Delayed"] = data["Minutes_Delayed"].fillna(0)
late_flights = data[data["Minutes_Delayed"] > 30]
most_late = late_flights.loc[late_flights["Minutes_Delayed"].idxmax()]
f = Flight(most_late["Flight_Number"], most_late["Minutes_Delayed"])
f.check_severity()
log_entry = pd.DataFrame({
    "Flight_Number": [most_late["Flight_Number"]],
    "Airline": [most_late["Airline"]],
    "Minutes_Delayed": [most_late["Minutes_Delayed"]]
})
try:
    old_log = pd.read_csv("p_severe_delays_log.csv")
    final_log = pd.concat([old_log, log_entry], ignore_index=True)
except FileNotFoundError:
    final_log = log_entry
final_log.to_csv("p_severe_delays_log.csv", index=False)
