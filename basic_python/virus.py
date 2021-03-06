# from match_fuzzy import match_fuzzy
# Virus_database =    {
#                     "Corona SARS" : {"ระบาดใน":"ไทย" 
#                                   , "จำนวนคนที่ติดเชื้อ" : 100 
#                                   , "จำนวนคนเสียชีวิต" : 20 }
#                     ,"Corona MERS" : {"ระบาดใน":"ญี่ปุ่น" 
#                                   , "จำนวนคนที่ติดเชื้อ" : 80 
#                                   , "จำนวนคนเสียชีวิต" : 10 }
#                 }

# Virus_names = Virus_database.keys() # get list of Virus Name

# print("ยินดีต้อนรับสู่ฐานข้อมูล ไวรัส ของโลก")
# while True:
#     คำสั่ง = str(input("กรุณาเลือกคำสั่งด้วยคะ \nเพิ่มฐานข้อมูลไวรัส(1)\nลบฐานข้อมูลไวรัส(2)\nเปลี่ยนแปลงข้อมูล(3)\nเรียกดูข้อมูลไวรัส(4)\nออกจากโปรแกรม(E)"))
#     if คำสั่ง == "1":
#         ชื่อไวรัส = input("กรุณาพิมพ์ชื่อไวรัส")
#         ระบาดใน = input("กรอกบริเวณที่ระบาด")
#         จำนวนคนที่ติดเชื้อ = input("กรอกจำนวนคนที่ติดเชื้อ")
#         จำนวนคนเสียชีวิต = input("กรอกจำนวนคนเสียชีวิต")
#         Virus_database[ชื่อไวรัส] = {"ระบาดใน":ระบาดใน 
#                                   , "จำนวนคนที่ติดเชื้อ" : จำนวนคนที่ติดเชื้อ 
#                                   , "จำนวนคนเสียชีวิต" : จำนวนคนเสียชีวิต }
#         print("ท่านได้ทำการเพิ่มข้อมูลไวรัส :",ชื่อไวรัส)
#     elif คำสั่ง == "2":
#         ชื่อไวรัส = input("กรุณาพิมพ์ชื่อไวรัส")
#         ชื่อไวรัส = match_fuzzy(ชื่อไวรัส,Virus_names,score=50)
#         try:
#             Virus_database.pop(ชื่อไวรัส)
#             print("ท่านได้ทำการลบข้อมูลไวรัส : ", ชื่อไวรัส)
#         except:
#             print("เกิดข้อผิดพลาด ไม่พบชื่อไวรัสดังกล่าว")
    
#     elif คำสั่ง == "3": #update ข้อมูลไวรัส
#         ชื่อไวรัส = input("กรุณาพิมพ์ชื่อไวรัส")
#         ชื่อไวรัส = match_fuzzy(ชื่อไวรัส,Virus_names,score=50)
#         try:
#             Virus_database[ชื่อไวรัส][ระบาดใน] = input("ระบุบริเวณที่ระบาด")
#             Virus_database[ชื่อไวรัส][จำนวนคนที่ติดเชื้อ] = input("ระบุจำนวนคนที่ติดเชื้อ")
#             Virus_database[ชื่อไวรัส][จำนวนคนเสียชีวิต] = input("ระบุจำนวนคนเสียชีวิต")
            
#             print("ท่านได้ทำการลบข้อมูลไวรัส : ", ชื่อไวรัส)
#         except:
#             print("เกิดข้อผิดพลาด ไม่พบชื่อไวรัสดังกล่าว")
    
#     elif คำสั่ง == "4":
#         ชื่อไวรัส = input("กรุณาพิมพ์ชื่อไวรัส")
#         ชื่อไวรัส = match_fuzzy(ชื่อไวรัส,Virus_names,score=50)
#         try:
#             print("พบชื่อไวรัสที่ท่านทำการค้นหา")
#             print(Virus_database[ชื่อไวรัส])
#         except:
#             print("เกิดข้อผิดพลาด ไม่พบชื่อไวรัสดังกล่าว")
            
#     else:
#         print(Virus_database)
#         break


user_database = {}
from config import CSV_PATH , DB_PATH
import os
from .match_fuzzy import match_fuzzy
from .utils.csvFinder import csvFinder
from .msgflex.flex import flex_find_row , make_carousel
from .utils.reply import SetMessage_Object
from linebot.models import *
from .main_menu import main_menu_message
csv_path = os.path.join(CSV_PATH,"รายการบ้านสองชั้น.csv")
CSV = csvFinder(csvPath=csv_path)
CSV.set_finding_column("รายการ")
CSV.add_stop_word("อยากทราบ","ครับ","ค่ะ")

