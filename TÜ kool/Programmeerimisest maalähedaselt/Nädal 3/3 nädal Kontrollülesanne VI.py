import re

IK = (input("Sisesta isikukood: "))


if ( re.match("^[1-6][0-9]{10}", IK)
     and len(IK)==11):

    print("On Eesti isikukood")
else:
    print("Ei ole Eesti isikukood")