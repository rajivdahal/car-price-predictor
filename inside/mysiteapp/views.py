from django.shortcuts import render
import pandas as pd
from django.http import HttpResponse
import pickle
import os
from .models import prediction,predictionSerializer;
path0=os.getcwd()
path1=os.path.join(path0,"static")
path2=os.path.join(path1,"model")
path3=os.path.join(path2,"finalmodel.pickle")
print(path3)

lr_model=pickle.load(open(path3,'rb'))
path4=os.path.join(path1,"datasets")
path5=os.path.join(path4,"data.csv")


car=pd.read_csv(path5)
brand=sorted(car['Brand'].unique())
Chevrolet_model=car.loc[car['Brand']=="Chevrolet",['Model']]
pd.DataFrame(Chevrolet_model)
Chevrolet_model=Chevrolet_model['Model'].tolist()
Chevrolet_model_unique=[]
for i in Chevrolet_model:
    if i not in Chevrolet_model_unique:
        Chevrolet_model_unique.append(i)



Fiat_model=car.loc[car['Brand']=="Fiat",['Model']]
pd.DataFrame(Fiat_model)
Fiat_model=Fiat_model['Model'].tolist()
Fiat_model_unique=[]
for i in Fiat_model:
    if i not in Fiat_model_unique:
        Fiat_model_unique.append(i)



Ford_model=car.loc[car['Brand']=="Ford",['Model']]
pd.DataFrame(Ford_model)
Ford_model=Ford_model['Model'].tolist()
Ford_model_unique=[]
for i in Ford_model:
    if i not in Ford_model_unique:
        Ford_model_unique.append(i)


Honda_model=car.loc[car['Brand']=="Honda",['Model']]
pd.DataFrame(Honda_model)
Honda_model=Honda_model['Model'].tolist()
Honda_model_unique=[]
for i in Honda_model:
    if i not in Honda_model_unique:
        Honda_model_unique.append(i)


Hyundai_model=car.loc[car['Brand']=="Hyundai",['Model']]
pd.DataFrame(Hyundai_model)
Hyundai_model=Hyundai_model['Model'].tolist()
Hyundai_model_unique=[]
for i in Hyundai_model:
    if i not in Hyundai_model_unique:
        Hyundai_model_unique.append(i)



Kia_model=car.loc[car['Brand']=="Kia",['Model']]
pd.DataFrame(Kia_model)
Kia_model=Kia_model['Model'].tolist()
Kia_model_unique=[]
for i in Kia_model:
    if i not in Kia_model_unique:
        Kia_model_unique.append(i)



Land_Rover_model=car.loc[car['Brand']=="Land Rover",['Model']]
pd.DataFrame(Land_Rover_model)
Land_Rover_model=Land_Rover_model['Model'].tolist()
Land_Rover_model_unique=[]
for i in Land_Rover_model:
    if i not in Land_Rover_model_unique:
        Land_Rover_model_unique.append(i)



Mahindra_model=car.loc[car['Brand']=="Mahindra",['Model']]
pd.DataFrame(Mahindra_model)
Mahindra_model=Mahindra_model['Model'].tolist()
Mahindra_model_unique=[]
for i in Mahindra_model:
    if i not in Mahindra_model_unique:
        Mahindra_model_unique.append(i)


Maruti_Suzuki_model=car.loc[car['Brand']=="Maruti Suzuki",['Model']]
pd.DataFrame(Maruti_Suzuki_model)
Maruti_Suzuki_model=Maruti_Suzuki_model['Model'].tolist()
Maruti_Suzuki_model_unique=[]
for i in Maruti_Suzuki_model:
    if i not in Maruti_Suzuki_model_unique:
        Maruti_Suzuki_model_unique.append(i)



Nissan_model=car.loc[car['Brand']=="Nissan",['Model']]
pd.DataFrame(Nissan_model)
Nissan_model=Nissan_model['Model'].tolist()
Nissan_model_unique=[]
for i in Nissan_model:
    if i not in Nissan_model_unique:
        Nissan_model_unique.append(i)



Skoda_model=car.loc[car['Brand']=="Skoda",['Model']]
pd.DataFrame(Skoda_model)
Skoda_model=Skoda_model['Model'].tolist()
Skoda_model_unique=[]
for i in Skoda_model:
    if i not in Skoda_model_unique:
        Skoda_model_unique.append(i)


Tata_model=car.loc[car['Brand']=="Tata",['Model']]
pd.DataFrame(Tata_model)
Tata_model=Tata_model['Model'].tolist()
Tata_model_unique=[]
for i in Tata_model:
    if i not in Tata_model_unique:
        Tata_model_unique.append(i)


Toyota_model=car.loc[car['Brand']=="Toyota",['Model']]
pd.DataFrame(Toyota_model)
Toyota_model=Toyota_model['Model'].tolist()
Toyota_model_unique=[]
for i in Toyota_model:
    if i not in Toyota_model_unique:
        Toyota_model_unique.append(i)



