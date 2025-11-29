import requests
url = "https://gist.githubusercontent.com/phillipj/4944029/raw/75ba2243dd5ec2875f629bf5d79f6c1e4b5a8b46/alice_in_wonderland.txt"
try:
    response = requests.get(url, allow_redirects=True)
    response.raise_for_status()
    response.encoding = "utf-8"
    text_content = response.text
    lines = text_content.splitlines()
    print(f"Successful crawl! A total of {len(lines)} lines of text were obtained")
    
except requests.exceptions.RequestException as e:
    print(f"Failed to obtain the file:{e}")
    
with open("Alice.txt", "r", encoding="utf_8") as file:
    lines = file.readlines()
if lines:
    with open("Alice.txt", "w+", encoding="utf-8")as file:
        file.write(text_content)
        print(f"\nAll the text has been written into Alice.txt (a total of {len(lines)} lines)")
def check_list(a, b):
    if not (isinstance(a, (str, list)) and isinstance(b, (str))):
        raise TypeError("Parameter a muss eine zeichenfolge/liste sein, parameter b muss eine zeichenfolge sein")
    if isinstance(a, str):
        a = [a]
    count = 0
    for idx, elem in enumerate(a):
        if not isinstance(elem, str):
            print("Ignore the non-string elements of the index {idx} in a: {elem}")
            continue
    if elem in b:
        count += 1
    return count

negative_words = ["bad", "scream", "ugly", "mad", "terrible", "horror", "assault", "attack", "terror", "blame", "guilt", "shame", "brutal", "corrupt"]
positive_words = ["good", "cheer", "beautiful", "nice", "awesome", "terrific", "calm", "friendly", "friendship", "great", "amazing", "comfort", "joy", "happy"]

total_neg = 0
total_pos = 0
negative_ids = []
positive_ids = []
for line_num, line_content in enumerate(lines, start=1):
    neg_count = check_list(negative_words, line_content.lower())
    pos_count = check_list(positive_words, line_content.lower())
    total_neg += neg_count
    total_pos += pos_count
    if neg_count > 0:
        negative_ids.append(line_num)
    if pos_count > 0:
        positive_ids.append(line_num)
print(f"The total number of negative words in the entire book:{total_neg}")
print(f"The total number of positive words in the entire book:{total_pos}")        
print(f"The total Line numbers containing negative words:{negative_ids}")        
print(f"The total Line numbers containing positive words:{positive_ids}")        

import matplotlib.pyplot as plt
plt.hist(negative_ids, color="red", alpha=0.5, label="Negative words")
plt.hist(positive_ids, color="green", alpha=0.5, label="Positive words")
plt.xlabel("Line Number")
plt.ylabel("Count")
plt.title("Distribution of Positive/Negative Words in Alice in Wonderland")
plt.legend()
plt.show()


        
