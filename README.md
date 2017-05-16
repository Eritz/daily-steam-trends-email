# daily-steam-trends-email

Emails a list of trending game titles on Steam based upon specific scoring criterias and rankings defined by the user. 
All score information is collected from
[Steam Spy](https://steamspy.com/). The program is best used as a cron job.

# Specifics
This program is created using Python, and utilizes the Beautiful Soup and smtplib packages. Regular expressions are used to locate any
missing data (written as "N/A" on Steam Spy) and to identify the score percentages.

# Set Up
Before beginning, ensure that the SMTP protocol and SMTP server match with the sending email. For example, 'smtp.gmail.com' and the 587 protocol
should be used if example@gmail.com is the sender's email.


For security reasons, it is advised to let the password be manually entered **each time** the program runs.
