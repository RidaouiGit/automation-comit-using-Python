import subprocess as cmd
# from termcolor import colored

# Optionally use
# $black . --quiet


cp = cmd.run("git add .", check=True, shell=True)

response = input("Do you want to use the default message for this commit?([y]/n)\n")
message = "update the repository"

if response.startswith('n'):
    message = input("What message you want?\n")

cp = cmd.run(f"git commit -m '{message}'", check=True, shell=True)

cp = cmd.run("git push -u origin master -f", check=True, shell=True)
