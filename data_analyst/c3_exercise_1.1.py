# compare the tags in each picture and return their common tags with the picture name

l = [
    {
        'name' : 'photo1.jpg',
        'tags' : {'coffee','breakfast','drink','table','tableware','cup','food'}
    },
    {
        'name' : 'photo2.jpg',
        'tags' : {'food','dish','meat','meal','tableware','dinner','vegetable'}

    },
    {
        'name' : 'photo3.jpg',
        'tags' : {'city','skyline','cityscape','skyscraper','architecture','building','travel'}
    },
    {
        'name' : 'photo4.jpg',
        'tags' : {'drink','juice','glass','meal','fruit','food','grapes'}
    }
]

intercept_tag = {}
for m in range(0,len(l)-1):
    for n in range(m+1, len(l)):
        for tag in l[m]['tags']:
            if tag in l[n]['tags']:
                if tag not in intercept_tag:
                    intercept_tag.setdefault(tag,{l[m]['name'],l[n]['name']})
                else:
                    new_set= intercept_tag[tag]
                    new_set.add(l[n]['name'])
                    new_data = {tag:new_set}
                    intercept_tag.update(new_data)
print(intercept_tag)