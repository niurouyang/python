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
photo_group = {}


for m in range(0, len(l)-1):
    for n in range(m+1, len(l)):
        intersection_result_tag=''
        intersection_result = l[m]['tags'].intersection(l[n]['tags'])
        intersection_result_group = {l[m]['name'], l[n]['name']}
        if intersection_result:
            for tag in intersection_result:
                if intersection_result_tag == '':
                    intersection_result_tag =tag
                else:
                    intersection_result_tag = intersection_result_tag + "_" + tag
        
            photo_group.update({intersection_result_tag : (intersection_result_group)})
print(photo_group)
