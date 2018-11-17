class ShotInputException(Exception):
    def __init__(self,length,atleast):
        Exception.__init__(self)
        self.length = length
        self.atleast = atleast

while True:
    try:
        text = input('Enter somgthing-->')
        if len(text) < 3:
            raise ShotInputException(len(text),3)
    except EOFError:
        print('Why did you do an EOF on me')
    except ShotInputException as ex:
        print('ShotInputException the input was {0} long,ecepted at least {1}.'.format(ex.length,ex.atleast))
    else:
        print('No exception was raised.')
    finally:
        print('Over')