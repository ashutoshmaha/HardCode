def parseURL(url):
                                   
    seg2 = url.split('/')[2]    # Separating domain name
    seg1 = url.split(seg2)[-2]  # Deriving protocol
    print('Protocol:', seg1, '\n')
    print('Domain name:', seg2, '\n')
    seg3 = url.split(seg2)[1]   #Getting the path; if output is empty,the there is no path in URL
    print('Path:', seg3, '\n')

    if '#' in url:  # Extracting fragment id, else None
        seg4 = url.split('#')[1]
        print('Fragment ID:', seg4, '\n')
    else:
        seg4 = 'None'
    if '@' in url:              # Extracting user name, else None
        seg5 = url.split('/')[-1]
        print('Scheme with User Name:', seg5, '\n')
    else:
        seg5 = 'None'
    if '?' in url:              # Extracting query string, else None
        seg6 = url.split('?')[-1]
        print('Query string:', seg6, '\n')
    else:
        seg6 = 'None'

    print('**The dictionary is in the sequence: 0.URL 1.Protocol 2.Domain name 3.Path 4.Fragment id 5.User name 6.Query string** \n')
    
    dictionary = {'0.URL': url, '1.Protocol': seg1, '2.Domain name': seg2, '3.Path': seg3, '4.Fragment id': seg4,
                  '5.User name': seg5, '6.Query string': seg6}  # Printing required dictionary
    print(dictionary, '\n')

    print('The TLD in the given URL is following: ')
    if '.com' in url:           # Extracting most famous TLDs maintained by ICAAN
        print('.com\n')
    elif '.de' in url:
        print('.de\n')
    elif '.uk' in url:
        print('.uk\n')
    elif 'gov' in url:
        print('gov\n')
    elif '.org' in url:
        print('.org\n')
    elif '.ru' in url:
        print('.ru\n')
    elif '.net' in url:
        print('.net\n')
    elif '.info' in url:
        print('.info\n')
    elif '.biz' in url:
        print('.biz\n')
    elif '.online' in url:
        print('.online\n')
    elif '.in' in url:
        print('.in\n')
    elif '.edu' in url:
        print('.edu\n')
    else:
        print('Other low level domain!\n')
    
    return dictionary


if __name__ == '__main__':
    url = input("Enter your URL: ")
    parseURL(url)
    
    #Sample URLS to copy
    # url='https://www.facebook.com/photo.php?fbid=2068026323275211&set=a.269104153167446&type=3&theater'   
    # url='http://www.blog.google.uk:1000/path/to/myfile.html?key1=value1&key2=value2#InTheDocument'      
    # url='https://www.overleaf.com/9565720ckjijuhzpbccsd#/347876331/' 
