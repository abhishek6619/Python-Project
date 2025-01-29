import time
import winsound


def set_alarm():
    print("Welcome to your alarm clock!")
    alarm_time = input("Enter the time for alarm (in HH:MM:SS format): ")

    while True:
        current_time = time.strftime("%H:%M:%S")
        print(f"Current time: {current_time}", end="\r")
        time.sleep(1)

        if current_time == alarm_time:
            print("\nIt's time!")
            winsound.Beep(1000, 10000)
            break


if __name__ == "__main__":
    set_alarm()
