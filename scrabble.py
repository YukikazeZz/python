#!/usr/local/bin/python
import sys
import time

def calculate_func_exec_time(func):
    def wrapper(word):
        print('{0} execute begin time is {1}'.format(func.__name__,time.clock()))
        res = func(word)
        print('{0} execute end time   is {1}'.format(func.__name__,time.clock()))
        return res
    return wrapper


@calculate_func_exec_time
def valid_words(rack):
    word_list=[]
    with open('/tmp/word.txt') as f:
        for word in f:
            rack_list=list(rack)
            found=True
            for d in word.strip():
                if d in rack_list:
                    rack_list.remove(d)
                else:
                    found=False
                    break
            if found:
                word_list.append(word.strip().lower())
        return word_list

@calculate_func_exec_time
def prind_valid_word_score(word_list):
    word_dict={}
    for word in word_list:
        word_score=sum([scores.get(d) for d in word])
        word_dict[word]=word_score     
    for v,k in sorted(word_dict.items(),key=lambda d:d[1],reverse=True):         
        print('{0},{1}'.format(v,k))
    print('do you want to input word:{0}'.format(sorted(word_dict.items(),key=lambda d:d[1],reverse=True)[0][0]))

#def guess_wanted_word(word_list):
    #print('do you want to input word:{0}'.format(sorted(word_dict.items(),key=lambda d:d[1],reverse=True)[0][0]))
    
    

def main():
    sys.argv.append("")
    rack=sys.argv[1]


    if not rack:
        raise SystemExit('Usage: {0} [RACK]'.format(sys.argv[0]))

    else:
        prind_valid_word_score(valid_words(rack))


if __name__ == "__main__":
    scores = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2,"f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3,"l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1,"r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4,"x": 8, "z": 10}
    main()
