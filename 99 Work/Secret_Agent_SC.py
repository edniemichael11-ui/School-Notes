agent_Numb = int(input("Agent Number? "))
security_lv = int(input("Security Level? "))

if agent_Numb == 0o7 or  security_lv >= 5:
    print("Access Granted")
elif security_lv == 0:
    print("SECURITY ALERT!")
else:
    print("Access Denied")
