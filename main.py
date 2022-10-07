import requests
from datetime import datetime
pixela_endpoint="https://pixe.la/v1/users"
USERNAME="vishnusaddikutirjy"
TOKEN="abcdefghi1234"
GRAPH_ID="graph1"
PIXELDATA_ENDPOINT="https://api.sheety.co/25625e1188e03ed6296be01fd8862fce/pypro9,pixeldata/sheet1"


class pixela:
    #-------------------------------------------ENDPOINTS COMPLETED-----------------------------------------
    def __init__(self):
        self.a = 1

    def get_pixels(self):
        self.a = 2
        response=requests.get(url=PIXELDATA_ENDPOINT)
        datum=response.json()
        x=datum['sheet1']
        return x

    def check_sheet(self,x):
        for y in x:
            if y['date'] == 20220801:
                #count+=1
                datas={
                'sheet1' : {
                    'distance':30
                }}
                ch=requests.put(url=f"{PIXELDATA_ENDPOINT}/{y['id']}",json=datas)
                break



    #module=input("Enter date (YYYYmmDD):")
    #module_format=datetime.strptime(module,'%Y%m%d')
    def user_details(self):
        while(1):
            try:
                module = input("Enter date (YYYYmmDD):")
                module_format = datetime.strptime(module, '%Y%m%d')
                module_format_integer = int(module)
                today=datetime.now()
                today_format=today.strftime("%Y%m%d")
                today_actual=datetime.strptime(today_format,'%Y%m%d')
                difference=module_format-today_actual
                while(difference.days>0):
                    module = input("Enter past date or today's date(YYYYmmDD):")
                    module_format = datetime.strptime(module, '%Y%m%d')
                    difference = module_format - today_actual
                return module
            except:
                print("Entered in wrong format")

    '''
    user_params={
        "token":TOKEN,
        "username":USERNAME,
        "agreeTermsOfService":"yes",
        "notMinor":"yes"
    }
    '''
    def update_sheet_pixela(self,x,module):
        self.choice=0
        self.count=0
        for y in x:
            if y['date'] == int(module):
                print(f"You have run {y['distance']}")
                self.count+=1
                '''
                datas={
                'sheet1' : {
                    'distance':30
                }}
                
                #ch=requests.put(url=f"{PIXELDATA_ENDPOINT}/{y['id']}",json=datas)
                '''
                break
        if self.count==0:
            print("No data found")

        '''
        graph_endpoint=f"{pixela_endpoint}/{USERNAME}/graphs"
        graph_config={
            "id":GRAPH_ID,
            "name":"Running Graph",
            "unit":"Km",
            "type":"float",
            "color":"ajisai"
        }
        '''
        #print("hello")
        while 1:
            try:
                self.choice=int(input("Do you want to proceed? 1 for yes, any other number for no: "))
                break
            except:
                continue
        headers={
            "X-USER-TOKEN":TOKEN
        }

        #Commenting because the graph is created
        #response=requests.post(url=graph_endpoint,json=graph_config,headers=headers)
        #print(response.text)

        pixel_creation_endpoint=f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
        '''
        
        #print(type(today.strftime("%Y%m%d")))
        
        pixel_data={
                "date":today_format,
                "quantity":input("How many Km:"),
        }
        #Commoned out as pixels are inserted for a certain date
        response=requests.post(url=pixel_creation_endpoint,json=pixel_data,headers=headers)
        print(response.text)
        '''
        quantity=0
        while(1):
            try:
                quantity=int(input("How many Km: "))
                quantity=str(quantity)
                break
            except:
                print("Wrong input")
        if self.choice==1:
            pixel_update_endpoint=f"{pixel_creation_endpoint}/{module}"
            pixel_update_data={
                    "quantity":quantity
            }
            #Commoned out as we updated the pixel
            response=requests.put(url=pixel_update_endpoint,json=pixel_update_data,headers=headers)
            datas1 = {
                'sheet1': {
                    'distance': quantity
                }
            }
            datas2 = {
                'sheet1': {
                    'date': int(module),
                    'distance': quantity
                }
            }
            if self.count==0:
                requests.post(url=PIXELDATA_ENDPOINT,json=datas2)
            else:
                for y in x:
                    if y['date']==int(module):
                        requests.put(url=f"{PIXELDATA_ENDPOINT}/{y['id']}", json=datas1)
                        print("Data added successfully")
                        break
        #print(response.text)
        '''
        pixel_delete_endpoint=f"{pixel_update_endpoint}"
        response=requests.delete(url=pixel_delete_endpoint,headers=headers)
        print(response.text)
        '''


if __name__ == '__main__':
    obj=pixela()
    sheet_data=obj.get_pixels()
    #obj.check_sheet(sheet_data)
    user_date=obj.user_details()
    obj.update_sheet_pixela(sheet_data,user_date)