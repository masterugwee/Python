import re
def reading_emails():
    f = open("/home/masterugwee/projects/bi0s/challenges!/python/list_mails..txt", "r")
    content = f.readlines()
    for line in content:
            if (re.search(r"^[\w\.\+\-]+\@[\w]+\.[a-zA-Z]{3}$", line)):
                print(line)
        #print(domainpart)

if __name__ == "__main__":
    reading_emails()
