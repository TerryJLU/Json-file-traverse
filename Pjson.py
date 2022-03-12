if __name__ == '__main__':
    aa = {

        "interface_body_format": '8008',
        "aaa": 3,
        "bbb": [1, 2],
        "ccc": 'sun'
    }

    bb = {
        "nterface_body_format": '8008',
        "aaa": '',
        "bbb": [1, 2],
        "ccc": ['Moon','']
    }



for key,value in bb.items():
    if (key not in aa):
        print('The json The %s is not exist key' %(key))
    if  (value == '') :
        print('Has null value')
