from datetime import datetime, timedelta

def predict_cycle():

    last_period = input("Enter last period date (YYYY-MM-DD): ")
    cycle_length = int(input("Enter cycle length in days: "))
    period_duration = int(input("Enter period duration in days: "))

    start_date = datetime.strptime(last_period, "%Y-%m-%d")

    next_period = start_date + timedelta(days=cycle_length)

    period_end = next_period + timedelta(days=period_duration - 1)

    ovulation_date = next_period - timedelta(days=14)

    fertility_start = ovulation_date - timedelta(days=5)
    fertility_end = ovulation_date

    print("\nMenstrual Cycle Prediction")

    print("Next Period Date:",
          next_period.strftime("%B %d, %Y"))

    print("Period End Date:",
          period_end.strftime("%B %d, %Y"))

    print("Ovulation Date:",
          ovulation_date.strftime("%B %d, %Y"))

    print("Fertility Window:")
    print("Start:",
          fertility_start.strftime("%B %d, %Y"))

    print("End:",
          fertility_end.strftime("%B %d, %Y"))


while True:

    predict_cycle()

    again = input("\nDo you want to predict again? (yes/no): ").lower()

    if again != "yes":
        print("Goodbye and take care!")
        break