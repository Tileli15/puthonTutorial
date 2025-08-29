# rogram that converts a duration into hours, minutes, and seconds
duration = int(input("Enter a duration in seconds: ")) 
hours = duration // 3600
minutes = (duration % 3600) // 60
seconds = duration % 60
print(f"{duration} seconds is equal to {hours} hours, {minutes} minutes, and {seconds} seconds.")
