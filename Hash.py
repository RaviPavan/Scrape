import hashlib
import binascii
# Python3 code for above approach 
def idToShortURL(id):
    map = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789" # `~!@#$%^&*()_-+=[]{};:'",.<>?/|\
    shortURL = ""
      
    # for each digit find the base 62
    while(id > 0):
        shortURL += map[id % 62]
        id //= 62
  
    # reversing the shortURL
    return shortURL[len(shortURL): : -1]
  
def shortURLToId(shortURL):
    id = 0
    for i in shortURL:
        val_i = ord(i)
        if(val_i >= ord('a') and val_i <= ord('z')):
            id = id*62 + val_i - ord('a')
        elif(val_i >= ord('A') and val_i <= ord('Z')):
            id = id*62 + val_i - ord('A') + 26
        else:
            id = id*62 + val_i - ord('0') + 52
    return id

def idToShortUR_new(id):
    map = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789`~!@#$%^&*()_-+=[]\{\};:'\",.<>?/|\\"
    shortURL = ""
      
    # for each digit find the base 94
    while(id > 0):
        shortURL += map[id % 94]
        id //= 94
  
    # reversing the shortURL
    return shortURL[len(shortURL): : -1]
  
def shortURLToId(shortURL):
    id = 0
    for i in shortURL:
        val_i = ord(i)
        if(val_i >= ord('a') and val_i <= ord('z')):
            id = id*94 + val_i - ord('a')
        elif(val_i >= ord('A') and val_i <= ord('Z')):
            id = id*94 + val_i - ord('A') + 26
        else:
            id = id*94 + val_i - ord('0') + 52
    return id
  
if (__name__ == "__main__"):
    input=["https://in.linkedin.com/in/riyaz-ali?trk=public_profile_browsemap", \
             "https://in.linkedin.com/in/srithar-dhulasiraman?trk=public_profile_browsemap", \
           "https://in.linkedin.com/in/heybharghavi?trk=public_profile_browsemap", \
            "https://in.linkedin.com/in/harivelaayutham?trk=public_profile_browsemap", \
            "https://www.linkedin.com/in/albertdesign?trk=public_profile_browsemap", \
            "https://in.linkedin.com/in/harshini-tanneeru-a91a99131?trk=public_profile_browsemap", \
            "https://sk.linkedin.com/in/michal-jur%C3%AD%C4%8Dek-8845978b?trk=public_profile_browsemap" \
    ]

    for url in input:
        processed_url=url.replace("https://","").replace(".linkedin.","").replace("?trk=public_profile_browsemap","")

        id=int(binascii.hexlify(processed_url.encode('utf-8')), 16)
        #id = 12345
        shortURL = idToShortURL(id)
        shortURL_new = idToShortUR_new(id)
        print(url, processed_url,id,shortURL,"-->",shortURL_new,len(shortURL),len(shortURL_new))
        #print("ID from", shortURL, "is : ", shortURLToId(shortURL))
        print("****************************************************************************************")