Virus_database =    {
                    "Corona SARS" : {"ระบาดใน":"ไทย" 
                                  , "จำนวนคนที่ติดเชื้อ" : 100 
                                  , "จำนวนคนเสียชีวิต" : 20 }
                    ,"Corona MERS" : {"ระบาดใน":"ญี่ปุ่น" 
                                  , "จำนวนคนที่ติดเชื้อ" : 80 
                                  , "จำนวนคนเสียชีวิต" : 10 }
                }

Virus_names = Virus_database.keys()

### adding pickle
import pickle

### adding domain url to web
from flask import request


def save(user_database,virus_database):
    ##write database    
    data = [user_database,virus_database]
    with open(DB_PATH, 'wb') as handle:
        pickle.dump(data, handle, protocol=pickle.HIGHEST_PROTOCOL)
##ทำการ save virus สองตัวแรก
save(user_database=user_database,virus_database=Virus_database)

def virus_app(userid , text_input):
    text_input = str(text_input)
    ### read database
    with open(DB_PATH, 'rb') as handle:
        data = pickle.load(handle)
        user_database = data[0]
        Virus_database = data[1]
        Virus_names = Virus_database.keys()
        
    if userid not in user_database.keys():
        user_database[userid] = {"session":None,"ชื่อของไวรัส":None}

    if user_database[userid]["session"] is None:
        if text_input == "1":
            user_database[userid]["session"] = "CREATE_VIRUS"
            save(user_database,Virus_database)  
            return "กรุณาระบุชื่อไวรัส"
        
        elif text_input == "2":
            user_database[userid]["session"] = "DELETE_VIRUS"
            save(user_database,Virus_database)  
            return "กรุณาระบุชื่อไวรัส"
        
        elif text_input == "3":
            user_database[userid]["session"] = "UPDATE_VIRUS"
            save(user_database,Virus_database)  
            return "กรุณาระบุชื่อไวรัส"
        
        elif text_input == "4":
            user_database[userid]["session"] = "SHOW_VIRUS"
            save(user_database,Virus_database)  
            return "กรุณาระบุชื่อไวรัส"
        
        elif text_input == "เข้าสู่เมนู CSV Search":
            user_database[userid]["session"] = "CSV_FINDER"
            save(user_database,Virus_database)  
            return "ท่านได้เข้าสู่เมนูการค้นหาข้อมูลจากไฟล์ Excel , CSV \n กรุณาระบุ Keyword ที่ท่านต้องการค้นหา"
        
        else :
            flex_message = main_menu_message()
            return flex_message
    
    elif user_database[userid]["session"] == "CSV_FINDER":
        if text_input == "ออกจากการค้นหา":
            user_database[userid]["session"] = None
            save(user_database,Virus_database)  
            return "ท่านได้ออกจากเมนูค้นหาไฟล์ CSV"
        
        else:
            result = CSV.find_row(text_input,limit=5)  #ทำการค้นหาแล้วส่งค่ากลับเป็น ข้อมูลผลลัพ
            
            all_bubbles = []
            for each in result:
                แถวที่พบ = each["true_row"]
                คำที่ค้นหา = text_input
                คะแนนความเที่ยงตรง = each["score"]
                คอลัมน์ที่ค้นพบคำนี้ = each["col_name"]

                รายการที่ค้นพบ = each["result"]  #dictionary

                bubble = flex_find_row(แถวที่พบ,คำที่ค้นหา,คะแนนความเที่ยงตรง,คอลัมน์ที่ค้นพบคำนี้,รายการที่ค้นพบ)
                all_bubbles.append(bubble)
            ### adding Text and quick reply
            q_btn = QuickReplyButton(action=MessageAction(label="ออกจากการค้นหา",text="ออกจากการค้นหา"))
            q_reply = QuickReply(items=[q_btn])
            add_text = TextSendMessage(text="หากต้องการออกจากกันค้นหากรุณากดปุ่มหรือพิมพ์ 'ออกจากการค้นหา' นะคะ",quick_reply=q_reply)
            add_text = add_text.as_json_dict()
            
            flex_to_reply = make_carousel(all_bubble = all_bubbles)
            flex_to_reply = SetMessage_Object(Message_data=[flex_to_reply,add_text])
            # print(type(flex_to_reply))
            # TEXT_TO_REPLY_2 = TextSendMessage(text="ท่านสามารถพิมพ์คีย์เวิดในการค้นหาต่อไปได้ หรือหากต้องการหยุด ให้พิมพ์ว่า 'ออกจากการค้นหา'")
            return flex_to_reply
            
        
    elif user_database[userid]["session"] == "DELETE_VIRUS":
        ## validate (text from user)
        if match_fuzzy(text_input,Virus_names,score = 50):
            ชื่อของไวรัส = match_fuzzy(text_input,Virus_names,score = 50)
            ## update
            Virus_database.pop(ชื่อของไวรัส)
            user_database[userid]["session"] = None  
            save(user_database,Virus_database)  
            ## output
            return "ท่านได้ทำการลบข้อมูลของไวรัส {} สามารถตรวจสอบได้ที่\n {}".format(ชื่อของไวรัส,'https://'+request.host)
        else:
            return "กรุณากรอกชื่อไวรัสใหม่อีกครั้งคะ"
    
    elif user_database[userid]["session"] == "SHOW_VIRUS":
        ## validate (text from user)
        if match_fuzzy(text_input,Virus_names,score = 50):
            ชื่อของไวรัส = match_fuzzy(text_input,Virus_names,score = 50)
            ## update
            Data_To_Show = Virus_database[ชื่อของไวรัส]
            user_database[userid]["session"] = None 
            save(user_database,Virus_database)   
            ## output
            return "นี้คือข้อมูลของไวรัส {} มีข้อมูลดังนี้\n{} สามารถตรวจสอบได้ที่\n {}".format(ชื่อของไวรัส,Data_To_Show,'https://'+request.host)
        else:
            return "กรุณากรอกชื่อไวรัสใหม่อีกครั้งคะ"
        
    ## check-intent
    elif user_database[userid]["session"] == "CREATE_VIRUS":
        ## validate (text from user)
        if True:
            ชื่อของไวรัส = text_input
            ## update
            user_database[userid]["ชื่อของไวรัส"] = ชื่อของไวรัส
            Virus_database[ชื่อของไวรัส] = {}
            user_database[userid]["session"] = "INPUT_VIRUS_DATA_AREA"  ### ใส่ข้อมูลของ ไวรัส
            save(user_database,Virus_database)  
            ## output
            return "กรุณากรอกข้อมูล บริเวณที่ระบาด ของไวรัสด้วยค่ะ"
        else:
            return "กรุณากรอกชื่อไวรัสใหม่อีกครั้งคะ"
    
    ## check-intent
    elif user_database[userid]["session"] == "๊UPDATE_VIRUS":
        ## validate (text from user)
        if match_fuzzy(text_input,Virus_names,score = 50):
            ชื่อของไวรัส = match_fuzzy(text_input,Virus_names,score = 50)
            ## update
            user_database[userid]["ชื่อของไวรัส"] = ชื่อของไวรัส
            Virus_database[ชื่อของไวรัส] = {}
            user_database[userid]["session"] = "INPUT_VIRUS_DATA_AREA"  ### ใส่ข้อมูลของ ไวรัส
            save(user_database,Virus_database)  
            ## output
            return "กรุณากรอกข้อมูล บริเวณที่ระบาด ของไวรัสด้วยค่ะ"
        else:
            return "กรุณากรอกชื่อไวรัสใหม่อีกครั้งคะ"
        
    ## check-intent
    elif user_database[userid]["session"] == "INPUT_VIRUS_DATA_AREA":
        ## update
        ชื่อของไวรัส = user_database[userid]["ชื่อของไวรัส"]
        Virus_database[ชื่อของไวรัส]["ระบาดใน"] = text_input
        user_database[userid]["session"] = "INPUT_VIRUS_DATA_INFECTED"
        save(user_database,Virus_database)  
        ## output
        return "กรุณากรอกข้อมูล จำนวนผู้ติดเชื้อ ของไวรัสด้วยค่ะ (ระบุเป็นตัวเลขเท่านั้น)"
 
    ## check-intent
    elif user_database[userid]["session"] == "INPUT_VIRUS_DATA_INFECTED":
        ## validate (text from user)
        if text_input.isdigit():
            ## get data from user
            ชื่อของไวรัส = user_database[userid]["ชื่อของไวรัส"]
            ## update
            Virus_database[ชื่อของไวรัส]["จำนวนผู้ติดเชื้อ"] = text_input
            user_database[userid]["session"] = "INPUT_VIRUS_DATA_DEAD"
            save(user_database,Virus_database)  
            ## output
            return "กรุณากรอกข้อมูล จำนวนผู้เสียชีวิต ของไวรัสด้วยค่ะ (ระบุเป็นตัวเลขเท่านั้น)"  
        else :
            return "กรุณาระบุตัวเลขผู้ติดเชื้อใหม่อีกครั้งคะ" 
    
    elif user_database[userid]["session"] == "INPUT_VIRUS_DATA_DEAD":
        if text_input.isdigit():
            ชื่อของไวรัส = user_database[userid]["ชื่อของไวรัส"]
            Virus_database[ชื่อของไวรัส]["จำนวนผู้เสียชีวิต"] = text_input
            user_database[userid]["session"] = None
            save(user_database,Virus_database)
            return "ท่านได้สร้างข้อมูลไวรัส {} เสร็จแล้วเรียบร้อย ตรวจสอบได้ที่\n{}".format(ชื่อของไวรัส,'https://'+request.host)
        else :
            return "กรุณาระบุตัวเลขผู้ติดเสียชีวิตอีกครั้งคะ" 
    


        