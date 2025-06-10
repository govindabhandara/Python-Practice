def send_campaign(subject, *recipients, **options):
    print("Subject:", subject)
    print("To:", ", ".join(recipients))
    print("Options:")
    for key, val in options.items():
        print(f"  {key} = {val}")

send_campaign(
    "New Product Launch",
    "user1@example.com", "user2@example.com",
    sender="marketing@company.com",
    track_opens=True,
    urgency="high"
)