Volkswagen_model=car.loc[car['Brand']=="Volkswagen",['Model']]
pd.DataFrame(Volkswagen_model)
Volkswagen_model=Volkswagen_model['Model'].tolist()
Volkswagen_model_unique=[]
for i in Volkswagen_model:
    if i not in Volkswagen_model_unique:
        Volkswagen_model_unique.append(i)









# Create your views here.
def home(request):
    return render(request,'homepage.html')
def about(request):
    
    return render(request,'about.html')
def team(request):
    
    return render(request,'team.html')
def ads(request):
    
    return render(request,'ads.html')    
def history(request):
    
    return render(request,'history.html')            

def goprediction(request):
    Brand=sorted(car['Brand'].unique())
    Model=sorted(car['Model'].unique())
    Model_year=sorted(car['Model_year'].unique(),reverse=True)
    Transmission=sorted(car['Transmission'].unique())
    Engine_size=sorted(car['Engine_size(cc)'].unique())
    Drivetrain=sorted(car['Drivetrain'].unique())
    Fuel_type=sorted(car['Fuel_type'].unique())
    Lot_no=sorted(car['Lot_no'].unique())
    kilometer=sorted(car['Kilometer'].unique())
    context={'bb':Brand,'Model':Model,'Transmission':Transmission,'Engine_size':Engine_size,
             'Drivetrain':Drivetrain,'Fuel_type':Fuel_type,'Lot_no':Lot_no,'kilometer':kilometer,'Chevrolet_model_unique':Chevrolet_model_unique,'Fiat_model_unique':Fiat_model_unique,'Ford_model_unique':Ford_model_unique,
                'Honda_model_unique':Honda_model_unique,'Hyundai_model_unique':Hyundai_model_unique,'kia_model_unique':Kia_model_unique,'Land_Rover_model_unique':Land_Rover_model_unique,
                'Mahindra_model_unique':Mahindra_model_unique,'Maruti_Suzuki_model_unique':Maruti_Suzuki_model_unique,'Nissan_model_unique':Nissan_model_unique,
                'Skoda_model_unique':Skoda_model_unique,'Tata_model_unique':Tata_model_unique,'Toyota_model_unique':Toyota_model_unique,'Volkswagen_model_unique':Volkswagen_model_unique}
    
    
    return render(request,'prediction.html',context)    

def predict(request):
    if request.method=="POST":
        brand=request.POST.get('brand')
        model=request.POST.get('car_model')
        model_year=int(request.POST.get('model_year'))
        transmission=request.POST.get('transmission')
        drivetrain=int(request.POST.get('drivetrain'))
        fueltype=request.POST.get('fueltype')
        km_driven=int(request.POST.get('km_driven'))
        Engine_size=int(request.POST.get('Engine_size'))
        Lot_no=int(request.POST.get('Lot_no'))
        prediction=lr_model.predict(pd.DataFrame([[brand,model,model_year,transmission,Engine_size,drivetrain, fueltype,Lot_no,km_driven]],columns=['Brand','Model','Model_year','Transmission','Engine_size(cc)','Drivetrain','Fuel_type','Lot_no','Kilometer']))
        con={'prediction':prediction}
    return render(request,'index.html',con)


def save_car(request):
    brand=request.GET['brand'];
    #print(brand)
    car_model=request.GET['car_model'];
    transmission=request.GET['transmission'];   
    model_year=request.GET['model_year'];
    drivetrain=request.GET['drivetrain'];
    fueltype=request.GET['fueltype'];
    km_driven=request.GET['km_driven'];
    Engine_size=request.GET['Engine_size']
    Lot_no=request.GET['Lot_no'];
    prediction_model=lr_model.predict(pd.DataFrame([[brand,car_model,model_year,transmission,Engine_size,drivetrain, fueltype,Lot_no,km_driven]],columns=['Brand','Model','Model_year','Transmission','Engine_size(cc)','Drivetrain','Fuel_type','Lot_no','Kilometer']))
    prediction_model=prediction_model[0]
    prediction_db =prediction(brand=brand,model=car_model,model_year=model_year,Transmission=transmission,Engine_size=Engine_size,Fuel_type=fueltype,Drivetrain=drivetrain,Lot_no=Lot_no,Kilometer=km_driven,Price=prediction_model);
    try:
        prediction_db.save();
        return HttpResponse('True')
    except:
        return HttpResponse('False')


def getalldata(request):
    data=prediction.objects.all();  
    #print(data)
    ser=predictionSerializer(data,many=True) # it is serializing process:converts model object data type to python data type i.e dictionery
    #print(ser) #many=True indicates apply for all the model objects 
    import json;
    from rest_framework.renderers import JSONRenderer
    json_data=JSONRenderer().render(ser.data) # it convers python data type i.e dictionary to json :front rnd like XHMLneeds json data type
   
   
    return HttpResponse(json_data);  #httpResponse is used to render json data type to templates or XHML
    




    