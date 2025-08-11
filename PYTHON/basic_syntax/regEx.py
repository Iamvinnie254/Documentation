# python regular expresion(regex), sequence of characters that form a search pattern
# can be used to check if a string contains the specified pattern

import re

txt = "Results driven Full-Stack Developer with 2+ years of hands-on experience in designing, developing, and deploying scalable web applications. Proficient in React.js, Vue.js, Django, Laravel and MySQL, with a strong ability to translate business requirements into efficient technical solutions. Adept at leading cross-functional teams, optimizing performance, and implementing CI/CD pipelines. Passionate about building high-impact, user-centric applications in fast-paced environments."

x = re.search("^Results.*environments.$", txt)

if x:
    print("There is a match")

else:
    print("No match!")

r = "The rain in Spain"
x = re.search("^The.*Spain$", r)
print(x)