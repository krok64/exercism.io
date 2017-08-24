allegs = {'eggs':1, 'peanuts':2, 'shellfish':4, 'strawberries':8,
 'tomatoes':16, 'chocolate':32, 'pollen':64, 'cats':128 }

class Allergies(object):
    
    def __init__(self, num):
        self.num = num & 255
    
    def is_allergic_to(self, a_name):
        if (a_name in allegs) and (self.num & allegs[a_name]):
            return True
        else:
            return False

    @property
    def lst(self):
        ret_list=[]
        for a_name in allegs:
            if self.is_allergic_to(a_name):
                ret_list.append(a_name)
        return ret_list

if __name__ == '__main__':
    print(Allergies(255).lst)
