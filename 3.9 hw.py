zodiac_elements = {"water": ["Cancer", "Scorpio", "Pisces"], "fire": ["Aries", "Leo", "Sagittarius"], "earth": ["Taurus", "Virgo", "Capricorn"], "air":["Gemini", "Libra", "Aquarius"]}
print(zodiac_elements.get("water"))
print(zodiac_elements.get("air"))

user_ids = {"superCoder": 103419, "pythonGuy": 182921, "samTheJavaMaam": 123112, "lyleLoop": 102931, "keysmithKeith": 129384}
tc_id=(user_ids.get("superCoder",100000))
print(tc_id)
stack_id=(user_ids.get("fakeUser",100000))
print(stack_id)

fruits = {"apples": 10, "banana": 5, "berries": 20, "grapes": 25, "melon": 15, "pear": 30}
fruits.pop("berries")
fruits.pop("melon")

coding_languages = {"scratch": 10, "python": 13, "HTML": 15, "CSS": 22, "Java": 19, "C": 18, "Javascript": 18}
lessons=list(coding_languages.keys())
print(lessons)

total=list(coding_languages.values())
print(total)

men_in_occupation = {"CEO": 28, "Engineering Manager": 10, "Pharmacist": 48, "Physician": 45, "Lawyer": 35, "Aerospace Engineer": 19}
for i,j in men_in_occupation.items():
    print("Men make up",j,"percent of",i+"s.")
