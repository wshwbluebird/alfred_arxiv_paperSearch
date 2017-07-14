#!/usr/local/bin/python
# encoding: utf-8




import sys
reload(sys)
sys.setdefaultencoding('utf-8')


def get_need_url(search):
     begin_url = 'https://arxiv.org/find/all/1/all:'
     end_url = '/0/1/0/all/0/1'
     words = search
     if len(words)==1:
         middle_url = '+'+words[0]
     else :
         middle_url =  '+'+words[-1]
         middle_url = "".join(list(['+AND+'+content for content in words[:-1]]))+middle_url

     ult_url = begin_url+middle_url+end_url
     print ult_url




def main():
    query = sys.argv[1:]
    get_need_url(query)



if __name__ == "__main__":
    main()
