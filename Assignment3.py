import json
from pylab import *
from collections import Counter


def pie1(com, edu):
    labels = '.COM', '.EDU'
    sizes = [com, edu]
    colors = ['gold', 'yellowgreen']
    explode = (0, 0)
    plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)
    plt.axis('equal')
    plt.show()


def pie2(linklist2, vis_list2):
    new_link = []
    new_vis = []
    for i in range(0, 10):
        new_link.append(linklist2[i])
        new_vis.append(vis_list2[i])
    labels = new_link
    sizes = new_vis
    colors = ['gold', 'yellowgreen', 'blue', 'green', 'red', 'purple', 'black', 'orange', 'white', 'lightcoral']
    explode = (0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)
    plt.axis('equal')
    plt.show()


def getDate(line):
    start = line.find('[')
    end = line.find(':')
    date = line[start:end]
    date = date.replace('[', '')
    return date


def getWebsite(line):
    end = line.find('- -')
    website = line[:end]
    website = website.strip()
    return website


def getDay(date):
    try:
        end = date.find('/')
        day = date[:end]
    except:
        day = 1
    return day


def keepDigits(visitors):
    new_visitors = '0'
    for c in str(visitors):
        if c.isdigit():
            new_visitors += c
    return new_visitors


def getAccessNumber(date, jul_counter):
    day = getDay(date)
    visitors = 1
    try:
        visitors = int(visitors)
    except:
        visitors = 0
    if date:
        jul_counter[day] += visitors
    else:
        pass
    return jul_counter


def getSize(line):
    count = 0
    while line[count - 1:count] != ' ':
        count -= 1
    visitors = line[count:]
    try:
        visitors = keepDigits(visitors)
        visitors = visitors.strip()
        visitors = int(visitors)
    except:
        visitors = 0
    return visitors


def getEduVsCom(website, com, edu):
    if '.com' in website:
        com += 1
    elif '.edu' in website:
        edu += 1
    return com, edu


def checkLine(line):
    foo = 0
    for c in line:
        foo += 1
    if foo < 30:
        return False
    else:
        return True


k = 0
linklist2 = []
vis_list2 = []
text2 = open('Total_Access_Number_Of_Each_Day.txt', 'w')
jul_counter = {'01': 0, '02': 0, '03': 0, '04': 0, '05': 0, '06': 0, '07': 0, '08': 0, '09': 0, '10': 0, '11': 0,
               '12': 0, '13': 0, '14': 0, '15': 0, '16': 0, '17': 0, '18': 0, '19': 0, '20': 0, '21': 0, '22': 0,
               '23': 0, '24': 0, '25': 0, '26': 0, '27': 0, '28': 0, '29': 0, '30': 0}
month_counter = 1
com = 0
edu = 0
linklist = []
size_list = []
previous_date = '01/Jul/1995'
text = open('NASA_access_log_Jul95.txt', 'r', encoding='utf-8', errors='ignore')
for line in text:
    my_bool = checkLine(line)
    if my_bool == False:
        break
    print(k)
    k += 1
    date = getDate(line)
    jul_counter = getAccessNumber(date, jul_counter)
    website = getWebsite(line)
    size = getSize(line)
    size_list.append(int(size))
    linklist.append(website)
    com, edu = getEduVsCom(website, com, edu)
text.close()

print('Finding Total Access_Number Of Each Day...')
json.dump(jul_counter, text2, ensure_ascii=False, indent=2)
print('Done finding. Check "Total_Access_Number_Of_Each_Day.txt"\n')
text2.close()

print('Finding .com and .edu websites...')
text4 = open('ComVsEdu_DomainCount.txt', 'w')
text4.write('.com websites: \t' + str(com) + '\n .edu websites: \t' + str(edu))
text4.close()
print('Done finding. Check "ComVsEdu_DomainCount.txt"\n')

print('Finding Top 10 Visited...')
text3 = open('Top10_Visited.txt', 'w')
count_website = Counter(linklist)
count = 0
for key, value in ([(k, v) for v, k in sorted([(v, k) for k, v in count_website.items()], reverse=True)]):
    if count > 9:
        break
    linklist2.append(key)
    vis_list2.append(value)
    count += 1
    text3.write(key + ':\t' + str(value) + '\n')
print('Done Sorting, Check "Top10_Visited.txt"\n')
text3.close()

print('Finding unique addresses...')
unique_list = set(linklist)
text5 = open('Distinct_Clients.txt', 'w')
for w in unique_list:
    text5.write(str(w) + '\n')
print('Done. Check "Distinct_Clients.txt"\n')
text5.close()

print('Finding average size of delivered files...')
text6 = open('Average_Size.txt', 'w')
text6.write(str(sum(size_list) / float(len(size_list))))
print('Done. Check "Average_Size.txt"\n')
text6.close()

print("Pie chart for EDU vs COM count should appear...")
print("Pie chart for top 10 visited should appear...")

pie1(com, edu)
pie2(linklist2, vis_list2)
